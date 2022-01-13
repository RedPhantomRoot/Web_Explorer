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
    print("[*]Declaration: Please use this tool for a domain or website that you are allowed to pentest. "\
       "I am not responsible for any trouble you might cause.")
    print("[*]If something unexpected happens while using this tool, you can exit by 'Ctrl + c'(you might see weird errors but just ignore it. )\n")

if __name__ == "__main__":        
    introduction()
    options_list = ["Crawler(find subdirectories, endpoints and possible emails)", "Directory Brute Forcer", "Subdomain Brute Forcer", "Detect technology", "Exit"]
    valid_option = ["1", "2", "3", "4", "5"]
    counter = 1
    for option in options_list:
        print(f"{counter}:) {option}")
        counter += 1
    user_option = input("\nChoose number: ")
    if user_option in valid_option:    
        if user_option == "1":
            spider = Spider()
            # Need partition here cuz extract_link is recursion
            spider.print_partition("Extracted links")
            spider.extract_link()
            spider.print_email()
        elif user_option == "2":
            spider = Spider()
            spider.start_bruteforce_checking_extension()
        elif user_option == "3":
            spider = Spider()
            spider.bruteforce_subdomain()
        elif user_option == "4":
            spider = Spider()
            spider.detect_technology()
        elif user_option == "5":
            exit()
    else:
        print("[-]You gave me invalid value.")
