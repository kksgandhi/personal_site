#notesFromPaper
Year   :
Tags   :
Authors: [[Gandhi]] [[Spatharioti]] [[Eustis]] [[Wylie]] [[Cooper]]

[[citizen science|Citizen science]] and [[crowdsourcing]] are powerful ways to solve problems, and organizations looking towards these approaches have two major populations they can draw on: [[microwork]] platforms like [[mturk|Mechanical Turk]], or volunteers who are interested in the topic. Which approach is better?

This paper is a retrospective analysis using data from Healthy Gulf, which spent the last two years using both approaches. MTurk workers and volunteers voted on the appropriate labels for 4644 images, we analyzed those votes as compared to experts to understand the nuances of using either approach.

Major Takeaways
---------------

While both populations have useful niches, in the context of this difficult image labeling task, volunteers were accurate while little information was gained from MTurk workers. A straightforward workflow emerged for soliciting volunteer votes: Where volunteers are highly confident, take their labels as truth. For images of medium confidence, solicit further votes. Finally, for images of low confidence, spend limited expert resources on those images specifically.

Background
----------

 - Citizen Science is a useful tool for ecological projects ([[citizen science]])
 - Citizen science volunteers are motivated by community, challenge, and achievement ([[motivation in citizen science]])
   - Citizen science volunteers overwhelmingly identify as white and educated
   - Citizen science volunteers shouldn't be exploited as unpaid labor!
 - [[mturk|Mechanical Turk]] is an effective way to complete many crowdsourcing projects. Beyond payment, MTurk workers enjoy autonomy, variety, and meaningfulness in the tasks they complete.
   - Mechanical Turkers can cheat for payment ([[malicious turkers|Malicious Mechanical Turk Workers]]).
   - Mechanical Turkers (like everyone) should be paid a fair wage.
 - There has been some previous work looking at [[volunteers vs turkers|whether to use MTurk workers or volunteers]]. Differences in accuracy between the two groups show up when the tasks are of high complexity.

Methodology and Setup
---------------------

 - Both volunteers and MTurk workers were looking at satellite data of wetland loss or restoration patterns in Louisiana.
 - Volunteers were recruited via social media, SciStarter, and Healthy Gulf's mailing lists.
 - MTurk workers were paid USD 1.30 for participation, regardless of how many images they labeled. This payment scheme:
   - Allows workers to determine the worth of their own labor
   - Prevents spamming, since there's no incentive to label a lot of images
   - Allows us to understand the natural rate at which MTurk workers would want to leave a project.
   - Past work shows that this scheme actually increases the number of images labeled.

The analysis had some confounding issues, that prevented us from doing full inferential statistics (with p values and everything)

 - There was a progress indicator that some volunteers saw and others didn't
 - There were aesthetic UI changes
 - There were smaller A/B tests, though their small size means we're not overly concerned about their confounding effects.

Summary of Results and Discussion
---------------------------------

 - Volunteers were very accurate, but MTurk workers were barely better than baseline
 - Volunteers who saw a progress indicator submitted more images than MTurk workers, who submitted more images than volunteers who didn't see a progress indicator (on average)
 - If volunteers agreed with each other, they were likely to be correct. If they didn't agree with each other, they were unlikely to. There was no notable correlation between the level MTurk workers agreed with each other and their accuracy.
 - Easy images didn't gain from having a ton of volunteer votes (presumably since they are so easy that more votes aren't necessary). Hard images didn't gain either (presumably since they are so hard that it's a crapshoot)
 - The last two bullet points in combination lead to a straightforward workflow: get a few votes for each image. If it's near unanimous, it's an easy image, and don't get too many more votes for it. If there's disagreements, get more votes. If you have a lot of votes and there's still heavy controversy, then it's a tough image, and call in an expert to review it.
   - This workflow doesn't really work for MTurk, since an image's votes could be controversial / unanimous just from chance.
 - Accuracy between members of Healthy Gulf and non-members was the same. (there is a selection bias though since we only captured people who filled out the survey.)
 - There's no notable correlation between the number of images someone submitted and their accuracy.
 - MTurk workers weren't appropriate here, but are more accessible and possibly cheaper, so of course MTurk has its uses.
 - Outreach, advocacy, and longer term community building isn't possible due to the structure of MTurk.
   - Funnily enough, the diversity of MTurk workers may have inadvertently added to the diversity of views into the project.

Future Work
-----------

 - The analysis was exploratory, and should be redone with proper inferential statistics.
 - What about other tasks than image labeling?
 - What about other platforms than MTurk or even subgroups within MTurk
 - Can the issues with MTurk be ameliorated via algorithms like the Dawid-Skene expectation maximization algorithm?
