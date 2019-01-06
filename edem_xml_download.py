import xml.etree.ElementTree as ET
import requests 
import os

tree = ET.parse('./edem.xml')							#Путь к файлу (может быть сетевой) 
root = tree.getroot()
REQUEST_STATUS_CODE = 200
folfer = "./img/"

if not os.path.isdir(folfer):								#Проверяем существование папки
	os.mkdir(folfer)									#Создаем папку (путь в переменной 'folfer')

for country in root.findall('channel'):
	name_tv = country.find('display-name').text

	try:

		name_tv = name_tv.replace("/", " ") 			#Замена слеша на пробел
		url = country.find('icon').attrib['src']
		
		p = folfer + str(name_tv) + ".png"
		send=requests.get(url) 

		if send.status_code == REQUEST_STATUS_CODE:
			with open (p,'wb') as f:
				f.write(send.content)
				print(p)
	except AttributeError:
		print('icon - отсутствует')

print("Копирование завершено!")



