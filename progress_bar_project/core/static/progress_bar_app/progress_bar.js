document.addEventListener('DOMContentLoaded', function() {
    const lessonSections = document.querySelectorAll('.lesson-section');
    const completionSyncInterval = 60000; // Interval for checking cookies (milliseconds)

    // Load completed lesson IDs from cookies
    const completedLessons = getCompletedLessons();

    // Iterate over each lesson section
    lessonSections.forEach(section => {
        const lessonId = section.getAttribute('data-lesson-id');
        const isCompleted = completedLessons.includes(lessonId);

        // Update the visual status of the lesson section
        if (isCompleted) {
            section.classList.add('completed');
        } else {
            section.classList.remove('completed');
        }

        // Add click event listener to toggle completion status
        section.addEventListener('click', function() {
            toggleLessonCompletion(section, lessonId);
        });
    });

    // Sync completion status with database when browser is closed
    window.addEventListener('beforeunload', function(event) {
        syncCompletionStatusWithDatabase();
    });

    // Periodically check for cookies and sync completion status with database
    setInterval(function() {
        if (!areCookiesPresent()) {
            syncCompletionStatusWithDatabase();
        }
    }, completionSyncInterval);

    function toggleLessonCompletion(section, lessonId) {
        if (section.classList.contains('completed')) {
            section.classList.remove('completed');
            removeCompletedLesson(lessonId); // Remove lesson from cookies
        } else {
            section.classList.add('completed');
            addCompletedLesson(lessonId); // Add lesson to cookies
        }
    }

    function addCompletedLesson(lessonId) {
        let completedLessons = getCompletedLessons();
        completedLessons.push(lessonId);
        document.cookie = `completed_lessons=${JSON.stringify(completedLessons)}`;
    }

    function removeCompletedLesson(lessonId) {
        let completedLessons = getCompletedLessons();
        completedLessons = completedLessons.filter(id => id !== lessonId);
        document.cookie = `completed_lessons=${JSON.stringify(completedLessons)}`;
    }

    function getCompletedLessons() {
        const cookieValue = document.cookie.replace(/(?:(?:^|.*;\s*)completed_lessons\s*=\s*([^;]*).*$)|^.*$/, "$1");
        return cookieValue ? JSON.parse(cookieValue) : [];
    }

    function syncCompletionStatusWithDatabase() {
        const completedLessons = getCompletedLessons();
        fetch('/sync_completion_status/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({ completed_lessons: completedLessons })
        })
        .then(response => {
            if (response.ok) {
                console.log('Completion status synchronized with the database');
            } else {
                console.error('Failed to synchronize completion status with the database');
            }
        })
        .catch(error => {
            console.error('An error occurred while synchronizing completion status with the database:', error);
        });
    }

    function areCookiesPresent() {
        return document.cookie.indexOf('completed_lessons') !== -1;
    }

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
