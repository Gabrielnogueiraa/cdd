from biblioteca import Cliente
cliente = Cliente(numero=611, saldo=4500, nome='João', tipo='Conta Corrente', status='.')
cliente.ativarconta()
cliente.ativarLimite(1000)
cliente.depositar(300)
cliente.sacar(400)
cliente.verificarsaldo()
cliente.verificarLimite()
