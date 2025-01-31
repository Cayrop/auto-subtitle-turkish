# Auto-Subtitle-Turkish

Auto-Subtitle-Turkish, [auto-subtitle](https://github.com/m1guelpf/auto-subtitle) kütüphanesinin bir forkudur ve Türkçe çeviri desteği eklenmiştir. Bu proje, videolar için otomatik altyazı oluşturur ve çevirisini sağlar.

## Özellikler
- Videolardan altyazı oluşturma
- OpenAI Whisper modelini kullanarak ses transkripsiyonu
- Türkçe çeviri desteği (Helsinki-NLP/opus-mt-tc-big-en-tr modeli ile)
- MP4 ve WEBM formatlarını destekler

## Kurulum
Projeyi kullanabilmek için aşağıdaki adımları takip edin:

### pip ile Kurulum
```bash
pip install git+https://github.com/Cayrop/auto-subtitle-turkish.git
```

### Bağımlılıkları Yüklenme
```bash
pip install -r requirements.txt
```
veya
```bash
pip install ffmpeg-python openai-whisper transformers sentencepiece numpy==1.26.4
```

## Kullanım
Komut satırından şu şekilde çalıştırabilirsiniz:
```bash
auto-subtitle /path/to/videos --translate_to_turkish True
```
Bu komut, belirtilen dizindeki tüm videolar için otomatik altyazı oluşturur ve bunları Türkçeye çevirir.

### Opsiyonel Argümanlar
- `--model`: Kullanılacak Whisper modeli (varsayılan: large-v3-turbo)
- `--verbose`: Ayrıntılı hata ayıklama mesajlarını görmek için (varsayılan: False)
- `--translate_to_turkish`: Altyazıları Türkçeye çevirmek için (varsayılan: True)

## Lisans
Bu proje [MIT Lisansı](LICENSE) altında sunulmuştur.

## Katkıda Bulunma
Katkıda bulunmak için repo'yu fork edip, değişikliklerinizi pull request olarak gönderebilirsiniz.

## Bağlantılar
- Orijinal proje: [auto-subtitle](https://github.com/m1guelpf/auto-subtitle)
- Bu fork: [auto-subtitle-turkish](https://github.com/Cayrop/auto-subtitle-turkish)

