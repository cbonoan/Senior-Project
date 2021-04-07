var questions = [
    ["I have been feeling great the past few days!", 1], 
    ["I have been feeling tired of my daily lifestyle.", -1], 
    ["I feel energized and well rested.", 1],
    ["Activities I usual enjoy have been less entertaining",-1],
    ["I feel secure about myself and my place in the world.", 1], 
    ["I feel like I am mentally in a good place.", 1],
    ["Activities I usual enjoy have been less entertaining", -1],
    ["My environment makes me feel confident in myself.", 1],
    ["I have been having a hard time focusing.", -1],
    ["Life would be better without me.", -1],
    ["The majority of my thoughts are positive.", 1],
    ["I have been lashing out at loved ones unexpectedly.", -1],
    ["I feel confident with my capabilities.", 1],
    ["Over the past few days, I have been feeling anxiety and discomfort.", -1],
    ["Over the past couple days, I have had pleasure and interest in doing things.", 1],
    ["If a friend asked me to join them at a party, I would be happy to go with them.", 1],
    ["Past trauma has been affecting my day-to-day life.", -1],
    ["I have been feeling generous lately.", 1],
    ["I feel like I have friends who care about me and make me feel less lonely.", 1],
    ["I spend my time fulfillingly and how I want", 1]
];

var questionsSeen = []; // Keep track of what questions user has answered to make sure questions arent repeated
function generateQuestionNum() {
    var min = 0;
    var max = questions.length; 

    var num = Math.floor(Math.random() * (max - min) + min);
    while(questionsSeen.includes(num)) {
        num = Math.floor(Math.random() * (max - min) + min);
    }

    questionsSeen.push(num);
    return num;
}

var scores = [];  // Keep track of user score which will be averaged once they finished. 
                // This also helps if user wants to go back to a previous question so we can easily reset that answer value.


var totalQuestions = 10; 
var questionsAnswered = 0; // User will answer 20 questions total 
var numQuestion = generateQuestionNum(); // Keeps track of what question user is on
var avg = 0; 
$(".question").append("<p>"+questions[numQuestion][0]+"</p>");
$(document).ready(function () {
    function getNextQuestion() {
        console.log(scores);

        // Uncheck previous radio answer, then show next question requested
        $("input[name='answer']:checked").prop("checked", false); 

        numQuestion = generateQuestionNum(); 
        $(".question").empty();
        $(".question").append("<p>"+questions[numQuestion][0]+"</p>");
    }

    // Get value of answer user inputted
    $("#nextBtn").click(function () {
        // If user is not done
        console.log(questionsAnswered);
        if(questionsAnswered < totalQuestions-1) {
           var radioVal = $("input[name='answer']:checked").val(); 
            if(radioVal) {
                var val = parseInt(radioVal);
                scores.push(val*questions[numQuestion][1]);
                questionsAnswered++; 
                getNextQuestion(); 
            } 
        } else {
            // Get results 
            var sum = 0;
            for(var i=0; i<scores.length; i++) {
                sum += scores[i];
            }
            avg = sum/scores.length; 
            console.log(avg);
        }
        
    });

    $("#backBtn").click(function () {
        if(numQuestion > 0) {
            scores.pop();
            questionsAnswered--;
            getNextQuestion();
        }
    });
});
