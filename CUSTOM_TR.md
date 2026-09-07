# Concat 0.2.1 – Türkçe özel sürüm

Bu dal, Concat 0.2.1 kaynak kodu üzerinde şu değişiklikleri içerir:

- Arayüz ilk açılışta Türkçe başlar; Ayarlar'dan başka dil seçilebilir.
- Otomatik altyazıda Türkçe (`tr`) dili ayrı seçenek olarak eklendi.
- Hiç Whisper modeli kurulu değilse **Altyazı oluştur** ilk tıklamada ücretsiz çok dilli `base` modelini indirir ve indirme bitince otomatik olarak altyazı oluşturmaya devam eder.
- Otomatik altyazılar daha okunaklı olması için kalın ve ince siyah dış çizgili oluşturulur.
- `Ctrl` + `+` Türkçe klavye dahil `+` için Shift gereken düzenlerde de zaman çizelgesini yakınlaştırır.
- Klavye yakınlaştırması oynatma imlecini ekranda aynı noktada tutacak şekilde yapılır.
- Kırmızı oynatma imleci doğrudan tutulup sürüklenebilir; sürüklerken önizleme canlı olarak seek eder.
- İmleç yakınlaştırılmış zaman çizelgesinin kenarına sürüklenirse çizelge otomatik kaydırılır.

## Windows x86_64 derleme

Kaynak kodu bir GitHub deposuna koyduktan sonra **Actions → Build Windows TR → Run workflow** seçin. İş bittiğinde `Concat-TR-windows-x86_64` artifact'i içinde EXE ve gerekli DLL'lerle birlikte ZIP oluşur.

Bu proje AGPL-3.0-or-later lisanslıdır; değiştirilmiş kaynak kodu ve lisans dosyalarını dağıtımınızla birlikte erişilebilir tutun.
