data = open('Mario/SMario.sfc', 'rb').read()
hex_list = ["{:02x}".format(ord(c)) for c in data]
print hex_list[520000:524288]

print len(hex_list)

