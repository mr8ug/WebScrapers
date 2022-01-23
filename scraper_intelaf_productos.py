
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
        self.nombre=str(nombre).replace("<h1 class=\"descripcion_p\">","").replace("</h1>","").rstrip("\n")
        
        precion = html.find('p', class_="precio_normal")
        self.precion = str(precion).replace("<p class=\"precio_normal\"> Precio normal <strong> Q","").replace("</strong></p>","").strip()

        precioe = html.find('p',class_="beneficio_efectivo")
        precioe = str(precioe).replace("<p class=\"beneficio_efectivo\" style=\"color: darkorange; font-weight: bold;\"> Beneficio Efectivo","").replace("</p>","").strip()
        precioe = str(precioe).split("Q")
        self.precioe = str(precioe[1])


        self.subtotaln = str( float(str(self.precion).replace(",","")) * float(self.cantidad) )

        self.subtotale = str( float(str(self.precioe).replace(",","")) * float(self.cantidad) )

        img = html.find('div',class_="col-xs-12 col-md-6")
        img = img.attrs['style'].split("url(\"")
        img = img[1].split(".jpg\");")
        self.imagen = str("https://www.intelaf.com/"+img[0]+'.jpg')

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




#print("\nINTELAF")
#intelaf = intelaf_Scraper("https://www.intelaf.com/precios_stock_detallado.aspx?codigo=CAM-NXT-SMW4U2", "2")
#dataIntelaf = intelaf.getProducto()
#print(dataIntelaf['nombre'], dataIntelaf['precion'], dataIntelaf['precioe'], dataIntelaf['imagen'])


