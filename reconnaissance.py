# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 17:21:00 2019

@author: Sonia DNA, Fayçal HAFID, Kaci Islam MAKOUR

Module de traitement des requêtes, mise en lien avec la base de données
"""

import sqlite3

def treat_request(phrase):
    #Permet de traiter une requête concernant les objets personnels
    conn = sqlite3.connect('reconnaissance.sqlite')
    cursor = conn.cursor()
    keyword=False
    if "maison" in phrase:
        cursor.execute("""SELECT reponse FROM réponses WHERE id_reponse = 1""")
        reponse1 = cursor.fetchone()
        conn.close()
        keyword=True

    if "voiture" in phrase:
        cursor.execute("""SELECT reponse FROM réponses WHERE id_reponse = 2""")
        reponse1 = cursor.fetchone()
        conn.close()
        keyword = True

    if ("clé" in phrase or "clés" in phrase) and ("voiture" not in phrase) and ("maison" not in phrase):
        keyword = True
        conn.close()
        return "Veuillez préciser. Clés de la voiture, ou bien clés de la maison ?"

    if "médicaments" in phrase or "médicament" in phrase:
        cursor.execute("""SELECT reponse FROM réponses WHERE id_reponse = 3""")
        reponse1 = cursor.fetchone()
        conn.close()
        keyword = True

    if "téléphone" in phrase or "smartphone" in phrase or "téléphones" in phrase:
        cursor.execute("""SELECT reponse FROM réponses WHERE id_reponse = 4""")
        reponse1 = cursor.fetchone()
        conn.close()
        keyword = True

    if "portefeuille" in phrase:
        cursor.execute("""SELECT reponse FROM réponses WHERE id_reponse = 5""")
        reponse1 = cursor.fetchone()
        conn.close()
        keyword = True

    if not keyword :
        conn.close()
        return ""
    return str(reponse1)[2:-3]

def get_names():
    #Retourne la liste des noms (personnes proches du malade) qui sont dans la base de données
    conn = sqlite3.connect('reconnaissance.sqlite')
    cursor = conn.cursor()
    cursor.execute("""SELECT personne FROM Personnes_rdv""")
    names=cursor.fetchall()
    conn.close()
    res=[]
    print(names)
    for name in names :
        res.append(name[0])
    return res

def get_appointment_by_date(jour):
    #Retourne la liste des rendez-vous dans la base de données pour la date indiquée
    conn = sqlite3.connect('reconnaissance.sqlite')
    cursor = conn.cursor()
    cursor.execute("""SELECT motif, personne, lieu FROM rendez_vous WHERE date_rdv= '%s' """ % (str(jour)))
    rdv=cursor.fetchall()
    conn.close()
    return rdv

def get_appointment_by_month(month):
    # Retourne la liste des rendez-vous dans la base de données pour le mois indiqué
    conn = sqlite3.connect('reconnaissance.sqlite')
    cursor = conn.cursor()
    cursor.execute("""SELECT date_rdv FROM rendez_vous""")
    list_of_dates = cursor.fetchall()

    dates_to_return=get_dates_with_month(month,list_of_dates)
    rdvs=[]
    for day in dates_to_return :
        cursor.execute("""SELECT motif, personne, lieu, date_rdv FROM rendez_vous WHERE date_rdv LIKE ('%s') """ % (day))
        rdv=cursor.fetchall()
        if rdv :
            rdvs.append(rdv[0])
    conn.close()
    return rdvs

def get_dates_with_month(month,list_of_dates):
    #Fonction qui met les dates dans le bon format
    dates_to_return=[]
    for date in list_of_dates :
        date=date[0]
        items=date.split('-')
        y, m, d=items[0],items[1],items[2]
        if int(m) == int(month):
            dates_to_return.append(y+'-'+m+'-'+d)
    return dates_to_return

def insert(date, mot, pers, li):
    #Ajout d'un nouveau rendez-vous dans la base de données
    conn = sqlite3.connect('reconnaissance.sqlite')
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO rendez_vous(date_rdv, motif, personne, lieu) VALUES(DATE (?),?,?,?)""",(date,mot,pers,li))
    conn.commit()
    conn.close()


