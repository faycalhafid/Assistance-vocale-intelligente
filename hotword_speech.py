"""
Fichier principal qui contient le comportement de l'assistance
"""

import speech_recognition as sr
import pyttsx3, os
from reconnaissance import treat_request, get_appointment_by_date, get_appointment_by_month, insert
from string_matcher import match_word, match_month, match_number, match_names, match_motif
from datetime import date, timedelta
"""from Capteur import sonner""" #cette ligne a été commentée, car si l'Arduino n'est pas branché à l'ordinateur,
                                 #le programme crash

r = sr.Recognizer()
m = sr.Microphone()

def say_it(phrase):
    #Fonction text-to-speech
    engine = pyttsx3.init()
    engine.say(phrase)
    engine.runAndWait()

def initiate (mot_cle1,mot_cle2):
    #Fonction qui permet de lancer l'assistance vocale en utilisant un mot clé
    text=""
    say_it("Bonjour ! Il faut dire le mot clé "+mot_cle1)
    print("Dites le mot clé")
    while mot_cle1 not in text and mot_cle2 not in text :
        with m as source :
            audio=r.listen(source,phrase_time_limit=1.5)
        try :
            text += r.recognize_google(audio, language="fr-FR")
            if text :
                match = match_word(text, 58)
                print("Vous avez dit : "+text)
                text += " "
                if match :
                    print("Ce que le système peut interpreter : "+match)
                if (match==mot_cle1) :
                    text=match
        except sr.UnknownValueError :
            print("Could not understand audio "+text)
            continue
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

def said_date(request):
    #Fonction qui permet de savoir si la requête comporte une date numérique
    if match_number(request):
        return match_number(request)
    return False

def said_month(request):
    #Fonction qui permet de savoir si la requête comporte un mois
    months_names=["janvier","février","mars","avril","mai","juin","juillet","août","septembre"
            ,"octobre","novembre","décembre"]
    months_nb=[i for i in range(1,13)]
    months=dict(zip(months_names,months_nb))
    for m in list(months.keys()):
        if match_month(request):
            return months[match_month(request)]
    return False

def said_name(request,names):
    #Fonction qui permet de savoir si la requête cite un nom (les noms interprétés sont stockés dans la base de données)
    for name in names:
        if name in match_word(request,80):
            return name
    return False

def appointment (request):
    #Fonction qui détecte si la requête consiste à demander si on a un rendez-vous pour une date précise et à
    #retourner une réponse
    today = date.today()
    jour=False
    if "aujourd'hui" in request :
        jour=today
    if "demain" in request :
        jour=today+timedelta(days=1)
    if "après-demain" in request :
        jour = today + timedelta(days=2)
    if said_date(request) or said_month(request):
        if said_date(request) and said_month(request):
            day = said_date(request)
            month = said_month(request)
            jour=date(today.year,int(month),int(day))
        elif said_month(request):
            month=said_month(request)
            rdvs=get_appointment_by_month(str(month))
            reponse="Vous avez "+str(len(rdvs))+" rendez-vous pendant ce mois. "
            i=0
            for rdv in rdvs :
                i+=1
                reponse+=" Rendez-vous numéro "+str(i)+"., "+str(rdv[3])+", avec "+rdv[1]+", lieu : "+rdv[2]+", pour "+rdv[0]+". "
            return reponse
        else :
            day = said_date(request)
            if (int(day)>=int(today.day)):
                jour=date(today.year,today.month,int(day))
            else :
                if (int(today.month) == 12) :
                    jour=date(today.year+1,1,int(day))
                else :
                    jour=date(today.year,today.month+1,int(day))
    #names=get_names()
    """
    if said_name(request,names):
        name=said_name(request,names)
        
    else :"""
    if (jour) :
        rdv=get_appointment_by_date(str(jour))
        reponse="Vous avez "+str(len(rdv))+" rendez-vous le "+str(jour)+" ."
        for i in range(len(rdv)):
            reponse+=" Rendez-vous numéro "+str(i+1)+", "+str(jour)+", avec "+rdv[i][1]+", lieu : "+rdv[i][2]+", pour "+rdv[i][0]+". "
        return reponse
    else :
        return "Pas de rendez-vous"

