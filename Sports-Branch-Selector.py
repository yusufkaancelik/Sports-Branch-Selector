def uygun():
  print("bu branşa yazılabilirsiniz")
def degil():
  print("bu branşa uygun değilsiniz")
brnslr=["Futbol","Yüzme","Handball","Basketbol","Jimnastik"]
k={"nihal","ipek","özden"}
e={"enes","ufuk","ulaş","burak","caner"}
isim_gir= input("adınızı girin:").lower()
yas_gir= int(input("yaşınızı girin:"))
ss=0
for branslar in brnslr:
  ss=ss+1
  print(ss,branslar)
brans_gir= input("seçmek isteiğiniz branşı yazınız:").lower()
if isim_gir in k:
  if brans_gir == "futbol" or brans_gir== "1":
    kontrol= input("futbol sertifikanız var mı [e/h] : ").lower()
    if kontrol == "e":
      print("bu branşa yazılabilirsiniz")
    else:
      print("bu branşa uygun değilsiniz")

  elif brans_gir == "yüzme" or brans_gir == "1" and yas_gir <=6:uygun()

  elif brans_gir == "handball" or brans_gir == "3" and yas_gir <=8:uygun()

  elif brans_gir == "basketbol" or brans_gir == "4" and 20 <= yas_gir <= 30 :uygun()

  elif brans_gir == "jimnastik" or brans_gir == "5":degil()

  else:degil()

elif isim_gir in e:
  if brans_gir == "futbol" or brans_gir== "1":
    kontrol= input("futbol sertifikanız var mı [e/h] :").lower()
    if kontrol == "e":uygun()
    else:degil()

  elif brans_gir == "yüzme" or brans_gir == "2" and yas_gir <=6:uygun()

  elif brans_gir == "handball" or brans_gir == "3" and yas_gir <=8:uygun()

  elif brans_gir == "basketbol" or brans_gir == "4" and 20 <= yas_gir <= 30 :uygun()

  elif brans_gir == "jimnastik" or brans_gir == "5":degil()

  else:degil()

else:
  print("Geçerli bir isim girin!")

