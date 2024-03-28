class Biblioteca:
    
    def __init__(self):
        self.catalogo = []
        
    def agregar_libro(self, Libro):
        self.catalogo.append(Libro)
        
    def mostrar_catalogo(self):
        
        if self.catalogo:
            print('Catalogo de libros')
            
            for i in self.catalogo:
                print(i)
                
        else: 
            print("el catalogo está vacio")
        

class Libro:
    
    titulo = ''
    autor = ''
    genero = ''
    disponibilidad = True
    
    def __init__(self,titulo, autor, genero, disponibilidad):
        
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.disponibilidad = disponibilidad
        
    def __str__(self):
        
        disponibilidad = "Disponible" if self.disponibilidad else "No disponible"
        return f"Título: {self.titulo}, Autor: {self.autor}, Género: {self.genero}, Disponibilidad: {disponibilidad}"

        
    def prestar(self):
        
        self.disponibilidad = False
        
    def devolver(self):
        self.disponibilidad = True
        
    def imprimir_valores(self):
        lista = {'titulo': self.titulo, 'autor': self.autor, 'genero': self.genero, 'disponibilidad': self.disponibilidad}
        print(lista)
        
        
bibliotecaa = Biblioteca()
librocreado = Libro('El principito', 'antonie de Saint', 'fabula', True)
l2 = Libro('Metamorfosis', 'Franz Kafka', 'Novela corta', True)
l3 = Libro('Psicologia Oscura', 'Steve Turner', 'Libro de auto ayuda', True)
l4 = Libro('Cien años de soledad', 'Gabriel Garcia Marquez', 'Novela', True)
l5 = Libro('Habitos Atomicos', 'James Clear', 'Libro de auto ayuda', True)

bibliotecaa.agregar_libro(librocreado)
bibliotecaa.agregar_libro(l2)
bibliotecaa.agregar_libro(l3)
bibliotecaa.agregar_libro(l4)
bibliotecaa.agregar_libro(l5)    
    
