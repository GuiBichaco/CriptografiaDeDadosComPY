# Intalável abaixo para fazer o projeto funcionar
# pip install cryptography

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

#1. Gerar par de chaves RSA
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

#2. Mensagem a ser criptografada
mensagem = b"Esta e uma mensagem secreta."

#3. Criptografar a mensagem com a chave pública
mensagem_criptografada = public_key.encrypt(
    mensagem,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("Mensagem criptografada:", mensagem_criptografada)

#4. Descriptografar a mensagem com a chave privada
mensagem_descriptografada = private_key.decrypt(
    mensagem_criptografada,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("Mensagem descriptografada:", mensagem_descriptografada.decode())