import json
import os

class VendingMachine:
    def __init__(self, stock_file):
        self.stock_file = stock_file
        self.stock = self.load_stock()
        self.saldo = 0

    def load_stock(self):
        if os.path.exists(self.stock_file):
            with open(self.stock_file, 'r') as file:
                return json.load(file)
        else:
            return []

    def save_stock(self):
        with open(self.stock_file, 'w') as file:
            json.dump(self.stock, file, indent=4)

    def display_stock(self):
        print("cod | nome | quantidade | preço")
        print("--------------------------------")
        for item in self.stock:
            print(f"{item['cod']} {item['nome']} {item['quant']} {item['preco']}")

    def add_coins(self, coins):
        try:
            total = sum([self.parse_coin(coin) for coin in coins])
            self.saldo += total
            print(f"maq: Saldo = {self.format_money(self.saldo)}")
        except ValueError:
            print("maq: Moeda inválida.")

    def parse_coin(self, coin):
        coin_value = coin[:-1]
        if coin[-1] == 'e':
            return int(coin_value) * 100
        elif coin[-1] == 'c':
            return int(coin_value)
        else:
            raise ValueError

    def format_money(self, amount):
        euros = amount // 100
        cents = amount % 100
        return f"{euros}e{cents}c"

    def select_product(self, code):
        product = next((item for item in self.stock if item['cod'] == code), None)
        if product:
            if product['quant'] > 0:
                if self.saldo >= product['preco'] * 100:
                    self.saldo -= product['preco'] * 100
                    product['quant'] -= 1
                    print(f"maq: Pode retirar o produto dispensado \"{product['nome']}\"")
                    print(f"maq: Saldo = {self.format_money(self.saldo)}")
                else:
                    print(f"maq: Saldo insuficiente para satisfazer o seu pedido")
                    print(f"maq: Saldo = {self.format_money(self.saldo)}; Pedido = {self.format_money(product['preco'] * 100)}")
            else:
                print("maq: Produto indisponível.")
        else:
            print("maq: Produto não encontrado.")

    def add_product(self, code, name, quantity, price):
        product = next((item for item in self.stock if item['cod'] == code), None)
        if product:
            product['quant'] += quantity
        else:
            self.stock.append({"cod": code, "nome": name, "quant": quantity, "preco": price})
        print("maq: Produto adicionado ao estoque.")
        self.save_stock()

    def end_transaction(self):
        change = self.saldo
        coins = [(200, '2e'), (100, '1e'), (50, '50c'), (20, '20c'), (10, '10c'), (5, '5c'), (2, '2c'), (1, '1c')]
        change_coins = []
        for coin_value, coin_name in coins:
            num_coins = change // coin_value
            if num_coins > 0:
                change_coins.append((num_coins, coin_name))
                change %= coin_value
        if change_coins:
            print("maq: Pode retirar o troco:", ", ".join([f"{num}x {coin}" for num, coin in change_coins]))
        else:
            print("maq: Não há troco a devolver.")
        print("maq: Até à próxima")
        self.saldo = 0

    def process_command(self, command):
        parts = command.split()
        if parts[0] == "LISTAR":
            self.display_stock()
        elif parts[0] == "MOEDA":
            self.add_coins(parts[1:])
        elif parts[0] == "SELECIONAR":
            self.select_product(parts[1])
        elif parts[0] == "SAIR":
            self.end_transaction()
        elif parts[0] == "ADICIONAR":
            if len(parts) == 5:
                code, name, quantity, price = parts[1], parts[2], int(parts[3]), float(parts[4])
                self.add_product(code, name, quantity, price)
            else:
                print("maq: Comando 'ADICIONAR' requer 4 argumentos.")
        else:
            print("maq: Comando inválido.")

# Exemplo de uso:
if __name__ == "__main__":
    vending_machine = VendingMachine("stock.json")
    print("maq:", "2024-03-08", "Stock carregado, Estado atualizado.")
    print("maq:", "Bom dia. Estou disponível para atender o seu pedido.")
    while True:
        command = input(">> ")
        vending_machine.process_command(command)
