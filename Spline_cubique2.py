import numpy as np
from matplotlib.pyplot import*
from math import*
def spline_cubique(X,dfo): # X est un vecteur contenant les point interpolation:
	N=len(X); n=N-1
	H=[None]*n
	F=[None]*N
	Y=[None]*n
	(ax,ay)=subplots()
	for i in range(0,n):
		H[i]=(X[i+1]-X[i])
	for i in range(0,N):
		F[i]=sin(X[i])
	for i in range(0,n):
		Y[i]=(2*(F[i+1]-F[i]))/H[i]
	Y[0]=Y[0]-dfo
	A=np.array([[None]*N]*n)
	for i in range(0,n):
		for j in range(0,n):
			if(i==j or j==i-1):
				A[i,j]=1
			else:
				A[i,j]=0
	for i in range(0,n):
		A[i,n]=Y[i]
	m=len(A)
	for i in range(0,m):
		for j in range(i+1,m):
			 coef=A[j,i]/A[i,i]
			 A[j,:]=A[j,:]-coef*A[i,:]
	for i in range(0,m):
			A[i,:]=A[i,:]/A[i,i]
	df=[None]*N #df doit contenir les conditions initiale et les solution du système matricielle
	df[0]=dfo
	sol=[None]*m
	sol[m-1]=A[m-1,m]
	for i in range(m-2,-1,-1):
		som=0
		for j in range(i+1,m):
			som=som+A[i,j]*sol[j]
		sol[i]=A[i,m]-som
	for i in range(1,N):
		df[i]=sol[i-1]
	x=np.array([[None]*(n+50)]*n)
	for i in range(0,n):
		for j in range(0,n+50):
			x[i,j]=X[i]+j*(H[i]/(n+50)) # construction des polynômes Sj sur n+50 points de chaque sous-intervalle Ij
	y=np.array([[None]*(n+50)]*n,float)
	for i in range(0,n):
		for j in range(0,n+50):
			y[i,j]=((df[i+1]-df[i])*((-X[i+1]+x[i,j])**2))/(2*H[i])+(df[i]*(-X[i]+x[i,j]))+F[i]
	ay.plot(x[0],y[0],":b",label="spline_cubique",linewidth=3)
	MEr=np.array([[None]*(n+50)]*n,float) #matrice contenant les erreurs
	for i in range(0,n):
		for j in range(0,n+50):
			MEr[i,j]=sin(x[i,j])-y[i,j]
	MaxEr=0
	for i in range(0,n):
		for j in range(0,n+50):
			if(MaxEr<abs(MEr[i,j])):
				MaxEr=MEr[i,j]
	print("Le maximale des erreurs de cette interpolation est:")
	print("MaxEr=",MaxEr) # affiche le max des erreurs
	ay.plot(x[0],MEr[0],"-k",label="Courbe des Erreurs",linewidth=2)
	for i in range(1,n):
			ay.plot(x[i],y[i],":b",linewidth=3)
			ay.plot(x[i],MEr[i],"-k",linewidth=2)
	ysn=np.sin(X)
	ay.plot(X,ysn,"o-r",label="solution exacte",linewidth=1)
	xlabel("axe des abscisses")
	ylabel("axe des ordonnées")
	ay.legend()
	show()
	return()
#X=[-1,2,4,5,6.7,8,9.3,10]
a=-2*pi
b=2*pi
N=100
Q=(b-a)/N
X=np.array([a+j*Q for j in range(0,N+1)])
dfo=cos(a)  # la valeur de la derivée au primiére point.
(s)=spline_cubique(X,dfo)