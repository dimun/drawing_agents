# Docker

docker run -it --rm -v /home/diego/personal-apps/drawing_agents/text_generation/models:/app/models -p 4000:80 diegomunozc/transformers:latest 

# Running locally

uvicorn app.main:app --proxy-headers --host localhost --port 4000 --reload


# Valid prompts

- You have to write 10 sentences for the cards of a drawing game. 1. ''A book over the bed'' 2.''Two cats stretching over the kitchen''
- You have to write 10 sentences for the cards of a drawing game. * ''A book over the bed'' * ''Two cats stretching over the kitchen''
- Generate creative and vivid phrases for a drawing game. Each prompt should inspire a visual representation. Examples of prompts include:
"A mouse on a skateboard"
"A castle in the clouds"
"A forest with talking animals"
Please ensure that each prompt is clear and concise, allowing participants to easily envision the scene or object they are expected to draw. Your answer should be placed after the three points ...
