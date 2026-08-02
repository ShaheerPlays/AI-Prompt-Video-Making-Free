// AI Studio Main JavaScript

import API from "../api/config.js";


// Generate AI Video

async function generateVideo(prompt, settings){

    try{

        const response = await fetch(
            API.getURL(API.GENERATE_VIDEO),
            {
                method:"POST",

                headers:{
                    "Content-Type":"application/json"
                },

                body:JSON.stringify({

                    prompt:prompt,

                    settings:settings

                })

            }
        );


        const data = await response.json();


        return data;


    }

    catch(error){

        console.error(
            "Video generation error:",
            error
        );


        return {

            status:"error",

            message:"Could not connect to server"

        };

    }

}



// Enhance Prompt

async function enhancePrompt(prompt){


    const response = await fetch(

        API.getURL(API.ENHANCE_PROMPT),

        {

            method:"POST",

            headers:{

                "Content-Type":"application/json"

            },

            body:JSON.stringify({

                prompt:prompt

            })

        }

    );


    return await response.json();


}




// Image To Video

async function imageToVideo(image, settings){


    const response = await fetch(

        API.getURL(API.IMAGE_TO_VIDEO),

        {

            method:"POST",

            body:image

        }

    );


    return await response.json();


}




// Voice Generation

async function generateVoice(text, voice){


    const response = await fetch(

        API.getURL(API.VOICE),

        {

            method:"POST",

            headers:{

                "Content-Type":"application/json"

            },

            body:JSON.stringify({

                text:text,

                voice:voice

            })

        }

    );


    return await response.json();


}




// Export functions

window.AIStudio = {

    generateVideo,

    enhancePrompt,

    imageToVideo,

    generateVoice

};
