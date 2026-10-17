const chatForm = document.getElementById("chat-form");
const userInput = document.getElementById("user-input");
const chatBox = document.getElementById("chat-box");

function addMessage(message, className) {
    const messageElement = document.createElement("div");

    messageElement.classList.add("message", className);
    messageElement.textContent = message;

    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}

chatForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    const message = userInput.value.trim();

    if (!message) {
        return;
    }

    addMessage(message, "user-message");
    userInput.value = "";
    userInput.focus();

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });

        const data = await response.json();

        if (!response.ok) {
            addMessage(
                data.reply || "Please try again.",
                "bot-message"
            );
            return;
        }

        addMessage(data.reply, "bot-message");

    } catch (error) {
        addMessage(
            "Unable to connect to the chatbot. Please try again.",
            "bot-message"
        );
    }
});