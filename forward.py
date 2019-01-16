# forwardprop
import math
import random 
import numpy as np
class forward:
        def __init__(self,pattern):
                
                self.AI,self.AH,self.AO,self.WIH,self.WHO=[],[],[],[],[]
                self.ni=2
                self.nh=3
                self.no=1

                
                self.AI =[1.0]*(self.ni)+1
                
                self.AH =[1.0]*(self.nh)+1
                
                self.AO =[1.0]*(self.no)

                for i in range((self.ni)+1):
                        self.WIH.append([0.0]*self.nh)
                        
                for i in range((self.ni)+1):
                        for j in range(self.nh):
                           self.WIH[i][j]=random.uniform(-0.2,0.2)


                for i in range((self.nh)+1):
                        self.WHO.append([0.0]*self.no)

                for i in range((self.nh)+1):
                        for j in range(self.no):
                                self.WHO[i][j]=random.uniform(-2.0,2.0)


        def forwardprop(self,inputs):
                for i in range(self.ni):
                        self.AI[i]=inputs[i]
                                         
                for j in range(self.nh):
                        sum=0.0
			for i in range(self.ni):
                                sum+=self.AI[i]*self.WIH[i][j]
                                
			self.AH[j]=sigmoid(sum)
                print("AH=",self.AH)
                                         
                for k in range(self.no):
                        sum=0.0
                        for j in range(self.nh):
                               sum+=self.AH[j]*self.WHO[j][k]
                        self.AO[k]=sigmoid(sum)
                print("AO=",self.AO)
                                         
        def train(self,pattern):
                for i in range(500):
                        for p in pattern:
                               inputs=p[0]
                               forwardprop(inputs)

def sigmoid(x):
        return 1/(1+math.exp(-x))

def main():
	pattern = [
		[[0,0], [0]],
		[[0,1], [1]],
		[[1,0], [1]],
		[[1,1], [1]]
	          ]
	Neural = forward(pattern)
	Neural.forwardprop(pattern)


if __name__ == "__main__":
    main()
                
