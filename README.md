# PAC Generator Plugin

This repository contains configuration files for various network tools and a Python
script for generating PAC files from those configurations.

## Usage

The `pac_generator.py` script converts a rule configuration file into three
formats:

- `switchy.pac` for SwitchyOmega
- `gfw.pac` for GFW list
- `v2ray.pac` for V2Ray

Run the script with the path to your configuration file:

```bash
python pac_generator.py <path-to-config>
```

Optional arguments:

- `-o, --output`  Directory where the PAC files will be written. Defaults to
  the current directory.

Example:

```bash
python pac_generator.py e.conf -o output
```

This will create `switchy.pac`, `gfw.pac`, and `v2ray.pac` inside the `output`
folder.
