matrix=[
  ["a","b","c","d","e"],
  ["f","g","h","i","j"],
  ["k","l","m","n","o"], 
  ["p","q","r","s","t"], 
  ["u","v","w","x","y"],
  ["z"],
]

for index_l, l in enumerate(range(len(matrix))):
  for index_c, c in enumerate(range(len(matrix[l]))):
    if matrix[l][c] == 'r':
      print(f'A letra é: {matrix[l][c]}\nLinha: {index_l} \nColuna: {index_c}')
    elif matrix[l][c] == 'v':
      print(f'A letra é: {matrix[l][c]}\nLinha: {index_l} \nColuna: {index_c}')