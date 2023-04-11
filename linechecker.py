print ("Nama : Safal")
print ("NIM : E1E120048")
print ("Program Periksa Garis (Horizontal/Vertikal)")
print ("===========================")

x1=float(input("Masukan titik x1 : "))
y1=float(input("Masukan titik y1 : "))
x2=float(input("Masukan titik x2 : "))
y2=float(input("Masukan titik y2 : "))

if (x1==x2):
    print("anda membentuk garis vertikal")
elif (y1==y2):
    print("anda membentuk garis horizontal")
else:
    print("garis anda tidak horizontal maupun vertikal")