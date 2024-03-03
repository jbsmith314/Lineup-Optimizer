# World Aquatics Swim Fantasy Game: Single Day Lineup Optimizer

## Introduction

The World Aquatics Swim Fantasy Game is held each time that there is a World Aquatics championship (most recently Doha in February 2024, next up is Budapest in December 2024). This game runs throughout the meet, with there being a gameday each day of the meet. The player chooses four male and four female swimmers, each with a price that is related to how good they are and how many events they are in, while staying under the budget of 200 stars. At the end of the gameday, each swimmer gets a number of points based on any of their individual semi-final or final performances on that day. The player who has the most points from their team of 8 swimmers wins that gameday.

## Description

This program is designed to take data about all of the swimmers and their projected points and costs for a given day of the World Aquatics Swim Fantasy Game, and then formulate and solve an integer program to find the optimal lineup to maximize points for that day of the game.

This is done by using python's linear solver from OR-Tools, with data imported from text files. The data in the text files in generated in Excel, where all of the raw data about the swimmers is easier to comb through and visualize.

It was hard to create all of the variables and constraints at runtime, so that feature of the code is still being developed, which will ultimately make it easier to run the program for different days of the game, when there are different swimmers that will being swimming, and all of the projected points are different.

## More Information

* [World Aquatics Swim Fantasy Game](https://swimming-fantasygame.com/#/welcome/login)
* [Swimming Points Formula](https://www.worldaquatics.com/swimming/points)
* [Swimming World Records](https://resources.fina.org/fina/document/2024/01/08/c535f50f-d3e7-4f56-8580-59e8c9ca28de/World-Aquatics-Points-Base-times-SCM-2023-and-LCM-2024.pdf)
