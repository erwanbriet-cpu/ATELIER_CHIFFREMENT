import os
import sys
from nacl.secret import SecretBox
from nacl.utils import random

def get_box():
    # La clé SecretBox doit faire exactement 32 octets
    key = os.getenv("NACL_KEY")
    if not key:
        print("Erreur : Variable NACL_KEY manquante.")
        sys.exit(1)
    # On encode la string en bytes (doit être une clé de 32 caractères)
    return SecretBox(key.encode().ljust(32)[:32])

def process(action, in_file, out_file):
    box = get_box()
    
    with open(in_file, "rb") as f:
        data = f.read()

    if action == "encrypt":
        # SecretBox génère automatiquement un nonce (sel d'unicité)
        processed_data = box.encrypt(data)
    else:
        processed_data = box.decrypt(data)

    with open(out_file, "wb") as f:
        f.write(processed_data)
    print(f"Opération {action} réussie.")

if __name__ == "__main__":
    process(sys.argv[1], sys.argv[2], sys.argv[3])