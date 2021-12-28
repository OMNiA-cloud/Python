import requests
import json

api_url = "https://freecurrencyapi.net/api/v2/latest?apikey=YOUR-APIKEY"

bozulan_doviz = input("Bozulan döviz türü: ")
alinan_doviz = input("Alınan döviz türü: ")
miktar = input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz: ")

result = requests.get(api_url)

result = json.loads(result.text)

print("1 {0} = {1} {2}".format(bozulan_doviz, result["rates"][alinan_doviz], alinan_doviz))
print("{0} {1} = {2} {3} ".format(miktar,bozulan_doviz,miktar * result["rates"][alinan_doviz], alinan_doviz))