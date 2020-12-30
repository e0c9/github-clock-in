import requests
from datetime import date

response = requests.get('http://area.sinaapp.com/bingImg/')
now = datetime.now()
now = now.strftime("%d/%m/%Y %H:%M:%S")

with open('README.md', 'w') as f:
    f.write('# github clock in\n')
    f.write('更新时间：{now}\n'.format(now=now))
    content = """ <img style="-webkit-user-select: none;margin: auto;cursor: zoom-in;" src="{url}" width="1004" height="564"> """.format(url=response.url)
    print(content)
    f.write(content)

