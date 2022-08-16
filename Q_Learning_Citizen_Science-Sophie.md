#notesFromPaper
Authors: [[Spatharioti]]
Year   :
Tags   : [[q learning]] [[reinforcement learning]] [[cartoscope]] #cairnsRL [[cairns]]

Diversity in tasks to prevent boredom

Three difficulty levels: Color matching, finding tennis courts, & finding bridges

RL algorithm compared to greedy and uniform random

The state was the last three difficulties played, so a state could be MHH aka the player just played a medium game and two hard games. Reward is how many tiles were collected, weighted by difficulty

I'm unsure how training was done... They took random samples from past games of uniform, but how does that train a Q table? I mean I guess you see how many times a triple led to a quit but isn't that all you can do?

I mean, are triples enough state to capture this game?

Greedy is just HHHHHHHH

Greedy dropped off early, but then matched Q learning. Random matched Q learn early, but then completely fell away. My interpretation is that greedy being tough scared away people early, but then those that stuck out stuck out. Random and Q learning had enough variety to keep people around, but then Q learning did something interesting and worthy enough to keep people around.

lack of past data. Reward function how? Comparison how?
