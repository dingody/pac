from string import Template
switchy_template = """[SwitchyOmega Conditions]
@with result

$domain

* +direct
"""
domain_template = """*$domain* +proxy
"""

st = Template(switchy_template)
dt = Template(domain_template)

f = open("d.conf")
domain = ""
for i in f.readlines():
  templine = i
  if templine.find("DOMAIN-KEYWORD")!=-1 or templine.find("DOMAIN-SUFFIX")!=-1:
    domain = domain + dt.substitute(domain=templine.split(",")[1])
f.close()

switchy_pac = st.substitute(domain=domain)
f = open('d.pac', 'w')
f.write(switchy_pac)
f.close()
