import http.client

#site reference: "developer.sportradar.com"

conn = http.client.HTTPSConnection("api.sportradar.us")

conn.request("GET", "/ncaafb-t1/2015/REG/12/TOL/BGN/extended-boxscore.xml?api_key=2p7j7ec2nvt9jq4d37xumaxb")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
