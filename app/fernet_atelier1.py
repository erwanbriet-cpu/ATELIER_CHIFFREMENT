import os
import sys
from cryptography.fernet import Fernet

def get_cipher():
    # Codespaces récupère la clé via cette variable d'environnement
    key = os.getenv("FERNET_KEY")
    if not key:
        print("Erreur : Variable FERNET_KEY introuvable.")
        print("Lancer : export FERNET_KEY='votre_clé'")
        sys.exit(1)
    return Fernet(key.encode())

def run():
    action, in_file, out_file = sys.argv[1], sys.argv[2], sys.argv[3]
    cipher = get_cipher()
    
    with open(in_file, "rb") as f:
        data = f.read()

    result = cipher.encrypt(data) if action == "encrypt" else cipher.decrypt(data)

    with open(out_file, "wb") as f:
        f.write(result)
    print(f"Terminé : {out_file} généré.")

if __name__ == "__main__":
    run()