pervyi_number = input()
vtoroi_number = input()
tretii_number = input()
chetvertii_number = input()

def formatrovanie_nomeroff(number_telefon):
    all_chifri = ''.join(filter(str.isdigit, number_telefon))

    if all_chifri.startswith('8'):
        all_chifri = '7' + all_chifri[1:]
    
    return all_chifri

formatrovanie_nomeroff_pervyi_number = formatrovanie_nomeroff(pervyi_number)
formatrovanie_nomeroff_vtoroi_number = formatrovanie_nomeroff(vtoroi_number)
formatrovanie_nomeroff_tretii_number = formatrovanie_nomeroff(tretii_number)
formatrovanie_nomeroff_chetvertii_number = formatrovanie_nomeroff(chetvertii_number)

print(formatrovanie_nomeroff_pervyi_number,'\n',formatrovanie_nomeroff_vtoroi_number, '\n',formatrovanie_nomeroff_tretii_number, '\n',formatrovanie_nomeroff_chetvertii_number, sep='')

def only_number(a):
    if a.startswith('7495'):
        a = a[4:]

    return a

formatrovanie_nomeroff_pervyi_number_only_number = only_number(formatrovanie_nomeroff_pervyi_number)
formatrovanie_nomeroff_vtoroi_number_only_number = only_number(formatrovanie_nomeroff_vtoroi_number)
formatrovanie_nomeroff_tretii_number_only_number = only_number(formatrovanie_nomeroff_tretii_number)
formatrovanie_nomeroff_chetvertii_number_only_number = only_number(formatrovanie_nomeroff_chetvertii_number)

def sravnenie_numbers(formatrovanie_nomeroff_pervyi_number_only_number, formatrovanie_nomeroff_vtoroi_number_only_number, formatrovanie_nomeroff_tretii_number_only_number, formatrovanie_nomeroff_chetvertii_number_only_number):
   dvoiki_numbers = [(formatrovanie_nomeroff_pervyi_number_only_number, formatrovanie_nomeroff_vtoroi_number_only_number),(formatrovanie_nomeroff_pervyi_number_only_number, formatrovanie_nomeroff_tretii_number_only_number),(formatrovanie_nomeroff_pervyi_number_only_number, formatrovanie_nomeroff_chetvertii_number_only_number)]
   result = []
   for dvoiki_numbers in dvoiki_numbers:
        if dvoiki_numbers[0] == dvoiki_numbers[1]:
            result.append('YES')
        else:
            result.append('NO')
   return result

otvet_resiltat = sravnenie_numbers(formatrovanie_nomeroff_pervyi_number_only_number, formatrovanie_nomeroff_vtoroi_number_only_number, formatrovanie_nomeroff_tretii_number_only_number, formatrovanie_nomeroff_chetvertii_number_only_number)
print(otvet_resiltat[0],'\n', otvet_resiltat[1], '\n', otvet_resiltat[2], '\n', sep='')
