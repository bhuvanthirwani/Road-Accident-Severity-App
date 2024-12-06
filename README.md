<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project Setup Guide</title>
</head>
<body>
    <h1>Project Setup Guide</h1>

    <h2>Team Information</h2>
    <p><strong>Team Number:</strong> 28</p>
    <p><strong>Team Members:</strong></p>
    <ul>
        <li><strong>Bhuvan Thirwani</strong> - 50565974</li>
        <li><strong>Harshit Malpani</strong> - 50608809</li>
        <li><strong>Piyush Gulhane</strong> - 50608504</li>
    </ul>

    <h2>Setup Instructions</h2>

    <h3>1. Download the <code>ml_models.zip</code> File</h3>
    <p>First, download the <code>ml_models.zip</code> file from the following URL:</p>
    <p><a href="https://www.google.drive.com/fgd/gsdgsdgsdgs" target="_blank">Download ml_models.zip</a></p>
    <p><strong>Make sure to create a folder called <code>ml_models</code> in your project directory.</strong></p>
    <img src="https://via.placeholder.com/150" alt="Step 1: Download and extract ml_models.zip">

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

    <h2>Register and Login</h2>
    <p>Once the server is running, open your browser and go to the URL:</p>
    <pre><code>http://127.0.0.1:8000/</code></pre>

    <h3>Register</h3>
    <p>First, register a new user by filling in the necessary details in the registration form.</p>

    <h3>Login</h3>
    <p>After registering, log in using your credentials.</p>

    <hr>

    <h2>Start Using the Website</h2>
    <p>Once logged in, you can start using the website and explore its features.</p>

    <hr>

    <h2>Troubleshooting</h2>
    <p>If you encounter any issues during the setup process, please ensure you’ve followed each step carefully. You can also check the following common issues:</p>
    <ul>
        <li>If <code>poetry install</code> doesn’t work, try updating Poetry by running:</li>
        <pre><code>pip install --upgrade poetry</code></pre>
        <li>Make sure that the virtual environment is activated before running server-related commands.</li>
    </ul>

    <hr>

    <h2>Contact</h2>
    <p>For any further queries, feel free to reach out to the team members:</p>
    <ul>
        <li><strong>Bhuvan Thirwani:</strong> bhuvanth@buffalo.edu</li>
        <li><strong>Harshit Malpani:</strong> hmalpani@buffalo.edu</li>
        <li><strong>Piyush Gulhane:</strong> pgulhane@buffalo.edu</li>
    </ul>
</body>
</html>
