from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import sqlite3

mw = Tk()
mw.geometry("400x700")
mw.title('Central de Alunos')

#Database

conn = sqlite3.connect('Aluno_info.db')

c = conn.cursor()

#TABLE

c.execute("""CREATE TABLE IF NOT EXISTS info (
        nome text,
        CPF text,
        data text,
        unidade text,
        curso text
        )""")


#IMAGEM
imagem = Image.open("Senac_logo.png")
imagem1= imagem.resize((70, 50), Image.LANCZOS)
imagemt= ImageTk.PhotoImage(imagem1)
senac = Label(mw,image=imagemt)
senac.place(x=160,y=10)
senacl = Label(mw,text="")
senacl.grid(row=0,column=0,sticky="w",pady=35)


#MANDAR DADOS PRA DATABASE

def vai():
    conn = sqlite3.connect('Aluno_info.db')
    c = conn.cursor()

    c.execute("INSERT INTO info VALUES (:NOME, :CPF, :DATA, :UNIDADE, :CURSO)",
              {
                  'NOME': cad_nome.get(),
                  'CPF': cad_cpf.get(),
                  'DATA': cad_data.get(),
                  'UNIDADE': cad_uni.get(),
                  'CURSO': cad_cur.get()
              })
    cad.destroy()


    conn.commit()

    conn.close()

def delet():
    conn = sqlite3.connect('Aluno_info.db')
    c = conn.cursor()


    c.execute("DELETE from info WHERE oid=" + nmd.get())

    dele.destroy()


    conn.commit()

    conn.close()

def consult():
    conn = sqlite3.connect('Aluno_info.db')
    c = conn.cursor()

    cons=Tk()
    cons.title('Informações do Aluno')
    canva1 = Canvas(cons, bg="#1150af", width=475, height=100).place(x=0, y=0)
    Label(cons, text="Informações do Aluno", bg="#1150af", fg="#f9970c", font=50).grid(row=1, padx=15, pady=37)
    fl6=LabelFrame(cons,padx=5,pady=5)
    fl6.grid(padx=10,pady=10)

    c.execute("SELECT *, oid FROM info WHERE oid=" + nmd1.get())
    dados = c.fetchall()

    print_nome = ""
    print_cpf = ""
    print_data = ""
    print_unidade = ""
    print_curso = ""
    print_mat = ""
    for dado in dados:
        print_nome += str(dado[0]) + "\n"
        print_cpf += str(dado[1]) + "\n"
        print_data += str(dado[2]) + "\n"
        print_unidade += str(dado[3]) + "\n"
        print_curso += str(dado[4]) + "\n"
        print_mat += str(dado[5]) + "\n"

    nl = Label(fl6,text='Nome',fg='#030303',font=20)
    nl.grid(row=0,column=0,padx=5,pady=5,sticky="w")
    n = Label(fl6,text=print_nome)
    n.grid(row=1,column=0,padx=5,pady=0,sticky="w")
    dl = Label(fl6,text='Data de Nascimento',fg='#030303',font=20)
    dl.grid(row=2,column=0,padx=5,pady=(10,5),sticky="w")
    d = Label(fl6,text=print_data)
    d.grid(row=3,column=0,padx=5,pady=0,sticky="w")
    ml = Label(fl6,text='Matrícula',fg='#030303',font=12)
    ml.grid(row=4,column=0,padx=5,pady=(10,5),sticky="w")
    m = Label(fl6,text=print_mat)
    m.grid(row=5,column=0,padx=5,pady=0,sticky="w")
    cpfl = Label(fl6,text='CPF',fg='#030303',font=12)
    cpfl.grid(row=0,column=1,padx=10,pady=5,sticky="w")
    cpf = Label(fl6,text=print_cpf)
    cpf.grid(row=1,column=1,padx=10,pady=0,sticky="w")
    ul = Label(fl6,text='Unidade',fg='#030303',font=12)
    ul.grid(row=2,column=1,padx=10,pady=(10,5),sticky="w")
    u = Label(fl6,text=print_unidade)
    u.grid(row=3,column=1,padx=10,pady=0,sticky="w")
    curl = Label(fl6,text='Curso',fg='#030303',font=12)
    curl.grid(row=4,column=1,padx=10,pady=(10,5),sticky="w")
    cur = Label(fl6,text=print_curso)
    cur.grid(row=5,column=1,padx=10,pady=0,sticky="w")

    con.destroy()

    conn.commit()

    conn.close()



