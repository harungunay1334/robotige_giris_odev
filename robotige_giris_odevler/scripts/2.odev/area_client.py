#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import rospy
from my_pkg.srv import RectangleArea, RectangleAreaRequest

def calculate_area_client(width, height):
    """
    Server'a bağlanarak verilen en ve boy değerleri için alan hesaplaması talep eder.
    """
    # Servisin aktif olmasını bekliyoruz
    rospy.wait_for_service('calculate_rectangle_area')
    
    try:
        # Servise bağlanmak için bir proxy (aracı) oluşturuyoruz
        calculate_area = rospy.ServiceProxy('calculate_rectangle_area', RectangleArea)
        
        # İsteği gönderip cevabı alıyoruz
        response = calculate_area(width, height)
        return response.area
        
    except rospy.ServiceException as e:
        rospy.logerr("Servis çağrısı başarısız oldu: %s", e)

if __name__ == "__main__":
    # Komut satırından 2 argüman (width ve height) gelmesini bekliyoruz
    if len(sys.argv) == 3:
        try:
            w = float(sys.argv[1])
            h = float(sys.argv[2])
        except ValueError:
            print("Lütfen sayısal değerler girin! Örnek kullanım: rosrun my_pkg area_client.py 5.2 10.0")
            sys.exit(1)
    else:
        print("Hatalı parametre sayısı!")
        print("Kullanım: rosrun my_pkg area_client.py <en> <boy>")
        print("Örnek: rosrun my_pkg area_client.py 5.2 10.0")
        sys.exit(1)
        
    # ROS Düğümünü client olarak başlatıyoruz
    rospy.init_node('area_client', anonymous=True)
    
    print("İstek gönderiliyor: En={}, Boy={}".format(w, h))
    hesaplanan_alan = calculate_area_client(w, h)
    
    # Sonucu ekrana yazdırıyoruz
    if hesaplanan_alan is not None:
        print("Sunucudan Gelen Sonuç (Alan): {:.2f}".format(hesaplanan_alan))
