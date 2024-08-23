function handleCredentialResponse(response) {
     //console.log("Encoded JWT ID token: " + response.credential);
    sendDjango(response);
  }
  
  window.onload = function () {
    google.accounts.id.initialize({
      client_id: GOOGLE_CLIENT_ID,
      callback: handleCredentialResponse
    });
    google.accounts.id.renderButton(
      document.getElementById("buttonDiv"),
      { theme: "filled_black", size: "large", shape: "pill" }  // customization attributes
    );
    google.accounts.id.prompt(); // also display the One Tap dialog
  }
  
  function sendDjango(response) {
    var id_token = response.credential;
  
    fetch('/google/', {

      // POST
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        id_token: id_token
      }),
    })
    .then((res) => res.json())
    .then((data) => {
      // console.log(data); NEVER USE IN PRODUCTION
      if (data.status === 'ok') {
        window.alert("Logado com sucesso!");
        window.location.href = "/home";
      } else {
        console.error('login falied:', data.error);
      }
    })
    .catch((err) => console.error('request error:', err));
  }
  