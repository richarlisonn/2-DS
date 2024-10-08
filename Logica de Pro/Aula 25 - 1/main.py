estoque = [20, 15 , 10 , 30 ,5]

def atualizar_estoque(estoque , produto , quantidade):
  if 0<= produto < len(estoque):
    if estoque[produto] >= quantidade:
      estoque[produto] -= quantidade
    else:
      print(f"Não háa estoque suficiente para o produto {produto + 1}.")
  else:
    print("Produto Inválido")

# Adiciona  Unidades de um produto ao estoque.
def adicionar_estoque(estoque , produto , quantidade):
  if 0 <= produto  < len(estoque):
    estoque[produto] += quantidade
  else:
    print("Produto Inválido")

# Exibe a quantidade atual de cada produto.
def exibir_estoque(estoque):
  for i , quantidade in enumerate(estoque):
    print(f"Produto {i + 1}: {quantidade} unidades")

# Atualizando Estoque
atualizar_estoque(estoque, 0 , 3)
atualizar_estoque(estoque, 3 , 2)

# Adicionando Unidade ao estoque
adicionar_estoque(estoque, 4 , 10 )

#Exibindo estoque Atualizado
exibir_estoque(estoque)


