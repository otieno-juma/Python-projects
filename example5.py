    # Convert each Fahrenheit temperature to Celsius and store
    # the Celsius temperatures in a list named cels_temps.
    cels_temps = list(map(
            lambda fahr: round((fahr - 32) * 5 / 9, 1),
            fahr_temps))
