from bs4 import BeautifulSoup
import requests
import lxml
import datetime
import pprint


class Getweather:
    '''Fetch the data for weather from website'''

    def __init__(self):
        # sourced = requests.get(
        #     'http://nwfc.pmd.gov.pk/media/CitiesForecast.html').text
        # with open(
        #         'D:\Python Files\Book learning python\sourcefile.html', 'w') as outfile:
        #     outfile.write(sourcefile.text)
        with open('D:\Python Files\Book learning python\sourcefile.html') as sourced:
            soup = BeautifulSoup(sourced, 'lxml')
            for all in soup.find_all('b'):
                print(soup)
            # search = soup.find_all('b')
        # first_data = soup.table.td.text
        # first_data = soup.table.text.replace('\n', ' ').replace('  ', ' ')
        # print(search.prettify())
        # print(search)
        # print(search[20])


def main():
    getweather = Getweather()


if __name__ == '__main__':
    main()
