#https://stepik.org/lesson/3380/step/2?unit=963
'''intab = input('vvedi symbols')
outab = input('vvedi chiffre')
word = input()
ciphered_word = input()'''
intab = 'abcd'
outab = '*d%#'
word = 'abacabadaba'
ciphered_word = '#*%*d*%'

encode = word.maketrans(intab, outab)
decode = ciphered_word.maketrans(intab, outab)
print(word.translate(encode))
print(ciphered_word.translate(decode))