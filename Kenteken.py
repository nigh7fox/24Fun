from collections import Counter
import urllib.request
import urllib.error
import csv
from bs4 import BeautifulSoup
from ordered_set import OrderedSet

#Words that you want the value of
keywords = ['Merk', 'Handelsbenaming', 'Inrichting', 'Brandstof', 'Vermogen', 'Bouwjaar', 'BPM','CO2 uitstoot gecombineerd', 'Cilinderinhoud','Massa leeg voertuig']                                    


def get_html(full_link): 
    """
    Requests and opens chosen link for reading.
    """

    url_request = urllib.request.Request(full_link, headers = {'User-Agent': 'Mozilla/5.0'})
    url_html = urllib.request.urlopen(url_request).read()
    return url_html


def get_info(full_link):
    """
    Returns value of keywords
    """
    soup = BeautifulSoup(get_html(full_link),'html.parser')
    all_tds = soup.find_all('td')
    keyword_index = []
    kenteken_data = []
    
    #Finds the position of the keyword in the list of 'td'. 
    for i, x in enumerate(all_tds):            
        if x.string in keywords:
            keyword_index.append(i)
    
    #Finds the value of the keyword in the list of 'td'        
    for y in keyword_index:
        kenteken_data.append(all_tds[y+2].string)
    return list(OrderedSet(kenteken_data))


def write_to_csv(full_link):
    try:
        with open('kenteken_data_test.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(get_info(full_link))
    except FileNotFoundError:
        print("File not found")
    finally:
        f.close()


def main():
    base_link = 'https://www.rdwdata.nl/kenteken/'  

    file_name = input('Enter filename for number plates: ')
    
    with open(file_name) as f:
        for line in f:
            full_link = base_link + line
            print(full_link)
            if full_link.strip() != base_link.strip():
                try:
                    write_to_csv(full_link)
                except urllib.error.HTTPError:
                    print("Link not found")

            else:
                print("Empty line")
                break
    
          

if __name__ == "__main__":
    main()