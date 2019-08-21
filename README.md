# QuizApp
A skill test for job at AppliedAI Consulting

## Assignment

- You need to write python code so that someone can take the quiz/MCQ from the attached quiz.json file. When the code is run on command line, it should print the two groups, sport and math. User can select any one group, then it should print the question, with its options and let user provide an answer.
After answering all the questions, final result should be printed.

- Once this Python code is ready, you also need to create docker image using Dockerfile for the code and you also need to upload image into Docker Hub.

## Building

```
git clone https://github.com/NP-compete/QuizApp code

cd code

python main.py
```

## Docker

### Manual

```
git clone https://github.com/NP-compete/QuizApp code

cd code

docker build -t <some name> .

docker run -it <some name>
```

### Single Line

```
docker run -it sohamdutta0109/quizapp
```
