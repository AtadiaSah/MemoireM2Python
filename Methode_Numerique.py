from matplotlib.pyplot import*
import numpy as np
from math import*
def Methode_Euler_explicite(a,b,n,xi,yi):
	if(n==0):
		print("pas de solution sur zero point")
	else:
		Q=(b-a)/n
		ySEA=[yi];yo=yi;ySEAM=[yo];yv=yo;ySVM=[yv]
		yRgK=[yi];yrgk=yi
		if(Q==0 and xi==a):
			(ax,ay)=subplots()
			x=[xi]
			ay.plot(x,ySEA,"o:",label="solution_exacte",linewidth=7)
			ay.legend()
			show()
		elif(Q==0 and (xi!=a)==True):
			print("cette probleme de cauchy admet pas de solution au point entre")
		elif(Q<0):
			print("l'intervalle n'est pas bien definie")
		else:
		   (ax,ay)=subplots()
		   x=np.array([a+i*Q for i in range(0,n)])
		   #print("x=",x)
		   #ySEN=np.exp(x)
	  	 #x=[xo]
		   for i in range(0,n-1):
		       yi=yi+Q*exp(x[i])
		       yv=yv+Q*exp(Q*(1/2)+x[i])
		       yo=yo+(Q/2)*(2*exp(x[i])+Q*exp(x[i]))
		       #xo=a+i*Q
		       #x.append(xo)
		       ySEA.append(yi)
		       ySEAM.append(yo)
		       ySVM.append(yv)
		   for i in range(1,n):
		     	k1=exp(x[i-1])
		     	k2=exp(x[i-1]+(1/2)*Q)
		     	k3=exp(x[i-1]+Q)
		     	yrgk=yrgk+((1/6)*k1+(2/3)*k2+(1/6)*k3)*Q
		     	yRgK.append(yrgk)
		   #print(yRgK)
		   ySEN=np.exp(x)
		   ay.plot(x,yRgK,"k",label="Runge kutta d'orde 3",linewidth=3)
		   ay.plot(x,ySEN,"r",label="C_Normale(SN)", linewidth=3)
		   ay.plot(x,ySEA,"4:b",  				label="C_explicite_Euler(SEE)",linewidth=2)
		   ay.plot(x,ySEAM,"|-m",label="C_Euler_améliore(SEA)",linewidth=2)  # -b en trait bleu
		   ay.plot(x,ySVM,"*:c",label="C_Euler_Valeur_Milieu(SEAVM)",linewidth=2)
		   Er=[None]*n # Er est l'erreur globale par rapport la solution d'Euler ameliorée
		   for i in range(0,n):
		   	A=[x[i],x[i]];B=[0,ySEA[i]]
		   	Er[i]=ySEN[i]-ySEAM[i]  # ici Er[i] est l'erreur locale de la troncature
		   	ay.plot(A,B,":",linewidth=1)
		   ay.plot(x,Er,"--",label="C_Erreur(ESEA)",linewidth=1) 
		   print(abs(max(Er)))
		   xlabel("axe des abscisses")
		   ylabel("axe des ordonnées")
		   ay.legend()
		   show()
		return()
a=0
b=1  # prendre encore b=3*pi et a=0
n=5
xi=0
yi=1
(s)=Methode_Euler_explicite(a,b,n,xi,yi)
#print(a)