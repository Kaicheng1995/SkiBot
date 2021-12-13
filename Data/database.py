import sys
sys.path.append('/Users/kai/PycharmProjects/pythonProject1/SkiBot/Class')
from resort import Resort
from data_weather import *
from data_operation import *

# create 5 Resort objects
kirkwood = Resort("Kirkwood")
aspen = Resort("Aspen Snowmass")
crystal = Resort("Crystal Mountain")
gore = Resort("Gore Mountain")
heavenly = Resort("Heavenly")

# append all resorts objects to a list
Resorts = [kirkwood, aspen, crystal, gore, heavenly]


# Populate resort objects with all data
def populate_data():
    set_weather(Resorts)
    set_operation(Resorts)
    return Resorts


'''
    Methods used for printing data
    
    1/ print resorts name and location
    2/ print the operating info of a resort
'''


def print_resorts(Resorts):
    info = ""
    for resort in Resorts:
        info += resort.name + "  --  " + resort.operation.location + "\n"
    return info.strip()


def print_operation(resort):
    info = resort.operation.__str__()
    return info
