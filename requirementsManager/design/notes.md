# Overview
This document is the scratch pad for analyzing and planning the appropriate design for the Requirements Manager CSCI. It is modeled using a Software Design Description (SDD) template; however, this document is not an SDD, but rather it could be used in the generation of an SDD.

# Design Decisions
## Programming Language
Python has been identified as the desired language to implement the Requirements Manager CSCI in due to the small scale of the application along with the abilitiy to rapidly implement and test the application. In addition, python provides several native libraries for parsing text data which will serve to reduce the overal effort required to implement the Requirements Manager CSCI.

# Architectural Patterns
## Layered Architecture
At least initially, an open Layered Architecture has been chosen until further analysis has been completed. The open Layered Architecutre provides a monolithic software application structure that is simple, flexible and able to be adapted to another pattern at a later date if the need should arise.

## Event Based Architecutre
This architectural style is not desireable due to the applicaiton being executed synchronously. The benifits of using an Event Based Architecture do not apply to this CSCI.

## Monolithic Architecture
The Requirements Manager CSCI will most likely mix aspects of this architectural style with the Layered Architecture to allow for flexibility in the future.

## Microkernel Architecture
It is possible that the CSCI eventually evolves into this pattern, or more specifically into an application that supports different plugins to add additional capabilities. However, for the time being the Microkernel Architecture seems like overkill.

## Microservices Architecture
The Microservices Architecture seems like overkill for the Requirements Manager Tool. This CSCI is currently not intended to be in a distributed environment. 
