# WordGrouperByInitial

## English

This project groups words from a text, DOCX, or PDF file by their initial letter and saves them in a JSON file. It is useful for text analysis, language processing, or educational purposes.

### Features
- Reads text from `.txt`, `.docx`, or `.pdf` files
- Groups words by their first letter
- Saves the grouped words as a single JSON file (`kelimeler.json`)

### Requirements
- Python 3.x
- `python-docx` and `PyPDF2` libraries

Install requirements:
```bash
pip install python-docx PyPDF2
```

### Usage
1. Place your file (e.g., `ornek.docx`) in the project directory.
2. Edit the `dosya_yolu` variable in `kelime.py` to your file name.
3. Run the script:
```bash
python kelime.py
```
4. The grouped words will be saved in `kelimeler.json`.

---

## Türkçe

Bu proje, bir metin, DOCX veya PDF dosyasındaki kelimeleri baş harfine göre gruplar ve JSON dosyasına kaydeder. Metin analizi, dil işleme veya eğitim amaçları için kullanılabilir.

### Özellikler
- `.txt`, `.docx` veya `.pdf` dosyalarından metin okur
- Kelimeleri ilk harfine göre gruplar
- Gruplanmış kelimeleri tek bir JSON dosyasına (`kelimeler.json`) kaydeder

### Gereksinimler
- Python 3.x
- `python-docx` ve `PyPDF2` kütüphaneleri

Gereksinimleri yüklemek için:
```bash
pip install python-docx PyPDF2
```

### Kullanım
1. Dosyanızı (örn. `ornek.docx`) proje klasörüne koyun.
2. `kelime.py` dosyasındaki `dosya_yolu` değişkenini dosya adınıza göre düzenleyin.
3. Scripti çalıştırın:
```bash
python kelime.py
```
4. Gruplanmış kelimeler `kelimeler.json` dosyasına kaydedilecektir. 