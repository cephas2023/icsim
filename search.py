import subprocess
import time

# Fonction pour envoyer un message CAN
def send_can_message(interface, message):
    command = f"cansend {interface} {message}"
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Message envoyé : {command}")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'envoi : {e}")

# Lire les messages CAN depuis le fichier
with open('/home/ubuntu/Downloads/Icsim/ICSim-master/builddir/lebon.log', 'r') as file:
    for i, line in enumerate(file):
        if i >= 5:  # Limite à 300 lignes
            break
        
        parts = line.split()  # Divise la ligne en parties
        if len(parts) == 3:  # Vérifie qu'il y a trois parties
            timestamp = parts[0]  # On peut ignorer le timestamp
            interface = parts[1]  # Deuxième partie : interface
            can_message = parts[2]  # Troisième partie : message CAN
            
            # Envoi du message CAN
            send_can_message(interface, can_message)
            time.sleep(0.01)  # Pause de 0.1 seconde entre les envois

