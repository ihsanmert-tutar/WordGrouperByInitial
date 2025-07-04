import json
import re
import os
from collections import defaultdict
from docx import Document
import PyPDF2

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

def kelimeleri_grupla_ve_kaydet(metin):
    kelimeler = re.findall(r'\b\w+\b', metin.lower())
    gruplar = defaultdict(list)

    for kelime in kelimeler:
        ilk_harf = kelime[0]
        gruplar[ilk_harf].append(kelime)


    gruplar = {
        harf: sorted(list(set(kelimeler)))
        for harf, kelimeler in sorted(gruplar.items())
    }

    with open("kelimeler1.json", "w", encoding="utf-8") as f:
        json.dump(gruplar, f, ensure_ascii=False, indent=2)

    print("Tüm kelimeler alfabetik olarak gruplandı ve 'kelimeler1.json' dosyasına yazıldı.")


dosya_yolu = r"ornek.docx" 
metin = metin_oku(dosya_yolu)
kelimeleri_grupla_ve_kaydet(metin)
