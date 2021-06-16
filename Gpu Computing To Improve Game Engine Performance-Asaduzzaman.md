#notesFromPaper
Year   :
Tags   : [[GPU]] [[GPGPU]]
Authors: [[Asaduzzaman]] [[Lee]]
#systemsSurvey

While GPUs were originally for graphics processing, GPGPUs is a paradigm that intends to aim them at general purpose computing

Multithreading in game engines is tough because the APIs just aren't there

Modern game engines need to shift to multi-core computing since individual cores are plateauing in how fast they can be.

An asynchronous model could work well?

Simple multithreading can be achieved by splitting server and client code, but GPGPU can do better.

Task level parallelism: different tasks are split across different threads, useful for graphics and physics simulation

also data level parallelism, but I don't really see how that's different to task level parallelism... oh ok I think I get it. data parallelism can be infinitely split, so [1.2.3...].map() is data parallelism and you can throw as many cores as you have on it. So use this to ensure that all cores are utilized

it talked about matrix convolutions? Not sure why, but I think it's saying that if you can take problems and turn them into convolutions, you can be more parallelisable.

they created a very single threaded game, and also the same game but multithreaded with task dependency (MAM), and also a multithreaded version with synchronization each cycle (MSM), and also created MSM but with some data parallelism in collision detection

MAM: Thread 1 gets input, updates logic, AI, physics, and nav meshes. Thread 2 updates meshes and graphics

MSM does all serial stuff in serial, then all parallel stuff in parallel. 

MSMDP was MSM, but the collision detection was split up so that they could have more worker threads working on it.

The last one won out, it's scalable and flexible. Asynchronous is still helpful for networking and file loading because that doesn't rely on the game loop.

@article{asaduzzaman2014gpu,
  title={GPU computing to improve game engine performance},
  author={Asaduzzaman, Abu and Lee, Hin Y},
  year={2014},
  publisher={ITB Journal Publisher}
}
