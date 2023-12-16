class SistemaExpertoComida:
    def __init__(self):
        self.respuestas = {}
        self.tipos_comida = {
            'Ensalada': ['Ensalada César', 'Ensalada de quinoa', 'Ensalada de aguacate'],
            'Tacos': ['Tacos al pastor', 'Tacos de carne asada', 'Tacos de pescado'],
            'Helado': ['Chocolate', 'Vainilla', 'Fresa'],
            'Ligero': ['Calabaza rellena de quesillo', 'Picadillo a la mexicana', 'Caldo de res'],
            'Hamburguesa': ['Hamburguesa clásica', 'Hamburguesa vegetariana', 'Hamburguesa con queso']
        }
        
        # Dividir la comida segun si es desayuno, comida o cena

    def hacer_pregunta(self, pregunta):
        respuesta = input(pregunta + " (Sí/No): ").lower()
        return respuesta == 's' or respuesta == 'si'

    def obtener_preferencias(self):
        print("¡Bienvenido a RecomendeitorTragon3000!, favor de responder algunas preguntas para obtener una recomendación.")
        
        #Agregar la pregunta si es desayuno, comida o cena
        self.respuestas['vegetariano'] = self.hacer_pregunta("¿Eres vegetariano/a?")
        self.respuestas['picante'] = self.hacer_pregunta("¿Te gusta la comida picante?")
        self.respuestas['dulce'] = self.hacer_pregunta("¿Prefieres platos dulces?")
        self.respuestas['salado'] = self.hacer_pregunta("¿Te gustan los platos salados?")
        self.respuestas['ligero'] = self.hacer_pregunta("¿Prefieres comidas ligeras?")

    def recomendar_comida(self):
        categoria = "Desconocido"

        '''Agregar a las reglas si es desayuno, comida o cena para cada comida, segun las respuestas y valoraciones segun quien
        esta programando esta wea porque para alguien un platillo puede ser adecuado para los tres o solo para uno
        otro puede opinar lo contrario y asi diceversa.'''
        
        if self.respuestas['vegetariano']:
            categoria = 'Ensalada'
        elif self.respuestas['picante'] and self.respuestas['salado']:
            categoria = 'Tacos'
        elif self.respuestas['dulce'] and not self.respuestas['salado']:
            categoria = 'Helado'
        elif self.respuestas['ligero']:
            categoria = 'Ligero'
        else:
            categoria = 'Hamburguesa'

        platillos = self.tipos_comida.get(categoria, [])
        if platillos:
            print(f"¡Recomendación de comida para ti: {categoria}!")
            print("Platillos recomendados:")
            for platillo in platillos:
                print(f"- {platillo}")
        else:
            print("No se encontraron platillos para la categoría seleccionada.")

# Uso del sistema experto
sistema = SistemaExpertoComida()
sistema.obtener_preferencias()
sistema.recomendar_comida()