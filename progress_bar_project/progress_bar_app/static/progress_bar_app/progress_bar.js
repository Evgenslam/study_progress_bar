document.addEventListener('DOMContentLoaded', function() {
    // Get all lesson sections
    const lessonSections = document.querySelectorAll('.lesson-section');

    // Load completed lesson IDs from cookies
    const completedLessons = getCompletedLessons();

    // Iterate over each lesson section
    lessonSections.forEach(section => {
        const lessonId = section.getAttribute('data-lesson-id');

        // Check if the lesson ID is in the list of completed lessons
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
        // Get existing completed lessons from cookies
        let completedLessons = getCompletedLessons();
        // Add the new lesson ID
        completedLessons.push(lessonId);
        // Update cookies with the new list of completed lessons
        document.cookie = `completed_lessons=${JSON.stringify(completedLessons)}`;
    }

    function removeCompletedLesson(lessonId) {
        // Get existing completed lessons from cookies
        let completedLessons = getCompletedLessons();
        // Remove the lesson ID
        completedLessons = completedLessons.filter(id => id !== lessonId);
        // Update cookies with the updated list of completed lessons
        document.cookie = `completed_lessons=${JSON.stringify(completedLessons)}`;
    }

    function getCompletedLessons() {
        // Get the value of the 'completed_lessons' cookie
        const cookieValue = document.cookie.replace(/(?:(?:^|.*;\s*)completed_lessons\s*=\s*([^;]*).*$)|^.*$/, "$1");
        // Parse the JSON string and return the array of completed lesson IDs
        return cookieValue ? JSON.parse(cookieValue) : [];
    }
});
