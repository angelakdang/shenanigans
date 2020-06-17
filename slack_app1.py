"""
@title: Icebreaker Selector
@author: Hayden Reece Hohns
@date: 5/6/2020
@brief: Icebreaker shenanigans.
"""

import numpy as np
import json
import sys

def get_data(filename='data.json'):
    """This function gets the data and reads it as a dictionary and checks if
    a whole round has been completed. If completed, then the 'Done' list is
    reset.

    Parameters:

    filename -- a string of the JSON file to be read.

    Returns:

    ice_breaker_data -- a dictionary of the data containing people to do
    icebreakers.
    """

    with open(filename) as f:
        ice_breaker_data = json.load(f)
    if len(ice_breaker_data['Names']) == len(ice_breaker_data['Done']):
        ice_breaker_data['Done'] == []

    return ice_breaker_data


def write_data(data: dict, filename='data.json'):
    """Given a dictionary and filename, write the data.

    Parameters:

    data -- a dictionary of the data.
    filename -- a string of the file to write to (probably the same you read).

    Returns: None
    """

    with open(filename, 'w') as outfile:
        json.dump(data, outfile)


def main(filename='data.json'):
    """Prints out the newest person to do an icebreaker and updates the data.

    Parameters:

    filename -- JSON filename to be read (string).
    """

    data = get_data()

    candidates = set(data['Names']) - set(data['Names']).intersection(set(data['Done']))
    candidates = np.array(list(candidates))
    victim = np.random.choice(candidates)

    print("The next victim is: ", victim)

    data['Done'].append(victim)
    write_data(data, filename)



if __name__ == "__main__":
    #main(sys.argv[1])
    main()
