function addTask() {
    let input = document.getElementById("taskInput");
    let taskText = input.value.trim();
    if (taskText === "") return;
    
    let li = document.createElement("li");
    let span = document.createElement("span");
    span.textContent = taskText;
    
    let completeButton = document.createElement("button");
    completeButton.textContent = "✔";
    completeButton.onclick = function() {
        span.classList.toggle("completed");
    };
    
    let removeButton = document.createElement("button");
    removeButton.textContent = "❌";
    removeButton.onclick = function() {
        li.remove();
    };
    
    li.appendChild(span);
    li.appendChild(completeButton);
    li.appendChild(removeButton);
    document.getElementById("taskList").appendChild(li);
    
    input.value = "";
}