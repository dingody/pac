from __future__ import annotations
import argparse
from pathlib import Path
from string import Template

SWITCHY_TEMPLATE = """[SwitchyOmega Conditions]
@with result

$domain

* +direct
"""

SWITCHY_DOMAIN_TEMPLATE = "*$domain* +proxy"
GFW_TEMPLATE = "$domain,"
V2RAY_TEMPLATE = "keyword:$domain,"

class PacGenerator:
    def __init__(self, conf_path: str | Path) -> None:
        self.conf_path = Path(conf_path)
        self.switchy_domains: list[str] = []
        self.gfw_domains: list[str] = []
        self.v2ray_domains: list[str] = []

    def parse(self) -> None:
        with self.conf_path.open() as f:
            for line in f:
                if "PROXY" not in line:
                    continue
                if "DOMAIN-KEYWORD" in line:
                    domain = line.split(",")[1].strip()
                    self._add_domain(domain)
                elif "DOMAIN-SUFFIX" in line:
                    domain = line.split(",")[1].strip()
                    self._add_domain("." + domain)

    def _add_domain(self, domain: str) -> None:
        self.switchy_domains.append(
            SWITCHY_DOMAIN_TEMPLATE.replace("$domain", domain)
        )
        base_domain = domain.lstrip(".")
        self.gfw_domains.append(GFW_TEMPLATE.replace("$domain", base_domain))
        self.v2ray_domains.append(V2RAY_TEMPLATE.replace("$domain", base_domain))

    def generate_files(self, output_dir: str | Path = ".") -> None:
        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)
        switchy_pac = Template(SWITCHY_TEMPLATE).substitute(
            domain="".join(self.switchy_domains)
        )
        (out / "switchy.pac").write_text(switchy_pac)
        (out / "gfw.pac").write_text("".join(self.gfw_domains))
        (out / "v2ray.pac").write_text("".join(self.v2ray_domains))

def main() -> None:
    parser = argparse.ArgumentParser(description="Generate PAC files from config")
    parser.add_argument("conf", help="Path to the rule config file")
    parser.add_argument(
        "-o", "--output", default=".", help="Directory to write generated PAC files"
    )
    args = parser.parse_args()

    gen = PacGenerator(args.conf)
    gen.parse()
    gen.generate_files(args.output)

if __name__ == "__main__":
    main()
