"""
Ce fichier contient la partie qui permet de communiquer avec les capteurs rattachés aux objets personnels (dans
notre cas : 1- les clés de la maison, et 2- les clés de la voiture) pour les faire sonner. Interface Arduino
"""

import serial
import time

#Liste des capteurs disponibles
capteurs = {"maison":b'2',"voiture":b'3'}

#Classe principale
class Capteur():
    def __init__(self,com="com3",rate=9600):
        self.ser=serial.serial_for_url(com,rate)
    def sonnerCapteur(self,nomCapteur):
        #Méthode qui permet de faire sonner le capteur cible
        time.sleep(2)
        self.ser.write(capteurs[nomCapteur])
    def ajouterCapteur(self,nomCapteur):
        #Méthode non implémentée, non nécessaire pour le prototype
        pass

#Fonction pour faire sonner le bon capteur selon le mot clé utilisé par la commande vocale, c'est ce qui va être utilisé
#par les autres fichiers du projet
def sonner(keyword):
    c = Capteur(com="com3")
    c.sonnerCapteur(keyword)

