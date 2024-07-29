# Information Management System

This is a basic Information Management System developed using Python and MongoDB. The system allows you to perform CRUD (Create, Read, Update, Delete) operations on faculties, courses, and students collections in a MongoDB database.

## Features

- **Faculties Management**
  - List all faculty details
  - Add a new faculty
  - Remove an existing faculty
  - Find a faculty by name

- **Courses Management**
  - List all course details
  - Add a new course
  - Remove an existing course
  - Find a course by course code

- **Students Management**
  - List all student details
  - Add a new student
  - Remove an existing student
  - Find a student by enrollment number

## Requirements

- Python 3.6 or above
- MongoDB
- Required Python packages (install using `pip`):
  - `pymongo`
  - `prettytable`
  - `textwrap`

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/sahilahmad6569/information-management-system.git
    cd information-management-system
    ```

2. **Install the required packages**:
    ```sh
    pip install pymongo prettytable
    ```

3. **Ensure MongoDB is running** on your local machine.

## Usage

1. **Run the script**:
    ```sh
    python main.py
    ```

2. **Follow the on-screen menu** to perform operations on the database.

## Code Overview

- **Database Connection**:
  ```python
  from pymongo import MongoClient
  client = MongoClient(serverSelectionTimeoutMS=5000)
  db = client['bca']
  faculties_collection = db['faculties']
  courses_collection = db['courses']
  students_collection = db['students']
  ```

- **CRUD Operations**:
  - Functions to list, add, remove, and find faculties, courses, and students.

- **Menu Functions**:
  - `main_menu()`: Main menu for the system.
  - `faculties_menu()`: Menu for faculties operations.
  - `courses_menu()`: Menu for courses operations.
  - `students_menu()`: Menu for students operations.

## Example

Here's an example of adding a new faculty:

```sh
Enter your choice: 1
1. List all faculties details
2. Add a new faculty
3. Remove an existing faculty
4. Find faculty by name
5. Previous Menu
Enter your choice: 2
Enter the name of the faculty: John Doe
Enter the post: Professor
Enter the email: john.doe@example.com
Enter the expertise: Computer Science
Enter the courses taught: CS101, CS102
Faculty added successfully!
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## Contact

If you have any questions or feedback, feel free to contact me at sahilahmad6569@gmail.com.