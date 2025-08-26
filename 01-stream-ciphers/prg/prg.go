package main

import (
	"crypto/aes"
	"crypto/cipher"
	"crypto/rand"
	"fmt"
	"io"
)

func generateRandomBytes(n int) []byte {
	b := make([]byte, n)
	if _, err := io.ReadFull(rand.Reader, b); err != nil {
		panic(err)
	}
	return b
}

// encryptDecryptAES_CTR encrypts or decrypts input using AES-CTR mode with given key and nonce.
func encryptDecryptAESCTR(key, nonce, input []byte) []byte {
	block, err := aes.NewCipher(key)
	if err != nil {
		panic(err)
	}
	stream := cipher.NewCTR(block, nonce)
	output := make([]byte, len(input))
	stream.XORKeyStream(output, input)
	return output
}

func main() {
	key := generateRandomBytes(16)
	nonce := generateRandomBytes(16)

	plaintext := []byte("Hello, this is a secret message!")

	ciphertext := encryptDecryptAESCTR(key, nonce, plaintext)
	fmt.Printf("Ciphertext: %x\n", ciphertext)

	decrypted := encryptDecryptAESCTR(key, nonce, ciphertext)
	fmt.Printf("Decrypted text: %s\n", decrypted)
}
