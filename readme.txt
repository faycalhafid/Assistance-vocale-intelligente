Ce projet est compos� de :
- Programme principal -> hotword_speech.py
			* Reconnaissance d'un mot cl� pour lancer l'assistance
			* Requ�te de l'utilisateur : passage speech-to-text
			* Traitement de la requ�te (�tude des diff�rents cas) , renvoie d'une r�ponse
			* R�ponse : passage text-to-speech
- Interface arduino pour faire sonner les capteurs des objets personnels -> Capteur.py
- Base de donn�es -> reconnaissance.sqlite
- Fuzzy logic, tol�rance d'erreur d'interpr�tation d'un mot -> string_matcher.py