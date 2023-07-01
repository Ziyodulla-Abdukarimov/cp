def saatcha_soatni_aytish(hour, minute):
    numbers = ["o' clock", 'one', 'two', 'three', 'four', 'five',
               'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
               'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
               'eighteen', 'nineteen', 'twenty', 'twenty-one', 'twenty-two',
               'twenty-three', 'twenty-four', 'twenty-five', 'twenty-six',
               'twenty-seven', 'twenty-eight', 'twenty-nine', 'thirty']

    if minute == 0:
        return numbers[hour] + " o' clock"
    elif minute == 15:
        return "quarter past " + numbers[hour]
    elif minute == 30:
        return "half past " + numbers[hour]
    elif minute == 45:
        return "quarter to " + numbers[(hour + 1) % 12]
    elif minute < 30:
        return numbers[minute] + " minutes past " + numbers[hour]
    else:
        remaining_minutes = 60 - minute
        return numbers[remaining_minutes] + " minutes to " + numbers[(hour + 1) % 12]


h = int(input())
m = int(input())
print(saatcha_soatni_aytish(h, m))
