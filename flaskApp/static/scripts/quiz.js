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
    ["I spend my time fulfillingly and how I want", 1],
    ["I would describe today as a good day", 1],
    ["I would not mind participating in a physical activity currently", 1],
    ["Lately, I have felt that my life has been pleasant", 1],
    ["As of late, I have had a postive outlook on the future", 1],
    ["I feel concentrated and motivated", 1],
    ["I have had pleasure and interest in doing things", 1],
    ["In general, I am satisfied with myself and who I am over the past few weeks", 1],
    ["I have had thoughts of hurting myself over the past couple of days", 1],
    ["In general, I have been able to get a good night’s sleep", 1],
    ["I have been hurt by someone I care about", 1],
    ["I would characterize my recent life experiences as being good", 1],
    ["I have been hurt by someone I care about", -1],
    ["I have many people I feel comfortable talking about my feelings with", 1],
    ["I feel my life moving in the direction I want", 1],
    ["I feel like some people are out to get me", -1],
    ["I've had a hard time focusing on my resposibilties today", -1],
    ["I haven't been sleeping well the past few nights", -1],
    ["I have been friendly and approachable when meeting with others", 1],
    ["I don't want to talk to others", -1],
    ["I have been feeling uneasy", -1],
    ["My responsibilites have been stressing me out more than usual", -1],
    ["My work feels as if it is not good enough no matter how much effort I put into it", -1],
    ["I've been finding it hard to cope with my emotions", -1],
    ["I have been feeling good overall", 1],
    ["I have been feeling angry", 1],
    ["My mood is easy to control", 1],
    ["My life is meaningful", 1],
    ["I have been feeling accomplished", 1],
    ["I have been easily distracted", -1],
    ["I feel comfortable around my friends and family", 1],
    ["I feel dissatisfied with how my life has been progressing", -1],
    ["I have no issue telling someone how I feel", 1]
];

var questionsSeen = []; // Keep track of what questions user has answered to make sure questions arent repeated
function generateQuestionNum() {
    var min = 0;
    var max = questions.length; 

    var num = Math.floor(Math.random() * (max - min) + min);
    while(questionsSeen.includes(num)) {
        num = Math.floor(Math.random() * (max - min) + min);
    }

    return num;
}

var scores = [];  // Keep track of user score which will be averaged once they finished. 
                // This also helps if user wants to go back to a previous question so we can easily reset that answer value.


var totalQuestions = 10; 
var questionsAnswered = 0; // User will answer 10 questions total 
var numQuestion = generateQuestionNum(); // Keeps track of what question user is on
var avg = 0; 
var index = 0;  // Use backtracking so that user can reanswer questions
$(".question").append("<p>"+questions[numQuestion][0]+"</p>");
$(document).ready(function () {
    function getNextQuestion(question = -1) {

        // Uncheck previous radio answer, then show next question requested
        $("input[name='answer']:checked").prop("checked", false); 

        if(question == -1 && index == questionsSeen.length) {
            numQuestion = generateQuestionNum(); 
        } else {
            numQuestion = questionsSeen[index];
        }
        $(".question").empty();
        $(".question").append("<p>"+questions[numQuestion][0]+"</p>");
    }

    // Get value of answer user inputted
    $("#nextBtn").click(function () {
        // If user is not done
        if(questionsAnswered < totalQuestions-1) {
            console.log(index);
           var radioVal = $("input[name='answer']:checked").val(); 
            if(radioVal) {
                var val = parseInt(radioVal);
                scores.push(val*questions[numQuestion][1]);
                questionsAnswered++; 
                if(index == questionsSeen.length) {
                    questionsSeen.push(numQuestion);
                }
                index++; 
                getNextQuestion();
            } 
        } else { // else user is on last question 
            // Grab last question result 
            var radioVal = $("input[name='answer']:checked").val(); 
            if(radioVal) {
                var val = parseInt(radioVal);
                scores.push(val*questions[numQuestion][1]);

                // Get results 
                var sum = 0;
                for(var i=0; i<scores.length; i++) {
                    sum += scores[i];
                }
                avg = sum/scores.length; 
                console.log(avg);
            } 
            console.log(scores);

            
        }
        console.log(scores);

    });

    $("#backBtn").click(function () {
        console.log(questionsSeen);
        if(questionsAnswered > 0) {
            var prevQuestion = questionsSeen[index-1];
            index--;
            scores.pop();
            questionsAnswered--;
            getNextQuestion(prevQuestion);
        }
    });
});
