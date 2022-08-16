#notesFromPaper
Year   :
Tags   : [[q learning]] [[cartoscope]] [[cairns]] #cairnsRL
Authors: [[Spatharioti]]

[[Q_Learning_Citizen_Science-Sophie]] had Q learning, but it didn't adapt to player skill on the fly

generate data by simulating players from a variety of [[player modeling|player models]]

0.95 discount factor, 0.1 learning rate. Used weighted Q picking

The state was the levels that had just been played and the number of mistakes that had been made in those levels (to decrease state space, players were categorized as G,B,U instead of having it be a limitless space of numbers)
