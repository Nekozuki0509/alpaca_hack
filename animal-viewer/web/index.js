const express = require('express');

const app = express();
app.use(express.static("public"));

const html = `
<!DOCTYPE html>
<html>
  <body>
    <h1>Animal Viewer</h1>
    <ul>
      <li>
        <a href="/?animal=alpaca">Alpaca</a>
      </li>
      <li>
        <a href="/?animal=bear">Bear</a>
      </li>
      <li>
        <a href="/?animal=cat">Cat</a>
      </li>
      <li>
        <a href="/?animal=dog">Dog</a>
      </li>
      <li>
        <a href="/?animal=elephant">Elephant</a>
      </li>
      <img src="/[ANIMAL].png">
  </body>
</html>
`;

app.get("/", async (req, res) => {
    const animal = req.query.animal || "alpaca";

    // no html tag!
    if (animal.includes("<") || animal.includes(">")) {
        return res.status(400).send("Bad Request");
    }

    const page = html.replace("[ANIMAL]", animal);
    res.send(page);
});

app.listen(3000, () => {
    console.log('Server listening on port 3000');
});