# Kanban: kurulum ve haftalık rutin

Projenin Agile / Kanban takibiyle ilgili dosyalar bu klasörde.

| Dosya | İçerik |
|---|---|
| `KANBAN_PLANI.md` | 5 haftalık plan ve 31 kartın tamamı (Description, Acceptance Criteria, Evidence) |
| `kanban_gorevleri.csv` | Aynı kartların tablo hâli (Excel'de açılıyor, Trello/Jira'ya da aktarılabilir). Final teslimdeki "Kanban görev detayları CSV export" için temel |
| `github_kanban_kur.py` | Kartları tek komutla GitHub Issues olarak açıp GitHub Projects panosuna ekleyen betik |
| `haftalik-snapshotlar/` | Her hafta sonu alınan pano ekran görüntüleri |

## 1. Panoyu kurma (bir kez, yaklaşık 10 dk)

Araç olarak GitHub Projects kullanılıyor. Kartlar Issue olduğu için commit ve Pull Request'ler doğrudan karta
bağlanıyor; PR açıklamasına `Closes #12` yazılınca PR birleştiğinde kart otomatik olarak Done'a geçiyor. Ödevdeki
Evidence şartının büyük kısmı bu şekilde karşılanıyor.

1. GitHub'da depoyu oluştur ve başlangıç dosyalarını push et (bkz. `docs/git-workflow.md`).
2. `gh` CLI ile proje oluşturma yetkisini ver ve kurulum betiğini çalıştır:
   ```bash
   brew install gh            # macOS; yoksa https://cli.github.com
   gh auth login
   gh auth refresh -s project # GitHub Projects panosu oluşturma ve kart ekleme yetkisi
   python3 kanban/github_kanban_kur.py --repo alimustafaekmen/etkinlik-kayit-sistemi --dry-run
   python3 kanban/github_kanban_kur.py --repo alimustafaekmen/etkinlik-kayit-sistemi --create-project
   ```
   Betik etiketleri (19), milestone'ları (`Hafta 1`–`Hafta 5`) ve 31 Issue'yu oluşturur; ardından public bir GitHub
   Projects panosu açar, depoya bağlar ve mevcut/yeni tüm Issue'ları tekrar etmeden panoya ekler.
   Var olan bir panoya eklemek için `--create-project` yerine `--project <numara>` kullanılabilir.
3. Pano açıldıktan sonra GitHub Projects > View > Board görünümünde Status alanına `Issues / Blocked` sütununu
   ekle (`Todo · In Progress · Issues / Blocked · Done`).
4. Proje > `⋯` > Workflows: "Item closed → Done" ve "Pull request merged → Done" otomasyonlarını kontrol et.
5. Haftalık görünüm için Board görünümünde Group by: `Milestone` veya `milestone:"Hafta 1"` filtresini kullan.
6. Proje URL'sini OnlineBeykoz'a bildir. 5 hafta boyunca aynı URL kullanılmalı.

Trello ile yapılacak olursa listeler To Do / In Progress / Issues / Done olur; her kartta `KANBAN_PLANI.md`'deki
Description açıklamaya, Acceptance Criteria Checklist'e, kanıtlar Attachment/Link olarak eklenir.

## 2. Kart yaşam döngüsü

```
To Do ──(çalışmaya başla, branch aç)──> In Progress ──(PR birleşti + kriterler sağlandı)──> Done
                                            │
                                            └──(hata/engel)──> Issues / Blocked ──(çözüldü)──┘
```

Bir kart Done'a taşınmadan önce:
- [ ] Acceptance Criteria kutularının hepsi işaretli
- [ ] Evidence bölümüne gerçek link eklendi (commit, PR, Actions run, Render URL, ekran görüntüsü)

## 3. Haftalık rutin (her hafta sonu yaklaşık 10 dk)

1. Kartların durumunu güncelle; yeni çıkan işler için kart aç (ör. bulunan bir hata için `Bug` etiketli kart).
2. Panonun tamamını gösteren ekran görüntüsü al (macOS: `Cmd + Shift + 4`, ardından boşluk tuşu ile pencere seçimi).
3. Önce yerel arşive `haftalik-snapshotlar/hafta-0N_YYYY-AA-GG.png` adıyla kaydet, ardından OnlineBeykoz teslim
   kuralına göre kopyala:
   - Güncel görüntü: `Kanban_Week_0N.png` (ör. `Kanban_Week_01.png`)
   - Kümülatif geçmiş ZIP: `Kanban_History_Week_01-0N.zip` (ör. `Kanban_History_Week_01-01.zip`)
4. Geçmiş ZIP'ini oluştur:
   ```bash
   cd kanban && zip -r ../teslim/Kanban_History_Week_01-0N.zip haftalik-snapshotlar -x "*.md"
   ```
5. OnlineBeykoz'a güncel `Kanban_Week_0N.png`, `Kanban_History_Week_01-0N.zip` ve pano URL'sini yükle.
6. Haftalık 3-5 dk sunum notlarını `docs/haftalik-sunum-notlari.md`'den hazırla.

Ekran görüntüleri o haftanın gerçek durumunu göstermeli; hoca ilerlemeyi bu geçmişe bakarak değerlendiriyor.

## 4. Final teslim için Kanban export

GitHub Projects > Table görünümü > `⋯` > Export view data (CSV) ile kartlar dışa aktarılabilir. Diğer seçenek, bu
klasördeki `kanban_gorevleri.csv` dosyasının `status` ve `evidence` sütunlarını gerçek değerlerle güncelleyip
teslim etmek.
