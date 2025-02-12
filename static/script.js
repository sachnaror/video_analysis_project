$(document).ready(() => {
    $("#processVideoBtn").click(async () => {
        let response = await fetch('/process_video/');
        let data = await response.json();
        let taskId = data.task_id;

        $(".progress").removeClass("d-none");

        let interval = setInterval(async () => {
            let progressResponse = await fetch(`/progress/`);
            let progressData = await progressResponse.json();
            let progressValue = progressData.progress;
            let progressStage = progressData.stage;

            $("#progressBar").css("width", progressValue + "%").text(progressValue + "%");
            $("#progressStage").text(progressStage); // ✅ Show current processing step

            if (progressValue >= 100) {
                clearInterval(interval);
                $("#chat-section").removeClass("d-none");  // ✅ Show chat box when done
            }
        }, 3000);
    });


    $("#askBtn").click(async () => {
        let query = $("#userQuery").val().trim();
        let apiKey = sessionStorage.getItem("openai_api_key");

        if (!query) return alert("Please enter a question!");
        if (!apiKey) return alert("Please enter and save your API Key!");

        // ✅ Move user message to chat history immediately
        $("#chatHistory").append(`<div class='chat-message user-message'>${query}</div>`);
        $("#userQuery").val(""); // ✅ Clear input field
        scrollToBottom();

        // ✅ Send request to OpenAI
        let response = await fetch('/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ question: query, api_key: apiKey })
        });

        let data = await response.json();

        // ✅ Display AI response in chat
        $("#chatHistory").append(`<div class='chat-message ai-message'>${data.response}</div>`);
        scrollToBottom();
    });

    // ✅ Auto-scroll function for chat box
    function scrollToBottom() {
        let chatBox = document.getElementById("chatHistory");
        chatBox.scrollTop = chatBox.scrollHeight;
    }

});


