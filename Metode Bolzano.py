import numpy
print('METODE BOLZANO DENGAN MAX 25 ITERASI')
x1 = float(input("INSERT X1: "))       
x2 = float(input("INSERT X2: "))      
 
def f(x) :
    #MASUKKAN FUNGSI DISINI
    return (x*x*x) + (x*x) -(3*x) -3

if f(x1) * f(x2) > 0:
    print('f(X1) DAN f(X2) BERTANDA SAMA')
    exit()
print("\n") 
print('i     X1         X2      (X1+X1)/2   f(Xt)')
imax = 25 
k = 10E-5 
for i in range(imax):
    xt = (x1 + x2)/2
    print(str(i + 1)+'% 10.6f % 10.6f % 10.6f % 10.6f' %(x1, x2, xt, f(xt)))
    if numpy.abs(f(xt)) < k:
        print('ITERASI SELESAI')
        print('AKAR PERSAMAAN: '+ str(xt))
        exit()
    if f(x1) * f(xt) < 0:
        x2 = xt
    else: 
        x1 = xt
print('ITERASI SELESAI')
if i == imax - 1:
    print('Nilai akar: '+ str(xt))
print("\n")