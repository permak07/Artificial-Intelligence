import re
with open("a.txt","r",encoding="utf-8") as file: # мне dz/verb_adverb/a.txt
    for s in file:
        if re.search(r'(\S+(ть|ться|шь)\s+\S+[оеиы]|\S+[оеиы]\s+\S+(ть|ться|шь))',s):
            print(s,end='')