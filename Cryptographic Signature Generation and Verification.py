from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec

def generate_key_pair():
    private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
    public_key = private_key.public_key()
    return private_key, public_key

def sign_message(private_key, message):
    signature = private_key.sign(
        message.encode(),  # Convertit le message en une représentation d'octets
        ec.ECDSA(hashes.SHA256())
    )
    return signature

def verify_signature(public_key, message, signature):
    try:
        public_key.verify(
            signature,
            message.encode(),  # Convertit le message en une représentation d'octets
            ec.ECDSA(hashes.SHA256())
        )
        return True
    except Exception as e:
        print("Verification failed:", e)
        return False

# Exemple d'utilisation
if __name__ == "__main__":
    private_key, public_key = generate_key_pair()
    message = "Exemple de message à signer"  # Utilisation d'une chaîne Unicode
    
    signature = sign_message(private_key, message)
    print("Signature:", signature.hex())
    
    if verify_signature(public_key, message, signature):
        print("La signature est valide.")
    else:
        print("La signature n'est pas valide.")
