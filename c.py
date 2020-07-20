from string import Template
switchy_template = """[SwitchyOmega Conditions]
@with result

$domain

* +direct
"""

v2rayng_template = """
$domain
"""

domain_template = """*$domain* +proxy
"""

st = Template(switchy_template)
dt = Template(domain_template)
dt_cb = Template(v2rayng_template)

f = open("d.conf")
domain = ""
domain_cb = ""
for i in f.readlines():
  templine = i
  if templine.find("DOMAIN-KEYWORD")!=-1:
    domain = domain + dt.substitute(domain=templine.split(",")[1])
    domain_cb = domain_cb + "geosite:"+templine.split(",")[1]+","
  if templine.find("DOMAIN-SUFFIX")!=-1:
    domain = domain + dt.substitute(domain="."+templine.split(",")[1])
    domain_cb = domain_cb + "domain:"+templine.split(",")[1]+","
  if templine.find("IP-CIDR")!=-1:
    domain_cb = domain_cb + templine.split(",")[1]+","
f.close()

switchy_pac = st.substitute(domain=domain)
f = open('d.pac', 'w')
f.write(switchy_pac)
f.close()

v2rayng_pac = st.substitute(domain=domain_cb)
f = open('d-cb.pac', 'w')
f.write(v2rayng_pac)
f.close()
