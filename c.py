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

domain_template_cb = """
*$domain*,
"""

st = Template(switchy_template)
dt = Template(domain_template)
v2t = Template(v2rayng_template)
dt_cb = Template(domain_template_cb)

f = open("d.conf")
domain = ""
domain_cb = ""
for i in f.readlines():
  templine = i
  if templine.find("DOMAIN-KEYWORD")!=-1:
    domain = domain + dt.substitute(domain=templine.split(",")[1])
    domain_cb = domain_cb + dt_cb.substitute(domain="geosite:"+templine.split(",")[1])
  if templine.find("DOMAIN-SUFFIX")!=-1:
    domain = domain + dt.substitute(domain="."+templine.split(",")[1])
    domain_cb = domain_cb + dt_cb.substitute(domain="domain:"+templine.split(",")[1])
  if templine.find("IP-CIDR")!=-1:
    domain_cb = domain_cb + dt_cb.substitute(domain=templine.split(",")[1])
f.close()

switchy_pac = st.substitute(domain=domain)
f = open('d.pac', 'w')
f.write(switchy_pac)
f.close()

v2rayng_pac = v2t.substitute(domain=domain_cb)
f = open('d-cb.pac', 'w')
f.write(v2rayng_pac)
f.close()