while True:
    print('''
        
    ██████╗░██╗██████╗░██╗░░░░░██╗░█████╗░████████╗███████╗░█████╗░░█████╗░
    ██╔══██╗██║██╔══██╗██║░░░░░██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██╔══██╗
    ██████╦╝██║██████╦╝██║░░░░░██║██║░░██║░░░██║░░░█████╗░░██║░░╚═╝███████║
    ██╔══██╗██║██╔══██╗██║░░░░░██║██║░░██║░░░██║░░░██╔══╝░░██║░░██╗██╔══██║
    ██████╦╝██║██████╦╝███████╗██║╚█████╔╝░░░██║░░░███████╗╚█████╔╝██║░░██║
    ╚═════╝░╚═╝╚═════╝░╚══════╝╚═╝░╚════╝░░░░╚═╝░░░╚══════╝░╚════╝░╚═╝░░╚═╝

    ██╗░░░██╗██╗██████╗░████████╗██╗░░░██╗░█████╗░██╗░░░░░
    ██║░░░██║██║██╔══██╗╚══██╔══╝██║░░░██║██╔══██╗██║░░░░░
    ╚██╗░██╔╝██║██████╔╝░░░██║░░░██║░░░██║███████║██║░░░░░
    ░╚████╔╝░██║██╔══██╗░░░██║░░░██║░░░██║██╔══██║██║░░░░░
    ░░╚██╔╝░░██║██║░░██║░░░██║░░░╚██████╔╝██║░░██║███████╗
    ░░░╚═╝░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚══════╝
        
        Bienvenido a la biblioteca virtual
    ''')

    bibliotecaa.mostrar_catalogo()

    print('''

        pedir prestado libro       (1)
        devolver libro             (2)
        agregar un libro           (3)
        salir de la biblioteca     (4)
        
    ''')
    option = int(input('digite el numero de la opcion: '))
    
    if option == 1:
        while True:
            busqueda = str(input('digite el titulo del libro: '))
            
            if busqueda in librocreado.titulo:
                print(f'deseas sacar el libro {librocreado.titulo}?')
                
                opt = str(input('si o no: '))
                opt.lower()
                if opt == 'si':
                    librocreado.prestar()
                    print(f'El libro {librocreado.titulo} se ha prestado correctamente')
                    break
                if opt == 'no':
                    break
                
            
            elif busqueda in l2.titulo:
                print(f'deseas sacar el libro {l2.titulo}?')
                
                opt = str(input('si o no: '))
                opt.lower()
                if opt == 'si':
                    l2.prestar()
                    print(f'El libro {l2.titulo} se ha prestado correctamente')
                    break
                if opt == 'no':
                    break
            
            elif busqueda in l3.titulo:
                print(f'deseas sacar el libro {l3.titulo}?')
                opt = str(input('si o no: '))
                opt.lower()
                if opt == 'si':
                    l3.prestar()
                    print(f'El libro {l3.titulo} se ha prestado correctamente')
                    break
                if opt == 'no':
                    break
            
            elif busqueda in l4.titulo:
                print(f'deseas sacar el libro {l4.titulo}?')
                opt = str(input('si o no: '))
                opt.lower()
                if opt == 'si':
                    l4.prestar()
                    print(f'El libro {l4.titulo} se ha prestado correctamente')
                    break
                if opt == 'no':
                    break

            elif busqueda in l5.titulo:
                print(f'deseas sacar el libro {l5.titulo}?')
                opt = str(input('si o no: '))
                opt.lower()
                if opt == 'si':
                    l5.prestar()
                    print(f'El libro {l5.titulo} se ha prestado correctamente')
                    break
                if opt == 'no':
                    break
            
            else:
                error1 = str(input('libro no encontrado. desea buscar otro libro? si o no: '))
                error1.lower()
                if error1 == 'no':
                    break
                if error1 == 'no':
                    pass 
    elif option == 2:
        while True:
            busqueda = str(input('digite el titulo del libro: '))
            
            if busqueda in librocreado.titulo:
                print(f'deseas devolver el libro {librocreado.titulo}?')
                
                opt = str(input('si o no: '))
                opt.lower()
                if opt == 'si':
                    librocreado.devolver()
                    print(f'El libro {librocreado.titulo} se ha devuelto correctamente')
                    break
                if opt == 'no':
                    break
                
            
            elif busqueda in l2.titulo:
                print(f'deseas devolver el libro {l2.titulo}?')
                
                opt = str(input('si o no: '))
                opt.lower()
                if opt == 'si':
                    l2.devolver()
                    print(f'El libro {l2.titulo} se ha devuelto correctamente')
                    break
                if opt == 'no':
                    break
            
            elif busqueda in l3.titulo:
                print(f'deseas devolver el libro {l3.titulo}?')
                opt = str(input('si o no: '))
                opt.lower()
                if opt == 'si':
                    l3.devolver()
                    print(f'El libro {l3.titulo} se ha devuelto correctamente')
                    break
                if opt == 'no':
                    break
            
            elif busqueda in l4.titulo:
                print(f'deseas devolver el libro {l4.titulo}?')
                opt = str(input('si o no: '))
                opt.lower()
                if opt == 'si':
                    l4.devolver()
                    print(f'El libro {l4.titulo} se ha devuelto correctamente')
                    break
                if opt == 'no':
                    break

            elif busqueda in l5.titulo:
                print(f'deseas devolver el libro {l5.titulo}?')
                opt = str(input('si o no: '))
                opt.lower()
                if opt == 'si':
                    l5.devolver()
                    print(f'El libro {l5.titulo} se ha prestado correctamente')
                    break
                if opt == 'no':
                    break
            
            else:
                error1 = str(input('libro no registrado. desea volver a intentar? si o no: '))
                error1.lower()
                if error1 == 'no':
                    break
                if error1 == 'no':
                    pass 
    elif option == 3:
        librocreado = Libro('','','',True)
        librocreado.titulo = str(input("digite el titulo: "))
        librocreado.autor = str(input("digite el autor: "))
        librocreado.genero = str(input("digite el genero: "))
        
        bibliotecaa.agregar_libro(librocreado)
        print(f'El libro {librocreado.titulo} se ha agregado al catalogo ')
    elif option == 4:
        break
        

          




# if opcion == 'si':


    
    

    
    




        
    
    
    
 