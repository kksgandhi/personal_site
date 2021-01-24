Year   : 2000
Tags   :
Authors: *Chi* *Pirolli* *Pitkow*

*information foraging theory*

presents an architecture and system for the analysis and prediction of user behavior and website usability

with the web being the way it is, an automated method of analyzing website usability is necessary

usability metrics are simplistic numerics like number of visitors, reading time, session length, etc.

There are some [GOMS](GOMS.md) analyses, but this doesn't look at higher level ideas and doesn't actually analyze content

webmasters want to understand alternative designs for slightly different users, not just understanding what current users are doing

foragers use cues such as graphics and snippets (proximal, easily viewable cues) to asses what might be on the other side of the link (distal, far information)

use something called longest repeating subsequence to model surfing paths...

assumes that users have some information goal

their bots scored links based on the distal content's similarity to their information goal. Despite the fact that users don't directly see distal content, it was still a fruitful way to find problems with proximal content

* content similarity (how similar are webpages)
* Usage graph: how much do real users actually move between edges
* co citation graph: How often is the same node linked to by the same page

LRS: If users start at some node, the LRS is the longest path users take often enough

something about dome trees?? A visualization method that shows links going outwards

Usage Based Layout trees represent paths that aren't hyperlinked between, such as links traversed with the back button

if the paths users actually take mismatch with the scented optimal paths, there is something wrong

some pages are way points, some are conduits.

Presentation: 

The year is 2000, search engines aren't that great and many websites have hyperlinked maps of information

Usability metrics are simple, but webmasters want to understand alternative designs or capture different users. There are some GOMS analyses, but they are simple and don't look at high level ideas, nor do they analyze content.

graphs and proximal vs distal cues?

creating graphs of content similarity, usage, and co-citations.

Let's model optimal users using information scent.
