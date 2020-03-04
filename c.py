from string import Template
switchy_template = """[SwitchyOmega Conditions]
@with result

$domain
$domain_cp

* +direct
"""

domain_template = """*$domain* +proxy
"""

domain_template_cb = """*$domain* +proxy-cb
"""

st = Template(switchy_template)
dt = Template(domain_template)
dt_cb = Template(domain_template_cb)

f = open("d.conf")
domain = ""
domain_cp = ""
for i in f.readlines():
  templine = i
  if templine.find("DOMAIN-KEYWORD")!=-1 or templine.find("DOMAIN-SUFFIX")!=-1:
    domain = domain + dt.substitute(domain=templine.split(",")[1])
    domain_cp = domain_cp + dt.substitute(domain_cp=templine.split(",")[1])
f.close()

switchy_pac = st.substitute(domain=domain)
switchy_pac = st.substitute(domain_cp=domain_cp)
f = open('d.pac', 'w')
f.write(switchy_pac)
f.close()
