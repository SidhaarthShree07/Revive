//registration form submission
document
  .getElementById("registration-form")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    // Perform AJAX request to register endpoint
    // Replace the following code with appropriate AJAX request
    var form = new FormData(this);
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/register", true);
    xhr.onload = function () {
      if (xhr.status === 200) {
        window.location.href = "/dashboard";
      }
    };
    xhr.send(form);
  });

// handling symptoms form submission
document
  .getElementById("symptoms-form")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    // Perform AJAX request to symptoms endpoint
    // Replace the following code with appropriate AJAX request
    var form = new FormData(this);
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/symptoms", true);
    xhr.onload = function () {
      if (xhr.status === 200) {
        var response = JSON.parse(xhr.responseText);
        document.getElementById("treatment-result").innerText =
          response.treatment;
      }
    };
    xhr.send(form);
  });

// handling chat form submission
document
  .getElementById("chat-form")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    // Perform AJAX request to chat endpoint
    // Replace the following code with appropriate AJAX request
    var form = new FormData(this);
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/chat", true);
    xhr.onload = function () {
      if (xhr.status === 200) {
        var response = JSON.parse(xhr.responseText);
        var messageElement = document.createElement("p");
        messageElement.innerText = response.message;
        document.getElementById("chat-messages").appendChild(messageElement);
      }
    };
    xhr.send(form);
  });
