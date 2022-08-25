import numpy as np
import math
import cmath
# Suma complejos representados como una tupla (real, imaginaria)
# la suma, la multiplicación y polar lo saque del codigo del profesor que publico en teams, y modifique el codigo dandome una idea como se podia hacer
def sumacplx(a,b):
    real = a[0] + b[0]
    img = a[1] + b[1]
    return (real, img)
# multiplicacion complejos representados como una tupla (real, imaginaria)
def multcplx(a,b):
    real = (a[0] * b[0]) - (a[1]* b[1])
    img = (a[0] * b[1]) + (b[0] * a[1])
    return (real, img)
# Resta complejos representados como una tupla (real, imaginaria)
def restacplx(a,b):
    real = a[0] - b[0]
    img = a[1] - b[1]
    return (real, img)
# divicion complejos representados como una tupla
def divicion(a,b):
    real = (((a[0] * b[0]) + (b[1] * a[1])) / (b[0]*2 + b[1]*2))
    img = (((b[0] * a[1]) - (a[0] * b[1])) / (b[0]*2 + b[1]*2))
    return (real, img)
# modulo complejos representado como numero real
def modul(a,b):
    real = a
    img =  b
    return math.sqrt(real*2 +img*2)
# conjugado de conplejo representado como una tupla
def con(a):
    real = a[0]
    img = (a[1] * -1)
    return (real , img)
# a polar
def toPolar(c):
    theta = np.arctan2(c[1],c[0])
    rho = np.sqrt((c[0] * c[0]) + (c[1] * c[1]))
    return (rho, theta)
def prettyprinting(c):
    #Para cartesianos
    print( str(c[0]) + "+" + str(c[1]) + "i")
def polprettyprinting(c):
    #Para polares
    print( str(c[0]) + " e^(i " + str(c[1]) + ")")
def back(a):
    real = a[0] * cmath.cos(a[1])
    img = a[0] * cmath.sin(a[1])
    return real,img
#if _name_ == '_main_':
#Prueba suma
prettyprinting(sumacplx((2,3),(4,7)))
#Prueba multiplicacion
prettyprinting(multcplx((2,3),(4,7)))
#Prueba resta
prettyprinting(restacplx((2,3),(4,7)))
#Prueba divicion
prettyprinting(divicion((-2,1),(1,2)))
#Prueba modul
print(modul(1,-1))
#Prueba conjugado
prettyprinting(con((-2,1)))
#Prueba polares
polprettyprinting(toPolar((-3,-2)))
prettyprinting(back((3.605551275463989,-2.5535900500422257)))
