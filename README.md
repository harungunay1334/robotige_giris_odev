# ROS Ödevleri: Publisher/Subscriber (Python)

Bu paket, ROS (Robot Operating System) eğitimleri kapsamında verilmiş Turtlesim Konum Okuma (Subscriber) ve Hareket Kontrol (Publisher) ödevini içermektedir.

---

## 🛠️ Kurulum ve Derleme (Installation & Build)

Bu paketteki düğümün çalışabilmesi için öncelikle ROS çalışma alanınızda (catkin workspace) derlenmesi gerekmektedir.

**1. Paketi çalışma alanınıza kopyalayın:**
İndirdiğiniz bu klasörü (`ros_noetic_odev` veya proje adı ne ise) ROS çalışma alanınızın `src` dizinine atın. (Örn: `~/catkin_ws/src/`)

**2. Çalışma alanınızın kök dizinine gidin ve derleyin (Derlenmesi zorunludur çünkü Python script dosya izinleri ve yolları CMakeList.txt ile ROS ekosistemine entegre edilir):**
```bash
cd ~/catkin_ws
catkin_make
```

**3. İşletim sistemi môi ortam değişkenlerini güncelleyin (Bunu her yeni terminalde yapmalısınız veya `~/.bashrc` dosyanıza ekleyebilirsiniz):**
```bash
source devel/setup.bash
```

**(ÖNEMLİ): Python betiğine çalıştırma yetkisi verin:**
Python düğümünü hatasız çalıştırabilmeniz için executable izinlerinin olduğuna emin olmalısınız:
```bash
cd ~/catkin_ws/src/ros_noetic_odev/scripts/1.odev/
chmod +x turtle_tracker_and_mover.py
```

---

## 📁 Ödev 1: Turtlesim Konum Dinleyici ve Hareket Yönetimi (Python)

Bu ödevde, Turtlesim simülasyonundaki kaplumbağanın `/turtle1/pose` konusundan (topic) anlık konum verisi saniyede bir kez ekrana yazdırılmakta, aynı anda `/turtle1/cmd_vel` konusu üzerinden aralıksız hız komutları gönderilerek kaplumbağa hareket ettirilmektedir.

* **İlgili Dosyalar:**
  * `scripts/1.odev/turtle_tracker_and_mover.py` -> (Düğüm: `turtle_manager`)

### 🚀 Nasıl Çalıştırılır?

*(Aşağıdaki 3 komutun her birini yeni ve ayrı bir terminal penceresi açıp çalıştırmalısınız. Klasör kurulumundayken çalıştırdığınız `source devel/setup.bash` satırını her yeni terminalde girmeyi unutmayın!)*

**1. Terminal: ROS çekirdeğini başlatın:**
```bash
roscore
```

**2. Terminal: Turtlesim simülasyonunu başlatın:**
```bash
rosrun turtlesim turtlesim_node
```

**3. Terminal: Yönetici Python Düğümünü Başlatın:**
```bash
rosrun my_pkg turtle_tracker_and_mover.py
```
*(Paket adı `my_pkg` yerine kullanmış olduğunuz klasör/paket adı neyse onunla değiştirmeyi unutmayın, örn: `rosrun ros_noetic_odev turtle_tracker_and_mover.py`)*

### 📈 Örnek Çıktı
`turtle_manager` çalıştığında ve robot hareket ettiğinde 3. terminalde şu şekilde anlık koordinatları görürsünüz (saniyede 1 kez basılır):
```text
[INFO] [Zaman Damgası]: Turtle_manager aktifleşti! Hareket ve konum dinleme başlıyor...
[INFO] [Zaman Damgası]: Turtlesim pozisyonu X=5.54 Y=5.54 Açı=0.00
[INFO] [Zaman Damgası]: Turtlesim pozisyonu X=5.62 Y=5.54 Açı=0.15
...
```

---

## 📁 Ödev 2: Dikdörtgen Alanı Hesaplama Servisi (Python)

Bu ödevde, istemcinin (Client) Terminal aracılığıyla gönderdiği En (`width`) ve Boy (`height`) parametrelerini alarak, dikdörtgenin alanını (`area`) hesaplayan ve istemciye sonucu geri döndüren bir ROS **Service** uygulaması geliştirilmiştir.

Uygulamanın adı (içeriksel proje mantığı olarak) **`rectangle_area_service`** yapısına dayanmakla beraber `my_pkg` paketi (`ros_noetic_odev`) içindeki `2.odev/` ağacına yerleştirilmiştir. Özel servis dosyası (`RectangleArea.srv`) kullanılmıştır.

* **İlgili Dosyalar:**
  * `srv/RectangleArea.srv` -> (Özel servis veri yapısı)
  * `scripts/2.odev/area_server.py` -> (Düğüm: `area_server`)
  * `scripts/2.odev/area_client.py` -> (Düğüm: `area_client`)

### 🚀 Nasıl Çalıştırılır ve Test Edilir?

**Ön Hazırlık:** Eğer yukarıdaki kurulum/derleme (1. ödev) adımındaki `catkin_make` 'i baştan çalıştırmadıysanız, yeni `.srv` dosyasının mesaj kütüphanelerinin derlenmesi için çalışma alanı kökünde kodlamayı tekrar derlemelisiniz:
```bash
cd ~/catkin_ws
catkin_make
source devel/setup.bash
chmod +x ~/catkin_ws/src/ros_noetic_odev/scripts/2.odev/*.py
```

*(Her işlemi yeni/ayrı terminal sekmelerinde yapmayı ve `source devel/setup.bash` çekmeyi unutmayın.)*

**1. Terminal: ROS Çekirdeğini (Master) Başlatın:**
```bash
roscore
```

**2. Terminal: Alan Hesaplayıcı Server'ı Çalıştırın:**
```bash
rosrun my_pkg area_server.py
```
*(Paket isminiz `my_pkg` yerine klasör adınız olabilir, örneğin: `rosrun ros_noetic_odev area_server.py`)*

#### Test Yöntemi 1: Manuel Kod Üzerinden İstek Atmak (Client)
**3. Terminal: Sayısal parametrelerle Client'ı çalıştırıp test edin (Ör: En=5.2, Boy=10.0):**
```bash
rosrun my_pkg area_client.py 5.2 10.0
```

#### Test Yöntemi 2: `rosservice call` Üzerinden Manuel Test
İstemci kodu (Client) haricinde, servisi doğrudan ROS komutlarıyla da çağırabilirsiniz:
```bash
rosservice call /calculate_rectangle_area "width: 5.2
height: 10.0"
```

### 📈 Örnek Çıktılar

**Sunucu (area_server.py) Terminali Çıktısı:**
```text
[INFO] [Zaman Damgası]: Dikdörtgen Alanı Hesaplama Servisi Başlatıldı. İstekler bekleniyor...
[INFO] [Zaman Damgası]: Hesaplama İsteği Alındı -> En: 5.20, Boy: 10.00 | Sonuç (Alan): 52.00
```

**İstemci (area_client.py) Terminali Çıktısı:**
```text
İstek gönderiliyor: En=5.2, Boy=10.0
Sunucudan Gelen Sonuç (Alan): 52.00
```
