#notesFromPaper
Year   : 2024
Tags   : 
Authors: [[Gandhi]] [[Cooper]]

[Link to the original paper](https://drive.google.com/file/d/1QZd7S4KzPwh9IO9FbkQ_TXBmuK2oOoWw/view?usp=sharing)
There are tons of papers that analyze a fully built educational game, but few that go into the process of building their game. Sure, a paper may say that a game was effective, but why was it effective? What worked, and didn't work, and what changes needed to be made during development?

This paper details the process of making *Building Forward*, a game designed to teach young adults about urban planning. The game's design draws on theories in [[constructivism]].

Summary of the Development Process
----------------------------------

Development began part time in the Summer of '23, I mostly worked on refreshing my technical skills by making traffic simulations and proofs of concept. Most of these simulations didn't actually end up being useful, since the game ended up being so complicated that players didn't really notice details of the simulation.

I built up a map of concepts, which served as a good anchor for features as I moved forward, and helped me communicate my ideas with [[subject matter experts|SMEs]]. SMEs were super helpful, though all my SMEs were in urban planning or architecture. I should have broadened out to environmental experts and racial justice experts.

Early prototypes were linear (didn't give the player's too much choice), so I moved to a system where players got to allocate space in the city, with private developers and citizens reacting to their allocations.

As I shifted into a consistent development / playtesting cycle, I looked into [[Transformational_Framework-Culyba|The Transformational Framework]] and other city builder games for inspiration. These resources weren't helpful to me specifically because I was already familiar with them — the tips in the Transformational Framework were things I was already doing! (having read the book a year ago).

I also tried to do a [[concept maps|concept mapping]] exercise with players, having them build a map before and after playing the game to see what they'd learned. I didn't reserve much time for the exercise though, and so it wasn't as illuminating as I thought it would be. My playtesters were also well educated college students, and while I took steps to limit that, it was still a problem and led to bias in my playtesters.

The last few months of development centered around polish and balancing the systems in the game. One of the more interesting systems was the "goodwill system", in which players spent and received the invisible resource of citizen goodwill. If a player didn't have enough goodwill, their requested changes would be blocked by political opponents. The heavy level of engagement this system received was surprising; players appreciated the system and talked about how it got them to think about how community outreach happens and the feedback-change iteration cycle that a city goes through.

As the game wrapped up, I met with my SMEs again to ensure there were no mistakes in the game.

Discussion
---------------

*Text*, and how it's used was an important factor in *Building Forward*. Text is important in actually conveying information, but too much text can feel boring, or worse, condescending. At certain times, the bluntness of a message would make players feel like they were being talked at by the developer. One thing that helped was making text more diegetic, having it be more a part of the game world. For example, an achievement that read "pedestrians now feel safer walking around" was replaced with a character in game saying "I now feel safer walking around with my kids!". Other benefits came from making text *timely* (having it only show up when relevant), and *meaningful* (removing redundant text and cutting down what remained).

The simulation was important, insofar as it created a sandbox for players to mess around and visualize their changes in, but I spent a lot of time programming features that didn't actually add to the experience. Playtesting would have identified critical features.

Conclusion and Design Insights
------------------------------

 - A detailed simulation is not as important as scaffolding (text and other elements that guide the player and make learning goals explicit).
 - Subject-Matter Experts are critical in refining learning goals, while diverse playtesters are critical in identifying features deserving of further iteration.
 - Player freedom is paramount in the game experience. Player freedom can be in harmony with the communication of learning goals, though one needs to tailor the learning goals to the path the player took through the game.
 - Verify the full publishing pipeline, otherwise you may be unable to publish the game in the format you intended.
 - Utilizing design frameworks and looking at other games is helpful, though less so if you are already familiar with these frameworks and other games.
 - Text can be made more palatable in a game if there is focused development into making it meaningful, timely, and diegetic.
 - Technical limitations should be addressed in even a minor way, at the least to prevent confusion about said limitations.
