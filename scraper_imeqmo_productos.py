import requests
from bs4 import BeautifulSoup


class imeqmo_Scraper():
    def __init__(self,url, cantidad):
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

        nombre = html.find('h1', class_='te_product_name')
        self.nombre = nombre.text
        #self.nombre=str(nombre).replace("<h1 class=\"te_product_name\" itemprop=\"name\">","").replace("</h1>","").rstrip("\n")
        
        

        precioe = html.find('b',class_="oe_price")
        precioe = str(precioe).split("<span class=\"oe_currency_value\">")
        self.precioe = str(precioe[1]).replace("</span></b>","")

        try:
            precion = html.find('span',class_="text-danger oe_default_price")
            precion = str(precion).split("class=\"oe_currency_value\">")
            self.precion = str(precion[1]).replace("</span>","")
        except:
            self.precion = self.precioe

        self.subtotaln = str( float(str(self.precion).replace(",","")) * float(self.cantidad) )

        self.subtotale = str( float(str(self.precioe).replace(",","")) * float(self.cantidad) )

        img = html.find('img', class_="img img-fluid product_detail_img")
        img = img.attrs['src'].replace("\"","")
        self.imagen = str("https://www.imeqmo.com" + str(img))


        

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


#print("\nIMEQMO")
#imeqmo = imeqmo_Scraper("https://www.imeqmo.com/shop/product/bx8070110100f-procesador-intel-core-i3-10100f-3-6ghz-10th-gen-13250?category=11", "2")
#dataImeqmo = imeqmo.getProducto()
#print(dataImeqmo['nombre'], dataImeqmo['precion'], dataImeqmo['precioe'], dataImeqmo['imagen'], dataImeqmo['subtotale'])

