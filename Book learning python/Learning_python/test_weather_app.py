from bs4 import BeautifulSoup
import requests
import lxml
import datetime
import pprint


class Getweather:
    '''Fetch the data for weather from website'''

    def __init__(self):
        sourced = requests.get(
            'http://nwfc.pmd.gov.pk/media/CitiesForecast.html').text
        soup = BeautifulSoup(sourced, 'lxml')
        # for tr in table soup.find_all('tr'):
        first_data = soup.table.text.replace('\n', ' ').replace('  ', ' ')
        # first_data = soup.find('table', class_='MsoNormalTable').text
        # for first_data in soup.find_all('first_data'):
        print(first_data)


def main():
    getweather = Getweather()


if __name__ == '__main__':
    main()
