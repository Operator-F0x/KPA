<p>
<img align = 'right' src="https://i.imgur.com/J1h1OAg.png"></img>
</p>

<h1>KPA</h1>

<h4>Project to create an automatic keepass database to import and automate the checking of many entries.</h4>


-------
- import csv files or other keepass databases and check and removing duplicates
- automatically set up groups for new entries based on the referrer URL of the new entry
-------

<h4>in the future i plan to expand this project when i have time with the following functions.</h4>

- Other methods of importing passwords other than just csv files

--------

<h5>🚩 Study project 🚩</5> 
<h6>
I divided the project into modules
for my easy code reuse and because i need to figure out how to create a single object to manage the database 😅
and keep the various modules external to the keepass management in the Toolbox folder,
i know i could just use the pykeepass library to manage the database,
but my goal is to have an automated database that only checks the contents of the cvs folder or other future import methods
and consequently check for duplicates by saving the new entries in the appropriate groups and I want to create my own object that performs this task
</h6>

--------

![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/Daniele-Polizzi/KPA)
