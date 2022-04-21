
class calc:

    def suma(self, x, y):
        '''argumentos de entrada: dos listas, cada una con un polinomio
        retorna: la suma de los dos polinomios
        '''
        
        may = x
        men = y
        
        if len(x) < len(y):
            men = x
            may = y
        sum1 = [men[i] + may[i] for i in range(len(men))]    
        aux = [may[i] for i in range(len(men),len(may))]
        suma = sum1 + aux

        print("--------------------------------------------------------------")
        print("El resultado de sumar ", str(x), "+", str(y), " es: ", str(suma))
        print("--------------------------------------------------------------")
    
    def resta(self, x, y):
        '''argumentos de entrada: dos listas, cada una con un polinomio
        retorna: la resta de los dos polinomios
        '''
        may = x
        men = [y[i]*(-1) for i in range(len(y))]

        if len(x) < len(y):
            men = x
            may = [y[i]*(-1) for i in range(len(y))]
        sum2 = [men[i] + may[i] for i in range(len(men))]    
        aux = [may[i] for i in range(len(men),len(may))]
        res = sum2 + aux

        print("--------------------------------------------------------------")
        print("El resultado de restar ", str(x), "-", str(y), " es: ", str(res))
        print("--------------------------------------------------------------")
    
