files_test = [
    't_Regex', 't_Quantifier', 't_Set', 't_Group', 't_Anchor',
    't_Helper_Range',
]

for filename in files_test:
    exec(open("./{}.py".format(filename)).read())
