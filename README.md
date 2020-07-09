# Web-Scraping
>This repo contains the python scripts to extract required information by scraping various websites.

**Note :** There is no universal solution for web scraping as data on every website is uniquely structured. Therefore, in order to scrape the data, you need to dig deeper and understand the website’s structure.

`Disclaimer :` 
- Web Scraping may be against the <ins>terms of use</ins> of some websites and users may be subject to legal ramifications depending on where and how they attempt to scrape information.
- So, Always inspect the Robots.txt as many websites specifies what is considered as good behaviour on that site, such as areas that are allowed to be crawled, restricted pages, and frequency limits for crawling.

## Scripts : (In Progress)

| Website | URL | Libraries | Action |
| --- | --- | --- | --- |
| Worldometer | https://www.worldometers.info/coronavirus/| <ul><li>- [x] BeautifulSoup</li></ul> | [View](worldometers) |
| Amazon | https://www.amazon.in/b?node=976389031| <ul><li>- [x] Scrapy</li></ul> | [View](amazon) |

## Dependencies

- Requests (https://requests.readthedocs.io/)
- Beautifulsoup (https://beautiful-soup-4.readthedocs.io/)
- Scrapy (https://docs.scrapy.org/)

## Installation
Set up a virtual environment and install the dependencies:
```sh
pip install -r requirements.txt
```

## License
This project is licensed under the terms of the [GLP-3.0 license](https://github.com/yyscoop/Web-Scraping/blob/master/LICENSE)
