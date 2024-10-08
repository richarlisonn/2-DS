estoque = [20, 15, 10, 30, 5]

def atualizar_estoque(estoque, produto, quantidade):
    if 0 <= produto < len(estoque):
        if estoque[produto] >= quantidade:
            estoque[produto] -= quantidade
        else:
            print(f"Não há estoque suficiente para o produto {produto + 1}.")
    else:
        print("Produto Inválido")

# Adiciona Unidades de um produto ao estoque.
def adicionar_estoque(estoque, produto, quantidade):
    if 0 <= produto < len(estoque):
        estoque[produto] += quantidade
    else:
        print("Produto Inválido")

# Exibe a quantidade atual de cada produto.
def exibir_estoque(estoque):
    for i, quantidade in enumerate(estoque):
        print(f"Produto {i + 1}: {quantidade} unidades")

# Atualizando Estoque
atualizar_estoque(estoque, 0, 3)
atualizar_estoque(estoque, 3, 2)

# Adicionando Unidade ao estoque
adicionar_estoque(estoque, 4, 10)

# Exibindo estoque Atualizado
exibir_estoque(estoque)

assentos = [[0 for _ in range(8)] for _ in range(5)]

def reserva_assento(assentos, fileira, assento):
    if 0 <= fileira < len(assentos) and 0 <= assento < len(assentos[0]):
        if assentos[fileira][assento] == 0:
            assentos[fileira][assento] = 1
            print(f"Assento ({fileira + 1}, {assento + 1}) reservado com sucesso.")
        else:
            print(f"Assento ({fileira + 1}, {assento + 1}) já está reservado.")
    else:
        print("Assento inválido")

def cancelar_reserva(assentos, fileira, assento):
    if 0 <= fileira < len(assentos) and 0 <= assento < len(assentos[0]):
        if assentos[fileira][assento] == 1:
            assentos[fileira][assento] = 0
            print(f"Reserva do assento ({fileira + 1}, {assento + 1}) cancelada com sucesso")
        else:
            print(f"Assento ({fileira + 1}, {assento + 1}) não está reservado.")
    else:
        print("Assento inválido.")

def exibir_mapa_assentos(assentos):
    print("Mapa dos assentos:")
    for i, fileira in enumerate(assentos):
        print(f"Fileira {i + 1}: " + " ".join(str(assento) for assento in fileira))

# Reservando assentos (1, 3), (2, 5), (4, 7)
reserva_assento(assentos, 0, 2)  # Assento (1, 3)
reserva_assento(assentos, 1, 4)  # Assento (2, 5)
reserva_assento(assentos, 3, 6)  # Assento (4, 7)

# Cancelando a reserva do assento (2, 5)
cancelar_reserva(assentos, 1, 4)  # Assento (2, 5)

# Exibir o mapa dos assentos atualizado
exibir_mapa_assentos(assentos)