#def pega():
 #   conn = sqlite3.connect('Aluno_info.db')
  #   c = conn.cursor()
#
 #   c.execute("SELECT *, oid FROM info")
  #  dados = c.fetchall()
 #   print(dados)


 #   conn.commit()

  #  conn.close()

def cadastrar():
    global cad
    global cad_nome
    global cad_cpf
    global cad_data
    global cad_uni
    global cad_cur

    cad = Tk()
    cad.geometry("475x330")
    cad.title('Cadastro de Alunos')
    canva1 = Canvas(cad, bg="#1150af", width=475, height=100).place(x=0, y=0)
    Label(cad,text="Insira as informações do aluno",bg="#1150af",fg="#f9970c",font=50).grid(row=1,padx=15,pady=37)
    lf1 = LabelFrame(cad,text='dados',padx=7,pady=7)
    lf1.grid(row=2,column=0,sticky="w",padx=10,pady=20,columnspan=2)
    cad_nomel = Label(lf1,text='Nome:')
    cad_nomel.grid(row=0,column=0,sticky="w")
    cad_nome = Entry(lf1)
    cad_nome.grid(row=0,column=1,sticky="w")
    cad_cpfl = Label(lf1, text='CPF:')
    cad_cpfl.grid(row=1, column=0, sticky="w")
    cad_cpf = Entry(lf1)
    cad_cpf.grid(row=1, column=1, sticky="w")
    cad_datal = Label(lf1, text='Nascimento:')
    cad_datal.grid(row=0, column=2,columnspan=2, sticky="w",padx=10)
    cad_data = Entry(lf1)
    cad_data.grid(row=0, column=3, sticky="w",padx=0)
    cad_unil = Label(lf1,text="Unidade:")
    cad_unil.grid(row=2,column=0,sticky="w",pady=10)
    var=StringVar()
    cad_uni = ttk.Combobox(lf1, textvariable=var)
    cad_uni['values'] = ["Lavras","Varginha","Nepomuceno"]
    cad_uni['state'] = 'readonly'
    cad_uni.grid(row=2,column=1,pady=10)
    cad_curl = Label(lf1,text='Curso:')
    cad_curl.grid(row=2,column=2,sticky="w",padx=30,pady=10)
    var1=StringVar()
    cad_cur = ttk.Combobox(lf1,textvariable=var1)
    cad_cur['values'] = ["Programação(o melhor)","Outro Curso"]
    cad_cur.grid(row=2,column=3,sticky="w",pady=10,padx=0)
    cadast=Button(cad,text="Cadastar",command=vai,bg="#1150af",foreground="white",activebackground="#f9970c",width=6,height=1)
    cadast.grid(row=3,padx=40,sticky="w")
    volt=Button(cad,command=cad.destroy,text='Voltar',bg="#1150af",foreground="white",activebackground="#f9970c",width=6,height=1)
    volt.grid(row=3,column=1,padx=40,sticky="e")







def consultar():
    global nmd1
    global con
    con = Tk()
    con.title('Consulta de Alunos')
    canva3 = Canvas(con, bg="#1150af", width=475, height=100).place(x=0, y=0)
    mn1 = Label(con, text="Insira o número de matrícula do aluno", bg="#1150af", fg="#f9970c", font=50).grid(row=1, padx=15, pady=37,columnspan=2)
    fl5 = LabelFrame(con, padx=5, pady=5)
    fl5.grid(row=2, column=0, padx=10, pady=20, columnspan=2)
    nmdl1 = Label(fl5, text='Número de Matrícula:', bg="#1150af", fg='white')
    nmdl1.grid(row=0, column=0, sticky="w")
    nmd1 = Entry(fl5)
    nmd1.grid(row=0, column=1)
    clb = Button(fl5, text='Consultar', bg="#1150af", fg='white', activebackground="#f9970c", command=consult)
    clb.grid(row=0, column=2, padx=35)
    volt2 = Button(con, text='Voltar', bg="#1150af", fg='white', activebackground="#f9970c", width=6, height=1,command=con.destroy)
    volt2.grid(row=3, column=1, sticky="e", padx=50, pady=(0, 20))


