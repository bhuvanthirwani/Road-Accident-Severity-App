# Project Setup Guide

**Team Information**
<p><strong>Team Number:</strong> 28</p>
<p><strong>Team Members:</strong></p>
<ul>
    <li><strong>Bhuvan Thirwani</strong> - 50565974</li>
    <li><strong>Harshit Malpani</strong> - 50608809</li>
    <li><strong>Piyush Gulhane</strong> - 50608504</li>
</ul>

<h3>1. Live Demo Link: <a href="http://34.70.177.116:8000/login/" target="_blank">http://34.70.177.116:8000/login/</a> </h3>
<p>This Instance may go down, if it goes down, I will update this link.</p>
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
    <li>Install project dependencies (make sure you’re in the directory where <code>poetry.lock</code> exists):</li>
    <pre><code>poetry install</code></pre>
</ul>

<h3>3. Activate the Poetry Virtual Environment</h3>
<p>Activate the virtual environment created by Poetry:</p>
<pre><code>poetry shell</code></pre>

<h3>4. Run Database Migrations</h3>
<p>To set up the database, run:</p>
<pre><code>python manage.py migrate</code></pre>

<h3>5. Start the Server</h3>
<p>Now, start the development server by running:</p>
<pre><code>python manage.py runserver</code></pre>

<hr>

**Register and Login**
<p>Once the server is running, open your browser and go to the URL:</p>
<pre><code>http://127.0.0.1:8000/</code></pre>

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
