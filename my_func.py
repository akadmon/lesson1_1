def get_summ(one, two, delimetr='&'):
    new_born = f'{str(one)}{delimetr}{str(two)}'.upper()
    return new_born

itog = get_summ("Learn", "python")
print(itog)
