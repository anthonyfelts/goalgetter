const form = document.getElementById("app-form");

function addGoal() {
  const goal = document.getElementById("goal").value;
  console.log(goal);
  form.reset();
}
