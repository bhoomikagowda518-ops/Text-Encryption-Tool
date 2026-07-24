import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
PRIVATE_KEY_PATH = "keys/rsa_private.pem"
PUBLIC_KEY_PATH = "keys/rsa_public.pem"
def generate_rsa_keys():
    if (
        not os.path.exists(PRIVATE_KEY_PATH)
        or
        not os.path.exists(PUBLIC_KEY_PATH)
    ):
        private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)
        private_bytes = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)
        with open(PRIVATE_KEY_PATH, "wb") as file:
            file.write(private_bytes)
        public_key = private_key.public_key()
        public_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
        with open(PUBLIC_KEY_PATH, "wb") as file:
            file.write(public_bytes)
        return private_key, public_key
    else:
        with open(PRIVATE_KEY_PATH, "rb") as file:
            private_data = file.read()
        private_key = serialization.load_pem_private_key(
        private_data,
        password=None
    )
        with open(PUBLIC_KEY_PATH, "rb") as file:
            public_data = file.read()
        public_key = serialization.load_pem_public_key(
        public_data
    )
        return private_key, public_key