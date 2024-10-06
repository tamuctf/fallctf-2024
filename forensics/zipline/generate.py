import zipfile

zf = zipfile.ZipFile('flag.zip', mode='w', compression=zipfile.ZIP_DEFLATED)

zf.writestr('flag.txt',      'Good luck finding my secret flag :)')
zf.writestr('flag.txt',      'Keep looking!')

for i in 'abcd':
    zf.writestr(i + '/../flag.txt', 'gigem{fake_flag}')

zf.writestr('d/../flag.txt', 'gigem{t00_many_l4y3rs_deep}')
zf.writestr('./flag.txt',    'gigem{another_fake_flag}')

zf.close()