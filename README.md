# Brazil Soccer Ranking

###  Get the information about Brazilian Soccer League API.

## SUMMARY

1. [Description](#description)
2. [Dependencies](#dependencies)
3. [How To Run?]()
4. [Structure](#structure)
5. [Routes](#routes)
6. [Response](#response)
7. [Faq](#faq)

## Description
My intention with this project is to build an API to get data from web by a process named *web scrapping*. The objective is to get data from the Brazilian Soccer Championship.

Basically it consists of make requests with required data, so our system will try it and get data from internet and response with a JSON. See [response](#response).

This project will make **web scrapping** at ESPN Brasil site. Please copy/paste or rename [.env.example](/.env.example) to [**.env**](/.env) file.

## Dependencies
You need **Python3.12** or over installed or consider to use an alternative version. See [**Faq**](#faq) about Python environments and install it.

Once Python is installed, I recommend to create a python environment to test this project, `.venv`... So just run:

* `pip install -r requirements.txt`
* File: [requirements.txt]()
* There, you can find the whole list of this project dependencies.

## How to Run?
Once dependencies okay and file **.env** found, run the file [**app.py**](/app.py).

## Structure
Here you can find the packages structure of this project.

```text
src/
├──controllers/
├──core/
├──├──web_scrapping/
├──exceptions/
├──routes/
├──service/
├──use_cases/
├──utilities/
.env.example
.gitignore
app.py
LICENSE
README.md
```

## Routes
Base URL: `/api/brazil/soccer`

The response model for each route you can find [here](#response).

> Brazilian Championship Ranking

```
Method: POST
Url: /ranking/{year}
```

## Response
> **Response: Brazilian Championship Racking**
```json
{
  "brazilian_championship_ranking": [
    {
      "position": 1,
      "name": "Team A",
      "points": 9,
      "matches": 3,
      "win": 3,
      "draw": 0,
      "lost": 0,
      "goals_for": 8,
      "goals_against": 2,
      "accuracy": "100"
    }
  ]
}
```

## Faq

<details>
    <summary>How to install a Python alternative version?</summary>
    <p>
        First, install PyEnv, access <a href="https://github.com/pyenv/pyenv" target="_blank">pyenv repository</a> and follow instructions.
    </p>
    <p>
        Once PyEnv installed, just type: <code>pyenv install 3.x.x</code> where 3.x.x represents a version number.
    </p>
    <p>
        Example: <code>pyenv install 3.12</code>
    </p>
    <p>
        Make it global? Type: <code>pyenv global version</code>
    </p>
</details>

<details>
    <summary>
        Create a Python Environment installation for projects?
    </summary>
    <p>
        PyCharm: you can create it using the IDE GUI to generate local python venvs.
    </p>
    <p>
        Command line: <code>python -m venv tutorial-env</code> where "tutorial-env" is it name. By conversion, I suggest you name it as <code>.venv</code>
    </p>
    <p>
        For more information, access the <a href="https://docs.python.org/pt-br/3.12/tutorial/venv.html" target="_blank">documentation</a>.
    </p>
</details>

---
That's all folks!

[Go Back](#brazil-soccer-ranking)
