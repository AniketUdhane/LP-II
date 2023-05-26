# Define a function to handle user input and generate responses
def chatbot():
    print("Chatbot: Hi, welcome to our food ordering service! How can I assist you today?")
    while True:
        user_input = input("User: ")

        # Check for exit condition
        if user_input.lower() == "bye":
            print("Chatbot: Thank you for using our service. Have a great day!")
            break

        # Generate a response
        response = generate_response(user_input)
        print("Chatbot:", response)

# Define a function to generate a response based on user input
def generate_response(user_input):
    # Mapping of user inputs to corresponding responses
    if "menu" in user_input:
        return "Sure, here is our menu: [list of menu items]"
    elif "order" in user_input or "place" in user_input:
        return "Great! Please provide me with your order details."
    elif "delivery" in user_input or "shipping" in user_input:
        return "We offer free delivery within the city. Your order will arrive within 30 minutes."
    elif "payment" in user_input or "pay" in user_input:
        return "We accept cash on delivery or online payment. How would you like to pay?"
    else:
        return "I'm sorry, I couldn't understand your request. Could you please rephrase it?"

# Start the chatbot
chatbot()
