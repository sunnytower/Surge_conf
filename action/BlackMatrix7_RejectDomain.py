import requests

RejectDomain = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Advertising/Advertising_Domain.list").text

result = list()
for rawresult in [RejectDomain]:
    result.extend([item for item in rawresult.split("\n") if not item.startswith('#')])
result_text = '\n'.join(result)

with open("./Surge/BM/RejectDomain.list", "w") as f:
    f.write("\n".join(result))