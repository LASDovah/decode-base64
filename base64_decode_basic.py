import base64

def main():
    try:
        while True:
            
            print("""
                  ___________MENU___________
                  [1] Decode base64.
                  [2] Exit.
                  __________________________
                  """)
            option = int(input('\n[*] Enter option: '))
            if option == 1:
                code_base64= input("\n[*] Enter BASE64: ")
                decoded_base64 = base64.b64decode(code_base64)
                print("[+] Response: " + decoded_base64.decode('utf-8') + "\n")
            elif option == 2:
                break
            else:
                print('[-] Enter a valid value...')
    except Exception as e:
        print(e)
    except KeyboardInterrupt as k:
        print(k)  
  
if __name__ == '__main__':
    main()