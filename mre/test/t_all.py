files_test = [
    't_Regex', 't_Quantifier', 't_Set', 't_Group',
]

for filename in files_test:
    exec(open("./{}.py".format(filename)).read())
