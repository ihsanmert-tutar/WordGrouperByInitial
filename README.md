# WordGrouperByInitial

## English

Groups words from text files, DOCX, PDF files, or web URLs by their initial letter and saves them in JSON files.

### Features
- Reads from `.txt`, `.docx`, `.pdf` files
- Extracts text from web URLs
- Groups words by first letter
- Filters Turkish words (URL version)
- Saves results as JSON

### Requirements
```bash
pip install python-docx PyPDF2 requests beautifulsoup4
```

### Usage

#### Local Files (`kelime.py`)
1. Place your file in the project directory
2. Edit `dosya_yolu` in `kelime.py`
3. Run: `python kelime.py`
4. Results saved to `kelimeler1.json`

#### Web URLs (`url_kelime.py`)
1. Edit `haber_linki` in `url_kelime.py`
2. Run: `python url_kelime.py`
3. Results saved to `kelimeler_url.json`

---

## Türkçe

Metin dosyaları, DOCX, PDF dosyaları veya web URL'lerindeki kelimeleri baş harfine göre gruplar ve JSON dosyalarına kaydeder.

### Özellikler
- `.txt`, `.docx`, `.pdf` dosyalarından okur
- Web URL'lerinden metin çıkarır
- Kelimeleri ilk harfine göre gruplar
- Türkçe kelimeleri filtreler (URL versiyonu)
- Sonuçları JSON olarak kaydeder

### Gereksinimler
```bash
pip install python-docx PyPDF2 requests beautifulsoup4
```

### Kullanım

#### Yerel Dosyalar (`kelime.py`)
1. Dosyanızı proje klasörüne koyun
2. `kelime.py` dosyasındaki `dosya_yolu` değişkenini düzenleyin
3. Çalıştırın: `python kelime.py`
4. Sonuçlar `kelimeler1.json` dosyasına kaydedilir

#### Web URL'leri (`url_kelime.py`)
1. `url_kelime.py` dosyasındaki `haber_linki` değişkenini düzenleyin
2. Çalıştırın: `python url_kelime.py`
3. Sonuçlar `kelimeler_url.json` dosyasına kaydedilir 