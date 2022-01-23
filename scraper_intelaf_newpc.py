
from audioop import add
from unittest import FunctionTestCase
import requests
from bs4 import BeautifulSoup


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
        self.getData()
    def objProducto(self, url, nombre, precio_normal, precio_efectivo, img, existencia):
        producto = {
            'url':url,
            'nombre':nombre,
            'precio_normal': precio_normal,
            'precio_efectivo': precio_efectivo,
            'imagen':img,
            'existencia':existencia
        }

        return producto
    def getData(self):
        urls = ['https://www.intelaf.com/Precios_stock_resultado.aspx?area=COMPU-CASES',
                'https://www.intelaf.com/Precios_stock_resultado.aspx?area=COMPU-UNIDAD',
                'https://www.intelaf.com/Precios_stock_resultado.aspx?area=COMPU-CASE-COOL',
                'https://www.intelaf.com/Precios_stock_resultado.aspx?area=DISCO-DURO-INT',
                'https://www.intelaf.com/Precios_stock_resultado.aspx?area=TODOS-SSD',
                'https://www.intelaf.com/Precios_stock_resultado.aspx?area=COMPU-FUENTES',
                'https://www.intelaf.com/Precios_stock_resultado.aspx?area=MEM-RAM-DDR2',
                'https://www.intelaf.com/Precios_stock_resultado.aspx?area=MEM-RAM-DDR3',
                'https://www.intelaf.com/Precios_stock_resultado.aspx?area=MEM-RAM-DDR4',
                'https://www.intelaf.com/Precios_stock_resultado.aspx?area=COMPU-MBOARD-AMD',
                'https://www.intelaf.com/Precios_stock_resultado.aspx?area=COMPU-MBOARD-INTEL',
                'https://www.intelaf.com/Precios_stock_resultado.aspx?area=COMPU-MBOARD-PROC',
                'https://www.intelaf.com/Precios_stock_resultado.aspx?area=PROC-VENT',
                'https://www.intelaf.com/Precios_stock_resultado.aspx?area=PROC-AMD',
                'https://www.intelaf.com/Precios_stock_resultado.aspx?area=COMPU-PROC-INTEL',
                'https://www.intelaf.com/Precios_stock_resultado.aspx?area=COMPU-TARJ-PCI',
                'https://www.intelaf.com/Precios_stock_resultado.aspx?area=AUDIO-TARJ-SON',
                'https://www.intelaf.com/Precios_stock_resultado.aspx?area=TARJ-VIDEO-NVIDIA',
                'https://www.intelaf.com/Precios_stock_resultado.aspx?area=TARJ-VIDEO-RADEON',
                'https://www.intelaf.com/Precios_stock_resultado.aspx?area=COMPU-VENT'
                ]
        for url in urls:
            response = requests.get(url)

            html = BeautifulSoup(response.text, 'html.parser')

            productos = html.findAll('div', class_='col-xs-12 col-md-4')
            

            for p in productos:
                #try:
                addProducto =self.objProducto(
                    'https://intelaf.com/'+p.contents[0].next_element.contents[0].next_element.attrs['name'],
                    p.contents[0].contents[1].contents[1].previous_sibling.text,
                    self.fixPrinceNormal(p),
                    str(p.contents[0].previous_element.next_element.contents[1].contents[2].text).replace("Beneficio Efectivo: Q", '').replace("TECNOPROMO: Q", '').replace(',',''),
                    self.fixImg(p.next_element.contents[0].attrs['style']),
                    p.next_element.attrs['title'].replace('EXISTENCIAS\\n','').split('\n')
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
            normal = str(product.contents[0].contents[1].contents[1].contents[0].contents[1].text).replace('Q','').replace(',','').strip()
        except:
            normal = str(product.contents[0].contents[1].contents[2].contents[0].text).replace('Q','').replace(',','').strip()
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

    


