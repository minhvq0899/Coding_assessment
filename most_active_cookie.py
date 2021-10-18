"""
Minh Quang Vu
Please use Python version 3.7+
"""

import csv
import collections
from typing import List, Tuple
import sys

class CookiesProcesser:
    def __init__(self):
        # use dictionary so the look up time is O(1)
        # self.list_of_days is now a dictionary with key: date - value: dict of {cookies : frequency in that day}
        self.list_of_days = collections.defaultdict(lambda:collections.defaultdict(int))
        # self.list_of_frequency is now a dictionary with key: date - value: highest frequency
        self.list_of_frequency = collections.defaultdict(lambda :0)
    

    # this is just taking tweets out of a list and put it into my own data structure
    def process_cookies(self, list_of_cookies_and_date: List[Tuple[str, str]]) -> None:
        """
        process_cookies processes a list of cookies
        """
        for row in list_of_cookies_and_date:           # O( number of cookies )
            cookie = row[0]
            date = row[1][:10]
            self.list_of_days[date][cookie] += 1
            if self.list_of_days[date][cookie] > self.list_of_frequency[date]:
                self.list_of_frequency[date] = self.list_of_days[date][cookie]
    
        # print("Number of days: {}".format( len(self.list_of_days) ))

    
    def search(self, date: str) -> List[str]:           # O( number of cookies )
        result_list = []
        for key, value in self.list_of_days[date].items():
            if value == self.list_of_frequency[date]:
                result_list.append(key)
        
        return result_list





if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit("Please format your input again")  
    
    cookies_csv_filename = str(sys.argv[1])
    time_stamp = str(sys.argv[3])
    list_of_cookies = []
    with open(cookies_csv_filename, "r") as f:
        csv_reader = csv.reader(f, delimiter=",")
        for i, row in enumerate(csv_reader):
            if i == 0:
                # header
                continue
            cookie = str(row[0])
            date_and_time = str(row[1])
            list_of_cookies.append((cookie, date_and_time))

    if not list_of_cookies:
        sys.exit("CSV file is empty")  

    # print("list_of_cookies: ", list_of_cookies)

    cp = CookiesProcesser()
    cp.process_cookies(list_of_cookies)

    # print(cp.list_of_days, "\n")
    # print(cp.list_of_frequency, "\n")

    list_of_most_active_cookies = cp.search(time_stamp)
    # print("list_of_most_active_cookies: ", list_of_most_active_cookies, "\n")

    for cookie in list_of_most_active_cookies:
        print(cookie)

    # assert cp.search("2018-12-09") == ["AtY0laUfhglK3lC7"]
    # assert cp.search("2018-12-08") == ["SAZuXPGUrfbcn5UA", "4sMM2LxV07bPJzwf", "fbcn5UAVanZf6UtG"]
    # print("Successful")
