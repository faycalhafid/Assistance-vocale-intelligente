Ce projet est composé de :
- Programme principal -> hotword_speech.py
			* Reconnaissance d'un mot clé pour lancer l'assistance
			* Requête de l'utilisateur : passage speech-to-text
			* Traitement de la requête (étude des différents cas) , renvoie d'une réponse
			* Réponse : passage text-to-speech
- Interface arduino pour faire sonner les capteurs des objets personnels -> Capteur.py
- Base de données -> reconnaissance.sqlite
- Fuzzy logic, tolérance d'erreur d'interprétation d'un mot -> string_matcher.py