import sys, re

if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    text = sys.argv[2]
    count = len(re.findall(re.escape(keyword), text))
    print(count if count > 0 else "none")