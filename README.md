# Author: vinod Kanwar
#Roll No:G23AI2009


# Dockerized Wordle Game

## Overview

This project demonstrates how to dockerize a simple Python-based Wordle game. The Wordle game is a word-guessing game where the player has to guess a hidden word by suggesting letters within a limited number of attempts. This example provides a practical introduction to containerizing a Python application using Docker and Docker Compose.

## Application Description

The Wordle game is a simple console-based application. The game selects a random word from a predefined list, and the player tries to guess the word one letter at a time. The player has a limited number of attempts to guess the word correctly. After each guess, the game displays the current state of the word with correctly guessed letters revealed and the remaining attempts.

## Project Files

- `wordle.py`: The main Python script containing the Wordle game logic.
- `Dockerfile`: The Dockerfile used to create a Docker image for the Wordle game.
- `requirements.txt`: An empty file as the Wordle game has no external dependencies.
- `docker-compose.yml`: The Docker Compose file to build and run the Docker container.

## Getting Started

### Prerequisites

To run this project, you need to have the following installed:

- Docker
- Docker Compose

### Running the Application on Gitpod

Note- my system does not support docker due to some constrains hence i used Gitpod to create and run the docker.

1. **Create a GitHub Repository**: Create a new GitHub repository and add the project files (`wordle.py`, `Dockerfile`, `requirements.txt`, and `docker-compose.yml`) to the repository.

2. **Open the Repository in Gitpod**:
   - Go to [Gitpod](https://gitpod.io/) and start a new session.
   - Open your repository in Gitpod by appending the GitHub repository URL to the Gitpod URL. 
     ```
    https://github.com/G23AI2009/docker/tree/main
     ```

3. **Create the Necessary Files**:
   - In the Gitpod editor, create and edit the following files.

4. **Build and run docker**

    -To build the docker: docker-compose build
    -Run the Docker container: docker-compose up


5.**Access the Running Container**
    Open a new terminal.
    List running containers to find the container ID of your running Wordle game: docker ps
    Use the docker exec command to open a bash shell in the running container : docker exec -it wordle_game bash

6.once inside the container's bash shell, you can start the game by running the Python script: python wordle.py
