#test = ["BGT 241"]
test = ["BGT 231 BGT 232 BGT 233 BGT 234"]

klasse = test[0]
count = sum(1 for i in klasse)
number = [zeichen for zeichen in klasse if zeichen.isdigit()]

klasse_number = str(''.join(number))[:2] + "x"
if count >= 8:
    klasse_prefix = klasse[:3]
    print(f"{klasse_prefix} {klasse_number}")
else:
    print("~rawr xD")