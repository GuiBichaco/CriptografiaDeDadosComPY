# 🔐 Projeto de Criptografia com RSA

Este projeto implementa **criptografia RSA** usando a biblioteca `cryptography` em Python. A criptografia RSA é um método assimétrico que utiliza um **par de chaves** (pública e privada) para proteger dados.

## 📌 Funcionalidades

- **Geração de Chaves RSA**: Criação de um par de chaves (privada e pública) para criptografia e descriptografia.
- **Criptografia de Mensagem**: A mensagem original é criptografada utilizando a **chave pública**.
- **Descriptografia de Mensagem**: A mensagem criptografada é decodificada utilizando a **chave privada**.
- **Uso de Hash SHA-256**: Protege a integridade dos dados no processo de criptografia.
- **Manipulação de Bytes (`b"texto"`)**: Explicação e uso correto na criptografia.

## 🚀 Como Usar

### 1️⃣ Instalar Dependências
Antes de rodar o código, instale a biblioteca `cryptography` com:

```sh
pip install cryptography
```

### 2️⃣ Executar o Código
Execute o script Python para **gerar as chaves, criptografar e descriptografar a mensagem**

### 🛠️ Explicação do Código
1. **Geração das chaves RSA**: Um par de chaves é gerado para criptografia e descriptografia.
2. **Uso de `b"texto"`**: A mensagem foi definida diretamente como **bytes**, sem conversão adicional.
3. **Criptografia com chave pública**: Usa `encrypt()` com `OAEP` e **SHA-256** para maior segurança.
4. **Descriptografia com chave privada**: Usa `decrypt()` para recuperar a mensagem original.

## 🔍 Sobre `b"texto"` e Manipulação de Bytes
No código, a mensagem foi definida diretamente como um **objeto `bytes`** (`b"Esta e uma mensagem secreta."`). Isso significa que ela será tratada como **dados binários**, o que é necessário para criptografia.

💡 **Atenção**: Strings definidas com `b""` só aceitam **caracteres ASCII puros**. Se precisar usar caracteres acentuados ou especiais, é necessário converter para UTF-8 com `.encode("utf-8")`.

Exemplo de conversão alternativa:
```python
mensagem = "Esta é uma mensagem segura.".encode("utf-8")
```

## 🔐 Segurança no Projeto
- **RSA com chave de 2048 bits**: Alta segurança contra ataques.
- **SHA-256 no padding**: Protege contra ataques de engenharia reversa.
- **Uso correto de bytes (`b"texto"`)**: Mantendo compatibilidade com os requisitos de criptografia.

---
