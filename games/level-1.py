sentence = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. 
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. 
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''

# str.isalpha(char)
# ord(char)
# chr(order)
page_url = "http://www.pythonchallenge.com/pc/def/map.html"

real_sentence = ''
for char in sentence:
    if str.isalpha(char):
        char_order = ord(char)
        if char_order >= ord('y'):
            char_order += (2 - 26)
        else:
            char_order += 2
        real_sentence += chr(char_order)
    else:
        real_sentence += char

print(real_sentence)
