# Edem_XmlParserLogo
Парсер иконок тв каналов из файла xml на примере файла от edem

Парсер написан для людей которым нужны логотипы телеканалов при просмотре iptv к примеру в kodi. Скрипт на писан на python 3 с использованием библиотек Requests, BeautifulSoup. Скачайте себе файл «edem.xml» или укажите ссылку на этот файл прописав ее в скрипте в 5 строчке (tree = ET.parse('./edem.xml') вместо «./edem.xml» Запустите скрипт убедившись что библиотеки установлены. Будет создана папка «IMG» в которой появятся изображения (логотипы каналов). 
