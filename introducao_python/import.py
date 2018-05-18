#This is how to import another file
import sys
sys.path.insert(0, 'bubble_sort.py')
sys.path.insert(0, 'classe_triangulo.py')
from bubble_sort import bubble_sort
from classe_triangulo import Triangulo


l = bubble_sort([5,4,3,1])
print(l, '\n')

k = Triangulo(1,1,1)
s = k.perimetro()
r = k.quadrado(1)
print(s, r)