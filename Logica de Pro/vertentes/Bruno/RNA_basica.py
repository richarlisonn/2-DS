input = 1
out_put_desire = 0
input_weight = 0.5

print('Entrada: ', input)
print('Desejado: ', out_put_desire)

bias = 1
bias_weigth = 0.5

sum = (input * input_weight) + (bias * bias_weigth)

def ativaction(sum):
  if sum >= 0:
    return 1
  else:
    return 0
  
def update_weigth(input_weigth, learning_rate, input, error):
  if error != 0:
    input_weight = input_weigth + (learning_rate * input * error)
    return input_weight

out_put = ativaction(sum)

error = out_put_desire - out_put

print('Erro: ', error)

print('Saida: ', out_put)