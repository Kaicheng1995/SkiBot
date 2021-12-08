from resort import Resort
from data_operation import set_operation
from data_weather import set_weather


# create 5 Resort objects
kirkwood = Resort("Kirkwood")
aspen = Resort("Aspen Snowmass")
crystal = Resort("Crystal Mountain")
gore = Resort("Gore Mountain")
heavenly = Resort("Heavenly")

# append all resorts objects to a list
Resorts = [kirkwood, aspen, crystal, gore, heavenly]


def get_realtime_data():
    set_weather()














