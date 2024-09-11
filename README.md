# LearningApp

## Project Name
LearningApp

## Description
This project is a Tkinter-based application designed for managing profiles, vocabulary, and practice sessions. It allows users to create and manage profiles, add and delete words, and engage in various language learning activities. The application also supports text creation, text-to-speech functionalities, and generating practice questions based on user input.

## Features
- **Profile Management**: Create, choose, and delete user profiles.
- **Vocabulary Management**: Add, revise, and delete vocabulary words.
- **Practice Sessions**: Engage in practice sessions with generated texts and questions.
- **Text Creation**: Create custom texts using specified vocabulary.
- **Text-to-Speech**: Convert text to speech using external libraries.
- **Dynamic User Interface**: Switch between different views for managing profiles, vocabulary, and practice activities.

## Usage

### Running the Application
To run the application, use the following command:
```bash
python run.py

 ## Profile Management
-   Create a new profile using the profile management view.
Choose an existing profile to start working with.
Delete unwanted profiles through the profile management interface.
Vocabulary Management
Add new words to your profile.
Revise and delete vocabulary words as needed.
Practice Sessions
Start practice sessions to learn new words or revise existing ones.
Use the text creation feature to generate practice texts based on specific vocabulary.
Engage in interactive text-based tasks and receive feedback.
Classes
ProfileManager: Handles profile creation, selection, and deletion.
WordsManager: Manages vocabulary words, including adding, revising, and deleting words.
PracticeManager: Facilitates practice sessions by generating texts, questions, and handling text-to-speech functionality.
WhatToDoToday: Manages daily tasks by adding and updating profiles in a JSON file, rotating tasks daily, and retrieving today's task. It ensures tasks are cycled and updated, facilitating effective daily task management.
WordsManager: Handles word translation and management, including adding and retrieving translated words, tracking daily additions, and revising words based on learning progress. It integrates Google Translate for translations and manages CSV data for efficient vocabulary learning and tracking.
Libraries
json: For handling JSON data.
datetime: For working with dates and times.
google.cloud.translate_v2: For accessing the Google Translate API.
os: For interacting with the operating system.
csv: For working with CSV files.