from string import Template
switchy_template = """[SwitchyOmega Conditions]
@with result

$domain

* +direct
"""

domain_template = """*$domain* +proxy
"""

domain_template_cb = """*$domain_cb* +proxy-cb
"""

st = Template(switchy_template)
dt = Template(domain_template)
dt_cb = Template(domain_template_cb)

f = open("d.conf")
domain = ""
domain_cb = ""
for i in f.readlines():
  templine = i
  if templine.find("DOMAIN-KEYWORD")!=-1 or templine.find("DOMAIN-SUFFIX")!=-1:
    domain = domain + dt.substitute(domain=templine.split(",")[1])
    domain_cb = domain_cb + dt_cb.substitute(domain_cb=templine.split(",")[1])
f.close()

switchy_pac = st.substitute(domain=domain)
f = open('d.pac', 'w')
f.write(switchy_pac)
f.close()

switchy_pac = st.substitute(domain=domain_cb)
f = open('d-cb.pac', 'w')
f.write(switchy_pac)
f.close()
