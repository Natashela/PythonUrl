
from http import HTTPStatus
from tkinter import *
import sqlite3
from tkinter import messagebox
import tkinter
from tkinter.simpledialog import askstring
import typing
from urllib import request
#import pyping


###################################################### conexão para criação do banco
conexaobd = sqlite3.connect('url.db')
######################################################

##################################################################### Sessão desafios - 3
from ping3 import ping, verbose_ping
def importarUrl():                                                                       
    arquivo = open('urls.txt', 'r', encoding="UTF8").readlines()                         
    Label(janela, text=" ".join(arquivo)).grid(row=2)                                   
    # arquivo.close() 
    bd = conexaobd.cursor()        
    sql = 'INSERT INTO CadastroUrl VALUES (?,?)'
    for row in arquivo:
        bd.execute(sql, (None, str(row)))
        conexaobd.commit()
        print(row)
    return selectBd()
    #messagebox.showinfo('URL','Você importou {}\nDados inseridos no banco de dados!'.format(arquivo))
    

from ping3 import ping, verbose_ping
################################################### janela tkinter
janela = Tk()
janela.title("Gerenciamento de Enderecos Web")                  
janela.geometry('2050x550')                                    
texto = Label(janela, text='Tempo de resposta da conexão em ms: '+
              str(ping('NOTMCT002684'))) #coloque o teu hostname entre ''
texto.grid(column=4, row=0, padx=100, pady=150)               


###################################################################### funções
def incluirUrl():                                                                           
    name = askstring('URL', 'Digite uma nova URL')
    messagebox.showinfo('URL','Você digitou {}\nDado inserido no banco de dados!'.format(name))
    c = conexaobd.cursor()
    sql = 'INSERT OR IGNORE INTO CadastroUrl VALUES (?,?)'
    c.execute(sql, (None, format(name))) 
    #janela.mainloop()
    print(name)
    conexaobd.commit()     
    #conexaobd.close()                                       
                                                                          
def alterarUrl():                                                         
    sql = 'UPDATE CadastroUrl SET url = ? WHERE id = ?'
    id = askstring('URL', 'Digite o id da url que irá alterar')
    url = askstring('URL', 'Digite a nova url')
    messagebox.showinfo('URL','Você digitou o id {}\n'.format(id))
    messagebox.showinfo('URL','Você digitou a url {}\nDado alterado no banco!'.format(url))
    c = conexaobd.cursor()
    c.execute(sql, (format(url),id)) 
    conexaobd.commit()                                      
                                                                          
def excluirUrl():                                                         
    sql = 'DELETE FROM CadastroUrl WHERE id = ?'
    id = askstring('URL', 'Digite o id da url que irá deletar')
    messagebox.showinfo('URL','Você digitou o id {}\nDado deletado do banco!'.format(id))
    c = conexaobd.cursor()
    c.execute(sql, (id,)) 
    print('item deletado')
    conexaobd.commit()                                          
import requests                                                            
def validarUrl(): 
    id = askstring('URL', 'Digite o id da url que deseja validar')    
    #messagebox.showinfo('URL','Você digitou o id {}\n'.format(id))
    cur = conexaobd.cursor()
    cur.execute("SELECT url FROM CadastroUrl WHERE ID = ?", (id, ))  
    return [line for line in cur]   
    # url = str(rows)
    # page = requests.get(url)
    # print(page)
    # messagebox.showinfo('URL','Você digitou o id {}, site is {}'.format(id),format(page))
    # return messagebox.showinfo('URL','Você digitou o id{}'.format(page))                             
                                                                          
def validarallUrl():                                                      
    messagebox.showinfo("")                                               
                                                                          
def detalhesValidacao():                                                  
    messagebox.showinfo("")   

def listarUrl():
    cur = conexaobd.cursor()
    cur.execute('SELECT * FROM CadastroUrl')
    rows = cur.fetchall() 
    return Label(janela,justify = 'center', text=rows)                                       

def selectBd(): #validar depois
    cur = conexaobd.cursor()
    cur.execute('SELECT * FROM CadastroUrl')
    rows = cur.fetchall()  
    return rows

##### aqui tem que vir o select da janela principal
texto_resposta = Label(janela,justify = 'center', text=messagebox
                       .showinfo('Lembrete!','Ao fazer alterações, feche e abra a tela novamente!'))
texto_resposta = Label(janela,justify = 'center', text=selectBd())
texto_resposta.grid(column=0, row=0)

######################################################################################## botões
botaoImport = Button(janela, text="Importar URL",command=lambda: importarUrl())#                                        
botaoImport.grid(column=1, row=2)                                        
botaoIncluir = Button(janela, text="Incluir URL", command=lambda: incluirUrl())#
botaoIncluir.grid(column=2, row=2)                                                                                
botaoAlterar = Button(janela, text="Alterar URL", command=lambda: alterarUrl())
botaoAlterar.grid(column=1, row=3)                                       
botaoExcluir = Button(janela, text="Excluir URL", command=lambda: excluirUrl())
botaoExcluir.grid(column=2, row=3)                                       
botaoValidar = Button(janela, text="Validar Url", command=lambda: validarUrl())
botaoValidar.grid(column=1, row=4)                                       
botaoValidarTodos = Button(                                                                ####
    janela, text="Validar Url(all)", command=lambda: validarallUrl())                      ####
botaoValidarTodos.grid(column=2, row=4)                                   ####
botaoDetalharValidacao = Button(                                                           ####
    janela, text="Detalhar Validacao", command=lambda: detalhesValidacao())                ####
botaoDetalharValidacao.grid(column=3, row=4)                             ####
###############################################################################################

# finaliza

janela.mainloop()
