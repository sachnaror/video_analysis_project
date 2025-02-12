$(document).ready(() => {
    $("#processVideoBtn").click(async () => {
        let response = await fetch('/process_video/');
        let data = await response.json();
        let taskId = data.task_id;

        $(".progress").removeClass("d-none");

        // Polling progress every 2 seconds
        let interval = setInterval(async () => {
            let progressResponse = await fetch(`/progress/`);
            let progressData = await progressResponse.json();
            let progressValue = progressData.progress;

            $("#progressBar").css("width", progressValue + "%").text(progressValue + "%");

            if (progressValue >= 100) {
                clearInterval(interval);
                $("#chat-section").removeClass("d-none");  // Show chat when done
            }
        }, 2000);
    });
});
