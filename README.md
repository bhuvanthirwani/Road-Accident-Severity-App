# Project Setup Guide

**Team Information**
<p><strong>Team Number:</strong> 28</p>
<p><strong>Team Members:</strong></p>
<ul>
    <li><strong>Bhuvan Thirwani</strong> - 50565974</li>
    <li><strong>Harshit Malpani</strong> - 50608809</li>
    <li><strong>Piyush Gulhane</strong> - 50608504</li>
</ul>

**App Features**
<h4>1. Login & Registraion</h4>
<h4>2. Add/Edit/Delete Data for Road Accidents</h4>
<h4>3. Predict Accident Severity</h4>
<h4>4. Dynamic Chart Visualtization from the Dataset</h4>
<h4>5. ML Model Results</h4>
<h4>6. Guidelines</h4>

<h4>Video Link: <a href="https://drive.google.com/file/d/12MUpvx2y0xK9hq_jEnSePjqvCclMPQqi/view?usp=drive_link" target="_blank">Link</a> </h4>
<p>This Instance may go down, if it goes down, I will update this link. Also, /login/ is important as / was not working.</p>

**Setup Instructions**

<h3>1. Download the <code>ml_models.zip</code> File</h3>
<p>First, download the <code>ml_models.zip</code> file from the following URL:</p>
<p><a href="https://drive.google.com/file/d/10cMzD10C5Z5I2Zi-fZYxg8TdpM4yQV5r/view?usp=sharing" target="_blank">Download ml_models.zip</a></p>
<p><strong>Make sure to create a folder called <code>ml_models</code> in your project directory.</strong></p>
<img src="road_accident_severity_app/images/ml_models.png" alt="Step 1: Download and extract ml_models.zip">

<h3>2. Install Dependencies</h3>
<p>After setting up the <code>ml_models</code> folder, open your terminal/command prompt and follow these steps:</p>
<ul>
    <li>Install Poetry (Dependency Manager):</li>
    <pre><code>pip install poetry</code></pre>
    <img src="road_accident_severity_app/images/pip_poetry.jpg" alt="pip_poetry.jpg">
    <li>Install project dependencies (make sure you’re in the directory where <code>poetry.lock</code> exists):</li>
    <pre><code>poetry install</code></pre>
    <img src="road_accident_severity_app/images/poetry_install.jpg" alt="poetry_install.jpg">
</ul>

<h3>3. Activate the Poetry Virtual Environment</h3>
<p>Activate the virtual environment created by Poetry:</p>
<pre><code>poetry shell</code></pre>
<img src="road_accident_severity_app/images/poetry_shell.png" alt="poetry_shell.png">

<h3>4. Run Database Migrations | You should be in road_accident_severity_app folder</h3>
<p>To set up the database, run:</p>
<pre><code>python manage.py migrate</code></pre>
<img src="road_accident_severity_app/images/migrate.png" alt="migrate.png">

<h3>5. Start the Server</h3>
<p>Now, start the development server by running:</p>
<pre><code>python manage.py runserver</code></pre>
<img src="road_accident_severity_app/images/runserver.png" alt="runserver.png">
<hr>

**Register and Login**
<p>Once the server is running, open your browser and go to the URL:</p>
<pre><code>http://127.0.0.1:8000/login/</code></pre>
<p>/login/ is important as / will not going to work

<h3>Register</h3>
<p>First, register a new user by filling in the necessary details in the registration form.</p>

<h3>Login</h3>
<p>After registering, log in using your credentials.</p>

<hr>

**Start Using the Website**
<p>Once logged in, you can start using the website and explore its features.</p>

<hr>

**Troubleshooting**
<p>If you encounter any issues during the setup process, please ensure you’ve followed each step carefully. You can also check the following common issues:</p>
<ul>
    <li>If <code>poetry install</code> doesn’t work, try updating Poetry by running:</li>
    <pre><code>pip install --upgrade poetry</code></pre>
    <li>Make sure that the virtual environment is activated before running server-related commands.</li>
</ul>

<hr>

**Contact**
<p>For any further queries, feel free to reach out to the team members:</p>
<ul>
    <li><strong>Bhuvan Thirwani:</strong> bhuvanth@buffalo.edu</li>
    <li><strong>Harshit Malpani:</strong> hmalpani@buffalo.edu</li>
    <li><strong>Piyush Gulhane:</strong> pgulhane@buffalo.edu</li>
</ul>
</body>
</html>
