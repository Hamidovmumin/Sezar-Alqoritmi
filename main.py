def Sezar_alqoritm(text,acar_nomre):
	netice = ''
	for i in range(len(text)):
		char = text[i]
		if (char.isupper()):
			netice += chr((ord(char) + acar_nomre - 65) % 26 + 65)
		else:
			netice += chr((ord(char) + acar_nomre - 97) % 26 + 97)
	return netice

text=input('Mətni daxil edin: ')
acar_nomre =int(input('Açar nömrəsini daxil edin: '))
print ("Şifrə: " + Sezar_alqoritm(text,acar_nomre)+'\n')

# #================================================== isupper() metodu =================================================#
# # Əgər sözdəki bütün hərflər böyükdürsə True əks halda False qaytarır
# text='HELLO WORLD'
# x=text.isupper()
# print(x) ## True
# #=====================================================================================================================#
#
# #================================================== ord() metodu =====================================================#
# # ord() metodu hərfin əlifbadakı sıra nömrəsini tapır.
# herf=ord(input('Herfi daxil edin:'))
# print('Hərfin əlifbada sıra nömrəsi: '+f'{herf}')
# #=====================================================================================================================#
#
# #================================================== chr() metodu =====================================================#
# # chr() metodu nömrəyə əsasən əlifbadakı hərfi tapır.
# nomre=chr(int(input('Hərfin nömrəsini daxil edin: ')))
# print('Daxil edilən nömrəyə əsasən əlifbadakı hərf: '+f'{nomre}')
# #=====================================================================================================================#
