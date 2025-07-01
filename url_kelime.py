import json
import re
import os
from collections import defaultdict
from docx import Document
import PyPDF2
import requests
from bs4 import BeautifulSoup

def metin_oku(dosya_yolu):
    uzanti = os.path.splitext(dosya_yolu)[1].lower()

    if uzanti == ".txt":
        with open(dosya_yolu, "r", encoding="utf-8") as f:
            return f.read()

    elif uzanti == ".docx":
        doc = Document(dosya_yolu)
        return "\n".join([para.text for para in doc.paragraphs])

    elif uzanti == ".pdf":
        with open(dosya_yolu, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            metin = ""
            for sayfa in reader.pages:
                metin += sayfa.extract_text() + "\n"
            return metin

    else:
        raise ValueError("Desteklenmeyen dosya türü: " + uzanti)

def urlden_metin_cek(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

 
    content = soup.find("div", id="mw-content-text")
    if not content:
        content = soup  

   
    yazilar = []
    for tag in content.find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6", "li", "span", "b", "a"]):
        text = tag.get_text(strip=True)
        if text:
            yazilar.append(text)

    metin = "\n".join(yazilar)
    return metin

def kelimeleri_grupla_ve_kaydet(metin):
    turkce_harfler = set("abcçdefgğhıijklmnoöprsştuüvyz")
    kelimeler = re.findall(r'\b\w+\b', metin.lower())
    gruplar = defaultdict(list)

    for kelime in kelimeler:
        ilk_harf = kelime[0]
        if ilk_harf in turkce_harfler:
            gruplar[ilk_harf].append(kelime)


    gruplar = {
        harf: sorted(list(set(kelimeler)))
        for harf, kelimeler in sorted(gruplar.items())  
    }

    with open("kelimeler_url.json", "w", encoding="utf-8") as f:
        json.dump(gruplar, f, ensure_ascii=False, indent=2)

    print("Sadece Türkçe harflerle başlayan kelimeler alfabetik sırayla 'kelimeler_url.json' dosyasına yazıldı.")




haber_linki = "https://www.milliyet.com.tr/"  
metin = urlden_metin_cek(haber_linki)
kelimeleri_grupla_ve_kaydet(metin)
