a form of [[machine learning]] that focuses on receiving feedback from the environment and updating its policy (set of actions to maximize reward)

episodic: Training is from a finite set of examples

incremental: each training example mildly changes the policy

bootstrapping: Estimate how good a state is based on how good the next state is. Don't fully understand this, might be worth coming back to...

backup: Go from an ideal state in the future back to the current state and see what it takes to get there. 

Dynamic Programming: Have a model of the world and bootstrap to figure out the optimal path to some goal state.

[[q learning]]
