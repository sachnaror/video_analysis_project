$(document).ready(() => {
    let socket;

    function connectWebSocket() {
        socket = new WebSocket("ws://127.0.0.1:8000/ws/progress/");

        socket.onopen = () => {
            console.log("WebSocket connected.");
        };

        socket.onmessage = (event) => {
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

        socket.onerror = (error) => {
            console.error("WebSocket error:", error);
        };

        socket.onclose = () => {
            console.warn("WebSocket closed. Reconnecting in 3 seconds...");
            setTimeout(connectWebSocket, 3000);
        };
    }

    connectWebSocket();  // ✅ Ensure WebSocket always stays connected

    $("#processVideoBtn").click(() => {
        if (socket.readyState === WebSocket.OPEN) {
            socket.send("start_processing");  // ✅ Start WebSocket communication
        } else {
            alert("WebSocket connection is not open. Try again.");
        }
    });

    // ✅ Chat Functionality Fix
    $("#askBtn").click(async () => {
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

        // ✅ Move user message to chat history immediately
        $("#chatHistory").append(`<div class='chat-message user-message'>${query}</div>`);
        $("#userQuery").val(""); // ✅ Clear input field
        scrollToBottom();

        try {
            let response = await fetch('/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ question: query, api_key: apiKey })
            });

            if (!response.ok) throw new Error("Error getting AI response");

            let data = await response.json();

            // ✅ Display AI response in chat
            $("#chatHistory").append(`<div class='chat-message ai-message'>${data.response}</div>`);
            scrollToBottom();
        } catch (error) {
            console.error("Chat error:", error);
            $("#chatHistory").append(`<div class='chat-message ai-message error'>Error fetching response. Try again.</div>`);
        }
    });

    // ✅ Auto-scroll function for chat box
    function scrollToBottom() {
        let chatBox = document.getElementById("chatHistory");
        setTimeout(() => {
            chatBox.scrollTop = chatBox.scrollHeight;
        }, 100);  // ✅ Ensures smooth scrolling
    }
});
$(document).ready(() => {
    let chatSocket = new WebSocket("ws://127.0.0.1:8000/ws/chat/");

    chatSocket.onopen = () => {
        console.log("Chat WebSocket connected.");
    };

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
        setTimeout(() => {
            chatSocket = new WebSocket("ws://127.0.0.1:8000/ws/chat/");
        }, 3000);
    };

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

        chatSocket.send(JSON.stringify({ question: query, api_key: apiKey }));
    });

    function scrollToBottom() {
        let chatBox = document.getElementById("chatHistory");
        setTimeout(() => {
            chatBox.scrollTop = chatBox.scrollHeight;
        }, 100);
    }
});
