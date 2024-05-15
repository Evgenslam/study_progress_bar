# Progress Bar Project for Japanese Language Learning
## Overview
The Progress Bar project facilitates Japanese language learning by providing customizable progress bars for students. Each student has an account where they can view progress bars representing textbooks and their respective lessons. The project is built using Django, JavaScript, and HTML.

## Features
- Customizable Progress Bars: Students can view progress bars representing textbooks and their associated lessons. The sections (lessons) are predefined by the teacher.
- Toggle Completion: Students can mark sections (lessons) as completed or incomplete with a simple click, allowing them to track their progress through each textbook.
- Detailed Tracking: Students can log additional details such as homework, study dates, and personal notes for each lesson, providing a comprehensive overview of their learning journey.

## Future Development
Planned features for future development include:
- Homework Tracking: Integration of a homework tracking feature to help students manage their assignments more effectively.
- Date of Study: Adding the ability for students to log the dates they studied each lesson to monitor their study habits.
- Lesson Summaries: Allowing students to write summaries or reflections on each lesson for better understanding and revision.
- Teacher Interaction: Incorporating features for teacher-student interaction, such as submitting questions or requests for clarification to teachers and receiving feedback.

## Getting Started
To get started with the Progress Bar project:

- Sign Up: Create a student account to access personalized progress bars.
- View Progress Bars: Log in to view progress bars representing textbooks and their associated lessons.
- Track Progress: Mark sections as completed or incomplete and log additional details for each lesson.


## Starting locally
- git clone
- python -m venv venv
- pip install -r requirements.txt
- fill lesson_data folder with csv files, each file representing textbook and containing names of lessons. Use bookmarks_extractor if neccessary
- populate db by running in order: populate_users (make sure to have correct list of students in the same file), import_lessons, cross_poopulate

Feedback and contributions to the Progress Bar project are welcome. Please feel free to submit any suggestions or bug reports. 