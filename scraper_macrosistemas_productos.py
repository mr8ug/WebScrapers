import requests
from bs4 import BeautifulSoup


class macrosistemas_Scraper():
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

        nombre = html.find('h1', class_='title-product')
        self.nombre = nombre.text
        #self.nombre=str(nombre).replace("<h1 class=\"title-product\">\n","").replace("</h1>","").rstrip("\n")
        
        precion = html.find('span',class_="PricesalesPrice")
        self.precion = str(precion).replace("</span>","").replace("<span class=\"PricesalesPrice\">Q","").strip()

        precioe = html.find('div',class_="cash")
        self.precioe = str(precioe).replace("<div class=\"cash\"><i class=\"far fa-money-bill-alt\"></i> En efectivo: Q","").replace("</div>","").strip()

        self.subtotaln = str( float(str(self.precion).replace(",","")) * float(self.cantidad) )

        self.subtotale = str( float(str(self.precioe).replace(",","")) * float(self.cantidad) )


        img = html.find('a', class_="cloud-zoom")
        img = img.attrs['href'].replace(" ","%20")

        self.imagen =str(img)

    def getProducto(self):
        self.getData()
        self.descuento = float(str(self.precion).replace(",","")) - float(str(self.precioe).replace(",","")) * float(self.cantidad)
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

#print("\nMACROSISTEMAS")
#macrosistemas = macrosistemas_Scraper("https://www.macrosistemas.com/productos/memorias/memorias-ram/brocs,-memoria-ddr4-de-8gb-para-pc,-bus-pc3200,-3-a%C3%B1os-de-garantia-detail", "2")
#dataMacro = macrosistemas.getProducto()
#print(dataMacro['nombre'], dataMacro['precion'], dataMacro['precioe'], dataMacro['imagen'], dataMacro['subtotale'])