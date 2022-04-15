
class calc:

    def suma(self, x, y):
        '''argumentos de entrada: dos listas, cada una con un polinomio
        retorna: la suma de los dos polinomios
        '''
        may = x
        men = y
        sum = [0]*len(may)
        if len(x) < len(y):
            men = x
            may = y
        sum = [men[i] + may[i] for i in range(len(men))]    
        aux = [may[i] for i in range(len(men),len(may))]
        sum = sum + aux

        print("--------------------------------------------------------------")
        print("El resultado de sumar ", str(x), "+", str(y), " es: ", str(sum))
        print("--------------------------------------------------------------")
    
    def resta(self, x, y):
        '''argumentos de entrada: dos listas, cada una con un polinomio
        retorna: la resta de los dos polinomios
        '''
        may = x
        men = [y[i]*(-1) for i in range(len(y))]
        sum = [0]*len(may)
        if len(x) < len(y):
            men = x
            may = [y[i]*(-1) for i in range(len(y))]
        sum = [men[i] + may[i] for i in range(len(men))]    
        aux = [may[i] for i in range(len(men),len(may))]
        res = sum + aux

        print("--------------------------------------------------------------")
        print("El resultado de restar ", str(x), "-", str(y), " es: ", str(res))
        print("--------------------------------------------------------------")
    
