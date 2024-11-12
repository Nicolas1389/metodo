from math import*

#-----------------------------FUNCIÓN A ANALIZAR---------------------------------------
def f(x):
    return 10*x**4-3*x*exp(x)-3*exp(x)


#------------------------METODO DE BISECCIÓN APLICADO-------------
"""
#-------------lOS ARGUMENTOS QUE RECIBE SON:
# F= es igual a la función  a analizar
# a= es el punto izquierdo en la función a anlizar, desde donde comienza
# b= es el punto derecho en la función a analizar desde donde termina
# tol = es la tolerancia maxima aceptada
# n= es el numero maximo de iteraciones permitidas para ese ejercicio
"""
def biseccion(f,a,b,tol,n):
    i=1
    while i<=n:
        p=a+(b-a)/2.0

        print("iter=","%03d"%i, " ; p=","%.14f" %p)

        if abs(f(p))<= 1e-15 or (b-a)/2.0<tol:
            return p
        i+=1
        if f(a)*f(p)>0:
            a=p
        else:
            b=p
    print("iteraciones agotadas: Error")
    return
print("\n"+r"Método de la bisección: "+"\n")
biseccion(f,-1.0,-0.25,1e-4,100)
