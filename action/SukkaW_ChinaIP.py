import requests

ChinaIP = requests.get("https://ruleset.skk.moe/List/ip/china_ip.conf").text

result = list()
for rawresult in [ChinaIP]:
    for item in rawresult.split("\n"):
        if (item not in result) and (not item.startswith('#')) :
            result.append(item)

result_text = '\n'.join(result)

with open("./Surge/SW/ChinaIP.list", "w") as f:
    f.write(result_text)
