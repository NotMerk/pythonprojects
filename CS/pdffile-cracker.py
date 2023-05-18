import pikepdf
from tqdm import tqdm

# load password list
passwords = [ line.strip() for line in open("wordlist.txt") ]

# iterate over passwords
for password in tqdm(passwords, "Decrypting PDF"):
    try:
        # open pdf file
        with pikepdf.open("abc_protected.pdf", password=password) as pdf:
            # Password decrypted successfully, break out of the loop
            print("[+] Password found > ", password)
            break
    except pikepdf._core.PasswordError as e:
        #wrong password, just continue looping
        continue