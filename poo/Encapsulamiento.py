class CuentaBancaria:
    def __init__(self, titular,saldo):
        self.titular = titular
        self._saldo = saldo

    def depositar(self,cantidad):
        self._saldo += cantidad

    def obtenersaldo(self):
        return self._saldo

cuenta=CuentaBancaria("Pedrito",1000)
cuenta.depositar(500)
print(cuenta.obtenersaldo())