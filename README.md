# icsim TP


CONTEXTE:
---------------------------------------------------------------------------
Dans le cadre de notre formation en école d'ingénieur, nous effectuons un certains nombre de travaux pratiques afin de découvrir d'avantage un certains nombre de techniques de pentest.
La technique qui sera mis en relief dans cet exercice est le Fuzzing, est la technique que nous allons utilisée.
En effet le fuzzing consiste a envoyé des données aléatoires dans un système d'informations(SOFT/HARDware) afin de découvrir les différentes vulnérabilités.

CAS PRATIQUE:
-------------------------------------------------------------------------------
Précisement dans nnotre cas pratique, il s'agit à l'aide de la technologie ICSIM développé par Zombie Craig, d'envoyé des commandes dans le bus CAN d'une voiture dans un premier temps, ensuite grâce au à notre terminal créer un fichier .log contenant les différentes commandes et enfin par dicothomie ou autre méthode d'analyse de donnée retrouver la tarme de commandes qui ouvre les portes de notres voitures.

RESSOURCES:
--------------------------------------------------------------------------------------
            ICSIM: https://github.com/zombieCraig/ICSim
            Machine Virtuel:https://ubuntu.com/download/desktop
            Script: https://www.python.org/downloads/
            ChatGPT: (: A utiliser avec la tête et non les pieds :)
            
VIF DU SUJET:
--------------------------------------------------------------------------------------------------------
LEBON.LOG:
Ce fichier contient la liste des différentes commandes enregistrées lors de l'interaction entre notre controleurs et l'interface ICSIM.

SEARCH.PY:
Ce fichier contient en effet un code python qui par dicothomie fait envoie à l'aide d'une boucle le commande au bus CAN grâce au terminal.
Pour ce faire, il divise en trois parties la ligne contenu dans le fichier et envoie grâce à la commande cansend vcan0... transmet la commande au bus CAN de notre voiture (VROUMMMMM!!!!)
Pour ce faciliter la tâche nous avons mis en place une boucle qui permettra à l'utilisateur de préciser le nombre de commandes qu'il souhaite envoyé (soit les 3000 premières contenu dans le fichier ou les premières premières "pour les tortues :) "

CLEAN.PY:
Ce fichier permet avec son programme de nettoyer les lignes utiliseer grâce search.py si elle n'arrive pas à ouvrir les portes (A ne pas exécuter après un AFTERWORK à l'ESEO).

BACK.PY:
Ce fichier permet quand à lui de charger le commandes utiliser dans search.py si elle arrive à ouvrirr les portières (Un peu notre filtre, l'antonnoir) car la sortie de ce script permettra chargé à nouveau notre lebon.log pour approfodir nos recherches.

lebon.log: Fichier contennat les logs qui seront exécuter
backup.log: Fichier qui contiendra les commandes probables que noous recherchons (resultats de l'xécution de BACK.PY)

FOR MORE DETAILS:
------------------------------------------------------------------------------------------------------------------------------------

 PETIT A PETIT ON Y ARRIVERA----------------------------
 
CONTENU DES DIFFERENTS FICHIER (JE JURE SUR GNS3 C'EST SANS L'AIDE DE CHAT GPT)
 ------------------------------------------------------------------------------

SEARCH.PY:
---------- 
            import subprocess
            import time
          
            ##Fonction pour envoyer un message CAN
            def send_can_message(interface, message):
              command = f"cansend {interface} {message}"
                try:
                    subprocess.run(command, shell=True, check=True)
                    print(f"Message envoyé : {command}")
                except subprocess.CalledProcessError as e:
                    print(f"Erreur lors de l'envoi : {e}")
          
              ##Lire les messages CAN depuis le fichier
                with open('/home/ubuntu/Downloads/Icsim/ICSim-master/builddir/lebon.log', 'r') as file:
                for i, line in enumerate(file):
                    if i >= 5:  # Limite à 5 lignes
                        break
          
                      parts = line.split()  # Divise la ligne en parties
                          if len(parts) == 3:  # Vérifie qu'il y a trois parties
                          timestamp = parts[0]  # On peut ignorer le timestamp
                          interface = parts[1]  # Deuxième partie : interface
                          can_message = parts[2]  # Troisième partie : message CAN
                        
                          # Envoi du message CAN
                          send_can_message(interface, can_message)

CLEAN.PY:
--------

          ##Chemin vers le fichier
          file_path = '/home/ubuntu/Downloads/Icsim/ICSim-master/builddir/lebon.log'
        
          ##Lire le fichier et supprimer les 5 premières lignes
          with open(file_path, 'r') as file:
              lines = file.readlines()
        
          ##Écrire les lignes restantes dans le même fichier
            with open(file_path, 'w') as file:
              file.writelines(lines[5:])  # Écrit toutes les lignes à partir de la 6ème

BACK.PY:
--------

          import os
        
          ##Chemin vers le fichier
          file_path = '/home/ubuntu/Downloads/Icsim/ICSim-master/builddir/lebon.log'
          backup_file_path = '/home/ubuntu/Downloads/Icsim/ICSim-master/builddir/backup.log'
        
          ##Ouvrir le fichier d'origine et le fichier de sauvegarde
            with open(file_path, 'r') as source_file, open(backup_file_path, 'w') as backup_file:
                # Lire les XX premières lignes et les écrire dans le fichier de sauvegarde
                for _ in range(10): ##10 dans notre cas
                    line = source_file.readline()
                    if not line:  # Si le fichier a moins de 600 lignes
                        break
                      backup_file.write(line)
              
                ##Écrire le reste des lignes (s'il y en a) dans le même fichier
                  remaining_lines = source_file.readlines()
          
              ##Réécrire le fichier d'origine sans les XX premières lignes:
              with open(file_path, 'w') as source_file:
                source_file.writelines(remaining_lines)

                  print(f"Les XX premières lignes ont été sauvegardées dans '{backup_file_path}' et le reste a été supprimé.")



IT'S NOT LOTTERY: WE FOUND IT: 19B#00000E000000
-----------------------------
Après ce process nous avons pu trouver la commande qui est la suivante: 19B#00000E000000

DES COMMANDES NON NEGLIGEABLES
---------------------------------------------------------

#cansend vcan0 #XXXXXXXXXXXXXXXXX : Envoyer une commande au bus can

#candump vcan0: générer les logs

#candump -l vcan0 : générer les logs dans un fichier 




COPYRIGHT: GrosseEpicerieFine 2024
----------------------------------
                                                 