def add_appointment():
    #Fonction qui traite l'enregistrement d'un nouveau rendez-vous dans la base de données à partir des commandes vocales
    r = sr.Recognizer()
    m = sr.Microphone()
    print("Ajout d'un nouveau rendez-vous dans la base de donnée. ")
    say_it("Ajout d'un nouveau rendez-vous dans la base de donnée. ")
    print("Avec qui aura lieu le rendez-vous ?")
    say_it("Avec qui aura lieu le rendez-vous ?")
    name=""
    while name=="" :
        with m as source:
            audio = r.listen(source, phrase_time_limit=2.5)
        try :
            name+= r.recognize_google(audio,language="fr-FR")
            if match_names(name):
                name=match_names(name)
            print(name)
        except sr.UnknownValueError:
            print("Could not understand audio "+name)
            engine = pyttsx3.init()
            engine.say("Répétez")
            engine.runAndWait()
    lieu=""
    while lieu =="":
        print("où aura lieu le rendez-vous ?")
        say_it("Où aura lieu le rendez-vous ?")
        with m as source:
            audio = r.listen(source, phrase_time_limit=2.5)
        try :
            lieu+= r.recognize_google(audio,language="fr-FR")

        except sr.UnknownValueError:
            print("Could not understand audio "+lieu)
            engine = pyttsx3.init()
            engine.say("Répétez")
            engine.runAndWait()
    motif=""
    while motif=="" :
        print("Quel est le motif ?")
        say_it("Quel est le motif ?")
        with m as source:
            audio = r.listen(source, phrase_time_limit=2.5)
        try :
            motif+= r.recognize_google(audio,language="fr-FR")
            if match_motif(motif):
                motif=match_motif(motif)
        except sr.UnknownValueError:
            print("Could not understand audio "+motif)
            engine = pyttsx3.init()
            engine.say("Répétez")
            engine.runAndWait()
    jour=""
    while ( not said_date(jour) ) and ("aujourd'hui" not in jour ) and ("demain" not in jour) :
        auj=date.today()
        print("Pour quelle date ?")
        say_it("Pour quelle date ?")
        with m as source:
            audio = r.listen(source, phrase_time_limit=2.5)
        try :
            jour+= r.recognize_google(audio,language="fr-FR")
            if "aujourd'hui" in jour :
                appointment_date=str(auj)
            elif "demain" in jour :
                appointment_date=str(auj+timedelta(days=1))
            elif said_month(jour):
                j=said_date(jour)
                m=said_month(jour)
                if (int(m)<int(auj.month)):
                    appointment_date=str(date(auj.year+1,int(m),int(j)))
                else :
                    appointment_date = str(date(auj.year,int(m),int(j)))
            else :
                j = said_date(jour)
                if (int(j)<int(auj.day)):
                    appointment_date = str(date(auj.year,auj.month+1,int(j)))
                else :
                    appointment_date = str(date(auj.year,auj.month,int(j)))


        except sr.UnknownValueError:
            print("Could not understand audio")
            engine = pyttsx3.init()
            engine.say("Répétez")
            engine.runAndWait()
    import sqlite3
    conn = sqlite3.connect('reconnaissance.sqlite')
    cursor = conn.cursor()
    print(" Appointment date : "+appointment_date)
    print(motif)
    print(name)
    print(lieu)
    insert(str(appointment_date),motif,name,lieu)
    reponse="Rendez-vous ajouté dans la base de donnée. "+str(appointment_date)+" avec "+name+" , lieu : "+lieu+", pour "+motif+". "
    return reponse

#Début du programme principal

#On attend que le mot clé soit prononcé avant de lancer l'assistance
initiate("bonjour","Bonjour")
print("Comment puis-je vous aider?")
say_it('Comment puis-je vous aider ?')

text="" #buffer pour stocker tout ce qu'à dit le client
while "merci" not in text and "Merci" not in text :
    #Le mot "merci" permet d'arrêter la session vocale, tant qu'il n'est pas prononcé par l'utilisateur,
    #on traite tout ce qu'il dit
    with m as source:
        # On écoute par intervalles de 3 secondes
        audio = r.listen(source, phrase_time_limit=3)
    try:
        text += r.recognize_google(audio, language="fr-FR") #traitement speech-to-text
        if text:
            print("Vous avez dit : " + text)
            text+=" "
            if "jeu" in text or "jeux" in text or "jouer" in text :
                #Si l'utilisateur parle de jeu, on lance le jeu de mémoire et on met fin à la session
                #(on ne veut pas continuer à écouter/traiter pendant que l'utilisateur joue)
                os.system("MemoryGame.html")
                text="merci"
            elif "ajout" in text or "nouveau" in text :
                #Si l'utilisateur emploie les mots ajout et/ou nouveau, c'est qu'il veut ajouter un nouveau rendez-vous
                reponse = add_appointment() #traitement de la requête
                print(reponse)
                say_it(reponse) #output vocal de la réponse
                text=""
            elif "rendez-vous" in text or "consulter" in text or "voir" in text or "faire" in text or said_date(text) or said_month(text) :
                #L'utilisateur veut savoir s'il a des rendez-vous pour une date
                reponse=appointment(text)
                print(reponse)
                say_it(reponse)
                text=""


            else :
                #Le cas restant est celui où l'utilisateur cherche un objet personnel
                match=match_word(text,90) #Petite tolérence qui permet de comprendre un mot de la base de données
                                          #si l'utilisateur ne l'a pas prononcé correctement
                if match=="merci":
                    text="merci"
                if "merci" not in text and "Merci" not in text:
                    reponse = treat_request(text) #traitement de la requête
                    if reponse :
                        print(reponse)
                        say_it(reponse)
                        """
                        if "voiture" in text :
                            sonner("voiture")
                        if "maison" in text :
                            sonner("maison")"""
                        text=""
                    else :
                        #Si on a pas de réponse, c'est qu'il y a eu une erreur d'interprétation de ce que l'utilisateur
                        #a dit, on lui demande de répéter
                        print("Répétez. Vous avez dit : "+text)
                        say_it("Répétez")
                else :
                    text="merci"
    except sr.UnknownValueError:
        print("Could not understand audio")
        engine = pyttsx3.init()
        engine.say("Répétez")
        engine.runAndWait()