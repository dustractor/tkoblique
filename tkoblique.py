import tkinter as tk
import tkinter.ttk as ttk
from random import choice
from textwrap import wrap

data = """(Organic) machinery
A line has two sides
A very small object--Its centre
Abandon desire
Abandon normal instructions
Abandon normal instruments
Accept advice
Accretion
Adding on
Allow an easement
Always first steps
Always give yourself credit for having more than personality
Are there sections?  Consider transitions
Ask people to work against their better judgement
Ask your body
Assemble some of the elements in a group and treat the group
Assemble some of the instruments in a group and treat the group
Balance the consistency principle with the inconsistency principle
Be dirty
Be extravagant
Be less critical
Be less critical more often
Breathe more deeply
Bridges [ ] build [ ] burn
Cascades
Change ambiguities to specifics
Change instrument roles
Change nothing and continue consistently
Change nothing and continue with immaculate consistency
Change specifics to ambiguities
Children's voices [ ] speaking [ ] singing
Cluster analysis
Consider different fading systems
Consider transitions
Consult other sources [ ] promising [ ] unpromising
Convert a melodic element into a rhythmic element
Courage!
Cut a vital connection
Decorate, decorate
Define an area as `safe' and use it as an anchor
Destroy [ ] nothing [ ] the most important thing
Destroy nothing; Destroy the most important thing
Discard an axiom
Disciplined self-indulgence
Disconnect from desire
Discover the recipes you are using and abandon them
Discover your formulas and abandon them
Display your talent
Distort time
Do nothing for as long as possible
Do something boring
Do something sudden, destructive and unpredictable
Do the last thing first
Do the washing up
Do the words need changing?
Do we need holes?
Don't avoid what is easy
Don't be afraid of things because they're easy to do
Don't be frightened of cliches
Don't be frightened to display your talents
Don't break the silence
Don't stress one thing more than another
Emphasize differences
Emphasize repetitions
Emphasize the flaws
Faced with a choice, do both
Feed the recording back out of the medium
Feedback recordings into an acoustic situation
Fill every beat with something
Find a safe part and use it as an anchor
From nothing to more than nothing
Get your neck massaged
Ghost echoes
Give the game away
Give way to your worst impulse
Go outside.  Shut the door.
Go slowly all the way round the outside
Go to an extreme, come part way back
Go to an extreme, move back to a more comfortable place
Honor thy error as a hidden intention
How would someone else do it?
How would you have done it?
Humanize something free of error
Idiot glee
Imagine the music as a moving chain or caterpillar
Imagine the music as a set of disconnected events
Imagine the piece as a set of disconnected events
In total darkness, or in a very large room, very quietly
Infinitesimal gradations
Intentions: credibility of, nobility of, humility of
Into the impossible
Is it finished?
Is something missing?
Is the intonation correct?
Is the style right?
Is the tuning appropriate?
Is there something missing?
It is quite possible
It is simply a matter of work
Just carry on
Left channel, right channel, centre channel
Listen in total darkness, or in a very large room, very quietly
Listen to the quiet voice
Look at a very small object, look at its centre
Look at the order in which you do things
Look closely at the most embarrassing details and amplify them
Lost in useless territory
Lowest common denominator
Lowest common denominator check: single beat, single note, single riff
Magnify the most difficult details
Make a blank valuable by putting it in an exquisite frame
Make a sudden, destructive unpredictable action; incorporate
Make an exhaustive list of everything you might do and do the last thing on the list
Make it more sensual
Make what's perfect more human
Mechanicalize something idiosyncratic
Move towards the unimportant
Mute and continue
Not building a wall but making a brick
Once the search has begun, something will be found
Only a part, not the whole
Only one element of each kind
Openly resist change
Overtly resist change
Put in earplugs
Question the heroic
Remember those quiet evenings
Remove a restriction
Remove ambiguities and convert to specifics
Remove specifics and convert to ambiguities
Repetition is a form of change
Retrace your steps
Reevaluation (a warm feeling)
Reverse
Short circuit
Shut the door and listen from outside
Simple subtraction
Simply a matter of work
Slow preparation, fast execution
Spectrum analysis
State the problem as clearly as possible
Take a break
Take away the elements in order of apparent non-importance
Take away the important parts
Tape your mouth
The inconsistency principle
The most easily forgotten thing is the most important
The tape is now the music
Think [ ] inside the work [ ] outside the work
Think of the radio
Tidy up
Towards the insignificant
Trust in the you of now
Try faking it
Turn it upside down
Twist the spine
Use an old idea
Use an unacceptable colour
Use cliches
Use fewer notes
Use filters
Use something nearby as a model
Use your own ideas
Use `unqualified' people
Voice your suspicions
Water
What are the sections sections of? Imagine a caterpillar moving
What context would look right?
What is the reality of the situation?
What is the simplest solution?
What mistakes did you make last time?
What to increase? What to reduce? What to maintain?
What would your closest friend do?
What wouldn't you do?
When is it for?
Where is the edge?
Which parts can be grouped?
Work at a different speed
Would anyone want it?
You are an engineer
You can only make one dot at a time
You don't have to be ashamed of using your own ideas
Your mistake was a hidden intention
Steal a solution.
Describe the landscape in which this belongs.
What else is this like?
List the qualities it has. List those you'd like.
Instead of changing the thing, change the world around it.
What would make this really successful?
How would you explain this to your parents?
What were the branch points in the evolution of this entity?
Back up a few steps.
What else could you have done?
When is it for?
Who is it for?
What do you do? Now, what do you do best?
First work alone, then work in unusual pairs.
What most recently impressed you?
How is it similar?
What can you learn from it?
What could you take from it?
Take away as much mystery as possible. What is left?""".splitlines()


if __name__ == "__main__":
    app = tk.Tk()
    app.title("Oblique Strategy")
    frame = ttk.Frame(app,padding="100px")
    frame.pack(fill="both",expand=True)
    s = choice(data)
    lines = wrap(s,width=32)
    for line in lines:
        label = ttk.Label(frame,text=line,font=("Arial",72))
        label.pack(fill="both",expand=True)
    app.bind("<Escape>",lambda _:app.quit())
    app.bind("<Control-w>",lambda _:app.quit())
    app.mainloop()
