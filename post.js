async function postTTS() {
    let data = new FormData();

    data.append("model", "tts_models/de/thorsten/vits");
    data.append("emotion", "Angry");
    data.append("speed", "2.0");
    data.append("text", "Hallo aus JavaScript");

    let response = await fetch("http://localhost:8080/tts/SingleSpeaker", {
        method: "GET",
        headers: {
            "Content-Type": "multipart/form-data"
        },
        body: data 
    });

    console.log(response.json());
}

postTTS();