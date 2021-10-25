beautifulsoup4

parsing문제



xml형식으로 서비스하는 페이지를 requests.get으로 가져와 html parsing을 하면 파싱이 완벽히 이루어지지 않는 문제.

문제가 되는 코드는

```python
soup = BeautifulSoup(html, 'html.parser')
```

html을 출력하면 `</link>`가 있으나, soup를 출력하면 사라짐.



방법:

- html.parser가 아닌 lxml, xml로 parsing을 해보자.

  ```
  bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: xml. Do you need to install a parser library?
  ```

  xml(lxml)이라는 라이브러리를 깔으란다.

  ``` 
  pip install lxml
  ```

  이렇게 하면 되는데~~~ 리눅스는 조금 다르다.

  ```
  sudo apt-get install python3-lxml
  ```

  요래 하고 실행을 했더니 된다 ㅎㅎㅎ

  

- `xmltodict`라는 라이브러리를 사용해보자.

  이건 `Beautifulsoup`를 사용하지 않고, xml을 dictionary로 바꾼 후 다시 json으로 바꿔서 출력하는 방법이다.

  해당 코드는 다음과 같다.

  ```python
  import requests
  import xmltodict
  import json
  
  url = 'https://fs.jtbc.joins.com//RSS/newsrank.xml'
  response = requests.get(url)
  dict_data = xmltodict.parse(response.content)
  json_data = json.loads(json.dumps(dict_data))
  
  for value in json_data['rss']['channel']['item']:
    print(value['link'])
  ```

  출력의 결과는~

  ```
  https://news.jtbc.joins.com/article/article.aspx?news_id=NB12018034
  https://news.jtbc.joins.com/article/article.aspx?news_id=NB12018018
  https://news.jtbc.joins.com/article/article.aspx?news_id=NB12018141
  https://news.jtbc.joins.com/article/article.aspx?news_id=NB12017950
  https://news.jtbc.joins.com/article/article.aspx?news_id=NB12018096
  https://news.jtbc.joins.com/article/article.aspx?news_id=NB12018126
  https://news.jtbc.joins.com/article/article.aspx?news_id=NB12018139
  https://news.jtbc.joins.com/article/article.aspx?news_id=NB12018148
  https://news.jtbc.joins.com/article/article.aspx?news_id=NB12018199
  https://news.jtbc.joins.com/article/article.aspx?news_id=NB12018121
  https://news.jtbc.joins.com/article/article.aspx?news_id=NB12018032
  https://news.jtbc.joins.com/article/article.aspx?news_id=NB12018026
  https://news.jtbc.joins.com/article/article.aspx?news_id=NB12017919
  https://news.jtbc.joins.com/article/article.aspx?news_id=NB12018119
  https://news.jtbc.joins.com/article/article.aspx?news_id=NB12018213
  https://news.jtbc.joins.com/article/article.aspx?news_id=NB12018207
  https://news.jtbc.joins.com/article/article.aspx?news_id=NB12018115
  https://news.jtbc.joins.com/article/article.aspx?news_id=NB12018153
  https://news.jtbc.joins.com/article/article.aspx?news_id=NB12017662
  https://news.jtbc.joins.com/article/article.aspx?news_id=NB12018185
  ```

  잘 나온다 ㅎㅎ

  이 방식은 내가 한건 아니고 팀원이 도와줘서 발견한 방법이다. (땡큐 성민님)

