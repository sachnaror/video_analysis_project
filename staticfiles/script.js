$(document).ready(() => {
    let progressSocket, chatSocket;

    // ✅ Connect WebSocket for Progress Updates
    function connectProgressWebSocket() {
        progressSocket = new WebSocket("ws://127.0.0.1:8000/ws/progress/");

        progressSocket.onopen = () => console.log("Progress WebSocket connected.");

        progressSocket.onmessage = (event) => {
            let data = JSON.parse(event.data);
            let progressValue = data.progress;
            let progressStage = data.stage;
            let reportReady = data.report_ready;

            $("#progressBar").css("width", progressValue + "%").text(progressValue + "%");
            $("#progressStage").text(progressStage);

            if (reportReady) {
                $("#downloadReportBtn").attr("href", "/download_report/").removeClass("d-none");
                $("#chat-section").removeClass("d-none");
            }
        };

        progressSocket.onerror = (error) => console.error("WebSocket error:", error);

        progressSocket.onclose = () => {
            console.warn("Progress WebSocket closed. Reconnecting in 3 seconds...");
            setTimeout(connectProgressWebSocket, 3000);
        };
    }

    // ✅ Connect WebSocket for Chat
    function connectChatWebSocket() {
        chatSocket = new WebSocket("ws://127.0.0.1:8000/ws/chat/");

        chatSocket.onopen = () => console.log("Chat WebSocket connected.");

        chatSocket.onmessage = (event) => {
            let data = JSON.parse(event.data);

            if (data.response) {
                $("#chatHistory").append(`<div class='chat-message ai-message'>${data.response}</div>`);
            } else if (data.error) {
                $("#chatHistory").append(`<div class='chat-message ai-message error'>${data.error}</div>`);
            }
            scrollToBottom();
        };

        chatSocket.onclose = () => {
            console.warn("Chat WebSocket closed. Reconnecting in 3 seconds...");
            setTimeout(connectChatWebSocket, 3000);
        };
    }

    // ✅ Ensure WebSocket connections are maintained
    connectProgressWebSocket();
    connectChatWebSocket();

    // ✅ Start Video Processing
    $("#processVideoBtn").click(() => {
        if (progressSocket.readyState === WebSocket.OPEN) {
            progressSocket.send("start_processing");
        } else {
            alert("WebSocket connection is not open. Try again.");
        }
    });

    // ✅ Chat Functionality Fix
    $("#askBtn").click(() => {
        let query = $("#userQuery").val().trim();
        let apiKey = sessionStorage.getItem("openai_api_key");

        if (!query) {
            alert("Please enter a question!");
            return;
        }
        if (!apiKey) {
            alert("Please enter and save your API Key!");
            return;
        }

        $("#chatHistory").append(`<div class='chat-message user-message'>${query}</div>`);
        $("#userQuery").val(""); // ✅ Clear input field
        scrollToBottom();

        if (chatSocket.readyState === WebSocket.OPEN) {
            chatSocket.send(JSON.stringify({ question: query, api_key: apiKey }));
        } else {
            alert("Chat WebSocket connection is not open. Try again.");
        }
    });

    // ✅ Auto-scroll function for chat box
    function scrollToBottom() {
        let chatBox = document.getElementById("chatHistory");
        setTimeout(() => {
            chatBox.scrollTop = chatBox.scrollHeight;
        }, 100);
    }
});
