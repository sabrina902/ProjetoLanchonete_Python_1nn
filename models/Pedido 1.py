class Pedido:

    def __init__(self, numero, data, hora, pagamento, cliente, lista) -> None:
        self.numero=numero
        self.data=data
        self.hora=hora
        self.pagamento=pagamento
        self.cliente=cliente
        self.status="Aberto"
        self.lista=lista

    def imprimir(self):
         print(  f"------Pedido N° {self.numero}------\n"
                 f"Data: {self.data} - Horário:{self.hora}\n"
                 f"Status: {self.status}\n"
                 f"Forma de pagamento: {self.pagamento}\n"
                 f"Cliente: {self.cliente.nome}"
                 f"| Endereço: {self.cliente.endereco}"
                 f"| Telefone: {self.cliente.telefone}"
                 )
         print("\n")
         for item in self.lista:
             item.imprimir()