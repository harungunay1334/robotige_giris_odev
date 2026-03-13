#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from my_pkg.srv import RectangleArea, RectangleAreaResponse

def handle_calculate_area(req):
    """
    İstemciden gelen width (en) ve height (boy) değerlerini alıp alanı hesaplar.
    Sonucu (area) geri döndürür.
    """
    area = req.width * req.height
    rospy.loginfo("Hesaplama İsteği Alındı -> En: %.2f, Boy: %.2f | Sonuç (Alan): %.2f", req.width, req.height, area)
    return RectangleAreaResponse(area)

def calculate_rectangle_area_server():
    """
    'calculate_rectangle_area' adında bir servis başlatır ve gelen istekleri dinler.
    """
    rospy.init_node('area_server')
    
    # Servisi tanımlıyoruz
    s = rospy.Service('calculate_rectangle_area', RectangleArea, handle_calculate_area)
    
    rospy.loginfo("Dikdörtgen Alanı Hesaplama Servisi Başlatıldı. İstekler bekleniyor...")
    rospy.spin()

if __name__ == "__main__":
    try:
        calculate_rectangle_area_server()
    except rospy.ROSInterruptException:
        pass
