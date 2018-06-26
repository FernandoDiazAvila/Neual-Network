##Neural Network##
inputAr = [0,0,1,0]
WeightAr = [0,0,0,0]
learnRate = 0.10

def evaluateNN(inputAr,WeightAr):
    result = 0
    for i in range(len(inputAr)):
        product = inputAr[i]*WeightAr[i]
        result += product
    
    return round(result,3)


def learn(WeightAr,inputAr,learnRate):
    for i in range(len(inputAr)):
        if (inputAr[i] == 1):
            WeightAr[i] +=learnRate
    


def trainAI(learnRate,WeightAr,inputAr,trials):
    for i in range(trials):
        result=evaluateNN(inputAr,WeightAr)
        learn(WeightAr,inputAr,learnRate)
        print("result: ", result)


    WeightAr[2]= round(WeightAr[2],3)
    
    print(WeightAr)





if __name__ =="__main__":
    inputAr = [0,0,1,0]
    WeightAr = [0,0,0,0]
    learnRate = 0.10
    trials= 10
    trainAI(learnRate,WeightAr,inputAr,trials)
    
        
