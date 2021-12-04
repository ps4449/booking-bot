<!-- INTRODUCTION -->
<div align="center">
  <h1>Booking.com Assistant</h1>
  <img src="https://media.istockphoto.com/vectors/cute-robot-vector-id1191411962?k=20&m=1191411962&s=612x612&w=0&h=sDV5muSvtgaWJ7rNdAcb4aLQQlIkQnQaONn47aPqSKs=" width=250 height=250>

  An automated bot that provides listings for bookings on the website <code>www.booking.com</code>.<br>
  <a href="#explore"><strong>Explore the implementation »</strong></a>
  <br>
  <br>
  <a href="#">View Demo</a>
  ·
  <a href="#">Report Bug</a>
  ·
  <a href="#">Request Feature</a>
</div>

<!-- TABLE OF CONTENTS -->
<details open="open" id="explore">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#introduction">Introduction</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
      <a href="#about">About the Bot</a>
      <ul>
        <li><a href="#overview">Overview</a></li>
        <li><a href="#execution">Execution</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#further-work">Further Work</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
<h2 id="introduction">Introduction</h2>
To understand automation, its usage in testing and effectiveness with time, Booking.com Assistant was created to automate the hotel-booking process to accommodate for people's travel. This project is entirely built with <code>python [ver 3.9]</code>.<br>

<!-- GETTING STARTED -->
<h2 id="getting-started">Getting Started</h2>

<!-- PREREQUISITES -->
<h3>Prerequisites</h3>
<h4>System</h4>
<ul>
  <li>OS: Windows 10</li>
  <li>Code Editor: <a href="https://code.visualstudio.com/download">VS Code</a> or <a href="https://www.jetbrains.com/pycharm/download/#section=windows">PyCharm</a></li>
</ul>
<h4>Software</h4>
<ul>
  <li>Chrome Webdriver</li>
  <li>Python 3.9 Interpreter</li>
</ul>
<h4>Packages</h4>
<ul>
  <li>For the automation: <code>selenium</code></li>
  <li>For CLI printing (python): <code>prettytable</code></li>
</ul>

<!-- INSTALLATION -->
<h3>Installation</h3>
<ul>
  <li>Install the requirements file using <code>pip install -r requirements.txt</code></li>
  <li>Find the Chrome Webdriver <a href="https://chromedriver.chromium.org/downloads">here</a>. (download the version most compatible with your browser version)</li>
  <li>Please make sure to check the versions of all the packages mentioned, since some packages may not work on recent releases.</li>
</ul>

<!-- ABOUT THE BOT -->
<h2 id="about">About the Bot</h2>

<!-- OVERVIEW -->
<h3 id="overview">Overview</h3>
<code>www.booking.com</code> is one of the largest online hotel booking facilitators in the world. On this website, I have learned to execute selenium-based automation along with python as my base language. This program takes in the city as location, along with the duration and the number of adults, and searches deals for the given location.<br>
<br>

This program automates on a Chrome browser. Selenium uses a framework called Web Driver, which allows us to execute tests across various browsers. Web Driver makes it possible to write a test script in Linux and run it in Windows, all by setting one variable correctly. There are multiple programming languages which are supported by Web Driver such as Java, Python, Ruby, .Net, PHP to create test scripts.<br>

<!-- EXECUTION -->
<h3 id="execution">Execution</h3>
For smooth execution of the script, all you need to do is set the <code>PATH</code> variable to direct to the path of the directory which stores your webdriver.<br>

<h4>For Webdrivers:</h4>
<ul>
  <li>For Windows: <code>setx PATH "%PATH%;C:\webdriver-location-here\"</code></li>
  <li>For macOs and Linux: <code>export PATH=$PATH:/webdriver-location-here >> ~/.profile</code></li>
</ul>

<!-- CONTRIBUTING -->
<h2 id="contributing">Contributing</h2>
Projects are made successful and more efficient due to the contribution of many developers worldwide. The spirit of open source is greatly appreciated, and you are encouraged to make any valid contributions to fix a bug or add an appropriate feature. 

<ul>
  <li><h4>Rules</h4>
    Read <a href="https://github.com/ps4449/booking-bot/blob/main/CONTRIBUTING.md">CONRIBUTING.md</a> before submitting a pull request.</li>
  <li><h4>File Structure</h4>
    Go through our directory structure to get a better idea about performing and commiting changes.
    <pre>
      |   main.py
      |   README.md
      |   CONTRIBUTING.md
      |   requirements.txt
      |   
      +---.idea
      |   [many config files]
      |           
      +---Bot
      |   |   booking.py
      |   |   booking_filtration.py
      |   |   booking_report.py
      |   |   constants.py
      |   |   __init__.py
      |   |   
      |   \---__pycache__
      |           [many cache files here]
      |           
      \---help
              pip_show.png
              refactoring_html.png
              terminal_output.txt
              tree.txt
    </pre>
    Most of the contributions will be made in the <code>Bot</code> directory or <code>main.py</code> file. The <code>help</code> directory contains some resources that helped me figure out the project.</li>
</ul>

<!-- FURTHER WORK -->
<h2 id="further-work">Further Work</h2>
<ul>
  <li>To make the CLI execution more detailed</li>
  <li>To authorize login from CLI</li>
  <li>To add a sorting feature according to stars and prices</li>
  <li>To provide top 5 deals for every search based on price, rating</li>
  <li>Add <code>lxml</code> functionality to clean the html entities such as <code>(amphersant)nbsp</code>
</ul>

<!-- LICENSE -->
<h2 id="License">License</h2>
THE WORK (AS DEFINED BELOW) IS PROVIDED UNDER THE TERMS OF THIS CREATIVE COMMONS PUBLIC LICENSE ("CCPL" OR "LICENSE"). THE WORK IS PROTECTED BY COPYRIGHT AND/OR OTHER APPLICABLE LAW. ANY USE OF THE WORK OTHER THAN AS AUTHORIZED UNDER THIS LICENSE OR COPYRIGHT LAW IS PROHIBITED.<br>
<br>
BY EXERCISING ANY RIGHTS TO THE WORK PROVIDED HERE, YOU ACCEPT AND AGREE TO BE BOUND BY THE TERMS OF THIS LICENSE. TO THE EXTENT THIS LICENSE MAY BE CONSIDERED TO BE A CONTRACT, THE LICENSOR GRANTS YOU THE RIGHTS CONTAINED HERE IN CONSIDERATION OF YOUR ACCEPTANCE OF SUCH TERMS AND CONDITIONS.<br>
<br>
<b>Note: Read the <a href="https://creativecommons.org/licenses/by-nc/3.0/legalcode">terms and conditions</a> of the Creatives Commons License.</b>
