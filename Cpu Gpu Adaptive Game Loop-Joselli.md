#notesFromPaper
Year   :
Tags   : [[GPU]]
Authors: [[Joselli]] [[Zamith]] [[Clua]] [[Montenegro]] [[Leal-Toledo]] [[Conci]]
#systemsSurvey

They run processes then analyze which process worked better on CPUs and GPUs and then place them in the appropriate spot wtf.

games are realtime applications that require user input 

CPUs good for small amount of data, GPUs good for large

GPUs have been evolving fast, and as part of a [[GPGPU]] push, [[Nvidia]] and [[AMD]] have been developing languages that open GPU computing (though these are ABSOLUTELY PROPRIETARY)

the game loop has three tasks:

 - data acquisition (from controllers)
 - data processing
 - data presentation (graphics)

Some previous work that utilizes GPGPU in these kinds of things, but no CPU / GPU interplay

some tasks can only be run on certain processors

task manager uses aspects of various tasks to figure out how they are going to execute. Task manager acts as a server in server client architecture

tracked CPUtime and GPUtime as a direct way to compare them

paper mentions that they re-implemented the game in CUDA that way they could run as both CPU and GPU... but does that mean every game would need to be rewritten in [[CUDA]]? Is this scalable?

## Criticism

 - What should the tasks be split up as? It provides some examples, but these still seem granular
 - What if a task is better split in a different way?
 - Overhead of task manager?
 - Is this the engine's problem, or the programmers?
   - If engine, is this generalizable?
   - If programmer, is this worth it? How should a programmer know?
