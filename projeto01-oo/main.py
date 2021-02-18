from conta import Conta

conta1 = Conta(1, "Fulano", 10000.0, 1000.0)
conta2 = Conta(2, "Beltrano", 0.0, 1000.0)
conta3 = Conta(3, "Sicrano", 0.0, 2000.0)

print(conta1)

print(conta1.extrato())

print(conta1.saca(200))

print(conta1.deposita(200))

print(conta1.extrato())