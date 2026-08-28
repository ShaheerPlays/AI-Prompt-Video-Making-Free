<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta
name="viewport"
content="width=device-width, initial-scale=1.0"

>

<title>Generate AI Video | AI Studio</title>

<link
    href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap"
    rel="stylesheet"
>

<style>

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: Poppins, sans-serif;
}

body {
    background: #070B14;
    color: white;
    overflow-x: hidden;
}

header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 40px;
    background: #111827;
    border-bottom: 1px solid rgba(255,255,255,.08);
    position: sticky;
    top: 0;
    z-index: 100;
}

.logo {
    font-size: 32px;
    font-weight: bold;
    color: #00D4FF;
}

nav {
    display: flex;
    gap: 15px;
}

nav a {
    color: white;
    text-decoration: none;
    padding: 10px 18px;
    border-radius: 10px;
    transition: .3s;
}

nav a:hover {
    background: #00D4FF;
    color: black;
}

.container {
    max-width: 1400px;
    margin: auto;
    padding: 40px;
}

.title {
    font-size: 45px;
    font-weight: bold;
    margin-bottom: 10px;
}

.subtitle {
    color: #bfc8d8;
    margin-bottom: 35px;
}

.grid {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 30px;
}

.left,
.right {
    background: #111827;
    padding: 25px;
    border-radius: 20px;
}

label {
    display: block;
    margin-top: 18px;
    margin-bottom: 8px;
    font-weight: 600;
}

textarea {
    width: 100%;
    height: 220px;
    padding: 18px;
    background: #1F2937;
    border: none;
    border-radius: 15px;
    color: white;
    resize: vertical;
    font-size: 15px;
    outline: none;
}

textarea::placeholder {
    color: #94a3b8;
}

select,
input[type="file"] {
    width: 100%;
    padding: 15px;
    margin-top: 8px;
    background: #1F2937;
    border: none;
    border-radius: 12px;
    color: white;
    font-size: 15px;
}

button {
    width: 100%;
    padding: 18px;
    margin-top: 20px;
    border: none;
    border-radius: 15px;
    background: #00D4FF;
    color: black;
    font-size: 18px;
    font-weight: bold;
    cursor: pointer;
    transition: .3s;
}

button:hover:not(:disabled) {
    transform: translateY(-3px);
}

button:disabled {
    opacity: .6;
    cursor: not-allowed;
}

.option {
    margin-top: 20px;
    padding: 18px;
    background: #1F2937;
    border-radius: 15px;
}

.option p {
    color: #bfc8d8;
    margin-top: 6px;
}

.preview {
    margin-top: 25px;
    min-height: 250px;
    background: #1F2937;
    border-radius: 15px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 22px;
    color: #7dd3fc;
    overflow: hidden;
    text-align: center;
    padding: 20px;
}

.preview video {
    width: 100%;
    max-height: 500px;
    border-radius: 12px;
}

.progress {
    margin-top: 25px;
    height: 16px;
    background: #333;
    border-radius: 20px;
    overflow: hidden;
}

.progress-bar {
    width: 0%;
    height: 100%;
    background: linear-gradient(
        90deg,
        #00D4FF,
        #7C3AED
    );
    transition: width .4s ease;
}

.status-success {
    color: #4ade80;
}

.status-error {
    color: #f87171;
}

.status-working {
    color: #7dd3fc;
}

@media (max-width: 900px) {

    header {
        padding: 15px 20px;
        flex-direction: column;
        gap: 15px;
    }

    nav {
        flex-wrap: wrap;
        justify-content: center;
    }

    .container {
        padding: 20px;
    }

    .title {
        font-size: 32px;
    }

    .grid {
        grid-template-columns: 1fr;
    }

}

</style>

</head>

<body>

<header>

<div class="logo">
AI Studio
</div>

<nav>

<a href="dashboard.html">Dashboard</a>

<a href="projects.html">Projects</a>

<a href="settings.html">Settings</a>

<a href="profile.html">Profile</a>

</nav>

</header>

<div class="container">

<h1 class="title">
🎥 AI Video Generator
</h1>

<p class="subtitle">
Generate professional AI videos using text prompts.
</p>

<div class="grid">

<!-- LEFT SIDE -->

<div class="left">

<label>
Describe your video
</label>

<textarea
    id="prompt"
    placeholder="Example: A cinematic documentary about Venus with realistic space scenes, dramatic lighting and smooth camera movement..."
></textarea>

<label>
Upload Images (Optional)
</label>

<input
id="imageUpload"
type="file"
accept="image/*"
multiple

>

<label>
Video Resolution
</label>

