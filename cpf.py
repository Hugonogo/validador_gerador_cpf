import re
import string
import random

def validarId(cpf):
  n = 0
  id = []
  for i in range(10, 1, -1):
    id.append(int(cpf[n]) * i)
    n = n + 1
  if (sum(id) % 11) <= 1:
    digt1 = 0
  else:
    digt1 = 11 - (sum(id) % 11)


  id.clear()
  
  n = 1

  for j in range(10, 1, -1): 
    id.append(int(cpf[n]) * j)
    n = n + 1

  if (sum(id) % 11) <= 1:
    digt2 = 0
  else:
    digt2 = 11 - (sum(id) % 11)

  return digt1, digt2

  

def Validador(cpf):
  formatacao = re.compile("^\d{3}\.\d{3}\.\d{3}-\d{2}")

  if not formatacao.search(cpf):
    return False

  cpf = cpf.translate(str.maketrans('', '', string.punctuation))

  if len(cpf) != 11:
    return False

  id = validarId(cpf)

  if not cpf[9] == str(id[0]) and not cpf[10] == str(id[1]):
    return False

  return True


def calc_id(cpf):
  n = 0
  id = []
  for i in range(10, 1, -1):
    id.append(int(cpf[n]) * i)
    n = n + 1

  if (sum(id) % 11) <= 1:
    digt1 = 0
  else:
    digt1 = 11 - (sum(id) % 11)

  id.clear()

  cpf.append(digt1)
  n = 1
  for j in range(10, 1, -1): 
    id.append(int(cpf[n]) * j)
    n = n + 1

  if (sum(id) % 11) <= 1:
    digt2 = 0
  else:
    digt2 = 11 - (sum(id) % 11)
 
  return digt1, digt2
  
def gerador():

  cpf = []
  ##Gerando 10 números aleatórios
  for i in range(0, 9):
    cpf.append(random.randint(0, 9))
 
  ##calculando os Digitos de verificação
  id = calc_id(cpf)

  ##Substituindo os digitos por números válidos
  cpf[9] = id[0]
  cpf.append(id[1])

  ##Formatando o CPF
  cpf.insert(3, '.')
  cpf.insert(7, '.')
  cpf.insert(11, '-')
 
  cpf_str = ''.join(map(str, cpf))

  return cpf_str

  ##Main##

cpf = gerador()
if Validador(cpf):
  print(f"CPF: {cpf} é válido")
else:
   print(f"CPF: {cpf} não é válido")

validar = input(">>").strip()

if Validador(validar):
  print("CPF válido")
else:
  print("CPF inválido")

