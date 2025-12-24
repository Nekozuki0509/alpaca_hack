from flask import Flask, request
import sqlite3
import os

FLAG = os.environ.get("FLAG", "Alpaca{____________________________REDACTED____________________________}")
assert len(FLAG) == 72
FLAG_1, FLAG_2, FLAG_3 = FLAG[:24], FLAG[24:48], FLAG[48:]

app = Flask(__name__)


@app.get("/")
def index():
    return """
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://unpkg.com/sakura.css/css/sakura.css" type="text/css" /></head>
<body>
  <main>
    <h1>Xmas Login 🦙🦌🎅</h1>
    <p> There are three users: alpaca, reindeer and santa_claus_admin. </p>
    <form id="login-form">
      <label for="username">Username</label>
      <input name="username" placeholder="alpaca" maxlength="12" required>
      <label for="password">Password</label>
      <input name="password" placeholder="" maxlength="48" required>
      <button type="submit" id="login-btn">Login</button>
    </form>
    <h6>Executed SQL:</h6>
    <pre><code id="sql"></code></pre>
    <h6>Response:</h6>
    <pre><code id="code"></code></pre>
  </main>
  <script>
    document.getElementById("login-form").onsubmit = async (e) => {
      e.preventDefault();
      const form = e.target;
      const formData = new FormData(form);
      const response = await fetch("/login", {
        method: "POST",
        body: formData,
      });
      const text = await response.text();
      document.getElementById("sql").textContent = `SELECT * FROM users WHERE username='${formData.get("username")}' AND password='${formData.get("password")}';`;
      document.getElementById("code").textContent = text;
    };
  </script>
</body>
    """.strip()


@app.post("/login")
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    if len(username) > 12 or len(password) > 48:
        return "Your input is too long!"

    conn = sqlite3.connect("database.db")
    query = (
        f"SELECT * FROM users WHERE username='{username}' AND password='{password}';"
    )

    error = None
    try:
        user = conn.execute(query).fetchone()
    except sqlite3.Error as e:
        user = None
        error = str(e)
    conn.close()

    if error:
        return f"SQL error: {error}"

    if user is None:
        return "invalid credentials"

    if user[0] == "alpaca":
        return f"Hello, alpaca! Here is your flag: {FLAG_1}"
    elif user[0] == "reindeer":
        return f"Hello, reindeer! Here is your flag: {FLAG_2}"
    elif user[0] == "santa_claus_admin":
        return f"Hello, santa_claus_admin! Here is your flag: {FLAG_3}"
    else:
        return f"Hello, {user[0]}!"


def init_db():
    conn = sqlite3.connect("database.db")
    conn.execute(
        """
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL
    );
    """
    )
    password_1, password_2, password_3 = (
        os.urandom(16).hex(),
        os.urandom(16).hex(),
        os.urandom(16).hex(),
    )
    conn.execute(
        f"""INSERT OR IGNORE INTO users (username, password) VALUES
        ('alpaca', '{password_1}'),
        ('reindeer', '{password_2}'),
        ('santa_claus_admin', '{password_3}');
    """
    )
    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=3000)
