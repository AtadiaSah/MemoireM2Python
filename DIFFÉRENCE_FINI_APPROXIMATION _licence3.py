import numpy as np
from matplotlib.pyplot import*
from math import*
def difference_fini(a,b,n,Uo,Un):
	Q=float((b-a))/n   #le pas d'intervalle
	X=np.array([a+j*Q for j in range(0,n+1)],float)  # les valeurs de l'axe (ox)
	F=np.array([None]*(n-1),float)
	Y=np.array([None]*(n-1),float)
	(ax,ay)=subplots()    #creation des axes
	for i in range(1,n):
		F[i-1]=(X[i]**2)*exp(-X[i])  #les images de la fonction sur chaque point de (ox)
	for i in range(0,n-1):
		Y[i]=(Q**2)*F[i]   # le vecteur du système Ax=Y
	Y[0]=Y[0]+Uo
	Y[n-2]=Y[n-2]+Un
	A=np.array([[None]*n]*(n-1),float) #Matrice A, la taille des vecteurs intrieure (n) donc les case A[0,n+1] sont vide.
	for i in range(0,n-1):
		for j in range(0,n-1):
			if(i==j):
				A[i,j]=2
			elif(j==i-1 or i==j-1 ):
				A[i,j]=-1
			else:
				A[i,j]=0
	for i in range(0,n-1):
		A[i,n-1]=Y[i]    #ajouter le vecteur Y à la dermiere colonne de la matrice,pour echelonner
	m=len(A)
	for i in range(0,m):
		for j in range(i+1,m):
			 coef=A[j,i]/A[i,i]
			 A[j,:]=A[j,:]-coef*A[i,:]
	for i in range(0,m):
			A[i,:]=A[i,:]/A[i,i]
	df=[None]*(n+1) #df doit contenir les conditions initiale et les solution du système matricielle
	df[0]=Uo
	df[n]=Un
	df[n-1]=A[n-2,n-1]
	for i in range(n-2,0,-1):
		som=0
		for j in range(i+1,n):
			som=som+A[i-1,j-1]*df[j]
		df[i]=A[i-1,n-1]-som
	ay.plot(X,df,":b",label="différence_fini",linewidth=4) #construction de la courbe approché
	ysn=np.exp(-X)*(-X**2-4*X-6)-(6-11*exp(-1))*X+6 # pour la solution exacte
	ay.plot(X,ysn,"r",label="solution exacte",linewidth=2)
	Er=[None]*(n+1)
	for i in range(0,n):
		Er[i]=ysn[i]-df[i]
	ay.plot(X,Er,"--c",label="courbe_des_erreurs",linewidth=1)
	xlabel("axe des abscisses")
	ylabel("axe des ordonnées")
	ay.legend()
	show()
	return()
a=0
b=1
Uo=0
Un=0
n=50
(s)=difference_fini(a,b,n,Uo,Un)