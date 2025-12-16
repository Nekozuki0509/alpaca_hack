from flask import Flask, request
from pathlib import Path
import subprocess

app = Flask(__name__)


@app.get("/")
def index():
    return """
<head>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/simpledotcss/2.3.7/simple.min.css" integrity="sha512-taVA0VISClRMNshgWnlrG4lcEYSjwpgpI8vaoT0zGoPf9c74DA95SXMngcgjaWTrEsUbKmfKqmQ7toiXNc2l+A==" crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>
<body>
  <main>
    <h1>cat🐈</h1>
    <form action="/" method="get">
      <input name="file" placeholder="app.py" required>
      <button type="submit">Read</button>
    <form>
    <pre><code id="code"></code></pre>
  </main>
  <script>
    const file = new URLSearchParams(location.search).get("file");
    if (file) {
      fetch("/cat?file=" + encodeURIComponent(file))
        .then((r) => r.text())
        .then((text) => document.getElementById("code").textContent = text);
    }
  </script>
</body>
    """.strip()


@app.get("/cat")
def cat():
    file = request.args.get("file", "app.py")
    if not Path(file).exists():
        return "🚫"
    if "flag" in file:
        return "🚩"

    return subprocess.run(
        ["cat", file],
        capture_output=True,
        timeout=1,
        stdin=open("flag.txt"),  # !!
    ).stdout.decode()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
