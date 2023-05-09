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

Study project 
<h5>
I have broken down the project into modules,
for my reuse of the facilitated code and because I have to understand how to create a single object 😅
to manage the database and keep the various modules external to the keepass management in the Toolbox folder,
I could just use the Pykeepass library to manage the database,
but my goal is to have an automated database that simply checks the contents of the cvs folder or future other import methods
and consequently checks for duplicates by saving new entries into the appropriate groups
</h5>
--------
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/Daniele-Polizzi/KPA)
