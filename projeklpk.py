import streamlit as st

# Judul aplikasi
st.title("Kalkulator Kandungan Energi Makanan")

# Deskripsi aplikasi
st.markdown("""
Aplikasi ini membantu menghitung kandungan energi makanan (dalam kilokalori) berdasarkan jumlah karbohidrat, protein, dan lemak yang terkandung.
""")

# Input pengguna
st.header("Masukkan Data Komposisi Makanan")
karbohidrat = st.number_input("Karbohidrat (gram):", min_value=0.0, value=0.0, step=0.1)
protein = st.number_input("Protein (gram):", min_value=0.0, value=0.0, step=0.1)
lemak = st.number_input("Lemak (gram):", min_value=0.0, value=0.0, step=0.1)

# Perhitungan energi
def hitung_kalori(karbo, prot, lemak):
    energi_karbo = karbo * 4  # 4 kalori per gram
    energi_protein = prot * 4  # 4 kalori per gram
    energi_lemak = lemak * 9  # 9 kalori per gram
    total_energi = energi_karbo + energi_protein + energi_lemak
    return energi_karbo, energi_protein, energi_lemak, total_energi

energi_karbo, energi_protein, energi_lemak, total_energi = hitung_kalori(karbohidrat, protein, lemak)

# Tampilkan hasil
st.header("Hasil Perhitungan Energi")
st.write(f"**Energi dari Karbohidrat:** {energi_karbo:.2f} kkal")
st.write(f"**Energi dari Protein:** {energi_protein:.2f} kkal")
st.write(f"**Energi dari Lemak:** {energi_lemak:.2f} kkal")
st.write(f"**Total Energi:** {total_energi:.2f} kkal")

# Grafik Pie Chart (opsional)
if st.checkbox("Tampilkan Grafik Pie Chart"):
    import matplotlib.pyplot as plt

    # Data untuk pie chart
    labels = ["Karbohidrat", "Protein", "Lemak"]
    values = [energi_karbo, energi_protein, energi_lemak]
    colors = ["#FF9999", "#99FF99", "#9999FF"]

    # Plot grafik
    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=labels, autopct="%1.1f%%", colors=colors, startangle=140)
    plt.title("Distribusi Energi Makanan")
    st.pyplot(plt)

# Footer
st.write("---")
st.caption("Dibuat dengan 💻 oleh [Nama Anda]")
