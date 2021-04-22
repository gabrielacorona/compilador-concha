class semanticCube:
    def __init__(self):
        self.tabla =[[]]

    def validateType(self, values):
        #print(values)
        leftOp = values[0].type
        operation = values[1].type
        rightOp= values[2].type
        if (leftOp == "CONSTANTE_ENT" and rightOp =="CONSTANTE_ENT") :
            print("int")
        elif (leftOp == "CONSTANTE_ENT" and  rightOp =="CONSTANTE_FLOT") or (leftOp == "CONSTANTE_FLOT" and rightOp =="CONSTANTE_ENT") :
            print("float")
        elif (leftOp == "CONSTANTE_FLOT" and  rightOp =="CONSTANTE_FLOT")  :
            print("float")
        

        

 