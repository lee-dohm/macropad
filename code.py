from adafruit_macropad import MacroPad

macropad = MacroPad()

text_lines = macropad.display_text(title = '* lee-dohm Macropad *')

def send_string(text):
    macropad.keyboard_layout.write(text)

DEFAULTS = {
    'mode_text': '----- RimWorld  -----',
    'keys': [
        '1',
        '2',
        '3',
        "'",
        ',',
        '.',
        'a',
        'o',
        'e',
        None,
        None,
        ' '
    ]
}

text_lines[0].text = DEFAULTS['mode_text']
text_lines.show()

while True:
    key_event = macropad.keys.events.get()

    if key_event and key_event.pressed:
        send_string(DEFAULTS['keys'][key_event.key_number])
