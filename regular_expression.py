import re


line = 'G2 = NOT(3)'
line = line.strip()
print (line)
#line_syntax = re.match(r' *([a-zA-Z0-9_\$]+) *= *(.+) *\( *([^ ].*[^ ]) *\)',line)
#line_test = re.match(r'^([A-Za-z]?\[0-9]+)\[ ]?=\[ ]?\[A-Za-z]+\[(]\[A-Za-z]?\[0-9]+(\[,]\[ ]?\[A-Za-z]?\[0-9]+)?\[)]$',line)

#print (line_syntax.group(0))
#print (line_test.group(0))



#line_test = re.match(r'([a-zA-Z0-9\$]+)+(=)',line)
#print (line_test.group(0))

pattern = re.compile(r' *([a-zA-Z0-9_\$]+) *= *(.+) *\( *([^ ].*[^ ]) *\)')
line_test = pattern.match(line)
print (line_test.group(3))
#right_nodes = re.split(r' *, *', line_test.group(3))
#print(right_nodes)
