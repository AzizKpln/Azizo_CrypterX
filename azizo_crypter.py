from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path
from os import listdir
from os.path import isfile, join
import time

import getpass

class Encryptor:
    def __init__(self, key):
        self.key = key

    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, message, key, key_size=256):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)

    def encrypt_file(self, file_name):
        try:
            with open(file_name, 'rb') as fo:
                plaintext = fo.read()
            enc = self.encrypt(plaintext, self.key)
            with open(file_name + ".enc", 'wb') as fo:
                fo.write(enc)
                os.remove(file_name)
        except FileNotFoundError:
             
            os.system("cls||clear")
            print("Hocam girdiğin dosyayı kontrol et yanlış girmişsin.\n\n")
            time.sleep(2)
            
         

    def decrypt(self, ciphertext, key):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")
       
            

    def decrypt_file(self, file_name):
        try:
            with open(file_name, 'rb') as fo:
                ciphertext = fo.read()
            dec = self.decrypt(ciphertext, self.key)
            with open(file_name[:-4], 'wb') as fo:
                fo.write(dec)
            os.remove(file_name)
        except FileNotFoundError:
            os.system("cls||clear")
            print("->Eğer parola girerken bu yazı karşına çıkıyorsa ve aynı parolayı girdiğine eminsen programı kapat ve yeniden başlat.\n\n->Yukarıdaki seçenek değilse girdiğin dosya ismi yanlış demektir kontrol et ve tekrar dene.")
            time.sleep(4)
            
                
                
    def getAllFiles(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dirs = []
        for dirName, subdirList, fileList in os.walk(dir_path):
            for fname in fileList:
                if ((not 'crypter' in fname) and fname != 'data.txt.enc'):
                    dirs.append(dirName + "\\" + fname)
        return dirs

    def encrypt_all_files(self):
        ask=input("Valla reis şimdi sen bunu seçersen ne var ne yok şifreliyecek.\n\nDevam etmek istediğine emin misin?(e/h)")
        ask=ask.upper()
        if(ask=="H" or ask=="HAYIR"):
            print("->Tamam knk.Çıkıyom..")
            time.sleep(5)
            exit()
        dirs = self.getAllFiles()
        for file_name in dirs:
            self.encrypt_file(file_name)
        os.system("cls||clear")
        print("->Dosyalar Encryptlendi...\n->Çıkış Yapılıyor..")
        time.sleep(2)
        
            

    def decrypt_all_files(self):
        dirs = self.getAllFiles()
        for file_name in dirs:
            self.decrypt_file(file_name)
        os.system("cls||clear")
        print("->Dosyalar Encryptlendi...\n->Çıkış Yapılıyor..")
        time.sleep(2)
            


key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
enc = Encryptor(key)
clear = lambda: os.system('cls')

if os.path.isfile('data.txt.enc'):
    while True:
        password = getpass.getpass("Parolayı Giriniz: ")
        enc.decrypt_file("data.txt.enc")
        p = ''
        with open("data.txt", "r") as f:
            p = f.readlines()
        if p[0] == password:
            enc.encrypt_file("data.txt")
            break

    while True:
        clear()
        
        
        choice = int(input(
            "1->Dosyayı Encryptle.\n2->Dosyayı Decryptle.\n3->Tüm Dosyaları Encryptle.\n4->Bütün Dosyaları Decryptle\n5->Çıkış Yap.\n\nSeçim Yapın:"))
        clear()
        if choice == 1:
            enc.encrypt_file(str(input("Dosya Adını Giriniz: ")))
        elif choice == 2:
            enc.decrypt_file(str(input("Dosya Adını Giriniz: ")))
        elif choice == 3:
            enc.encrypt_all_files()
        elif choice == 4:
            enc.decrypt_all_files()
        elif choice == 5:
            exit()
        else:
            print("BİR İŞLEM SEÇİN!")

else:
    while True:
        clear()
        password = getpass.getpass("Parola Giriniz: ")
        repassword = getpass.getpass("Yeniden Parola Giriniz: ")
        if password == repassword:
            break
        else:
            print("Şifreler Uyuşmuyor!")
    f = open("data.txt", "w+")
    f.write(password)
    f.close()
    enc.encrypt_file("data.txt")
    print("Programı Yeniden Başlatın")
    time.sleep(15)
