from flask import Flask, render_template
import pandas

app = Flask(__name__)

sheet_id = "1Xu4zaMY4TYvHYQhfcLK0fvje4nguYarFf9XXhCmIh8c"


@app.route("/")
def hello():
    df = getData("daftar-inovasi")

    jenis_inovasi = []
    judul = []
    deskripsi = []
    link = []
    pengembang = []
    index = []

    for x in df["Jenis Inovasi"]:
        jenis_inovasi.append(x)
    for x in df["Judul"]:
        judul.append(x)
    for x in df["Deskripsi"]:
        deskripsi.append(x)
    for x in df["Link"]:
        link.append(x)
    for x in df["Pengembang"]:
        pengembang.append(x)

    data = {
        "jenis-inovasi": jenis_inovasi,
        "judul": judul,
        "deskripsi": deskripsi,
        "link": link,
        "pengembang": pengembang,
    }

    for x in range(len(df["Judul"])):
        index.append(x)

    return render_template("inovasi.html", data=data, index=index)


# read data from spreadsheet
def getData(sheet_name):
    url_spreadsheet = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    data = pandas.read_csv(url_spreadsheet)
    return data


# if __name__ == "__main__":
#     app.run(debug=True)
