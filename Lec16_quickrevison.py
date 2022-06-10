# (0°C × 9/5) + 32 = 32°F
def convert_farh(celcius: float) -> float:
    return (celcius * 9/5) + 32 # this value will be first computer and then returned


print(convert_farh(37))