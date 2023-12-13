
# konvertē datu mērvienības
def megabyte_to_megabit(megabyte):
   result = megabyte*8
   return result

# saskaiti degvielas patēriņu uz 100 km
def fuel_consumption(litres, kilometers):
   result = (litres/kilometers)*100
   return result

# konvertē temperatūru
def celsius_to_fahrenheit(celsius):
    result = 32 + celsius*1.8
    return result

# saliec visus skaitļus pirms dota skaitļa (izmanto for)
def sigma(tail):
    result = 0
    for i in range(tail+1):
        result += i
    return result

# nokonvertē svaru uz tuvāko mērvienību - grams, kilograms, tonna (izmanto if)
def weight(grams):
    if 0 < grams <= 999:
        return str(grams) + "g"
    elif 1000 <= grams <= 99999:
        kg = int(grams/1000)
        return str(kg) + "kg"
    elif 100000 <= grams <= 999999:
        c = int(grams/100000)
        return str(c) + "c"
    elif 1000000 <= grams <=  999999999:
        t = int(grams/1000000)
        return str(t) + "t"
