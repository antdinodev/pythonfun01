#please don't use my api key, thanks :)
from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='08bf3cdc2d174599a670d03fa46ee45c')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          #sources='bbc-news,the-verge',
                                          category='business',
                                          language='en',
                                          country='us')


for y in top_headlines['articles']:
    print(y)
# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2021-07-23',
                                      to='2021-08-22',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)


for y in all_articles['articles']:
    print(y)


# /v2/top-headlines/sources
sources = newsapi.get_sources()

for y in sources['sources']:
    print(y)