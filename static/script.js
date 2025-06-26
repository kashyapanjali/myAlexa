const micBtn = document.getElementById("mic-btn");
const responseText = document.getElementById("response-text");

const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
let recognizing = false;

recognition.onstart = function() {
  recognizing = true;
  responseText.innerText = "Listening...";
};

recognition.onend = function() {
  recognizing = false;
};

recognition.onresult = function(event) {
  const transcript = event.results[0][0].transcript;
  responseText.innerText = "Processing...";
  // Send transcript to backend
  fetch("/ask", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question: transcript })
  })
    .then(res => res.json())
    .then(data => {
      responseText.innerText = data.answer;
      // Speak the answer
      const utterance = new SpeechSynthesisUtterance(data.answer);
      window.speechSynthesis.speak(utterance);
    })
    .catch(() => {
      responseText.innerText = "Error!";
    });
};

micBtn.addEventListener("click", () => {
  if (!recognizing) {
    recognition.start();
  }
});
  