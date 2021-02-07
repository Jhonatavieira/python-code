from tkinter import *
from tkinter import ttk
# variavel que receber o objeto do tkinter
root = Tk()
style = ttk.Style()

# criando a class


class application():
    """O self é uma referencia á instancia atual da classe
       é usado para acessar a váriaveis dentro da classe, mas pode ser
       usado qualquer nome que não seja self.
    """

    def __init__(self):
        self.root = root
        self.style = style
        self.tela()
        self.frame_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        root.mainloop()

    def tela(self):
        # configurações e dimensionamentos da tela
        self.root.title('Cadastro de Clientes')
        self.root.configure(background='#1e3743')
        self.root.geometry('700x500')  # X x Y
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=600, height=400)

    def frame_da_tela(self):
        self.frame1 = Frame(self.root, bd=4, bg='#dfe3ee',
                            highlightbackground='#759fe6',
                            highlightthickness=3)
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame2 = Frame(self.root, bd=4, bg='#dfe3ee',
                            highlightbackground='#759fe6',
                            highlightthickness=3)
        self.frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets_frame1(self):

        # Botão limpar
        self.bt_limpar = Button(self.root, text='Limpar', bd=3,
                                bg='#107bd2', fg='white', font=('Verdana', 9, 'bold'))
        self.bt_limpar.place(relx=0.2, rely=0.09, relwidth=0.1, relheight=0.07)

        # Botão buscar
        self.bt_buscar = Button(self.root, text='Buscar',
                                bd=3, bg='#107bd2', fg='white', font=('Verdana', 9, 'bold'))
        self.bt_buscar.place(relx=0.3, rely=0.09, relwidth=0.1, relheight=0.07)

        # Botão novo
        self.bt_novo = Button(self.root, text='Novo', bd=3,
                              bg='#107bd2', fg='white', font=('Verdana', 9, 'bold'))
        self.bt_novo.place(relx=0.6, rely=0.09, relwidth=0.1, relheight=0.07)

        # Botão editar
        self.bt_alterar = Button(self.root, text='Alterar', bd=3,
                                 bg='#107bd2', fg='white', font=('Verdana', 9, 'bold'))
        self.bt_alterar.place(relx=0.7, rely=0.09,
                              relwidth=0.1, relheight=0.07)

        # Botão apagar
        self.bt_apagar = Button(self.root, text='Apagar', bd=3,
                                bg='#107bd2', fg='white', font=('Verdana', 9, 'bold'))
        self.bt_apagar.place(relx=0.8, rely=0.09, relwidth=0.1, relheight=0.07)

        # Label código do cliente
        self.lb_codigo = Label(self.frame1, text='Código',
                               bg='#dfe3ee', font=('Verdana', 9, 'bold'))
        self.lb_codigo.place(relx=0.05, rely=0.10)

        # Entry código do cliente
        self.codigo_entry = Entry(self.frame1)
        self.codigo_entry.place(relx=0.05, rely=0.19,
                                relwidth=0.10, relheight=0.10)

        # Label nome do cliente
        self.lb_nome = Label(self.frame1, text='Nome',
                             bg='#dfe3ee', font=('Verdana', 9, 'bold'))
        self.lb_nome.place(relx=0.05, rely=0.35)

        # Entry nome do cliente
        self.nome_entry = Entry(self.frame1)
        self.nome_entry.place(relx=0.05, rely=0.45,
                              relwidth=0.88, relheight=0.10)

        # Label Telefone
        self.lb_telefone = Label(
            self.frame1, text='Telefone', bg='#dfe3ee', font=('Verdana', 9, 'bold'))
        self.lb_telefone.place(relx=0.05, rely=0.60)

        # Entry telefone
        self.telefone_entry = Entry(self.frame1)
        self.telefone_entry.place(
            relx=0.05, rely=0.71, relwidth=0.44, relheight=0.10)

        # Label cidade
        self.lb_cidade = Label(self.frame1, text='Cidade',
                               bg='#dfe3ee', font=('Verdana', 9, 'bold'))
        self.lb_cidade.place(relx=0.51, rely=0.60)

        # Entry Cidade
        self.cidade_entry = Entry(self.frame1)
        self.cidade_entry.place(relx=0.51, rely=0.71,
                                relwidth=0.42, relheight=0.10)

    def lista_frame2(self):
        self.listaCli = ttk.Treeview(
            self.frame2, height=3, column=('col1', 'col2', 'col3', 'col4'))
        
        self.style.configure("Treeview", fielbackground='black')

        self.listaCli.heading("#0", text="")
        self.listaCli.heading('#1', text='Código')
        self.listaCli.heading('#2', text='Nome')
        self.listaCli.heading('#3', text='Telefone')
        self.listaCli.heading('#4', text='Cidade')

        self.listaCli.column('#0', width=1)
        self.listaCli.column('#1', width=50)
        self.listaCli.column('#2', width=200)
        self.listaCli.column('#3', width=125)
        self.listaCli.column('#4', width=125)

        self.listaCli.place(relx=0.01, rely=0.01,
                            relwidth=0.95, relheight=0.85)

        self.scrollList = Scrollbar(self.frame2, orient='vertical')
        self.listaCli.configure(yscroll=self.scrollList.set)
        self.scrollList.place(relx=0.96, rely=0.02,
                              relwidth=0.04, relheight=0.85)

        


application()
