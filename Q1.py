# 1 Check whether a character is a vowel or consonant
def ChkVowel(ch):
    if ch in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
        print("Vowel")
    else:
        print("Consonant")

def main():
    ch = input("Enter a character: ")
    ChkVowel(ch)

if __name__ == "__main__":
    main()