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
