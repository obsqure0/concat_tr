# Oblivion 0.2.2

Concat 0.2.1 tabanlı, Türkçe oyun videoları için özelleştirilmiş açık kaynak video düzenleyici.

## Minecraft videosuna altyazı

1. Videoyu içe aktarın, zaman çizelgesine ekleyin ve ses içeren klibi seçin.
2. **Altyazılar** aracını açın. Dil **Türkçe**, stil **Minecraft**, satır uzunluğu **Kısa satırlar** olsun.
3. **Modeli indir ve altyazı oluştur** düğmesine basın. İlk seferde internetten ücretsiz çok dilli Base modeli indirilir. Sonraki kullanımlar bilgisayarınızda çalışır; video herhangi bir sunucuya gönderilmez.
4. Oluşan yazılar zaman çizelgesinde düzenlenebilir metin klipleridir. Yazıyı seçerek içeriğini, boyutunu ve süresini değiştirebilirsiniz. Tüm eklemeyi tek seferde geri alabilirsiniz.
5. Videoyu dışa aktarınca altyazılar görüntüye işlenir.

Hazır altyazınız varsa aynı penceredeki **SRT altyazı içe aktar** ile UTF-8 `.srt` dosyasını seçin. SRT zamanları özgün video dosyasına göre olmalıdır; kırpılan klibin dışındaki satırlar alınmaz, sabit hız değişimi hesaba katılır. Kelime zamanlaması olmayan tanıma sonuçlarında kısa satır süreleri yaklaşık hesaplanır. Ters oynatma veya hız eğrisi kullanacaksanız altyazıları önce oluşturun.

## Eklenenler

- Uygulama adı, pencere başlığı ve Windows dosyası **Oblivion**.
- Windows'taki `Generic whisper error -6` üreten whisper.cpp yolu yerine sherpa-onnx CPU motoru.
- Tek model indirme akışı, ilerleme ve iptal desteği. Arşiv diske yazılmadan yalnızca gereken üç model dosyası açılır.
- Minecraft, klasik, sarı vurgu ve koyu zemin altyazı stilleri.
- Dört kelimelik kısa satırlar ve SRT içe aktarma.
- Metin kitaplığında Minecraft, sarı vurgu ve bölüm başlığı hazır stilleri.
- Altyazılar oyun görüntüsünün üzerinde, alt arayüzden biraz yukarıda konumlanır.
- Önceki dışa aktarma, yakınlaştırma, imleç ve metin önizleme düzeltmeleri bu sürümün kaynaklarına dahil edilmiştir.

## Derleme ve kaynak

GitHub Actions → **Build Oblivion Windows** çıktısı `Oblivion-TR-windows-x86_64` içinde program ZIP'ini ve değiştirilmiş kaynak ZIP'ini verir. Program ZIP'ini tamamen açın; `Oblivion.exe` gerekli DLL'lerle aynı klasörde olmalıdır.

Depodaki özgün kaynak ZIP'i korunur. `.github/patches/08-oblivion.patch` bu arşive uygulanan **birleştirilmiş** değişikliktir; 01–07 yamalarını ayrıca uygulamayın. Temiz bir klonda `python scripts/prepare_oblivion.py` çalıştırın, ardından `source/concat_tr/engine` altında `cargo build --profile app -p concat` ile derleyin. FFmpeg, LLVM ve sherpa-onnx geliştirme dosyaları için Windows iş akışına bakın.

Önceki iş akışı yamaları depo kökünün alt klasöründen çağırıyordu; Git bu yolları atlayıp başarılı dönebiliyordu. Yeni hazırlık betiği yamayı depo kökünden açık hedef diziniyle uygular, uygulama hatasında durur ve beklenen kaynak işaretlerini denetler.

AGPL-3.0-or-later lisansı ve özgün telif bildirimleri korunmuştur. Oblivion, özgün Concat projesinden bağımsız bir türevdir.
