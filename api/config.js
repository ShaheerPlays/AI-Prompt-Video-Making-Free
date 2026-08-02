// AI Studio API Configuration

const API = {

    // Change this when you deploy your backend
    // Example: "https://your-server.com"
    BASE_URL: "http://localhost:8000",


    // API Endpoints

    GENERATE_VIDEO: "/api/generate",

    ENHANCE_PROMPT: "/api/enhance",

    IMAGE_TO_VIDEO: "/api/image-to-video",

    EDIT_VIDEO: "/api/edit",

    SUBTITLES: "/api/subtitles",

    VOICE: "/api/voice",


    // Helper function
    getURL(endpoint){

        return this.BASE_URL + endpoint;

    }

};


export default API;
