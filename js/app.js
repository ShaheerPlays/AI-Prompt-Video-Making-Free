// ===============================
// AI Video Studio - app.js
// ===============================

console.log("AI Video Studio Loaded");

// -------------------------------
// Progress Bar
// -------------------------------

function startProgress(barId = "progressBar") {

    const bar = document.getElementById(barId);

    if (!bar) return;

    let progress = 0;

    bar.style.width = "0%";

    const timer = setInterval(() => {

        progress += Math.random() * 8;

        if (progress >= 100) {

            progress = 100;
            clearInterval(timer);

        }

        bar.style.width = progress + "%";

    }, 300);

}

// -------------------------------
// Image Preview
// -------------------------------

function previewImages(inputId, previewId) {

    const input = document.getElementById(inputId);
    const preview = document.getElementById(previewId);

    if (!input || !preview) return;

    preview.innerHTML = "";

    Array.from(input.files).forEach(file => {

        const reader = new FileReader();

        reader.onload = function(e){

            const img = document.createElement("img");

            img.src = e.target.result;

            img.style.width = "180px";
            img.style.margin = "10px";
            img.style.borderRadius = "12px";

            preview.appendChild(img);

        };

        reader.readAsDataURL(file);

    });

}

// -------------------------------
// Video Preview
// -------------------------------

function previewVideo(inputId, videoId){

    const input = document.getElementById(inputId);
    const video = document.getElementById(videoId);

    if(!input || !video) return;

    const file = input.files[0];

    if(file){

        video.src = URL.createObjectURL(file);

        video.style.display = "block";

    }

}

// -------------------------------
// Save Prompt History
// -------------------------------

function savePrompt(prompt){

    let history =
        JSON.parse(localStorage.getItem("promptHistory")) || [];

    history.unshift(prompt);

    history = history.slice(0,20);

    localStorage.setItem(
        "promptHistory",
        JSON.stringify(history)
    );

}

// -------------------------------
// Load Prompt History
// -------------------------------

function loadPromptHistory(){

    return JSON.parse(
        localStorage.getItem("promptHistory")
    ) || [];

}

// -------------------------------
// Fake AI Generation
// -------------------------------

function generateVideo(){

    const prompt =
        document.getElementById("prompt");

    if(prompt){

        if(prompt.value.trim()===""){

            alert("Please enter a prompt.");

            return;

        }

        savePrompt(prompt.value);

    }

    startProgress();

    setTimeout(()=>{

        alert("Later this will call your backend AI.");

    },4000);

}

// -------------------------------
// Dark Mode
// -------------------------------

function toggleDarkMode(){

    document.body.classList.toggle("light");

}

// -------------------------------
// Notification
// -------------------------------

function notify(message){

    alert(message);

}
