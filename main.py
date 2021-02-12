from data import data
from link_maker import LinkMaker

system_on = True
link = LinkMaker(data)

while system_on:
    option = str(input("\n-----------------------------------------------\nPlease select an option: "
                       "\n1) Create a short link \n2) Delete a link \n"
                       "3) Show all urls\n4) Turn off\n-----------------------------------------------\nOption: ")).lower()

    if option == "1":
        long_link = input("Please enter the long url :\n").lower()
        wants_custom_url = input("Do you want a custom URL ? 'Yes/No': ").lower()

        if wants_custom_url == "yes":
            custom_url = input("Please enter your custom link 'Only Letters and Number!': \n").lower()

            while link.url_exists(custom_url):
                custom_url = input(f"This {custom_url}, is already taken, please select a new one! \n").lower()

            link.add_url_to_db(custom_url, long_link)

        else:
            short_url_generated = link.generate_url()

            while link.url_exists(short_url_generated):
                short_url_generated = link.generate_url()

            link.add_url_to_db(short_url_generated, long_link)

    elif option == "2":
        delete_url = input("Type the short url that you want to delete: \n").lower()

        if link.url_exists(delete_url):
            link.find_and_delete_url(delete_url)
        else:
            print(f"{delete_url} doesn't exists in database, please make sure you type it right!")

    elif option == "3":
        link.show_all_urls()

    elif option == "4":
        print("System going offline...")
        system_on = False

    else:
        print("Wrong command, please select a command from above!")