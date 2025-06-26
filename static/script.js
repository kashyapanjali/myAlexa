document.getElementById("mic-btn").addEventListener("click", () => {
    document.getElementById("response-text").innerText = "Listening...";
    fetch("/listen", {
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        document.getElementById("response-text").innerText = data.response;
      })
      .catch((err) => {
        document.getElementById("response-text").innerText = "Error!";
      });
  });
  