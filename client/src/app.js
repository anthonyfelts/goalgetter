const form = document.getElementById("app-form");
const result = document.getElementById("result");

document.onkeypress = function(e) {
  var keyCode = e.keyCode;
  if (keyCode == 13) {
    pressedEnter = true;
    addGoal();
    keyCode = 0;
  }
};

function addGoal() {
  const goal = document.getElementById("title").value;
  const list = document.createElement("p");
  const text = document.createTextNode(goal);
  list.appendChild(text);
  result.appendChild(list);
  form.reset();
}
