This is a toy simulation for playing around with the Monty Hall problem - a famous problem in statistics. The problem is as follows:

>_You are a contestant on a gameshow. In front of you on the stage, there are three doors. The gameshow host informs you that behind one door, there is a car. The other two doors conceal goats. You get to choose a door, and you get to take home whatever prize happens to be behind it._

>_You are permitted to choose a door. After you have chosen a door, but before it is opened, the host opens a second door, different from the one you chose, revealing a goat. The host then gives you the opportunity to see what behind the door you chose, or to switch your choice, and instead open the door that neither you nor the host chose._

As it turns out, you have a much better chance of winning the car if you switch your choice to the third door. How much better? Well, let's run this simulation and find out!

Once cloned, the program should run on any version of python above 3.6. To run it in the default configuration, open your terminal of choice, navigate to the repository, and run:

```> python3 monty-hall.py```

Here's an example of the output:

```
====================
Strategy is: switch.
won 658/1000 games, or 65.8000%
====================
====================
Strategy is: stick.
won 328/1000 games, or 32.8000%
====================
```

As it turns out, your chance of winning a car approximately doubles when you switch doors!

You can also adjust a variety of parameters, including:
- The number of doors
- The number of doors that the host reveals to you
- The number of iterations to run
- The number of prizes spread among the doors
- The strategy to use (switching to the other door, or sticking to your original choice)
- The random number seed

The result of this problem is highly counterintuitive to most people. To help illustrate the mechanism at play, sometimes an alternative version of the scenario is sketched.

>_Suppose that instead of just three doors, there were a million doors, with all but one of those doors concealing a goat. After you pick a door, the host then rapidly opens 999,998 doors, each one revealing a goat, leaving only two doors closed: the one you chose, and one additional door. In this situation, should you switch?_

Let's use the optional parameters exposed by this program to find out!

(to be completed later)
