import re

ime = input('Unesite ime: ')
prezime = input('Unesite prezime: ')

regex_fpmoz = "(^[a-z]{2,15})[.]([a-z]{2,15})([@]fpmoz[.]sum[.]ba$)"
regex_sum = "^" + ime.lower()[0] + prezime.lower() + "(\d*[@]sum[.]ba$)"

while 1:
    fpmoz_mail= input('Unesite @fpmoz.sum.ba mail: ')
     sum_mail= input('Unesite @sum.ba mail: ')
    unos1 = re.match(regex_fpmoz, fpmoz_mail)
    unos2 = re.match(regex_sum, sum_mail)
    if unos1 and unos2:
        print('Uspjesno ste unijeli email adrese')
        break
    elif not unos1:
        print('Neispravan format @fpmoz.sum.ba adrese')
    elif not unos2:
        print('Neispravan format @sum.ba adrese')
