from bs4 import BeautifulSoup

# Buka file HTML lama
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# 1. Ubah title
if soup.title:
    soup.title.string = "Penyedia Stok Produk Sembako Murah | UD Sinar Gemilang"

# 2. Tambahkan canonical link
canonical = soup.find("link", rel="canonical")
if not canonical:
    canonical = soup.new_tag("link", rel="canonical", href="https://pesananmu.vercel.app/")
    soup.head.append(canonical)
else:
    canonical["href"] = "https://pesananmu.vercel.app/"

# 3. Ubah menu header
nav = soup.find("nav")
if nav:
    nav.clear()
    ul = soup.new_tag("ul")
    li1 = soup.new_tag("li")
    a1 = soup.new_tag("a", href="Mitrashopee.html")
    a1.string = "Ajukan Pre Order Dengan Mitra Shopee"
    li1.append(a1)
    li2 = soup.new_tag("li")
    a2 = soup.new_tag("a", href="Mitrabukalapak.html")
    a2.string = "Ajukan Pre Order Dengan Mitra Bukalapak"
    li2.append(a2)
    ul.append(li1)
    ul.append(li2)
    nav.append(ul)

# 4. Tambahkan "Daftar Produk" sebelum footer
footer = soup.find("footer")
if footer:
    produk_section = BeautifulSoup("""
    <section id="daftar-produk" style="padding:50px 0; background-color:#fff;">
      <div class="container">
        <h2 style="text-align:center;">Daftar Produk</h2>
        <table border="1" cellspacing="0" cellpadding="8" style="width:100%; border-collapse:collapse;">
          <thead style="background:#f0f0f0;">
            <tr><th>No</th><th>Produk</th><th>Merek / Produsen</th><th>Kemasan</th><th>Harga per Karton</th></tr>
          </thead>
          <tbody>
            <tr><td>1</td><td>Minyak Kita 1L</td><td>Wilmar Nabati</td><td>Refill</td><td>Rp185.000</td></tr>
            <tr><td>2</td><td>Minyak Kita 1L</td><td>Sinar Mas</td><td>Refill</td><td>Rp176.000</td></tr>
            <tr><td>3</td><td>Minyak Kita Botol 1L</td><td>UD Sinar Gemilang</td><td>Botol</td><td>Rp188.000</td></tr>
          </tbody>
        </table>
      </div>
    </section>
    <section id="peringatan" style="background-color:#fff3cd; border:1px solid #ffeeba; padding:20px; margin-top:30px; text-align:center;">
      <h3>⚠️ Peringatan Resmi</h3>
      <p>Ajukan Pre Order Resmi Dari Web Kami.<br><b>Awas penipuan!</b> UD Sinar Gemilang hanya mempunyai web ini saja — tidak ada yang lain!</p>
    </section>
    """, "html.parser")
    footer.insert_before(produk_section)

# 5. Ubah footer kontak
if footer:
    footer.clear()
    new_footer = BeautifulSoup("""
    <footer style="background:#222; color:#fff; padding:20px; text-align:center;">
      <p>📞 083852320434 | ✉️ sinargrubminyakgoreng@gmail.com</p>
      <p>🌐 <a href="https://pesananmu.vercel.app/" style="color:#ffa500;">https://pesananmu.vercel.app/</a></p>
      <p>© 2025 UD Sinar Gemilang. All rights reserved.</p>
    </footer>
    """, "html.parser")
    soup.body.append(new_footer)

# Simpan hasil
with open("index.html", "w", encoding="utf-8") as f:
    f.write(str(soup))

print("✅ index.html berhasil diperbarui tanpa mengubah struktur lama.")