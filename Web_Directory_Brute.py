import requests
import datetime

def getTarget():
    url = input("Enter Target URL. example : http://127.0.0.1:8080 : ").rstrip("/")
    wordlist = input("Enter wordlist path : ")
    return url, wordlist

def loadWordlist(path):
    try:
        with open(path, "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        print(" [-] wordlist file not found.")
        exit()

def bruteforce(url, words):
    print("\n" + "="*50)
    print(f"Target : {url}")
    print(f"Words : {len(words)}")
    print(f"Started : {datetime.datetime.now()}")

    for word in words:
        target_url = f"{url}/{word}"

        try:
            response = requests.get(target_url, timeout=3)
            if response.status_code == 404:
                print(f" [-] /{word}")
            else:
                print(f" [+] /{word} --> {response.status_code}")
            
        except requests.exceptions.RequestException:
            print(f" [!] /word --> Connection Failed")
    
    print("Brute force complete.")
    # response = requests.get(url)
    # print(response.status_code)

# url = "http://127.0.0.1:8080/admin"
# response = requests.get(url)
# print(response.status_code)

def main():
    url, wordlists_path = getTarget()
    words = loadWordlist(wordlists_path)
    bruteforce(url, words)

main()