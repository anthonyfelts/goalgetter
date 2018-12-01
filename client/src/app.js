const form = document.getElementById("app-form");

function addGoal() {
  const goal = document.getElementById("goal").value;
  console.log("new goal: " + goal);
  form.reset();
}
