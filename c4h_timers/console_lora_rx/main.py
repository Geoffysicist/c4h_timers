'''console_lora_rx
'''
DEBUG = True

if DEBUG: print('console_lora_rx started')

from c4h_gates import Console

console = Console(debug=DEBUG)

if DEBUG:
    print(console.get_pins())
    print(console.get_volts())