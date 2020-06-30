import requests
from bs4 import BeautifulSoup
import csv


def make_soup(url):
    page_html = requests.get(url)
    soup = BeautifulSoup(page_html.text, "html.parser")
    return soup


def get_data(soup):
    """
    Function to scrap data and return data in a list
    """
    covid_stat = []
    # print(soup.prettify())

    ## Getting Table header -------------------
    thead_block = soup.find("table", id="main_table_countries_today").thead
    header = (thead_block.tr.text).split("\n")
    # print(len(header[:19]),header[:19])        ##List with table headlines
    covid_stat.append(header)

    ## Getting country wise detail ------------------
    tbody_block = soup.select("table#main_table_countries_today>tbody")
    country_tbody_block = tbody_block[0]
    country_tr_block = country_tbody_block.find_all("tr")
    total_country = len(country_tr_block)
    for i in range(8, total_country):
        # print(len(country_data),country_data)    ##List with countrywise data
        country_data = (country_tr_block[i].text).split("\n")
        covid_stat.append(country_data)
    print(covid_stat[0])
    return covid_stat


def create_csv(scraped_data):
    """
    Function to store scraped data in CSV
    """
    ## header feild names
    # header_fields = ['', '#', 'Country,Other', 'TotalCases', 'NewCases', 'TotalDeaths', 'NewDeaths', 'TotalRecovered', 'NewRecovered', 'ActiveCases', 'Serious,Critical', 'Tot\xa0Cases/1M pop', 'Deaths/1M pop', 'TotalTests', 'Tests/', '1M pop', '', 'Population', 'Continent', '1 Caseevery X ppl1 Deathevery X ppl1 Testevery X ppl', '']

    # data rows of csv file
    rows = scraped_data

    # name of csv file
    filename = "output.csv"

    # writing to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the header fields names
        # csvwriter.writerow(header_fields)

        # writing the data rows
        csvwriter.writerows(rows)

    print("CSV Created")


def main():
    URL = "https://www.worldometers.info/coronavirus/"
    soup = make_soup(URL)
    scraped_data = get_data(soup)
    create_csv(scraped_data)


if __name__ == "__main__":
    main()
