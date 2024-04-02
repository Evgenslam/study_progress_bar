// progress_tracker.js

$(document).ready(function() {
    $('.lesson-checkbox').on('change', function() {
        var lessonId = $(this).data('lessonId');
        var completed = $(this).prop('checked');

        $.ajax({
            url: `/update_lesson_status/${lessonId}`,
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ completed: completed }),
            success: function(response) {
                console.log('Lesson status updated successfully');
                // Optionally, update UI based on response
            },
            error: function(xhr, status, error) {
                console.error('Failed to update lesson status:', error);
            }
        });
    });
});
