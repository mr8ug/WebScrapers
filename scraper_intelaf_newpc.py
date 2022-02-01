from audioop import add
from math import prod
from os import path
import re
from urllib import response
from webbrowser import Chrome
from click import option
from itsdangerous import exc
from matplotlib.pyplot import cla
import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from requests_html import HTMLSession
from webdriver_manager.chrome import ChromeDriverManager



class PC():
    def __init__(self):
        self.case = [] #https://www.intelaf.com/Precios_stock_resultado.aspx?area=COMPU-CASES
        self.lectorcd = [] #https://www.intelaf.com/Precios_stock_resultado.aspx?area=COMPU-UNIDAD
        self.cpucooler = [] #https://www.intelaf.com/Precios_stock_resultado.aspx?area=COMPU-CASE-COOL
        self.disco = [] #https://www.intelaf.com/Precios_stock_resultado.aspx?area=DISCO-DURO-INT
        self.ssd = [] #https://www.intelaf.com/Precios_stock_resultado.aspx?area=TODOS-SSD
        self.fuente = [] #https://www.intelaf.com/Precios_stock_resultado.aspx?area=COMPU-FUENTES
        self.ddr2 = [] #https://www.intelaf.com/Precios_stock_resultado.aspx?area=MEM-RAM-DDR2
        self.ddr3 = [] #https://www.intelaf.com/Precios_stock_resultado.aspx?area=MEM-RAM-DDR3
        self.ddr4 = [] #https://www.intelaf.com/Precios_stock_resultado.aspx?area=MEM-RAM-DDR4
        self.moboAMD = [] #https://www.intelaf.com/Precios_stock_resultado.aspx?area=COMPU-MBOARD-AMD
        self.moboIntel = [] #https://www.intelaf.com/Precios_stock_resultado.aspx?area=COMPU-MBOARD-INTEL
        self.moboInc = [] #https://www.intelaf.com/Precios_stock_resultado.aspx?area=COMPU-MBOARD-PROC
        self.pasta = [] #https://www.intelaf.com/Precios_stock_resultado.aspx?area=PROC-VENT
        self.procAMD = [] #https://www.intelaf.com/Precios_stock_resultado.aspx?area=PROC-AMD
        self.procIntel = [] #https://www.intelaf.com/Precios_stock_resultado.aspx?area=COMPU-PROC-INTEL
        self.tarjPCI = [] #https://www.intelaf.com/Precios_stock_resultado.aspx?area=COMPU-TARJ-PCI
        self.tarjSonido = [] #https://www.intelaf.com/Precios_stock_resultado.aspx?area=AUDIO-TARJ-SON
        self.tarjNvidia = [] #https://www.intelaf.com/Precios_stock_resultado.aspx?area=TARJ-VIDEO-NVIDIA
        self.tarjRadeon = [] #https://www.intelaf.com/Precios_stock_resultado.aspx?area=TARJ-VIDEO-RADEON
        self.fan = [] #https://www.intelaf.com/Precios_stock_resultado.aspx?area=COMPU-VENT

        #obtener la data
        self.getIntelaf()
        self.getImeqmo()

    def objProducto(self, url, nombre, precio_normal, precio_efectivo, img, existencia, tienda):
        producto = {
            'url':url,
            'nombre':nombre,
            'precio_normal': precio_normal,
            'precio_efectivo': precio_efectivo,
            'imagen':img,
            'existencia':existencia,
            'tienda':tienda
        }

        return producto
    def getIntelaf(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('window-size= 1920x1080')
        

        urls = ['https://www.intelaf.com/Precios_stock_resultado.aspx?area=COMPU-CASES',
                'https://www.intelaf.com/Precios_stock_resultado.aspx?area=COMPU-UNIDAD',
                'https://www.intelaf.com/Precios_stock_resultado.aspx?area=COMPU-CASE-COOL',
                'https://www.intelaf.com/Precios_stock_resultado.aspx?area=DISCO-DURO-INT',
                'https://www.intelaf.com/Precios_stock_resultado.aspx?area=TODOS-SSD',
                'https://www.intelaf.com/Precios_stock_resultado.aspx?area=COMPU-FUENTES',
                'https://www.intelaf.com/Precios_stock_resultado.aspx?area=MEM-RAM-DDR4',
                'https://www.intelaf.com/Precios_stock_resultado.aspx?area=COMPU-MBOARD-AMD',
                'https://www.intelaf.com/Precios_stock_resultado.aspx?area=COMPU-MBOARD-INTEL',
                'https://www.intelaf.com/Precios_stock_resultado.aspx?area=PROC-VENT',
                'https://www.intelaf.com/Precios_stock_resultado.aspx?area=PROC-AMD',
                'https://www.intelaf.com/Precios_stock_resultado.aspx?area=COMPU-PROC-INTEL',
                'https://www.intelaf.com/Precios_stock_resultado.aspx?area=TARJ-VIDEO-NVIDIA',
                'https://www.intelaf.com/Precios_stock_resultado.aspx?area=TARJ-VIDEO-RADEON',
                'https://www.intelaf.com/Precios_stock_resultado.aspx?area=COMPU-VENT'
                ]
        for url in urls:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('window-size= 1920x1080')
            driver = ''
            try:
                driver = webdriver.Chrome(options = chrome_options)
            except:
                driver = webdriver.Chrome(ChromeDriverManager().install(), options = chrome_options)
            #print('Porcentaje', str((int(urls.index(url))/len(urls))*100) )
            

            driver.get(str(url))
            time.sleep(10)
            
            response=driver.page_source
            html = BeautifulSoup(response, "html.parser")

    
            productos = html.findAll('div', class_='col-xs-12 col-md-6 col-lg-4')
            
            #print(productos)

            for p in productos:
                #try:
                addProducto =self.objProducto(
                    'https://intelaf.com/'+p.contents[1].contents[1].contents[1].contents[1].attrs['name'],
                    p.contents[1].text,
                    self.fixPrinceNormal(p.contents[1].contents[3].contents[3].text),
                    str(p.contents[1].contents[3].contents[5].text).replace("Beneficio Efectivo: Q", '').replace("TECNOPROMO: Q", '').replace(',',''),
                    self.fixImg(p.contents[1].contents[1].attrs['style']),
                    str(p.contents[1].attrs['title']),
                    'INTELAF'
                )

                if str(url).endswith('COMPU-CASES'):
                    self.case.append(addProducto)

                if str(url).endswith('COMPU-UNIDAD'):
                    self.lectorcd.append(addProducto)

                if str(url).endswith('COMPU-CASE-COOL'):
                    self.cpucooler.append(addProducto)

                if str(url).endswith('DISCO-DURO-INT'):
                    self.disco.append(addProducto)

                if str(url).endswith('TODOS-SSD'):
                    self.ssd.append(addProducto)

                if str(url).endswith('COMPU-FUENTES'):
                    self.fuente.append(addProducto)

                if str(url).endswith('MEM-RAM-DDR2'):
                    self.ddr2.append(addProducto)

                if str(url).endswith('MEM-RAM-DDR3'):
                    self.ddr3.append(addProducto)

                if str(url).endswith('MEM-RAM-DDR4'):
                    self.ddr4.append(addProducto)

                if str(url).endswith('COMPU-MBOARD-AMD'):
                    self.moboAMD.append(addProducto)

                if str(url).endswith('COMPU-MBOARD-INTEL'):
                    self.moboIntel.append(addProducto)

                if str(url).endswith('COMPU-MBOARD-PROC'):
                    self.moboInc.append(addProducto)
                
                if str(url).endswith('PROC-VENT'):
                    self.pasta.append(addProducto)

                if str(url).endswith('PROC-AMD'):
                    self.procAMD.append(addProducto)

                if str(url).endswith('COMPU-PROC-INTEL'):
                    self.procIntel.append(addProducto)
                
                if str(url).endswith('COMPU-TARJ-PCI'):
                    self.tarjPCI.append(addProducto)

                if str(url).endswith('AUDIO-TARJ-SON'):
                    self.tarjSonido.append(addProducto)

                if str(url).endswith('TARJ-VIDEO-NVIDIA'):
                    self.tarjNvidia.append(addProducto)

                if str(url).endswith('TARJ-VIDEO-RADEON'):
                    self.tarjRadeon.append(addProducto)

                if str(url).endswith('COMPU-VENT'):
                    self.fan.append(addProducto)
            #except Exception as e:
            #    print('Error',e,' con:', str(p), '\n\n')
    
    def getImeqmo(self):
        urls = ['https://www.imeqmo.com/shop/category/componentes-de-pc-cases-9',
                'https://www.imeqmo.com/shop/category/componentes-de-pc-discos-duros-internos-23',
                'https://www.imeqmo.com/shop/category/componentes-de-pc-enfriadores-y-ventiladores-150',
                'https://www.imeqmo.com/shop/category/componentes-de-pc-fuentes-de-poder-28',
                'https://www.imeqmo.com/shop/category/componentes-de-pc-memoria-ram-12',
                'https://www.imeqmo.com/shop/category/componentes-de-pc-motherboard-10',
                'https://www.imeqmo.com/shop/category/componentes-de-pc-procesadores-11',
                'https://www.imeqmo.com/shop/category/componentes-de-pc-quemadoras-30',
                'https://www.imeqmo.com/shop/category/componentes-de-pc-tarjetas-de-video-19',
                'https://www.imeqmo.com/shop/category/componentes-de-pc-unidades-de-estado-solido-144'

                ]

        for url in urls:
            response = requests.get(url)

            html = BeautifulSoup(response.text, 'html.parser')

            productos = html.findAll('td', class_='oe_product oe_grid te_t_image')
            #imagen productos[1].contents[1].contents[1].contents[3].contents[1].contents[1].contents[1].attrs['content']
            #print(productos)
            for p in productos:
                #get existencia
                urlProducto = ''
                try:
                    urlProducto = 'https://www.imeqmo.com'+str(p.contents[1].contents[1].contents[3].contents[1].contents[1].attrs['href'])
                except:
                    urlProducto = 'Error'
                precio = str(p.text)
                precio2 = re.sub('\n+','',precio)

                nombre = precio2.split('-')
                nombreProducto = ''
                try:
                    imagen = p.contents[1].contents[1].contents[3].contents[1].contents[1].contents[1].attrs['alt']
                except:
                    nombreProducto = str(nombre[0])
                precio3 = str(re.sub('Q\xa0','|', precio2)).split('|')
                precioNormal = str(precio3[1]).replace(',','')
                precio4 = str(precio3[2]).split('QTQ')
                precio5 = str(precio4[0]).split('.00')

                precioEfectivo = str(str(precio5[0]).replace(',','')+'.00')

                imagen = ''
                try:
                    imagen = p.contents[1].contents[1].contents[3].contents[1].contents[1].contents[1].attrs['content']
                except:
                    imagen = 'Error'
                #print(precioNormal, precioEfectivo)
                addProducto = self.objProducto(
                    urlProducto,
                    nombreProducto,
                    precioNormal,
                    precioEfectivo,
                    imagen,
                    'Hay Existencia',
                    'IMEQMO'
                )

                if 'cases' in str(url):
                    self.case.append(addProducto)

                if 'quemadoras' in str(url):
                    self.lectorcd.append(addProducto)

                if 'enfriadores-y-ventiladores' in str(url):
                    if ('enfriador' in str(addProducto['nombre']).lower()):
                        self.cpucooler.append(addProducto)
                    else:
                        self.fan.append(addProducto)

                if 'discos-duros-internos' in str(url):
                    self.disco.append(addProducto)

                if 'unidades-de-estado-solido' in str(url):
                    self.ssd.append(addProducto)

                if 'fuentes-de-poder' in str(url):
                    self.fuente.append(addProducto)

                if 'memoria-ram' in str(url):
                    if ('ddr2' in str(addProducto['nombre']).lower()):
                        self.ddr2.append(addProducto)

                    if ('ddr3' in str(addProducto['nombre']).lower()):
                        self.ddr3.append(addProducto)

                    if ('ddr4' in str(addProducto['nombre']).lower()):
                        self.ddr4.append(addProducto)
                

                if 'motherboard' in str(url):
                    if ('LGA' in str(addProducto['nombre']).lower()):
                        self.moboIntel.append(addProducto)
                    else:
                        self.moboAMD.append(addProducto)

                              
                if 'procesadores' in str(url):
                    if ('procesador' in str(addProducto['nombre']).lower()):
                        if ('intel' in str(addProducto['nombre']).lower()):
                            self.procIntel.append(addProducto)
                        if ('amd' in str(addProducto['nombre']).lower()):
                            self.procAMD.append(addProducto)
                    else:
                        self.pasta.append(addProducto)
                    
                if 'tarjetas-de-video' in str(url):
                    if ('tarjeta de video' in str(addProducto['nombre']).lower()):
                        if('geforce' in str(addProducto['nombre']).lower()):
                            self.tarjNvidia.append(addProducto)
                        else:
                            self.tarjRadeon.append(addProducto)

                

    def fixImg(self, style):
        imgLink = ''
        fiximg = str(style).split(';')
        for f in fiximg:
            if str(f).startswith('background-image: url'):
                imgLink = str(f).replace('background-image: url(\"','').replace('.jpg\")','')
                break

            imgLink = 'https://intelaf.com/'+imgLink + '.jpg'
        return imgLink

    def fixPrinceNormal(self, product):
        normal = ''
        try:
            
            normal = str(product).replace('Q','').replace(',','').replace('Precio normal:', '').strip()
        except:
            normal = 'F0.00'
        return normal


    def getCases(self):
        return self.case

    def getCdReaders(self):
        return self.lectorcd

    def getCpuCoolers(self):
        return self.cpucooler

    def getHDDs(self):
        return self.disco

    def getSSDs(self):
        return self.ssd

    def getPowerSupplies(self):
        return self.fuente

    def getDDR2s(self):
        return self.ddr2

    def getDDR3s(self):
        return self.ddr3

    def getDDR4s(self):
        return self.ddr4

    def getMoboAMD(self):
        return self.moboAMD

    def getMoboIntel(self):
        return self.moboIntel

    def getMoboIncorporated(self):
        return self.moboInc 
    
    def getTermalPastes(self):
        return self.pasta

    def getProcAMD(self):
        return self.procAMD

    def getProcIntel(self):
        return self.procIntel

    def getPCICards(self):
        return self.tarjPCI

    def getSoundCards(self):
        return self.tarjSonido

    def getNVidiaCards(self):
        return self.tarjNvidia

    def getRadeonCards(self):
        return self.tarjRadeon

    def getFans(self):
        return self.fan

#*
#start = time.time()
#pd = PC()
#time.sleep(1)
#end = time.time()
#print(f"Runtime of the program is {end - start}")