# Turtlebot3 5 Noktaya Otonom Navigasyon

Bu proje, Turtlebot3'ü Gazebo simülasyon ortamında, daha önceden kaydedilmiş bir harita üzerinde belirlenen 5 farklı noktaya otonom olarak gönderen bir ROS uygulamasıdır.

## Gereksinimler

- ROS (Robot Operating System) - (Örn: Noetic)
- Turtlebot3 paketleri (`turtlebot3_gazebo`, `turtlebot3_navigation`)
- Python (ve rospy kütüphanesi)

## Kurulum ve Çalıştırma

Projeyi çalıştırmak için sırasıyla aşağıdaki adımları izleyin. Her bir komutu **yeni bir terminal sekmesinde** veya penceresinde çalıştırmanız gerekmektedir.

### 1. Gazebo Simülasyonunu Başlatma

Turtlebot3'ün simülasyon dünyasını başlatmak için aşağıdaki komutu kullanın:

```bash
roslaunch turtlebot3_gazebo turtlebot3_world.launch
```

### 2. Navigasyonu ve Haritayı Başlatma

Simülasyon açıldıktan sonra, navigasyon düğümlerini ve daha önceden çıkardığınız haritayı (`map.yaml`) sisteme yüklemek için şu komutu çalıştırın:

```bash
roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/odev_3/map.yaml
```

*Not: RViz açıldığında robotun konumu yanlış görünüyorsa, üst menüdeki "2D Pose Estimate" aracını kullanarak robotun haritadaki ilk konumunu manuel olarak belirlemeniz gerekebilir.*

### 3. Robotu 5 Noktaya Gönderme (Python Scripti)

Navigasyon hazır olduktan sonra, robotun sırasıyla belirlenen 5 hedefe gitmesini sağlayan Python scriptini çalıştırın:

```bash
cd ~/odev_3
python3 5_nokta.py
```

**(Not: Python 2 kullanan bir ROS sürümü kullanıyorsanız `python 5_nokta.py` komutuyla da çalıştırabilirsiniz.)**

## Dosya Yapısı

- `map.pgm` & `map.yaml`: Ortamın önceden kaydedilmiş olan harita dosyaları.
- `5_nokta.py`: Turtlebot3'ü Action Client (`move_base`) kullanarak sırayla 5 farklı hedefe gönderen Python kodu.
