# Python Command Django-React project setup

## Description

This resource allows you to automatically setup a basic template for Django-React project just typing a simple command.

The need of this small tool comes from the need to stop wasting time on setting up every Django-React project from scratch, and at the same time, brings better features for the development process.

Only a single React project can take 200 MB of space, by creating it with `npx create-react-app` command. Caused by the `react-scripts` which seems to add a huge amount of bloat libraries. If `react-scripts` is substituted by `webpack` library and their derivates, the project can be reduced to 50 MB size.

While development, the frontend from Django is substitued by React, which behaves as normal being able to refresh using webpack. And Django is just limited to work as backend.

Let's say we want to upload your Django project, then you just need to run the webpack build to convert all the react project as a single javascript file which will be used by a Django html file. This way, the project will run entirely on Django, and can be hosted in sites like PythonAnywhere.

<br>


- Standard library modules used:
 - sys : build in module to manage specific parameters and function from the system.

 - pathlib : build-in module to manage file paths as objects.

 - shutil : build-in module to manage  high level operations like copy files or directories.

 - os : build-in module used as interface of the operative system.

 - webbrowser : build-in module that provides high-level interface to manage a browser.

 - json : build-in module to read and write json files.

- Framework libraries used:
 - Django 3.2.6 : Popular framework to easily create secure websites with their own database included.

- Project was made entirely in Python and tested on (platform).

## Setup

- Clone the repository anywhere in your local machine.

- Change the location directory name to something like `dj-rc`

- Create a new system variable from envirorment variables named : PYTHONPATH

- Add the directory to PYTHONPATH to allow python have access to the module globally by using:
  ```
  python -m module_name
  ```

- Create another folder where you want to create the React project.

- Open the terminal inside this new folder and type:
  ```
  python -m dj-rc
  ```

  **By default it will scope for local npm libraries and use npm as package manager.**

- Wait until everything is set and a browser window will be open.

## Setup Troubles
- If you want to use the `--scope=global`, make sure to install the next requirements:

  ```
  npm i -g react react-dom react-router-dom
  
  npm i -g @babel/core @babel/preset-env @babel/preset-react @babel/core @babel/preset-env @babel/preset-react
  
  npm i -g webpack webpack-cli webpack-dev-server html-webpack-plugin
  
  npm i -g babel-loader css-loader style-loader sass sass-loader file-loader
  ```
  if you want to use the `--pkg_mgr=pnpm` then change the requirement commands from npm to pnpm.
  
  PNPM will be much faster and less error verbose while setting up the project.

## Arguments:

- scope :
  - --scope=global ( default )
  - --scope=local
<br><br>
- pkg_mgr ( package manager ) :
  - --pkg_mgr=npm ( default )
  - --pkg_mgr=pnpm

## What I learned from this project

- The value of taking some time to automate repetitive tasks, which could easily take 15 minutes to setup everytime.

## Future Work
<!-- - ~~Done Task~~ ✅ -->
- Add common components that use Hooks as example.
- Implement generic useContext to the Navigation Bar.
- Add backend requests from react frontend.