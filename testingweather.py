from WeatherText import *
from Wunder import *

def main():
    a = False
    b = False
    while not a and not b:
        r = input(initial_Welcome)

        if r.lower() == 'atlanta':
            a = True
            print(atl_Welcome)
    
        elif r.lower() == 'dallas':
            b = True
            print(dal_Welcome)
        
        else:
            print(initial_Welcome)

        while a is True:
            s = input ("Text humidity, wind, rain, sunset, or moon for more information. Text all for all information. Text back for city selection.")
            if s.lower() == 'sunset':
                print(atl_sunsetText)
            elif s.lower() == 'moon':
                print(atl_moonText)
            elif s.lower() == 'humidity':
                print(atl_humidityText)
            elif s.lower() == 'wind':
                print(atl_windText)
            elif s.lower() == 'rain':
                print(atl_rainText)
            elif s.lower() == 'all':
                print(atl_allText)
            elif s.lower() == 'back':
                a = False
            else:
                print(s)


        while b is True:
            u = input ("Text humidity, wind, rain, sunset, or moon for more information. Text all for all information. Text back for city selection.")
            if u.lower() == 'sunset':
                print(dal_sunsetText)
            elif u.lower() == 'moon':
                print(dal_moonText)
            elif u.lower() == 'humidity':
                print(dal_humidityText)
            elif u.lower() == 'wind':
                print(dal_windText)
            elif u.lower() == 'rain':
                print(dal_rainText)
            elif u.lower() == 'all':
                print(dal_allText)
            elif u.lower() == 'back':
                b = False
            else:
                print(u)

main()
