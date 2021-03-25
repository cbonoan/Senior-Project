var questions = [
    ["I have been feeling great the past few days!", 1], 
    ["I feel dissatisfied with how my life has been progressing.", -1], 
    ["I feel energized and well rested.", 1]
];
var scores = [];  // Keep track of user score which will be averaged once they finished. 
                // This also helps if user wants to go back to a previous question so we can easily reset that answer value.

var numQuestion = 0; // Keeps track of what question user is on
$(".question").append("<p>"+questions[numQuestion][0]+"</p>");
$(document).ready(function () {
    function getNextQuestion() {
        console.log(scores);
        $(".question").empty();
        $(".question").append("<p>"+questions[numQuestion][0]+"</p>");
    }

    // Get value of answer user inputted
    $("#nextBtn").click(function () {
        // If user is not done
        if(numQuestion < questions.length) {
           var radioVal = $("input[name='answer']:checked").val(); 
            if(radioVal) {
                var val = parseInt(radioVal);
                scores.push(val*questions[numQuestion][1]);
                numQuestion++; 
                getNextQuestion(); 
            } 
        }
        
    });

    $("#backBtn").click(function () {
        if(numQuestion > 0) {
            scores.pop();
            numQuestion--;
            getNextQuestion();
        }
    });
});