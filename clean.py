# Chemin vers le fichier
file_path = '/home/ubuntu/Downloads/Icsim/ICSim-master/builddir/lebon.log'

# Lire le fichier et supprimer les 300 premières lignes
with open(file_path, 'r') as file:
    lines = file.readlines()

# Écrire les lignes restantes dans le même fichier
with open(file_path, 'w') as file:
    file.writelines(lines[5:])  # Écrit toutes les lignes à partir de la 301ème

