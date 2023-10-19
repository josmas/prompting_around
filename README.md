# Prompting Around...

## Overview

Welcome to "Prompting Around," an exploratory playground for prompting Language Models, including both OpenAI and local models. 

## Installation
This project is built with the [Poetry](https://python-poetry.org/) dependency management tool to simplify package management. Also this means that you don't need to worry about virtual environments as poetry will take care of it too.

### Pre-requisities
Given that you have a python version of 3.11+, the easiest way to install poetry is with ```pip install poetry```.

Other options are homebrew for mac or via binary.


### Getting started
To get started with "Prompting Around," follow these steps:

Consider forking the project first!

1. Clone the repository to your local machine:

    ```git clone https://github.com/YOUR_USERNAME/Prompting-Around.git```


2. Navigate to the project directory:

    ```cd prompting-around```


3. Install project dependencies using Poetry:

    ```poetry install```


4. Activate the virtual environment created by Poetry:

    ```poetry shell```


To exit the sheel simply type `exit`.

If you would like to use dotenv to set constants such as API keys, copy `sample.env` into `.env` and add your keys in the newly copied file.

## Database Operations

This project uses SQLAlchemy to connect to a postgreSQL database. The DB can be configured in the .env file (copied from sample.env). Alembic is used to manage databse changes and migrations.

### Setting up the DB
After cloning this repo and adding your database configuration to your .env file, simply run the `upgrade DB` command as follows:

```
poetry run python revision.py "Add created_at column to all tables"
```

### DB Migrations
You can modify the alembic.ini file directly to add your DB setings, but it is not recommended. There are two python scripts, namely revision.py and upgrade.py that will read the configuration from dotenv and call the revision and upgrade Alembic commands for you, based on the env values. Revision also autogenerates the migration script. This is the usage:

For revision, pass a message to autogenerate the script:

```
poetry run python revision.py "Add created_at column to all tables"
```

For upgrade, simply call the script:

```
poetry run python upgrade.py
```


Make sur you use `poetry` so that the virtual environment is used correctly.
When making changes to the DB, these two operations should alwyas be run, in this order; first run revision to auto-generate a migration script, then run the actual upgrade.

## Running Tests

To run tests for the project, you can use the following command:

    pytest

This will execute the test suite and provide feedback on the project's functionality and code quality.

## Logging and monitoring with aimos
If you want to use [AimOS](https://github.com/aimhubio/aimos) for observability, it can be initialized by running the following command in the root folder:

    aimos init

This will create a folder at `.aim` to store all the needed artefacts.

To run the AimOS server type:  ```aimos server```.

To run the AimOS UI and navigate to the provided URL after typing: ```aimos ui```.

The langchain debugging system will contain a `trace` for each time you run and log a completion or chat message.

## Initial sample files
There are two initial samples that use AimOS, so make sure you either set it up correctly or modify the samples before running them.

Note that these files are written to be executed as cells like a Jupyter notebook. If you use [VSCodium](https://vscodium.com/) make sure to install the Jupyter extension.

[langchain_openai.py](./src/samples/langchain_openai.py) shows an example of how to use langchain with OpenAI and store the debugging information in AimOS.

[langchain_ollama.py](./src/samples/langchain_ollama.py) shows the same example but this time using an local model through [Ollama](https://www.ollama.ai/). In this case it uses the `mistral` model, but it is just a matter of changing the name when initializing the model. The debugging information is also stored in AimOS.

## Contributing

We welcome contributions to "Prompting Around"! If you'd like to contribute, please follow these steps:

1. Fork the repository on GitHub.

2. Clone your forked repository to your local machine.

3. Create a new branch for your feature or bug fix:

    ```git checkout -b feature-name```

4. Make your changes and commit them to your branch.

5. Push your branch to your GitHub repository:

    ```git push origin feature-name```


6. Create a pull request from your branch to the main project repository on GitHub. Be sure to include a clear description of your changes.

7. Your pull request will be reviewed, and once approved, your changes will be merged into the project.

Please ensure that your contributions adhere to the project's coding standards and practices.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
