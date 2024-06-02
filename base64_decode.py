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
                file_txt = input('\n[-] Enter file: ')
                with open(f'{file_txt}','r') as file:
                    for content_txt in file:
                        base64_content = content_txt.strip()
                        decode_content = base64.b64decode(base64_content)
                        print('[+] Decrypted base64 content...')
                        print(f"{decode_content.decode('utf-8')} \n")

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