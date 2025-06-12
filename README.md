# Crypto101 Python Implementations

This repository contains my personal implementations and practice exercises of fundamental cryptographic algorithms and protocols in Python. The code is based on concepts from the book *Crypto101* and other resources, aimed at deepening my understanding of cryptography for my thesis work in cybersecurity.


**N.B.:** All implementations are done manually from scratch without relying on external cryptographic libraries, to deepen understanding of the underlying algorithms and mathematics.

---

## Contents

| File                     | Description                                          |
|--------------------------|------------------------------------------------------|
| [`rsa.py`](https://github.com/ayiman29/crypto101/blob/main/rsa.py)                 | Implementation of RSA encryption and decryption.    |
| [`rsa_signature.py`](https://github.com/ayiman29/crypto101/blob/main/rsa_signature.py)       | RSA digital signature scheme implementation.        |
| [`sha256.py`](https://github.com/ayiman29/crypto101/blob/main/sha256.py)              | SHA-256 cryptographic hash function (custom implementation). |
| [`h_mac.py`](https://github.com/ayiman29/crypto101/blob/main/h_mac.py)               | HMAC (Hash-based Message Authentication Code) using SHA-256. |
| [`diffie_hellman.py`](https://github.com/ayiman29/crypto101/blob/main/diffie_hellman.py)      | DH key exchange with safe prime generation and simulation. |
| [`aes.py`](https://github.com/ayiman29/crypto101/blob/main/aes.py)                 | AES block cipher implementation with block-level encryption and decryption functions. |
| [`dh_aes_sha256.py`](https://github.com/ayiman29/crypto101/blob/main/dh_aes_sha256.py)   | Demonstration of Diffie-Hellman key exchange, custom SHA-256 hashing, and AES encryption/decryption working together. |
| [`ecc.py`](https://github.com/ayiman29/crypto101/blob/main/ecc.py)                 | Elliptic Curve Cryptography implementation including point operations, key generation, encryption, and decryption. |
| [`ecdsa.py`](https://github.com/ayiman29/crypto101/blob/main/ecdsa.py) | Implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA), including key pair generation, signing, and signature verification using custom elliptic curve parameters. |
| [`elgamal.py`](https://github.com/ayiman29/crypto101/blob/main/elgamal.py) | Implementation of ElGamal public-key encryption scheme including key generation, encryption, and decryption. |
| [`utils.py`](https://github.com/ayiman29/crypto101/blob/main/utils.py)               | Utility functions.                                    |


---

## Purpose

This repo serves as my hands-on playground to:

- Implement my cryptographic knowledge practically on python.
- Develop a clear understanding of both the mathematical concepts and the coding.
- Keep track of my learning progress(and enjoy the GitHub green boxes for a dopamine rush🤩)

---

## How to Use 

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/crypto101.git
   cd crypto101
   ```

2. Run individual scripts to test implementations. For example:

   ```bash
   python sha256.py
   python h_mac.py
   ```

3. Study the source code for detailed comments and explanations.

---

## My Learning Process

* Learned the basics of cryptography from the book Crypto101 — an introductory guide to cryptography.
* Asked ChatGPT to provide Python skeletons with step-by-step outlines, without explicit code.
* Solved the coding problems myself, using online resources or ChatGPT for help when stuck.

---

## About

* Author: Me, duh! 
* Inspired by the book [*Crypto101*](https://crypto101.io/) — an introductory cryptography book freely available online.
* Field of study: Cybersecurity (Thesis research focus)

---

Feel free to reach out or open issues if you find bugs or want to suggest improvements!

---

*Unhappy cryptography learning!* 🔐🚀

---
<p align="center">
  <img src="https://drive.google.com/uc?export=view&id=18fPtry5wQwo76VxF7sAxDFefASLN5ozD" alt="Reference Image" width="700">
</p>
