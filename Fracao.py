class Fracao:
  numerador = 1
  decodificador = 1

  def _init_(self, numerador, denominador):
    self.numerador = numerador
    self.denominador = denominador

  def add(self, fracao):
    num = (self.numerador * fracao.denominador) + (fracao.numerador * self.denominador)
    den = self.denominador * fracao.denominador

    return Fracao(num, den)
    
  def sub(self, fracao):
    num = (self.numerador * fracao.denominador) - (fracao.numerador * self.denominador)
    den = self.denominador * fracao.denominador

    return Fracao(num, den)


  def mul(self, fracao):
    num = (self.numerador * fracao.numerador) 
    den = (fracao.denominador * self.denominador)

    return(num, den)
  
  def solve(self, fracao):
    return self.numerador / self.denominador

  def simplify(self):
    a = self.numerador
    b = self.denominador
    while b != 0:
      d = a % b
      a = b
      b = d

      num = self.numerador / a
      den = self.denominador / a 
      return Fracao(num, den)
    
  def _str_(self):
    return f" {int(self.numerador)} / {(self.denominador)}"
     

fracao1 = Fracao(1, 2)
fracao2 = Fracao(1, 3)
soma = fracao1.add(fracao2)
subtracao = fracao1.sub(fracao2)
multiplicacao = fracao1.mul(fracao2)

print(f"fracao1: {fracao1}")
print(f"fracao2: {fracao2}")
print(f"soma: {soma}")
print(f"subtracao: {subtracao}")
print(f"multiplicacao: {multiplicacao}")
print(f"fracao1 simplifica: {fracao1.simplify()}")
