import numpy as np
from matplotlib.pyplot import*
from math import*
def Volume_finis(a,b,N,Uo,dfn):
	n=N-1
	Q=float((b-a))/n #le pas d'intervalle
	X=np.array([a+j*Q for j in range(0,N)],float)  # les valeurs de l'axe (ox)
	xj=[None]*N
	xj[0]=X[0]
	xj[N-1]=X[n]
	for j in range(1,N-1):
		xj[j]=a+(j-1/2)*Q
	F=np.array([None]*(n),float)
	H=[None]*(n-1)
	Y=np.array([None]*(n-1),float)
	(ax,ay)=subplots()    #creation des axes
	for i in range(0,n):
		F[i]=2*sin(xj[i])  #la valeur moyenne sur chaque sous-intervalles
	for i in range(0,n-1):
		H[i]=(xj[i+1]-xj[i])
	for i in range(0,n-1):
		Y[i]=Q*H[i]*F[i]   # le vecteur du système Ax=Y
	Y[0]=Y[0]+Uo
	Y[n-2]=Y[n-2]+Q*dfn
	A=np.array([[None]*n]*(n-1),float) #Matrice A, la taille des vecteurs interieure (n) donc les case A[:,n-1] sont vide.
	Diag=[None]*(n-1)
	for i in range(0,n-1):
		Diag[i]=2+Q*(H[i]) 
	Diag[n-2]=1+Q*H[n-2] # elements de la diganale.
	for i in range(0,n-1):
		for j in range(0,n-1):
			if(i==j and i<n-1):
				A[i,j]=Diag[i]
			elif(j==i-1 or i==j-1 ):
				A[i,j]=-1
			else:
				A[i,j]=0
   # print(A)
	for i in range(0,n-1):
		A[i,n-1]=Y[i]    #ajouter le vecteur Y à la dermiere colonne vide de la matrice,pour echelonner
	m=len(A)
#	print(A)
	for i in range(0,m):
		for j in range(i+1,m):
			 coef=A[j,i]/A[i,i]
			 A[j,:]=A[j,:]-coef*A[i,:]
	for i in range(0,m):
			A[i,:]=A[i,:]/A[i,i]
	sol=[None]*m
	sol[m-1]=A[m-1,m]
	for i in range(m-2,-1,-1):
		som=0
		for j in range(i+1,m):
			som=som+A[i,j]*sol[j]
		sol[i]=A[i,m]-som
	df=[None]*N #df doit contenir les conditions initiale et les solutions du système matricielle
	df[0]=Uo
	df[N-1]=sol[m-1]+Q*dfn
	for i in range(1,N-1):
		df[i]=sol[i-1]
	ay.plot(xj,df,":b",label="volume_finis",linewidth=4) #construction de la courbe approché
	ysn=np.sin(xj) # solution exacte 
	Er=[None]*N
	for i in range(0,N):
		Er[i]=ysn[i]-df[i]
	MaxEr=abs(Er[0])
	for i in range(0,N):
		if (MaxEr<=abs(Er[i])):
			MaxEr=abs(Er[i])
	print("le maximale des erreurs est: MaxEr:")
	print(MaxEr)
	#print(A)
	ay.plot(xj,Er,"--c",label="courbe des erreurs",linewidth=2)
	ay.plot(xj,ysn,"r",label="solution exacte",linewidth=2)
	xlabel("axe des abscisses")
	ylabel("axe des ordonnées")
	ay.legend()
	show() #éléments fini sur des rectangles
	return()
a=0
b=pi*2  #pi/4
Uo=0
dfn=1  # sqrt(2)/2
N=300 # le nombres de points interpolations
(s)=Volume_finis(a,b,N,Uo,dfn)