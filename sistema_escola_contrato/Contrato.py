class Contrato:
    def __init__(self, escola):
        escola.contratos.append(self)
        print("escola")