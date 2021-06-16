#notesFromPaper
Year   :
Tags   :
Authors: [[Zhang]] [[Qi]] [[You]] [[Yu]] [[Guan]]
#systemsSurvey

It is difficult to virtualize a [[GPU]] in [[hypervisor]] due to the infrastructure and device driver

In games, this virtualization can be used for games streaming

the resource sharing model and performance variation hurts cloud gaming. 

They think the fps of a game should actually be fed to the controller to give more resources to a game demanding a lot

No modification to applications, OS, or graphics drivers required. 

slap some sleeps in there

it has a list of things that affect FPS variability, but it's not that great of a list

uses some complex math to figure out how sleepy to make the GPUs

SA allocates just enough GPU to get target FPS

FSA takes GPU resources from high FPS games and gives them to low FPS games

ESA sets an FPS and then tries to maximize GPU usage while letting everything stay at that FPS

created test suites based on a stable FPS game and an unstable FPS game

5-12% overhead

@article{zhang2013vgasa,
  title={vGASA: Adaptive scheduling algorithm of virtualized GPU resource in cloud gaming},
  author={Zhang, Chao and Yao, Jianguo and Qi, Zhengwei and Yu, Miao and Guan, Haibing},
  journal={IEEE Transactions on Parallel and Distributed Systems},
  volume={25},
  number={11},
  pages={3036--3045},
  year={2013},
  publisher={IEEE}
}