import tkinter as tk

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
        self.root = tk.Tk()
        self.root.title("Sistema experto - Recomendador de comida.")
        self.preguntas = [
            "¿Eres vegetariano/a?",
            "¿Te gusta la comida picante?",
            "¿Te gustan los platos salados?",
            "¿Prefieres platos dulces?",
            "¿Prefieres comidas ligeras?"
        ]
        self.recomendacion_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.bienvenida_label_1 = tk.Label(self.root, text="¡Bienvenido a RecomendeitorTragon3000!", font=("Helvetica", 16))
        self.bienvenida_label_2 = tk.Label(self.root, text="Favor de responder algunas preguntas para obtener una recomendación.", font=("Helvetica", 16))
        self.bienvenida_label_1.pack()
        self.bienvenida_label_2.pack()
        self.crear_interfaz()

    def hacer_pregunta(self, pregunta):
        respuesta = tk.StringVar()
        frame = tk.Frame(self.root)
        label = tk.Label(frame, text=pregunta, font=("Helvetica", 14))
        label.pack()
        btn_si = tk.Button(frame, text="Sí", command=lambda: self.guardar_respuesta(respuesta, 'Sí', frame), font=("Helvetica", 14))
        btn_no = tk.Button(frame, text="No", command=lambda: self.guardar_respuesta(respuesta, 'No', frame), font=("Helvetica", 14))
        label.pack(side="left")
        btn_si.pack(side="left")
        btn_no.pack(side="left")
        frame.pack()
        self.root.wait_window(frame)
        return respuesta.get()

    def guardar_respuesta(self, variable, valor, frame):
        variable.set(valor)
        frame.destroy()

    def crear_interfaz(self):
        for pregunta in self.preguntas:
            self.respuestas[pregunta] = self.hacer_pregunta(pregunta)

        self.mostrar_recomendacion()

    def mostrar_recomendacion(self):
        self.bienvenida_label_1.pack_forget()
        self.bienvenida_label_2.pack_forget()

        categoria = "Desconocido"
        if self.respuestas["¿Eres vegetariano/a?"] == 'Sí':
            categoria = 'Ensalada'
        elif self.respuestas["¿Te gusta la comida picante?"] == 'Sí' and self.respuestas["¿Te gustan los platos salados?"] == 'Sí':
            categoria = 'Tacos'
        elif self.respuestas["¿Prefieres platos dulces?"] == 'Sí' and self.respuestas["¿Te gustan los platos salados?"] == 'No':
            categoria = 'Helado'
        elif self.respuestas["¿Prefieres comidas ligeras?"] == 'Sí':
            categoria = 'Ligero'
        else:
            categoria = 'Hamburguesa'

        platillos = self.tipos_comida.get(categoria, [])
        recomendacion = f"¡Recomendación de  comida para ti: {categoria}!\nPlatillos recomendados:\n"
        for platillo in platillos:
            recomendacion += f"- {platillo}\n"

        self.recomendacion_label.config(text=recomendacion, font=("Helvetica", 14))
        self.recomendacion_label.pack()

        # Agregar botones para reiniciar o cerrar
        reiniciar_btn = tk.Button(self.root, text="Reiniciar", command=self.reiniciar, font=("Helvetica", 14))
        reiniciar_btn.pack(side="left")
        cerrar_btn = tk.Button(self.root, text="Cerrar", command=self.cerrar, font=("Helvetica", 14))
        cerrar_btn.pack(side="right")
        
    def reiniciar(self):
        self.root.destroy()
        self.__init__()

    def cerrar(self):
        self.root.destroy()
            
    def ejecutar_interfaz(self):
        self.root.mainloop()

# Uso del sistema experto
sistema = SistemaExpertoComida()
sistema.ejecutar_interfaz()