import requests

response = requests.get('http://area.sinaapp.com/bingImg/')

with open('README.md', 'w') as f:
    f.write('# github clock in\n')
    content = "![bing]('{url}')".format(url = response.url)
    f.write(content)

