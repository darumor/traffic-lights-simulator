# Traffic Lights Simulator - README

    https://github.com/darumor/traffic-lights-simulator

## General

* The idea is to create a simulator of crossings with traffic lights and traffic.
* Traffic through the crossings is controlled by the traffic lights. 
* Traffic lights are controlled by a controller that can be replaced and developed independently of the crossing itself.
* The engine tries to maximize the throughput through the network and minimize the waiting time for individual cars (and pedestrians)
* The goal is to find the ultimate traffic light controller, learn bunch of stuff and have fun while doing it.

## Ideas
* Traffic is generated according to some parameters. Real or generated data from past traffic could also be used.
* There could be several crossings
* The engine may use some sensors to gain information about the traffic or it could just be a smart, timer based engine.
* Cars should have speed and acceleration. They should know how to not crash

## Implementation
* Roads and crossings are defined as directed graph data structure.
* Individual cars etc. each have entry points and exit points.
* Path finding algorithm is used to find correct path through the crossing

## Things to optimize
* maximize total throughput of the crossing (all traffic)
* minimize total waiting time
* minimize waiting time of an individual
* equalize waiting time of individuals
* minimize light changing overhead
* prevent starvation of any route
* prepare for sensor malfunction


## Learned so far
* python coding routine
* python testing and project structure
* crossings and traffic lights are no trivial problems


## Random thoughts
