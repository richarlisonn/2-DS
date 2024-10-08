class Carro:
  
  def __init__(sef , marca , modelo , cor , ano , valor):
    self.marca=marca
    self.modelo=modelo
    self.cor=cor
    self.ano=ano
    self.valor=valor

class Estoque:
  def __init__(self):
    self.carro=[]
  def Adicionar_Carro(self,carro):
    self.carros.append(carro)
  def Mostrar_Estoque(self):
      for carro in self.carros:
        print(f'{carro.modelo} , {carro.marca}:adicinado ao estoque')
carro_1=Carro('porsche', 'carrera_gt' , 'branco', '2004' , '2000000000') 
carro_2=Carro('Mazda' , 'RX7' , 'braco' , '1978' , '1000000000') 
carro_3=Carro('Dodge' , 'Demom' , 'preto' , '1999' , '1005000000')

estoque=Estoque()
estoque.Adicionar_Carro(carro_1)

  