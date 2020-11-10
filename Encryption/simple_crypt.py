from simplecrypt import encrypt, decrypt, DecryptionException


def enc(password, text):
    result = encrypt(password, text)
    return result


def dec(password, text):
    try:
        result = decrypt(password, text).decode('utf8')
        return result
    except DecryptionException:
        return 'Wrong password'


def main():
    text = 'Hello world'
    password = '123456'
    enc_text = enc(password, text)
    dec_text = dec(password, enc_text)

    print(f'Sample text: {text}\n'
          f'Encrypted text: {enc_text}\n'
          f'Decrypted text: {dec_text}')


if __name__ == '__main__':
    main()


main()