<select id="resolution">

<option value="720p">
720P
</option>

<option
    value="1080p"
    selected
>
1080P
</option>

</select>

<label>
Video Duration
</label>

<select id="duration">

<option value="30 Seconds">
30 Seconds
</option>

<option value="1 Minute">
1 Minute
</option>

<option value="5 Minutes">
5 Minutes
</option>

<option value="10 Minutes">
10 Minutes
</option>

<option value="20 Minutes">
20 Minutes
</option>

<option value="30 Minutes">
30 Minutes
</option>

</select>

<label>
AI Voice
</label>

<select id="voice">

<option>
Male - English
</option>

<option>
Female - English
</option>

<option>
Male - Urdu
</option>

<option>
Female - Urdu
</option>

<option>
Male - Hindi
</option>

<option>
Female - Hindi
</option>

</select>

<label>
Language
</label>

<select id="language">

<option>
English
</option>

<option>
Urdu
</option>

<option>
Hindi
</option>

<option>
Arabic
</option>

<option>
Spanish
</option>

<option>
French
</option>

</select>

<div class="option">

<h3>
🤖 Gemini AI
</h3>

<p>
Improve your prompt using Gemini AI before generating the video.
</p>

<button
id="enhanceButton"
onclick="enhancePrompt()"

>

✨ Enhance Prompt

</button>

</div>

<div class="option">

<h3>
🎵 Background Music
</h3>

<select id="music">

<option>
No Music
</option>

<option>
Cinematic
</option>

<option>
Documentary
</option>

<option>
Adventure
</option>

<option>
Technology
</option>

<option>
Nature
</option>

</select>

</div>

<div class="option">

<h3>
📝 Automatic Subtitles
</h3>

<label>

<input
id="subtitles"
type="checkbox"
checked

>

Enable AI Subtitles

</label>

</div>

<button
id="generateButton"
onclick="generateVideo()"

>

🚀 Generate AI Video

</button>

<div class="progress">

<div
    class="progress-bar"
    id="progressBar"
></div>

</div>

</div>

<!-- RIGHT SIDE -->

<div class="right">

<h2>
Preview
</h2>

<div
    class="preview"
    id="preview"
>

🎬<br>
Your AI Video Preview

</div>

<div class="option">

<h3>
Generation Status
</h3>

<p
    id="status"
    class="status-working"
>

Waiting for prompt...

</p>

</div>

<div class="option">

<h3>
Export
</h3>

<button
id="downloadButton"
disabled

>

📥 Download MP4

</button>

</div>

</div>

</div>

</div>

<script>


/* =========================================================
   BACKEND URL

   If frontend and FastAPI backend are on the same domain,
   leave this as an empty string.

   Example for local testing:
   const API_BASE = "http://127.0.0.1:8000";
========================================================= */

const API_BASE = "";


/* =========================================================
   ELEMENTS
========================================================= */

const promptInput =
    document.getElementById("prompt");

const enhanceButton =
    document.getElementById("enhanceButton");

const generateButton =
    document.getElementById("generateButton");

const progressBar =
    document.getElementById("progressBar");

const statusElement =
    document.getElementById("status");

const preview =
    document.getElementById("preview");

const downloadButton =
    document.getElementById("downloadButton");

const resolutionSelect =
    document.getElementById("resolution");


let currentVideoUrl = null;


/* =========================================================
   UPDATE STATUS
========================================================= */

function setStatus(
    message,
    type = "working"
) {

    statusElement.textContent =
        message;

    statusElement.className =
        "status-" + type;

}


/* =========================================================
   ENHANCE PROMPT WITH GEMINI
========================================================= */

async function enhancePrompt() {

    const originalPrompt =
        promptInput.value.trim();


    if (!originalPrompt) {

        alert(
            "Please enter a prompt first."
        );

        return;

    }


    enhanceButton.disabled = true;

    enhanceButton.textContent =
        "✨ Enhancing...";


    setStatus(
        "Gemini is improving your prompt...",
        "working"
    );


    try {

        const response =
            await fetch(
                `${API_BASE}/api/enhance-prompt`,
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({

                        prompt:
                            originalPrompt

                    })

                }
            );


        const data =
            await response.json();


        if (!response.ok) {

            throw new Error(

                data.detail ||
                "Failed to enhance prompt."

            );

        }


        if (
            !data.enhanced_prompt
        ) {

            throw new Error(
                "No enhanced prompt was returned."
            );

        }


        promptInput.value =
            data.enhanced_prompt;


        setStatus(
            "✅ Prompt enhanced successfully!",
            "success"
        );


    }

    catch (error) {

        console.error(error);


        setStatus(
            "❌ " + error.message,
            "error"
        );


        alert(
            "Prompt enhancement failed: " +
            error.message
        );

    }

    finally {

        enhanceButton.disabled =
            false;

        enhanceButton.textContent =
            "✨ Enhance Prompt";

    }

}


