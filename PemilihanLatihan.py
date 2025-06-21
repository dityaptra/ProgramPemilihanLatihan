def pemilihan_latihan(daftar_latihan, waktu_tersedia, strategi):
    if strategi == "kalori":
        daftar_latihan.sort(key=lambda latihan: latihan['kalori'], reverse=True)
    elif strategi == "durasi":
        daftar_latihan.sort(key=lambda latihan: latihan['durasi'])
    elif strategi == "density":
        daftar_latihan.sort(key=lambda latihan: latihan['kalori'] / latihan['durasi'], reverse=True)
    else:
        raise ValueError("Pilih 'kalori', 'durasi', atau 'density'.")

    latihan_terpilih = []
    total_kalori = 0
    total_durasi = 0
    
    for latihan in daftar_latihan:
        if latihan['durasi'] + total_durasi <= waktu_tersedia:
            latihan_terpilih.append(latihan)
            total_kalori += latihan['kalori']
            total_durasi += latihan['durasi']
    
    return latihan_terpilih, total_kalori, total_durasi


daftar_latihan = [
    {'nama': 'Yoga', 'kalori': 110, 'durasi': 30},
    {'nama': 'Lompat Tali', 'kalori': 184, 'durasi': 15},
    {'nama': 'Push Up', 'kalori': 147, 'durasi': 15},
    {'nama': 'Hula Hoop', 'kalori': 61, 'durasi': 10},
    {'nama': 'Zumba', 'kalori': 86, 'durasi': 10},
    {'nama': 'Body Combat', 'kalori': 257, 'durasi': 30},
    {'nama': 'Bikram Yoga', 'kalori': 147, 'durasi': 30},
    {'nama': 'Trampoline', 'kalori': 74, 'durasi': 10}
]
waktu_tersedia = 75
strategi = "density" # ("kalori"/"durasi"/"density")

latihan_terpilih, total_kalori, total_durasi = pemilihan_latihan(daftar_latihan, waktu_tersedia, strategi)
print(f"=== Strategi Greedy by {strategi.capitalize()} ===")
print("Latihan yang terpilih:")
for latihan in latihan_terpilih:
    if strategi == "density":
        density = round(latihan['kalori'] / latihan['durasi'], 2)
        print(f"- {latihan['nama']}: {latihan['kalori']} kalori, {latihan['durasi']} menit, {density}")
    else:
        print(f"- {latihan['nama']}: {latihan['kalori']} kalori, {latihan['durasi']} menit")
print(f"\nTotal pembakaran kalori: {total_kalori} kalori")
print(f"Total durasi latihan: {total_durasi} menit")
