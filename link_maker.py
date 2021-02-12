import random
from data import data


class LinkMaker:

    def __init__(self, data):
        self.link_len = 6
        self.main_website = "shortty.io"
        self.data = data

    def generate_url(self):
        """This function generate a random url and returns it"""
        short_url = ""
        random_char = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
                       "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2",
                       "3", "4", "5", "6", "7", "8", "9"]

        for i in range(6):
            char = random.choice(random_char)
            short_url += char

        return short_url.lower()

    def find_and_delete_url(self, short_url):
        url_index = 0

        for idx, i in enumerate(data):
            s_url = i['short_url']

            if s_url == short_url:
                url_index = idx

        data.remove(data[url_index])

        # TODO: remove it form the list with remove function
        print(f"You {self.main_website}/{short_url} has been deleted!")

    def url_exists(self, input_url):
        """Checks if url exists in database and returns True or False"""
        exists = False
        for each_link in self.data:
            url = each_link['short_url']
            if url == input_url:
                exists = True

        return exists

    def add_url_to_db(self, s_url, l_url):
        database = data
        database.append({"long_url": l_url, "short_url": s_url})
        print(f"\nThis is your new short link: {self.main_website}/{s_url}")

    def show_all_urls(self):
        print("---------------------------------------------------")
        if len(data) == 0:
            print("NO RECORDS IN DATABASE!")
        for each_url in data:
            short_link = each_url['short_url']
            long_url = each_url['long_url']
            print(f"{self.main_website}/{short_link} / {long_url}")
        print("---------------------------------------------------")
