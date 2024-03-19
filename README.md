# World Aquatics Swim Fantasy Game: Single Day Lineup Optimizer

## Introduction

The World Aquatics Swim Fantasy Game is held each time that there is a World Aquatics championship (most recently Doha in February 2024, next up is Budapest in December 2024). This game runs throughout the meet, with there being a gameday each day of the meet.

The player chooses four male and four female swimmers, each with a price that is related to how good they are and how many events they are in, while staying under the budget of 200 stars. One swimmer is also chosen to be captain for the day, doubling their points for that day.

At the end of the gameday, each swimmer gets a number of points based on any of their individual semi-final or final performances on that day. The player who has the most points from their team of 8 swimmers wins that gameday.

## Description

This program is designed to take data about all of the swimmers and their projected points and costs for a given day of the World Aquatics Swim Fantasy Game, and then formulate and solve an integer program to find the optimal lineup to maximize points for that day of the game.

This is done by using python's linear solver from OR-Tools, with data imported from text files. The data in the text files in generated in Excel, where all of the raw data about the swimmers is easier to comb through and visualize.

It was hard to create all of the variables and constraints at runtime, so that feature of the code is still being developed, which will ultimately make it easier to run the program for different days of the game, when there are different swimmers that will being swimming, and all of the projected points are different.

## Using the Solver

1. Download the two python files and text file and place them in the same folder
2. Run `Swim Fantasy LP.py` to see an example output of the solver (optional)
3. Run `Swim Fantasy LP Day 2.py` and enter `example.txt` when prompted for an input file

## Understanding the Output

`Swim Fantasy LP Day 2.py`, when ran properly, will display the chosen number of lineups (the default is set at 10 if the choose_num_lineups variable isn't changed to True). This is in the form of the constraint that it adds to the linear program before the next iteration of the program, so the eight variables in the constraint represent the eight swimmers that make up that lineup.

The number to the right of the lineup is the projected points of that lineup, and the number to the left of each lineup in parentheses is the actual points scored by that lineup (if it's a previous gameday that the program is being tested on). The number on the final line of the output is the highest number out of all of the actual points scored values from all of the lineups listed.

## Future Direction

The next step be making another option for the solver to optimize lineups for the overall competition. This will mean making one big integer program where there are decision variables on whether or not to choose each swimmer for each day of the meet, with all of the same constraints as the single day integer program, along with a constraint for the number of swimmer switches that can be done throughout the whole meet.

## More Information

* [World Aquatics Swim Fantasy Game](https://swimming-fantasygame.com/#/welcome/login)
* [Swimming Points Formula](https://www.worldaquatics.com/swimming/points)
* [Swimming World Records](https://resources.fina.org/fina/document/2024/01/08/c535f50f-d3e7-4f56-8580-59e8c9ca28de/World-Aquatics-Points-Base-times-SCM-2023-and-LCM-2024.pdf)
