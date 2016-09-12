import string

x = string.lowercase

decryption = string.maketrans(x, x[2:] + x[:2])

encrypted_text = """g fmnc wms bgblr rpylqjyrc gr zw fylb.
                    rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb
                    gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
                    sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"""

print encrypted_text.translate(decryption)

print 'map'.translate(decryption)
