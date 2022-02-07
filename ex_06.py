print('Exersise 6.5')
str = 'X-DSPAM-Confidence: 0.8475'

ipos = str.find(':')
print(ipos)
dd=str[ipos + 1:]
print(dd)
nn = float(dd)
print(nn)