"""
  Python 2 ile IoThook REST Api Testi

  Kod çalıştırıldığında 'data' değişkenine verilen 'last' değişkeni ile
  auth sahipliğindeki en son veri alınır. 'channel' değişkeni Iothook dashboard
  Kanal oluşturma sırasında otomatik verilen id numarasıdır.

  Bu ornek IotHook servisine veri almak/gondermek icin baslangic seviyesinde
  testlerin yapilmasini amaclamaktadir.

  10 Mayıs 2017
  Sahin MERSIN

  Daha fazlasi icin

  http://www.iothook.com
  ve
  https://github.com/electrocoder/iotHook

  sitelerine gidiniz.

  Sorular ve destek talepleri icin
  https://github.com/electrocoder/iotHook/issues
  sayfasindan veya Meşe Bilişim den yardım alabilirsiniz.

  Yayin : http://mesebilisim.com
  
  Licensed under the Apache License, Version 2.0 (the "License").
  You may not use this file except in compliance with the License.
  A copy of the License is located at

  http://www.apache.org/licenses/

"""

import requests

# url = 'https://iothook.com/api/v1.2/datas/?data=last&channel=108'
url = 'http://localhost:8000/api/v1.2/datas/?data=last&channel=106'

auth=('test', 'test12345')

response = requests.get(url, auth=auth)
data = response.json()
print data
