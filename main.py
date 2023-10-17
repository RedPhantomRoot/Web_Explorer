from spider import Spider

def introduction():
    print("""
 ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄               ▄▄▄▄▄▄▄▄▄▄▄  ▄       ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄            ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌             ▐░░░░░░░░░░░▌▐░▌     ▐░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌            ▐░█▀▀▀▀▀▀▀▀▀  ▐░▌   ▐░▌ ▐░█▀▀▀▀▀▀▀█░▌▐░▌          ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌            ▐░▌            ▐░▌ ▐░▌  ▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌
▐░▌   ▄   ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▄▄▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄    ▐░▐░▌   ▐░█▄▄▄▄▄▄▄█░▌▐░▌          ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌
▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌    ▐░▌    ▐░░░░░░░░░░░▌▐░▌          ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░▌ ▐░▌░▌ ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▀▀▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀    ▐░▌░▌   ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌          ▐░▌       ▐░▌▐░█▀▀▀▀█░█▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ 
▐░▌▐░▌ ▐░▌▐░▌▐░▌          ▐░▌       ▐░▌            ▐░▌            ▐░▌ ▐░▌  ▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌     ▐░▌  ▐░▌          ▐░▌     ▐░▌  
▐░▌░▌   ▐░▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌            ▐░█▄▄▄▄▄▄▄▄▄  ▐░▌   ▐░▌ ▐░▌          ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌      ▐░▌ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌ 
▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌             ▐░░░░░░░░░░░▌▐░▌     ▐░▌▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌
 ▀▀       ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀               ▀▀▀▀▀▀▀▀▀▀▀  ▀       ▀  ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀ 
        """)
    print("[*] Declaration: Please use this tool for the domain or the website that you are allowed to pentest. "\
       "I am not responsible for any trouble you cause with this tool.")
    print("[*] If something unexpected happens while using this tool, you can exit by 'Ctrl + c' (you might see weird errors but just ignore them. )\n")

if __name__ == "__main__":        
    introduction()
    options_list = ["Crawler (find subdirectories/endpoints and possible emails)",
     "Directory Brute Forcer", "Subdomain Brute Forcer", "Detect technology", "Exit"]
    valid_option = ["1", "2", "3", "4", "5"]
    counter = 1
    for option in options_list:
        print(f"{counter}:) {option}")
        counter += 1
    user_option = input("\nChoose number: ")
    if user_option in valid_option:  
        if user_option == "5":
            exit()  
        spider = Spider()
        if user_option == "1":
            # Need partition here cuz extract_link is recursion
            spider.print_partition("Extracted links")
            spider.extract_link()
            spider.print_email()
        elif user_option == "2":
            spider.invoke_bruteforce()
        elif user_option == "3":
            spider.bruteforce_subdomain()
        elif user_option == "4":
            spider.detect_technology()
    else:
        print("[-] You gave me invalid value.")
