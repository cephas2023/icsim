import os

# Chemin vers le fichier
file_path = '/home/ubuntu/Downloads/Icsim/ICSim-master/builddir/lebon.log'
backup_file_path = '/home/ubuntu/Downloads/Icsim/ICSim-master/builddir/backup.log'

# Ouvrir le fichier d'origine et le fichier de sauvegarde
with open(file_path, 'r') as source_file, open(backup_file_path, 'w') as backup_file:
    # Lire les 600 premières lignes et les écrire dans le fichier de sauvegarde
    for _ in range(10):
        line = source_file.readline()
        if not line:  # Si le fichier a moins de 600 lignes
            break
        backup_file.write(line)
    
    # Écrire le reste des lignes (s'il y en a) dans le même fichier
    remaining_lines = source_file.readlines()

# Réécrire le fichier d'origine sans les 600 premières lignes
with open(file_path, 'w') as source_file:
    source_file.writelines(remaining_lines)

print(f"Les 10000 premières lignes ont été sauvegardées dans '{backup_file_path}' et le reste a été supprimé.")

