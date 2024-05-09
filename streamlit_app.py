import streamlit as st

st.write("Welcome to My Mini Market")

total = 0
barang = []
harga = {
    1: 5000,
    2: 7000,
    3: 8000,
    4: 12000,
    5: 10000,
    6: 4000,
    7: 3000,
}

lanjut = 'Ya'
i = 0
while lanjut == 'Ya':
    st.write("""Daftar Barang\n
    1. Roti \t 5000
    2. Es Krim \t 7000
    3. Keripik \t 8000
    4. Coklat \t 12000
    5. Buku \t 10000
    6. Pensil \t 4000
    7. Penghapus \t 3000
    """)

    kode = st.number_input("Masukkan kode barang:", min_value=1, max_value=7, key=f"kode_{i}")
    if kode in harga:
        barang.append(kode)
        total += harga[kode]
    else:
        st.write('Kode tidak valid')

    lanjut = st.selectbox('Lanjut belanja?', ['Ya', 'Tidak'], key=f"lanjut_{i}")
    i += 1

st.write('Barang yang dibeli:')
for item in barang:
    st.write(f"- {item}: {harga[item]}")

st.write(f'Total yang harus dibayar: {total}\n')

uang = st.number_input('Masukkan uang pembayaran: ')
if uang > total:
    st.write(f'Kembaliannya: {uang - total}')
elif uang == total:
    st.write('Uang pas')
else:
    st.write(f'Uangnya kurang: {total - uang}')
