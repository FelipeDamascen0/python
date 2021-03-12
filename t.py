from functools import partial
from tkinter import  *
memoria = []

def btClick(botao):
    visorPrincipal['text'] += botao['text']
    print(visorPrincipal)
def soma ():
    resultado = str(eval(visorPrincipal['text']))
    visorPrincipal['text'] = resultado

def mS():
    ResgatarvalorNaTela = visorPrincipal['text']
    if ResgatarvalorNaTela == '':
        print('Valor invalido')
        memoria.pop(0)
    elif len(memoria[1:2]):
        memoria.pop(0)
    else :
        memoria.append(ResgatarvalorNaTela)
    valorM = memoria[1:2]
    visor['text'] = valorM
    print(memoria)
def mM():
    if len(memoria) > 1:
        memoria.pop(0)
    elif len(memoria) == 0:
        print('Nenhum valor salvo')

    ResgataValorMemoria = memoria[0]
    m = int(ResgataValorMemoria)
    n = visorPrincipal['text']
    n =  int(n)
    somaMmais = m + n
    visorPrincipal['text'] = str(somaMmais)
def mSub():
    if len(memoria) > 1:
        memoria.pop(0)
    elif memoria  == []:
        print('Nenhum valor salvo')

    valorMemoria = memoria[0]
    m = int(valorMemoria)
    n = visorPrincipal['text']
    n = int(n)
    subEd = n - m
    visorPrincipal['text'] = str(subEd)
def clearM():
    memoria.clear()
    visor['text'] = ''


def clear():
    visorPrincipal['text'] = ''




janela = Tk()
janela.title("Calculadora")
janela['bg'] = 'grey'
janela.geometry('500x500+600+150')

visorPrincipal =Label(janela, width=40, height=2)
visorPrincipal.place(x=50,y=30)
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