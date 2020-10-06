import zipfile36 as zipfile

charlist = 'abcdefghijklmnopqrstuvwxyz'
complete = []

for current in range(4):
    a = [i for i in charlist]
    for x in range(current):
        a = [y + i for i in charlist for y in a]
    complete = complete + a

z = zipfile.ZipFile('test.zip')

tries = 0

for password in complete:
    try:
        tries += 1
        z.setpassword(password.encode('ascii'))
        z.extract('test.txt')
        print(f'Password was found after {tries} tries! It was {password}!')
        break
    except:
        pass
