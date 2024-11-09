# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 10:07:37 2024

@author: Dewi aulia nurjanah
"""

def hitung_hari_bulan():
    print("Program ini akan menentukan jumlah hari dalam bulan tertentu")
    print("Masukkan 0 untuk menghentikan program")
    while True:
        bulan = int(input("Masukkan bulan (1-12): "))
        if bulan == 0:
            print("Terima kasih sudah menggunakan program saya. Sampai berjumpa lagi.")
            break
        else:
            tahun = int(input("Masukkan tahun (misalnya, 2022): "))
            if bulan in [1, 3, 5, 7, 8, 10, 12]:
                print("Ada 31 hari dalam bulan")
            elif bulan in [4, 6, 9, 11]:
                print("Ada 30 hari dalam bulan")
            elif bulan == 2:
                # TAHUN KABISAT
                if (tahun % 400 == 0) or (tahun % 100 != 0 and tahun % 4 == 0):
                    print("Ada 29 hari dalam bulan")
                else:
                    print("Ada 28 hari dalam bulan")
            else:
                print("Bulan tidak valid. Silakan coba lagi.")

hitung_hari_bulan()