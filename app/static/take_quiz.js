let currentQuestionIndex = 0;
let score = 0;

function displayQuestion(questions) {
    const questionData = questions[currentQuestionIndex];
    
    // Select 3 random incorrect options
    const incorrectOptions = questions
        .filter(q => q.definition !== questionData.definition)
        .map(q => q.definition);
    const randomIncorrectOptions = [];
    while (randomIncorrectOptions.length < 3 && incorrectOptions.length > 0) {
        const randomIndex = Math.floor(Math.random() * incorrectOptions.length);
        randomIncorrectOptions.push(incorrectOptions.splice(randomIndex, 1)[0]);
    }

    // Combine correct and random incorrect options
    const options = [...randomIncorrectOptions, questionData.definition];
    options.sort(() => Math.random() - 0.5);

    document.getElementById('question-text').innerText = questionData.term;
    const optionsContainer = document.getElementById('options-container');
    optionsContainer.innerHTML = '';
    options.forEach(option => {
        const button = document.createElement('button');
        button.innerHTML = `<span>${option}</span>`;
        button.classList.add('option-button');
        button.onclick = () => handleOptionClick(option, questionData.definition, questions);
        optionsContainer.appendChild(button);
    });
}

function handleOptionClick(selectedOption, correctOption, questions) {
    const optionButtons = document.querySelectorAll('.option-button');
    optionButtons.forEach(button => {
        if (button.innerText === correctOption) {
            button.style.backgroundColor = 'green';
        } else if (button.innerText === selectedOption) {
            button.style.backgroundColor = 'red';
        }
        button.disabled = true;
    });

    if (selectedOption === correctOption) {
        score++;
    }

    setTimeout(() => {
        currentQuestionIndex++;
        if (currentQuestionIndex < questions.length) {
            displayQuestion(questions);
        } else {
            displayScore();
        }
    }, 1000);
}

function displayScore() {
    document.getElementById('question-container').style.display = 'none';
    document.getElementById('score-container').style.display = 'block';
    document.getElementById('score').innerText = `${score} / ${questions.length}`;
}
