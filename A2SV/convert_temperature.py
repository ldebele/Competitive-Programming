
class ConvertTemperature():

    def celsius_into_kelvin_and_fahrenheit(self, celsius):

        # convert into kelvin
        kelvin = celsius + 273.15

        # convert into fahrenheit
        fahrenheit = celsius * 1.8 + 32

        # [kelvin, fahrenheit]
        return [kelvin, fahrenheit]




if __name__ == "__main__":

    celsius = float(input())

    ct = ConvertTemperature()
    kf = ct.celsius_into_kelvin_and_fahrenheit(celsius)
    print(kf)