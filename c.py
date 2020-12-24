from string import Template
switchy_template = """[SwitchyOmega Conditions]
@with result

$domain

* +direct
"""

switchy_domain_template = """*$domain* +proxy
"""

gfw_template = """$domain,
"""

st = Template(switchy_template)
sdt = Template(switchy_domain_template)
gt = Template(gfw_template)

f = open("d.conf")
switchy_domain = ""
gfw_domain=""
for i in f.readlines():
  templine = i
  if templine.find("PROXY")!=-1:
    if templine.find("DOMAIN-KEYWORD")!=-1:
      switchy_domain = switchy_domain + sdt.substitute(domain=templine.split(",")[1])
      gfw_domain = gfw_domain + gt.substitute(domain=templine.split(",")[1])
    if templine.find("DOMAIN-SUFFIX")!=-1:
      switchy_domain = switchy_domain + sdt.substitute(domain="."+templine.split(",")[1])
      gfw_domain = gfw_domain + gt.substitute(domain=templine.split(",")[1])
  f.close()

switchy_pac = st.substitute(domain=switchy_domain)
f = open('switchy.pac', 'w')
f.write(switchy_pac)
f.close()

f = open('gfw.pac', 'w')
f.write(gfw_domain)
f.close()
