
import requests
from bs4 import BeautifulSoup


############INTELAF##################################################################################################
class intelaf_Scraper():
    def __init__(self,url,cantidad):
        self.url = url
        self.nombre = ''
        self.precion = ''
        self.precioe = ''
        self.descuento = ''
        self.cantidad=str(cantidad)
        self.subtotaln=''
        self.subtotale=''
        self.imagen=''
        


    def getData(self):

        response = requests.get(self.url)

        html  = BeautifulSoup(response.text, 'html.parser')

        nombre = html.find('h1', class_='descripcion_p')
        #self.nombre = nombre.text
        self.nombre=nombre.text
        
        precion = html.find('div', class_="col-xs-12 col-md-7 detalle_venta")
        for attr in precion.contents:
            if attr.text.startswith('Precio normal Q'):
                self.precion = str(attr.text).replace('Precio normal Q','')

            if attr.text.startswith('Beneficio Efectivo Q'):
                self.precioe = str(attr.text).replace('Beneficio Efectivo Q','')
            if attr.text.startswith('Semana Razer Q'):
                self.precioe = str(attr.text).replace('Semana Razer Q','')
            if attr.text.startswith('TecnoPromo: Q'):
                self.precioe = str(attr.text).replace('TecnoPromo: Q','')
            if attr.text.startswith('Promo Office: Q'):
                self.precioe = str(attr.text).replace('Promo Office: Q','')


        


        self.subtotaln = str( float(str(self.precion).replace(",","")) * float(self.cantidad) )

        self.subtotale = str( float(str(self.precioe).replace(",","")) * float(self.cantidad) )

        img = html.find('div',class_="col-xs-12 col-md-5")
        img = img.attrs['style'].split("url(\"")
        img = img[1].split(".jpg\");")
        self.imagen = str(img[0]+'.jpg')

    def getProducto(self):
        self.getData()
        self.descuento = (float(str(self.precion).replace(",","")) - float(str(self.precioe).replace(",","")) ) * float(self.cantidad)
        producto={
            'nombre':self.nombre, 
            'precion':self.precion, 
            'precioe':self.precioe,
            'descuento':str(self.descuento),
            'cantidad':self.cantidad,
            'imagen':self.imagen,
            'subtotaln':self.subtotaln,
            'subtotale':self.subtotale,
            'link':self.url
        }
        return producto




#print("\nINTELAF")
#intelaf = intelaf_Scraper("https://www.intelaf.com/precios_stock_detallado.aspx?codigo=AUDF-RAZ-TETST", "2")
#dataIntelaf = intelaf.getProducto()
#print(dataIntelaf['nombre'], dataIntelaf['precion'], dataIntelaf['precioe'], dataIntelaf['imagen'], dataIntelaf['subtotale'])


