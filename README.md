# Drawing game with agents

## Functional requirements

- I can add agents with personalities and drawing styles
- Before start the round each agent will imagine a situation (some small text) (Text generation)
- The following process is repeated
	- The topics are randomized and sent to other agents
	- Each agent will draw something with the topic (Text2Image)
	- The images will be randomized and sent to other agents
	- Each agent will describe the situation (Image2Text)
- The frontend will split the screen for every agent
	- Will show what the agent is doing at any given moment
		1 Thought situation
		2 Sitation given and image drawn
		3 Image given, description of the situation
- There is a button to continue each step
	1. Think about a situation
	2. Draw the situation given
	3. Describe the provided image

# Phases
1 Text2Text Project (TextGeneration)
2 Text2Image Project (Drawing)
3 Agents project until step 2. (POC)
4 Image2Text Project (Describing)
5 Continue with step 3.

