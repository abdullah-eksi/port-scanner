# Port Tarama Aracı

Bu program, belirtilen bir hedefe yönelik port taraması yapabilen basit bir Python betiğidir. Port taraması, hedefin belirli bir port üzerinde açık veya kapalı olup olmadığını kontrol etmek için kullanılır.

## Kurulum

1. Python'ın en son sürümünü [Python web sitesinden](https://www.python.org/downloads/) indirin ve kurun.

2. Programın çalışması için `socket` modülüne ihtiyaç duyar. Bu modül standart Python kitaplığına dahildir, dolayısıyla ek bir kurulum yapmanız gerekmez.

## Kullanım

1. Terminal veya komut istemcisini açın.

2. Port taramasını yapmak istediğiniz dizine gidin.

3. Aşağıdaki komutu çalıştırın:

   ```
   python port_scan.py
   ```

4. Program başlatılacak ve aşağıdaki bilgileri isteyecektir:

   - Hedef IP adresi veya alan adı: Tarama yapmak istediğiniz hedefin IP adresini veya alan adını girin.
   - Başlangıç port numarası: Taramanın başlayacağı port numarasını girin.
   - Bitiş port numarası: Taramanın sonlanacağı port numarasını girin.

5. Program taramayı gerçekleştirecek ve sonuçları ekranda gösterecektir.

## Örnek

Aşağıda bir örnek kullanım senaryosu bulunmaktadır:

```
Hedef IP adresini veya alan adını girin: example.com
Başlangıç port numarasını girin: 1
Bitiş port numarasını girin: 100

example.com için Port Tarama Sonuçları:

Port 80: Açık
Port 443: Kapalı
Port 22: Kapalı
...
```

Bu örnek, "example.com" alan adına 1 ile 100 arasındaki portları tarayacak ve sonuçları ekranda gösterecektir.

## Notlar

- Port taraması, hedef sisteme izinsiz erişim denemeleri içerebilir. Bu nedenle, port taraması yaparken hedef sistemin sahibinden veya ilgili makamdan izin almanız önemlidir. Aksi takdirde, yasaları ihlal etmiş olabilirsiniz.

- Port taraması, güvenlik testlerinde ve ağ yönetimi amaçlarıyla kullanılabilir. Ancak, başkalarının sistemlerini etkilemek veya zarar vermek amacıyla kullanmak suç teşkil eder.

- Bu program, sadece TCP portlarını tarar. Diğer protokoller veya port tipleri için değişiklikler yapmanız gerekebilir.

- Programın performansı, hedef sistemin cevap süresi ve ağ bağlantısı durumuna bağlı olacaktır. Büyük bir port aralığında tarama yaparken programın uzun sürebileceğini unutmayın.

- Program, basit bir örnek olarak sunulmuştur ve geliştirilmesi gereken birçok alanı bulunmaktadır. Gerçek dünyada kullanmadan önce güvenlik ve hata kontrolü gibi konulara dikkat etmeniz önemlidir.

