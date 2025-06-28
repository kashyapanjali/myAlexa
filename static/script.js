const micBtn = document.getElementById("mic-btn");
const responseText = document.getElementById("response-text");

// Check if speech recognition is supported
if (!('SpeechRecognition' in window) && !('webkitSpeechRecognition' in window)) {
  responseText.innerText = "Speech recognition not supported in this browser";
  micBtn.style.display = 'none';
} else {
  const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
  let recognizing = false;

  recognition.continuous = false;
  recognition.interimResults = false;
  recognition.lang = "en-US";

  recognition.onstart = function() {
    recognizing = true;
    micBtn.style.background = '#ff4444';
    responseText.innerText = "Listening...";
  };

  recognition.onend = function() {
    recognizing = false;
    micBtn.style.background = '#4CAF50';
  };

  recognition.onerror = function(event) {
    console.error('Speech recognition error:', event.error);
    recognizing = false;
    micBtn.style.background = '#4CAF50';
    responseText.innerText = "Error: " + event.error;
  };

  recognition.onresult = function(event) {
    const transcript = event.results[0][0].transcript;
    responseText.innerText = `You asked: "${transcript}"`;
    
    // Send transcript to backend
    fetch("/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question: transcript })
    })
      .then(res => {
        if (!res.ok) {
          throw new Error(`HTTP error! status: ${res.status}`);
        }
        return res.json();
      })
      .then(data => {
        responseText.innerText = `Anjali says: "${data.answer}"`;
        
        // Speak the answer
        if ('speechSynthesis' in window) {
          // Stop any ongoing speech
          window.speechSynthesis.cancel();
          
          const utterance = new SpeechSynthesisUtterance(data.answer);
          utterance.rate = 0.9; // Slightly slower for better clarity
          utterance.pitch = 1.0;
          utterance.volume = 1.0;
          
          utterance.onstart = function() {
            console.log('Speech synthesis started');
          };
          
          utterance.onend = function() {
            console.log('Speech synthesis ended');
          };
          
          utterance.onerror = function(event) {
            console.error('Speech synthesis error:', event.error);
          };
          
          window.speechSynthesis.speak(utterance);
        } else {
          console.log('Speech synthesis not supported');
        }
      })
      .catch(error => {
        console.error('Fetch error:', error);
        responseText.innerText = "Error: Could not get response from server";
      });
  };

  micBtn.addEventListener("click", () => {
    if (!recognizing) {
      try {
        recognition.start();
      } catch (error) {
        console.error('Error starting recognition:', error);
        responseText.innerText = "Error starting speech recognition";
      }
    }
  });
}
  