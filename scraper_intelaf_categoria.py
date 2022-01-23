import requests
from bs4 import BeautifulSoup


class categoria():
    def __init__(self, url, cat, img):
        self.url = url
        self.nombre = cat
        self.imagen = img


    def getCategoria(self):
        categoria={
            'url':self.url,
            'nombre':self.nombre, 
            'imagen':self.imagen     
        }
        
        return categoria


    
        
        

class subcategoria():
    def __init__(self, url, sub, padre):
        self.url = url
        self.nombre = sub,
        self.categoria_padre = padre

    def getSubCategoria(self):
        subcategoria={
            'url' : self.url,
            'nombre' : self.nombre,
            'padre' : self.categoria_padre
        }
        return subcategoria
        

class producto():
    def __init__(self, url, nombre, precion, precioe, img, existencias):
        self.url = url
        self.nombre = nombre
        self.precion = precion
        self.precioe = precioe
        self.img = img
        self.existencia = existencias

    def getProducto(self):
        producto={
            'url':self.url,
            'nombre':self.nombre, 
            'precion':self.precion, 
            'precioe':self.precioe,
            'imagen':self.imagen,
            'existencia':self.existencia           
        }

        return producto
        
class intelaf_Categoria():
    def __init__(self):

        #obtendremos todas las categorias no mas se ejecute la clase
        self.categorias = []
        self.subcategorias = []
        self.productos = []

        self.loadData()


        
    def loadData(self):
        lista_subExistentes = []
        response = requests.get("https://www.intelaf.com/Menu_areas.aspx?area=Componentes%20PCs&nivel=0")

        html  = BeautifulSoup(response.text, 'html.parser')

        
        categorias = html.findAll('div', class_='col-xs-6 col-sm-4 col-md-3')
        
        list_cat = []

        for c in categorias:
            list_cat.append([
                c.contents[0].attrs['href'], 
                c.contents[0].contents[0].next.attrs['title'], 
                c.contents[0].contents[0].next.attrs['style'] 
            ])

        for lc in list_cat:
            imgLink = ''
            fiximg = str(lc[2]).split(';')
            for f in fiximg:
                if str(f).startswith('background-image: url'):
                    imgLink = str(f).replace('background-image: url(\"','').replace('.jpg\")','')
                    break

            imgLink = imgLink + '.jpg'

            self.categorias.append(categoria('https://intelaf.com/' + str(lc[0]), str(lc[1]) , 'https://intelaf.com/' + imgLink.replace(' ','%20')))
            lista_subExistentes.append('https://intelaf.com/' + str(lc[0]))
        #for c in self.categorias:
        #    print(c.getCategoria())

        #categorias manuales

        self.categorias.append(categoria('https://www.intelaf.com/Precios_stock_resultado.aspx?area=TODOS-SSD', 'SSD', 'https://www.intelaf.com/img/menu_img/Unidad%20de%20estado%20solido%20ssd.jpg'))
        lista_subExistentes.append('https://www.intelaf.com/Precios_stock_resultado.aspx?area=TODOS-SSD')

        #######################################obtencion de subcategorias
        
        #print('Nivel 1')
        for c in self.getCategorias():
            response = requests.get(str(c.url))

            html  = BeautifulSoup(response.text, 'html.parser')

            
            subcategorias = html.findAll('div', class_='col-xs-6 col-sm-4 col-md-3')

            if len(subcategorias) != 0:

                list_sub = []

                for s in subcategorias:
                    
                    list_sub.append([
                        s.contents[0].attrs['href'], 
                        s.contents[0].contents[0].next.next, 
                    ])
                    
                for ls in list_sub:
                    self.subcategorias.append(subcategoria('https://intelaf.com/' + str(ls[0]), str(ls[1]), c ))

                    #agrega la subcategoria para luego comparar su existencia en el nivel 2
                    lista_subExistentes.append('https://intelaf.com/' + str(ls[0]))
                #print(list_sub)
        print('SC Nivel 1',len(self.subcategorias))
        ####obtencion de subcategorias nivel 2
        #print('Nivel 2')
        for c in self.getSubCategorias():           
            if str(c.url) not in lista_subExistentes:
                response = requests.get(str(c.url))

                html  = BeautifulSoup(response.text, 'html.parser')

                
                subcategorias = html.findAll('div', class_='col-xs-6 col-sm-4 col-md-3')

                if len(subcategorias) != 0:

                    list_sub = []

                    for s in subcategorias:
                        
                        list_sub.append([
                            s.contents[0].attrs['href'], 
                            s.contents[0].contents[0].next.next
                        ])
                        
                    for ls in list_sub:
                        self.subcategorias.append(subcategoria('https://intelaf.com/' + str(ls[0]), str(ls[1]), c ))
                        #agrega la subcategoria para luego comparar su existencia en el nivel 2
                        lista_subExistentes.append('https://intelaf.com/' + str(ls[0]))
                    #print(list_sub)
        print('SC Nivel 2',len(self.subcategorias))
        ####obtencion de subcategorias nivel 3
        for c in self.getSubCategorias():           
            if str(c.url) not in lista_subExistentes:
                response = requests.get(str(c.url))

                html  = BeautifulSoup(response.text, 'html.parser')

                
                subcategorias = html.findAll('div', class_='col-xs-6 col-sm-4 col-md-3')

                if len(subcategorias) != 0:

                    list_sub = []

                    for s in subcategorias:
                        
                        list_sub.append([
                            s.contents[0].attrs['href'], 
                            s.contents[0].contents[0].next.next
                        ])
                        
                    for ls in list_sub:
                        self.subcategorias.append(subcategoria('https://intelaf.com/' + str(ls[0]), str(ls[1]), c ))
                        #agrega la subcategoria para luego comparar su existencia en el nivel 2
                        lista_subExistentes.append('https://intelaf.com/' + str(ls[0]))
        #for c in self.subcategorias:
        #   print(c.getSubCategoria())
        print('SC Nivel 3',len(self.subcategorias))
        #print(lista_subExistentes)


    def getCategorias(self):
        return self.categorias

    def getSubCategorias(self):
        return self.subcategorias

    def getProductos(self):
        return self.productos
        

i = intelaf_Categoria()