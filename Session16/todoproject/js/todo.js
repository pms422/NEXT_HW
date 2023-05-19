const todoForm = document.getElementById("todo-form");
const todoList = document.getElementById("todo-list");
const submitBtn = document.getElementById(".submitBtn");
let TODOList = [];

todoForm.addEventListener("submit", submitAddTodo);

function submitAddTodo(event) {
  event.preventDefault();
  const content = document.getElementById("content");
  const newTodo = { text: content.value, id: Date.now() };
  TODOList.push(newTodo);

  window.localStorage.setItem("todo", JSON.stringify(TODOList));

  content.value = "";
  paintTodo(newTodo);
}

let TOdo = JSON.parse(localStorage.getItem("todo"));

if (TOdo !== null) {
  TODOList = TOdo;
  TODOList.forEach((todo) => paintTodo(todo));
}

function paintTodo(newTodo) {
  const li = document.createElement("li");
  li.id = newTodo.id;
  const span = document.createElement("span");
  const button = document.createElement("button");

  button.innerText = "취소";
  button.addEventListener("click", deleteTodo);

  span.innerText = newTodo.text;

  li.appendChild(span);
  li.appendChild(button);
  todoList.appendChild(li);
}

function deleteTodo(event) {
  const li = event.target.parentElement;
  li.remove();
  TODOList = TODOList.filter((todo) => todo.id !== parseInt(li.id));

  window.localStorage.setItem("todo", JSON.stringify(TODOList));
}

function saveTodos(e) {
  window.localStorage.setItem(todos, JSON.stringify(e));
}
