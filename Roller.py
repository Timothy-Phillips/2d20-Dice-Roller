import PySimpleGUI as sg
import random

def roll_value(num_dice, verbose):
    rolls_value = [0, 1, 1, 2, 2, 3]
    total = 0
    output= ""
    verbose_out = ""

    if verbose:
        verbose_out = "Individual Rolls:\n"

    for i in range(int(num_dice)):
        value = rolls_value[random.randint(0, 5)]
        total += value
        verbose_out += str(value) + "\n"

    output = "Total: " + str(total)
    return output, verbose_out
        

def roll_damage(num_dice, verbose):
    rolls_damage = ["No Effect", "One Hit", "One Hit", "Two Hits", "Two Hits", "Effect Hit"]
    num_hits = 0
    num_effects = 0
    output = ""
    verbose_out = ""

    for i in range(num_dice):
        rand = random.randint(0, 5)
        if (rand == 1 or rand == 2):
            num_hits += 1
        elif (rand == 3 or rand == 4):
            num_hits += 2
        elif (rand == 5):
            num_effects += 1
        if verbose:
            verbose_out += rolls_damage[rand] + "\n"

    output = "Number of Hits: " + str(num_hits) + "\n" + "Number of Effects: " + str(num_effects)
    return output, verbose_out

fallout_pipboy_theme = {
    'BACKGROUND': "#002f00",
    'TEXT': "#00ee00",
    'INPUT': "#002f00",
    'TEXT_INPUT': "#00ee00",
    'SCROLL': '#002f00',
    'BUTTON': ("#00ee00", "#002f00"),
    'PROGRESS': ("#00ee00", "#002f00"),
    'BORDER': 1,
    'SLIDER_DEPTH': 0,
    'PROGRESS_DEPTH': 0,
}

# Set the theme
sg.theme_add_new('FalloutPipBoyTheme', fallout_pipboy_theme)
sg.theme('FalloutPipBoyTheme')


layout = [[sg.Text("Welcome to the Fallout 2d20 Dice Roller!\n", justification="center", font=("roman 20 bold"))],
          [sg.Text("Are you rolling for damage or to get a total?")],
          [sg.Radio("Damage", 0, key="damage", default=True), sg.Radio("Total", 0, key="total")],
          [sg.Text("\nWould you like to see the individual dice rolls?")],
          [sg.Checkbox("View Rolls", key="view_rolls")],
          [sg.Text("\nHow many dice are you rolling?")],
          [sg.Input(key="num_dice")],
          [sg.Button("Roll Dice")],
          [sg.Text("Results:")],
          [sg.Text("", key="output", expand_x=True, expand_y= True)],
          [sg.Output(size=(40, 20), key="verbose_out", visible=False)]
          ]


window_size = (500, 600)
window = sg.Window("Dice Roller", layout, size=window_size)
out_text = ""
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    elif event == "Roll Dice":
        # Recieve and validate user input
        num_dice = values["num_dice"]
        if (num_dice.isnumeric() and int(num_dice) > 0):
            num_dice = int(num_dice)
            verbose = values["view_rolls"]
            if (values["damage"]):
                out, vout = roll_damage(num_dice, verbose)
                window["output"].update(out)
                if verbose:
                    window["verbose_out"].update(vout)
                    window["verbose_out"].update(visible=True)
                else:
                    window["verbose_out"].update(visible=False)
            else:
                out, vout = roll_value(num_dice, verbose)
                window["output"].update(out)
                if verbose:
                    window["verbose_out"].update(vout)
                    window["verbose_out"].update(visible=True)
                else:
                    window["verbose_out"].update(visible=False)
        else:
            sg.popup_error("That is not a valid number of dice to roll!")
        
        
        

window.close()