from biblioteca import Cliente
cliente = Cliente(numero=611, saldo=4500, nome='João', tipo='Conta Corrente', limite=9000, status='.')
cliente.ativarconta()
cliente.depositar(300)
cliente.sacar(400)
cliente.verificarsaldo()