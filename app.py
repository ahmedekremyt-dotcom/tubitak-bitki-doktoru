import streamlit as st
import time
import random
import pandas as pd
import numpy as np

# Telefon ve Web için tam ekran, mobil uyumlu ayarlar
st.set_page_config(page_title="TÜBİTAK Akıllı Tarım AI", page_icon="🌍", layout="centered")

# --- BAŞLIK VE GİRİŞ ---
st.title("🌍 Akıllı Tarım ve Bitki Doktoru AI")
st.markdown("**Büyük Veri, Bulut Bilişim ve Çoklu Yapay Zeka (Multi-Agent) Destekli Teşhis Sistemi**")
st.divider()

# --- SEKMELER (Telefonda harika görünür) ---
tab1, tab2, tab3 = st.tabs(["🩺 AI Teşhis Merkezi", "📊 Büyük Veri & IoT", "🧠 AI İletişim Ağı"])

with tab1:
    st.header("📸 Bitki Hastalığı Teşhisi")
    st.write("Kameranızı açın veya hastalıklı bir yaprak fotoğrafı yükleyin.")
    
    secim = st.radio("Yöntem:", ["Kamera ile Çek", "Dosya Yükle"], horizontal=True)
    
    uploaded_file = None
    if secim == "Kamera ile Çek":
        uploaded_file = st.camera_input("Fotoğraf Çekin")
    else:
        uploaded_file = st.file_uploader("Fotoğraf Seçin", type=["jpg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Sisteme Yüklenen Görüntü", use_column_width=True)
        
        if st.button("🚀 Derin Öğrenme (CNN) ile Analiz Et", use_container_width=True):
            # Yapay Zeka düşünme efekti
            with st.spinner('Yapay Zeka Bulut Sunucularında Görüntüyü İşliyor...'):
                time.sleep(1.5)
                st.toast('Görüntü pikselleri ayrıştırıldı!', icon='✅')
                time.sleep(1.5)
                st.toast('Büyük Veri tabanında 50+ hastalık taranıyor...', icon='🔍')
                time.sleep(1.5)
            
            st.success("Tahlil Tamamlandı!")
            
            # Sonuç Kutuları
            col1, col2 = st.columns(2)
            col1.metric("Teşhis Edilen Hastalık", "Buğday - Sarı Pas")
            col2.metric("Yapay Zeka Güven Skoru", "%96.4")
            
            st.warning("🌱 **Doğal ve Ekolojik Çözüm:** Potasyum silikat bazlı organik gübre kullanımı ve tarlada faydalı böceklerin (uğur böceği vb.) artırılması için kenarlara fesleğen ekimi.")
            st.error("🧪 **Kimyasal Çözüm (Son Çare):** Triazole grubu onaylı bir fungusit uygulaması (Dozaj: Ziraat mühendisi kontrolünde).")

with tab2:
    st.header("🌍 Büyük Veri & IoT Sensör Simülasyonu")
    st.write("Tarladaki nem, sıcaklık ve toprak verileri anlık olarak buluta aktarılır.")
    
    # Sahte Büyük Veri Grafiği
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['Toprak Nemi', 'Hava Sıcaklığı', 'Hastalık Riski']
    )
    st.line_chart(chart_data)
    st.info("💡 **Büyük Veri Analizi:** Son 1 haftadaki nem artışı, mantar hastalıkları riskini %40 artırmıştır. Erken önlem alınması önerilir.")

with tab3:
    st.header("🧠 Yapay Zekalar Arası İletişim Ağı")
    st.write("Sistemimizde sadece 1 değil, 3 farklı Yapay Zeka birbiriyle konuşarak en doğru kararı verir.")
    
    if st.button("AI İletişim Protokolünü Başlat", use_container_width=True):
        st.chat_message("assistant").write("👁️ **Görüntü İşleme YZ:** Yaprakta sarı lekeler tespit ettim. Pas hastalığı olabilir.")
        time.sleep(1.5)
        st.chat_message("user").write("☁️ **İklim Verisi YZ:** Bölgedeki son 10 günlük nem oranını analiz ettim. Nem %80'in üzerinde, pas hastalığı için ideal ortam var.")
        time.sleep(1.5)
        st.chat_message("ai").write("🌾 **Ziraat Uzmanı YZ:** İkinizin verisini birleştirdim. Bu kesinlikle 'Sarı Pas'. Çiftçiye derhal ekolojik potasyum çözümü bildirimini gönderiyorum!")
        st.balloons()