/* =========================================================
   GENERATE VIDEO
========================================================= */

async function generateVideo() {

    const prompt =
        promptInput.value.trim();


    if (!prompt) {

        alert(
            "Please enter a video prompt first."
        );

        return;

    }


    generateButton.disabled =
        true;


    generateButton.textContent =
        "⏳ Starting...";


    progressBar.style.width =
        "5%";


    downloadButton.disabled =
        true;


    currentVideoUrl =
        null;


    preview.innerHTML =
        "🎬<br>Preparing AI video generation...";


    setStatus(
        "Starting video generation...",
        "working"
    );


    try {


        const response =
            await fetch(
                `${API_BASE}/api/generate`,
                {

                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({

                        prompt:
                            prompt,

                        aspect_ratio:
                            "16:9",

                        resolution:
                            resolutionSelect.value

                    })

                }
            );


        const data =
            await response.json();


        if (!response.ok) {

            throw new Error(

                data.detail ||
                "Failed to start video generation."

            );

        }


        if (!data.job_id) {

            throw new Error(
                "No generation job ID received."
            );

        }


        generateButton.textContent =
            "🎥 Generating...";


        setStatus(
            "AI video generation started...",
            "working"
        );


        await checkVideoStatus(
            data.job_id
        );


    }

    catch (error) {

        console.error(error);


        progressBar.style.width =
            "0%";


        setStatus(
            "❌ " + error.message,
            "error"
        );


        preview.innerHTML =
            "❌<br>Video generation failed";


        generateButton.disabled =
            false;


        generateButton.textContent =
            "🚀 Generate AI Video";

    }

}


/* =========================================================
   CHECK VIDEO GENERATION STATUS
========================================================= */

async function checkVideoStatus(
    jobId
) {

    let fakeProgress = 10;


    const interval =
        setInterval(
            function() {

                if (
                    fakeProgress < 90
                ) {

                    fakeProgress +=
                        Math.random() * 3;

                    progressBar.style.width =
                        fakeProgress + "%";

                }

            },

            2000
        );


    try {

        while (true) {


            const response =
                await fetch(
                    `${API_BASE}/api/generate/${jobId}`
                );


            const data =
                await response.json();


            if (!response.ok) {

                throw new Error(

                    data.detail ||
                    "Could not check video status."

                );

            }


            setStatus(

                data.message ||
                "Generating AI video...",

                data.status === "failed"
                    ? "error"
                    : "working"

            );


            if (
                data.status === "completed"
            ) {


                clearInterval(
                    interval
                );


                progressBar.style.width =
                    "100%";


                currentVideoUrl =
                    `${API_BASE}${data.video_url}`;


                preview.innerHTML =

                    `<video
                        controls
                        autoplay
                        playsinline
                    >
                        <source
                            src="${currentVideoUrl}"
                            type="video/mp4"
                        >
                        Your browser does not support video playback.
                    </video>`;


                setStatus(
                    "✅ Video generated successfully!",
                    "success"
                );


                downloadButton.disabled =
                    false;


                downloadButton.onclick =
                    function() {

                        downloadVideo(
                            currentVideoUrl
                        );

                    };


                generateButton.disabled =
                    false;


                generateButton.textContent =
                    "🚀 Generate AI Video";


                return;

            }


            if (
                data.status === "failed"
            ) {


                clearInterval(
                    interval
                );


                throw new Error(

                    data.message ||
                    "Video generation failed."

                );

            }


            await new Promise(

                resolve =>

                    setTimeout(
                        resolve,
                        5000
                    )

            );

        }

    }

    catch (error) {


        clearInterval(
            interval
        );


        progressBar.style.width =
            "0%";


        setStatus(
            "❌ " + error.message,
            "error"
        );


        preview.innerHTML =
            "❌<br>Video generation failed";


        generateButton.disabled =
            false;


        generateButton.textContent =
            "🚀 Generate AI Video";

    }

}


/* =========================================================
   DOWNLOAD VIDEO
========================================================= */

function downloadVideo(
    url
) {

    const link =
        document.createElement("a");


    link.href =
        url;


    link.download =
        "ai-studio-video.mp4";


    document.body.appendChild(
        link
    );


    link.click();


    document.body.removeChild(
        link
    );

}


</script>

</body>

</html>
