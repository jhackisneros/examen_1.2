class TorreDeHanoi:
    def __init__(self, num_discos):
        self.num_discos = num_discos
        self.palos = {
            "A": list(range(num_discos, 0, -1)),  # Los discos están en el palo A al inicio
            "B": [],  # Palo auxiliar
            "C": []   # Palo destino
        }
        self.movimientos = []

    def mover_disco(self, origen, destino):
        """Mueve un disco de un palo a otro."""
        disco = self.palos[origen].pop()
        self.palos[destino].append(disco)
        self.movimientos.append(f"Mover disco {disco} de {origen} a {destino}")
        self.mostrar_palos()

    def resolver(self, num_discos=None, origen="A", auxiliar="B", destino="C"):
        """
        Resuelve el problema de la Torre de Hanoi.
        :param num_discos: Número de discos a mover
        :param origen: Palo de origen
        :param auxiliar: Palo auxiliar
        :param destino: Palo de destino
        """
        if num_discos is None:
            num_discos = self.num_discos

        if num_discos == 1:
            self.mover_disco(origen, destino)
        else:
            # Mover n-1 discos de origen a auxiliar usando destino como auxiliar
            self.resolver(num_discos - 1, origen, destino, auxiliar)
            # Mover el disco más grande al destino
            self.mover_disco(origen, destino)
            # Mover los n-1 discos de auxiliar a destino usando origen como auxiliar
            self.resolver(num_discos - 1, auxiliar, origen, destino)

    def mostrar_palos(self):
        """Muestra el estado actual de los tres palos."""
        print("\nEstado actual de los palos:")
        for palo, discos in self.palos.items():
            print(f"{palo}: {discos}")

    def imprimir_movimientos(self):
        """Imprime los movimientos realizados paso a paso."""
        print("\nMovimientos para resolver la Torre de Hanoi:")
        for paso, movimiento in enumerate(self.movimientos, start=1):
            print(f"Paso {paso}: {movimiento}")