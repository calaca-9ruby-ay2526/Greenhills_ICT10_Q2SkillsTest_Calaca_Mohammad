#working with dictionaries
from pyscript import display, document

def non_metal_value(e):
    document.getElementById('result').innerHTML = " "
    non_metal_v = document.getElementById('dictionary').value   

    non_metal = {
        'H':'Symbol: H Element: Hydrogen Atomic Number: 1 Atomic Mass: 1.008',
        'C':'Symbol: C  Element: Carbon Atomic Number: 6 Atomic Mass: 12.011',
        'N':'Symbol: N Element: Nitrogen Atomic Number: 7  Atomic Mass: 14.007',
        'F':'Symbol: F Element: Flourine  Atomic Number: 9 Atomic Mass: 18.998403162',
        'Ne':'Symbol: Ne Element: Neon  Atomic Number: 10 Atomic Mass: 20.1797',
        'I':'Symbol: I Element: Iodine  Atomic Number: 53 Atomic Mass: 126.90447',
        'Ar':'Symbol: Ar Element: Argon  Atomic Number: 18 Atomic Mass: 39.948 '
        
        

        }
  
    
    game_checker = non_metal_v in non_metal
    
    display_message = ('Sorry, please type a valid element', f'{non_metal[non_metal_v]}')

    display(display_message[game_checker], target='result')