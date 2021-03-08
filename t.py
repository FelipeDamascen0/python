from functools import partial
from tkinter import  *
memoria = [] #Lista de onde vai ficar os numeros que o usuario salvar

def btClick(botao):#Funçao do botao de numero e operaçoes para apareces no visor da calculadora
    ed['text'] += botao['text']
    print(ed)
def soma ():#Função do botao de igual em que a pessoa clica e realiza o calculo
    resultado = str(eval(ed['text']))#faz o calculo
    ed['text'] = resultado#imprime o resultaado na tela

def mS():#Função para salvar o numero na memoria
    valor = ed['text']#resgata o valor contido na tela
    if valor == '':#caso o usuario va salvar e nao digite nada ira imprimir essa mensagem e tirar esse valor da memoria
        print('Valor invalido')
        memoria.pop(0)
    elif len(memoria[1:2]):#se a memoria tiver acima de 2 numeros vai retira o numero anterior para nao dar bug
        memoria.pop(0)
    else :#se o usuario digitou um valor valido vai salvar na memoria
        memoria.append(valor)
    valorM = memoria[1:2]
    visor['text'] = valorM
    print(memoria)
def mM():#Função para somar o numero salvo com o numero na tela
    if len(memoria) > 1:
        memoria.pop(0)
    elif len(memoria) == 0:
        print('Nenhum valor salvo')

    m = memoria[0]
    m = int(m)
    n = ed['text']
    n =  int(n)
    somaEd = m + n
    ed['text'] = str(somaEd)

def mSub():#Função para subtrair o numero salvo com o numero na tela
    if len(memoria) > 1:
        memoria.pop(0)
    elif memoria  == []:
        print('Nenhum valor salvo')

    m = memoria[0]
    m = int(m)
    n = ed['text']
    n = int(n)
    subEd = n - m
    ed['text'] = str(subEd)
def clearM():#vai limpar a tela onde o usuario digita a operação
    memoria.clear()
    visor['text'] = ''


def clear():#vai limpar o visor onde ficou os numeros salvos na memoria
    ed['text'] = ''




#Abaixo o front-end da calculadora
janela = Tk()
janela.title("Calculadora")
janela['bg'] = 'grey'
janela.geometry('500x500+600+150')

ed =Label(janela, width=40, height=2)
ed.place(x=50,y=30)
visor =Label(janela,width=5,height=2)
visor.place(x=350,y=30)

bt19 = Button(janela, width=10, text='MC', height=2,command=clearM)

bt18 = Button(janela, width=10, height=2,text='M-', command=mSub)


bt17 = Button(janela, width=10, height=2,text='M+', command=mM)


bt16 = Button(janela, width=10, text='MS', height=2,command=mS)


bt1 = Button(janela, width=10, height=2,text='7')
bt1["command"] = partial(btClick, bt1)

bt2 = Button(janela, width=10, height=2,text='8')
bt2["command"] = partial(btClick, bt2)

bt3 = Button(janela, width=10, height=2,text='9')
bt3["command"] = partial(btClick, bt3)

bt4 = Button(janela, width=10, height=2,text='4')
bt4["command"] = partial(btClick, bt4)

bt5 = Button(janela, width=10, height=2,text='5')
bt5["command"] = partial(btClick, bt5)

bt6 = Button(janela, width=10, height=2,text='6')
bt6["command"] = partial(btClick, bt6)

bt7 = Button(janela, width=10, height=2,text='1')
bt7["command"] = partial(btClick, bt7)

bt8 = Button(janela, width=10, height=2,text='2')
bt8["command"] = partial(btClick, bt8)

bt9 = Button(janela, width=10, height=2,text='3')
bt9["command"] = partial(btClick, bt9)

bt10 = Button(janela, width=10, height=2,text='0')
bt10["command"] = partial(btClick, bt10)

bt11 = Button(janela, width=10, height=2,text='/')
bt11["command"] = partial(btClick, bt11)

bt12 = Button(janela, width=10, height=2,text='*')
bt12["command"] = partial(btClick, bt12)

bt13 = Button(janela, width=10, height=2,text='-')
bt13["command"] = partial(btClick, bt13)

bt14 = Button(janela, width=10, height=2,text='+')
bt14["command"] = partial(btClick, bt14)

bt20 = Button(janela, width=10, text='C', height=2,command=clear)


bt15 = Button(janela, width=10, text='=', height=2,command=soma)
#bt15["command"] = partial(btClick, bt14)
bt1.place(x=50, y=115)
bt2.place(x=135, y=115)
bt3.place(x=220, y=115)
bt4.place(x=50, y=160)
bt5.place(x=135, y=160)
bt6.place(x=220, y=160)
bt7.place(x=50, y=205)
bt8.place(x=135, y=205)
bt9.place(x=220, y=205)
bt10.place(x=50, y=250)
bt11.place(x=310, y=115)
bt12.place(x=310, y=160)
bt13.place(x=310, y=205)
bt14.place(x=310, y=250)
bt15.place(x=220, y=250)
bt16.place(x=50, y=70)
bt17.place(x=135, y=70)
bt18.place(x=220, y=70)
bt19.place(x=310, y=70)
bt20.place(x=135, y=250)

janela.mainloop()