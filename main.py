from dabases.conector import Conector
from controllers.produto_controller import ProdutoController

#main
conexao=  Conector.conectar()

if conexao!=None:
    print("conectado com o banco de dados!")

    #novo_produto= Produto("x-bacon",23,2)

    #inserir(conexao,novo_produto)
    #update(conexao,4758,39,1)
    #delete (conexao,4761)
    #listar(conexao)
    #buscar(conexao,"comida" )
    

    produtos = ProdutoController.listar(conexao)
    for produto in produtos:
       produto.listar()

    #produtos = buscar(conexao, 'Chapeu')
#    if produtos!=[]:
#        for produto in produtos:
#            produto.listar()
#    else:
#        print('Nenhum produto encontrado!')
 
    Conector.fechar_conecxao(conexao)