document.addEventListener("DOMContentLoaded", function() {
    $(".lesson").click(function() {
        const lessonId = $(this).data("lesson-id");
        const completed = $(this).hasClass("completed");
        
        // Toggle completed status
        $(this).toggleClass("completed");

        // Send an HTTP request to update the completion status
        fetch(`/update_lesson_status/${lessonId}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ completed: !completed }) // Send opposite value
        })
        .then(response => {
            if (!response.ok) {
                throw new Error("Failed to update lesson status");
            }
            // Optionally, update UI based on response
        })
        .catch(error => {
            console.error("Error:", error);
        });
    });
});
