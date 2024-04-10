# Database Practices Repository

This repository is dedicated to showcasing best practices for integrating SQL commands into Python scripts to compile data and generate HTML reports. It utilizes a combination of HTML, Python, and SQL to achieve this integration efficiently.

## Table of Contents

1. [Introduction](#introduction)
2. [Setup](#setup)
3. [Usage](#usage)
4. [Contributing](#contributing)
5. [License](#license)

## Introduction

Managing and reporting data stored in databases often involves executing SQL commands and generating reports to present the data in a meaningful way. This repository demonstrates how to leverage Python to execute SQL commands and generate HTML reports automatically.

## Setup

To use the scripts in this repository, follow these steps:

1. Clone the repository to your local machine:

```
git clone https://github.com/your_username/database-practices.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Ensure you have a database set up and accessible, and update the `config.py` file with your database credentials.

## Usage

After completing the setup, you can use the scripts in this repository as follows:

1. Write SQL queries in separate `.sql` files located in the `sql/` directory.

2. Use Python scripts located in the `scripts/` directory to execute the SQL commands and generate HTML reports.

3. Execute the Python scripts, passing the SQL file as an argument.

Example:

```bash
python execute_sql.py sql/query.sql
```

4. The script will execute the SQL commands and generate an HTML report containing the results. The HTML file will be saved in the `reports/` directory.

## Contributing

Contributions to improve the practices demonstrated in this repository are welcome! If you have suggestions for improvements, please feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify the code as needed.
