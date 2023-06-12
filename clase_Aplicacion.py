from tkinter import*
from tkinter import ttk, messagebox
class Aplicacion():
    __ventana = None
    __costo_canasta_anio_actual = None
    __costo_canasta_anio_base = None
    __cantidad = None
    __vestimenta = None
    __alimentos = None
    __educacion = None
    __total = None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('400x150')
        self.__ventana.title('Calculadora IPC')
        mainframe = ttk.Frame(self.__ventana, padding='3 3 12 12')
        mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0,weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__costo_canasta_anio_actual = StringVar()
        self.__costo_canasta_anio_base = StringVar()
        self.__cantidad = StringVar()
        self.__vestimenta = StringVar()
        self.__alimentos = StringVar()
        self.__educacion = StringVar()
        #Diseño los botones y cuadros de texto
        self.__costo_canasta_anio_actual_entry = ttk.Entry(mainframe, width=5, textvariable=self.__costo_canasta_anio_actual)
        self.__costo_canasta_anio_actual_entry.grid(row=1, column=3, sticky=(W,E))
        self.__costo_canasta_anio_actual_entry = ttk.Entry(mainframe, width=5, textvariable=self.__costo_canasta_anio_actual)
        self.__costo_canasta_anio_actual_entry.grid(row=2, column=3, sticky=(W,E))
        self.__costo_canasta_anio_actual_entry = ttk.Entry(mainframe, width=5, textvariable=self.__costo_canasta_anio_actual)
        self.__costo_canasta_anio_actual_entry.grid(row=3, column=3, sticky=(W,E))
        self.__costo_canasta_anio_base_entry = ttk.Entry(mainframe, width=5, textvariable=self.__costo_canasta_anio_base)
        self.__costo_canasta_anio_base_entry.grid(row=1, column=2, sticky=(W , E))
        self.__costo_canasta_anio_base_entry = ttk.Entry(mainframe, width=5, textvariable=self.__costo_canasta_anio_base)
        self.__costo_canasta_anio_base_entry.grid(row=2, column=2, sticky=(W , E))
        self.__costo_canasta_anio_base_entry = ttk.Entry(mainframe, width=5, textvariable=self.__costo_canasta_anio_base)
        self.__costo_canasta_anio_base_entry.grid(row=3, column=2, sticky=(W , E))
        self.__cantidad_entry = ttk.Entry(mainframe, width=5, textvariable=self.__cantidad)
        self.__cantidad_entry.grid(row=1, column=1, sticky=(W,E))
        self.__vestimenta_entry = ttk.Entry(mainframe, width=5, textvariable=self.__vestimenta)
        self.__vestimenta_entry.grid(row=1, column=2, sticky=(W,E))
        self.__alimentos_entry = ttk.Entry(mainframe, width=5, textvariable=self.__alimentos)
        self.__alimentos_entry.grid(row=2, column=1, sticky=(W,E))
        self.__educacion_entry = ttk.Entry(mainframe, width=5, textvariable=self.__educacion)
        self.__educacion_entry.grid(row=3, column=1, sticky=(W,E))
        ttk.Button(mainframe, text='Calcular IPC', command=self.formula).grid(row=4, column=1, sticky=E)
        ttk.Button(mainframe, text='Salir', command=self.__ventana.destroy).grid(row=4, column=3, sticky=W)
        #Diseño el objeto costo canasta_año_actual
        #Diseño el objeto costo canasta_año_base
        ttk.Label(mainframe, text='Item').grid(row=0, column=0, sticky=E)
        ttk.Label(mainframe, text='Cantidad').grid(row=0,column=1, sticky=W)
        ttk.Label(mainframe, text='Costo año actual').grid(row=0,column=3, sticky=W)
        ttk.Label(mainframe, text='Costo año base').grid(row=0, column=2, sticky=W)
        ttk.Label(mainframe, text='IPC %').grid(column=0, row=6, sticky=E)
        ttk.Label(mainframe, text='Vestimenta').grid(row=1, column=0, sticky=E)
        ttk.Label(mainframe, text='Alimentos').grid(row=2, column=0, sticky=E)
        ttk.Label(mainframe, text='Educacion').grid(row=3, column=0, sticky=E)
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
            self.__costo_canasta_anio_actual_entry.focus()
            self.__costo_canasta_anio_base_entry.focus()
            self.__cantidad_entry.focus()
            self.__vestimenta_entry.focus()
            self.__alimentos_entry.focus()
            self.__educacion_entry.focus()
            self.__ventana.mainloop()
    def formula(self):
        try:
            valor = int(self.__costo_canasta_anio_actual_entry.get())
            valor2 = int(self.__costo_canasta_anio_base_entry.get())
            valor3 = int(self.__cantidad.get())
            self.__vestimenta.get()
            self.__alimentos.get()
            self.__educacion.get()
            IPC = valor3 * valor
            IPC = valor3 * valor2
            self.__total.set(IPC * 100)
        except ValueError:
            messagebox.showerror(title='Error de tipo', message='Ingrese un año valido')
            self.__costo_canasta_anio_actual.set("")
            self.__costo_canasta_anio_base.set("")
            self.__cantidad.set("")
            self.__vestimenta.set("")
            self.__alimentos.set("")
            self.__educacion.set("")
            self.__costo_canasta_anio_actual_entry.focus()
            self.__costo_canasta_anio_base_entry.focus()
            self.__cantidad_entry.focus()
