from GoogleNews import GoogleNews

googlenews = GoogleNews()
googlenews = GoogleNews(period='7d')
googlenews.search('USA')
result = googlenews.result()
