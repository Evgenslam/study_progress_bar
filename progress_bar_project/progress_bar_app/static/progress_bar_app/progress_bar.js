document.addEventListener('DOMContentLoaded', function() {
    const lessonSections = document.querySelectorAll('.lesson-section');

    lessonSections.forEach(section => {
        section.addEventListener('click', function() {
            const lessonId = this.getAttribute('data-lesson-id');
            const isCompleted = this.classList.contains('completed');

            // Toggle completion status and color
            if (isCompleted) {
                this.classList.remove('completed');
                updateLessonStatus(lessonId, false);
            } else {
                this.classList.add('completed');
                updateLessonStatus(lessonId, true);
            }
        });
    });

    function updateLessonStatus(lessonId, completed) {
        // Send AJAX request to update lesson status
        const url = '/update_lesson_status/';
        const data = {
            lesson_id: lessonId,
            completed: completed
        };

        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')  // Ensure CSRF token is included
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                console.log('Lesson status updated successfully');
            } else {
                console.error('Failed to update lesson status:', data.error);
            }
        })
        .catch(error => {
            console.error('An error occurred while updating lesson status:', error);
        });
    }

    // Function to get CSRF token from cookie
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
