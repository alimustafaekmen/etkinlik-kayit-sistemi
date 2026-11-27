# Gereksinimler

## Amaç

Seminer, atölye gibi küçük etkinlikler için kayıt toplamak ve kontenjanın aşılmasını önlemek. Dersin odağı DevOps
olduğu için uygulamayı 5 temel fonksiyonla sınırladım. Kullanıcı girişi yok; etkinliği oluşturan da kayıt olan da
aynı arayüzü kullanıyor.

## Fonksiyonel gereksinimler

- FR-1 Etkinlik oluşturma: Ad (3-120 karakter), konum, gelecekte bir tarih ve 1-10.000 arası kontenjan zorunlu,
  açıklama isteğe bağlı. Hatalı alanlar ayrı ayrı gösterilir (400), başarılı olursa 201 döner.
- FR-2 Listeleme ve detay: Etkinlikler tarihe göre sıralanır. Kayıtlı sayısı ve kalan yer görünür. Ad veya konuma
  göre arama yapılabilir. Olmayan etkinlik 404 döner. Katılımcı e-postaları listede maskeli gösterilir.
- FR-3 Katılımcı kaydı: Ad soyad ve geçerli e-posta ile kayıt olunur. Aynı e-posta aynı etkinliğe ikinci kez
  kaydolamaz (409). Büyük/küçük harf farkı dikkate alınmaz.
- FR-4 Kontenjan kontrolü: Kontenjan dolunca yeni kayıt reddedilir (409 `capacity_full`). Aynı anda gelen isteklerde
  de kontenjan aşılmaz. Tarihi geçmiş etkinliğe kayıt yapılamaz (400).
- FR-5 Kayıt iptali: Katılımcı kayıtta kullandığı e-postayla kaydını iptal eder ve kalan yer bir artar. Kayıt yoksa
  404 döner.

## Fonksiyonel olmayan gereksinimler

- NFR-1 Test: En az 3 otomatik test, hedef %80 kapsam.
- NFR-2 CI: Her pull request'te lint ve testler otomatik çalışır. CI kırmızıysa merge yapılmaz.
- NFR-3 Docker: Uygulama Docker imajıyla çalışır, ayarlar ortam değişkenlerinden okunur.
- NFR-4 Bulut: Uygulama Render'da HTTPS ile yayında, veriler Neon PostgreSQL'de kalıcı.
- NFR-5 İzleme: `/health`, `/metrics` ve JSON loglar.
- NFR-6 Güvenlik: Gizli bilgiler kodda yok, konteyner root olmayan kullanıcıyla çalışır, formlarda CSRF koruması var,
  SQL sorguları parametreli.
- NFR-7 Arayüz: Türkçe, mobilde de okunabilir.

## Kapsam dışı

Kullanıcı hesabı, ödeme, e-posta bildirimi, bekleme listesi, etkinlik düzenleme ve silme.

## Demo senaryosu

1. Kontenjanı 2 olan "Docker Atölyesi" oluşturulur. (FR-1)
2. Etkinlik listede "Kayıt açık" olarak görünür. (FR-2)
3. Ayşe ve Mehmet kaydolur, etkinlik "Dolu" olur. (FR-3)
4. Zeynep kaydolmaya çalışır ve "Kontenjan dolu" mesajı alır. (FR-4)
5. Mehmet kaydını iptal eder, Zeynep kaydolabilir. (FR-5)
