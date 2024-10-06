name = "THIS IS A GLOBAL STRING"

def greet():
  name = "I AM AN ENCLOSING FUNCTION LOCALS"

  def hello():
    name = "i am local"
    print("Hello " + name)
  hello()
greet()


  