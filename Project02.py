'''
Sawyer Coleman
Project 02
SSW 555 - Agile
'''

Taglist = ['INDI', 'NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'FAM', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV', 'DATE', 'HEAD', 'TRLR', 'NOTE']
def Validation(tag):
    if tag in Taglist:
        return 'Y'
    else:
        return 'N'
with open(r'/Users/Sawyer/Downloads/Project01.ged', 'r') as f:
    d = {}
    for line in f:
        info = line.split()
        level = info[0]
        tag = info[1]
        otherInfo = info[2:]
        print('-->' + line)
        print('<--' + level, '|', tag, '|', Validation(tag), '|', ''.join(otherInfo), '\n')