def lista():
    conn = sqlite3.connect('Aluno_info.db')
    c = conn.cursor()
    lis = Tk()
    lis.title('Lista de Alunos')
    canva2 = Canvas(lis, bg="#1150af", width=475, height=100).place(x=0, y=0)
    lisn=Label(lis,text="Lista de Alunos",bg="#1150af",fg="#f9970c",font=50).grid(row=1,padx=15,pady=37,columnspan=2)
    fl3=LabelFrame(lis,padx=0,pady=0)
    fl3.grid(row=2,pady=20)
    nl=Label(fl3,text="Nome",width=40,bg="#1150af",fg="white")
    nl.grid(row=0,column=0,padx=0,pady=(0, 5),)
    matid=Label(fl3,text="Matrícula",width=15,bg="#1150af",fg="white")
    matid.grid(row=0,column=1,padx=(1,0),pady=(0,5))
    c.execute("SELECT *, oid FROM info")
    dados = c.fetchall()

    print_dados = ""
    print_mat = ""
    for dado in dados:
        print_dados += str(dado[0]) + "\n"
        print_mat += str(dado[5])+ "\n"

    dadol=Label(fl3,text=print_dados)
    dadol.grid(row=1,column=0,sticky="w")
    matl=Label(fl3,text=print_mat)
    matl.grid(row=1,column=1)


    conn.commit()
    conn.close()
def deletar():
    global nmd
    global dele
    dele = Tk()
    dele.title('Deletar Aluno')
    canva3 = Canvas(dele, bg="#1150af", width=475, height=100).place(x=0, y=0)
    mn = Label(dele, text="Insira o número de matrícula do aluno", bg="#1150af", fg="#f9970c", font=50).grid(row=1, padx=15, pady=37,columnspan=2)
    fl4 = LabelFrame(dele,padx=5,pady=5)
    fl4.grid(row=2,column=0,padx=10,pady=20,columnspan=2)
    nmdl = Label(fl4,text='Número de Matrícula:', bg="#1150af",fg='white')
    nmdl.grid(row=0,column=0,sticky="w")
    nmd = Entry(fl4)
    nmd.grid(row=0,column=1)
    dlb = Button(fl4,text='Deletar',bg="#1150af",fg='red',activebackground="red",command=delet)
    dlb.grid(row=0,column=2,padx=35)
    volt1=Button(dele,text='Voltar',bg="#1150af",fg='white',activebackground="#f9970c",width=6,height=1,command=dele.destroy)
    volt1.grid(row=3,column=1,sticky="e",padx=50,pady=(0,20))
#TELA INICIAL

canva =  Canvas(mw,bg="#1150af",width=400,height=100).place(x=0,y=85)
bv = Label (mw,text='Bem-vindo a Central de Alunos',fg='#f9970c',font=50,bg="#1150af")
bv.grid(row=1,column=0,sticky="w",padx=15,pady=15)
bv1 = Label (mw,text='O que deseja?',font=50,bg="#1150af",fg="white")
bv1.grid(row=2,column=0,sticky="w",padx=15,pady=0)

lf = LabelFrame(mw,padx=5,pady=5)
lf.grid(row=3,column=0,padx=20,pady=30,sticky="w")

ca = Button(lf,text='Cadastrar novo aluno',width=20,bg='#1150af',fg='white',activebackground="#f9970c",command=cadastrar)
ca.grid(row=0,column=0,sticky="w",padx=10,pady=10)
coa = Button(lf,text='Consultar Aluno',width=20,bg='#1150af',fg='white',activebackground="#f9970c",command=consultar)
coa.grid(row=1,column=0,sticky="w",padx=10,pady=10)
la = Button(lf,text='Lista de Alunos',width=20,bg='#1150af',fg='white',activebackground="#f9970c",command=lista)
la.grid(row=0,column=1,sticky="w",padx=10,pady=10)
da = Button(lf,text='Deletar Aluno',width=20,bg='#1150af',fg='white',activebackground="#f9970c",command=deletar)
da.grid(row=1,column=1,sticky="w",padx=10,pady=10)



conn.commit()

conn.close()

mw.mainloop()
