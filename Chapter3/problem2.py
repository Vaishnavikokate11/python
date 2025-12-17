# print name and date from this data
letter = """ Dear <|Name|>
You are selected! 
<|Date|>"""

print(letter.replace("<|Name|>", "vaishu").replace("<|Date|>", "29-Dec-2025"))