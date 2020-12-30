import requests

response = requests.get('http://area.sinaapp.com/bingImg/')

with open('README.md', 'w') as f:
    f.write('# github clock in\n')
    content = """ <img style="-webkit-user-select: none;margin: auto;cursor: zoom-in;" src="{url}" width="1004" height="564"> """.format(url=response.url)
    f.write(content)

