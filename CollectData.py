import arxivscraper
import pandas as pd

scraper = arxivscraper.Scraper(category='stat', date_from='2002-09-01', date_until='2017-09-01',
                               filters={'categories': ['stat.ML']})

output = scraper.scrape()

cols = ('id', 'authors')
df = pd.DataFrame(output, columns=cols)
print len(df)
df.to_csv('~/Data/ml_15year.csv')

