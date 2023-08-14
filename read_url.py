import pandas as pd

SHEET_ID = "1Xu4zaMY4TYvHYQhfcLK0fvje4nguYarFf9XXhCmIh8c"
SHEET_NAME = "inovasi"
url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"
df = pd.read_csv(url)
jenis = []
judul = []
deskripsi = []
link = []
pengembang = []

mess = []
for x in df["Jenis Inovasi"]:
    jenis.append(x)
for x in df["Judul"]:
    judul.append(x)
for x in df["Deskripsi"]:
    deskripsi.append(x)
for x in df["Link"]:
    link.append(x)
for x in df["Pengembang"]:
    pengembang.append(x)
mess.append(f"{jenis[0]} {judul[0]} {deskripsi[0]} {link[0]} {pengembang[0]}")
print(df)
# print(df["Perintah"])
