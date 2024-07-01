# WiQuiz: a Portfolio Project

This Quiz Application is a web-based platform designed to allow users to take quizzes on various topics. It features a user authentication system, quiz creation, and quiz-taking functionalities. The application is built using Flask for the backend and HTML, CSS, and JavaScript for the frontend.

## Features

- **User Authentication**: Users can sign up, log in, and log out.
- **Quiz Management**: Users can create quizzes and take quizzes created by others.
- **Dynamic Quiz Taking**: Quizzes are taken through a dynamic web interface with immediate feedback.

## Getting Started

### Prerequisites

Before running this application, ensure you have Python and Flask installed on your system. Additionally, you will need a database setup that is compatible with Flask SQLAlchemy.

### Installation

1. Clone the repository to your local machine.
2. Install the required Python packages:

```sh
pip install -r requirements.txt
```

3. Set up your database and update the [`app/config.py`]

4. Run the Flask application:

```sh
python run.py
```

The application will start running on `http://localhost:5000`.

## Usage

- **Home Page**: Accessible to authenticated users to view and take quizzes.
- **Sign Up**: New users can create an account.
- **Log In**: Existing users can log in to access their quizzes.
- **Take Quiz**: Users can take quizzes and receive immediate feedback on their answers.

## File Structure

- `run.py`: Entry point to start the Flask application.
- `routes.py`: Contains the Flask routes for the application's web pages.
- `auth_base.html`: Base HTML template for authentication-related pages.
- `take_quiz.html`: HTML template for the quiz-taking page.
- `take_quiz.js`: JavaScript for handling quiz-taking logic.
- `take_quiz.css`: CSS for styling the quiz-taking page.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.