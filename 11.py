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

'''
Objective:
 Understand and Implement chatbot for any suitable customer interaction application

Outcome:
 Ability to choose an appropriate problem solving method and knowledge representation
technique

Software Required:
 Python

Theory:
 Understanding the Chatbot:
A Chatbot is an Artificial Intelligence-based software developed to interact with humans in their
natural languages. These chatbots are generally converse through auditory or textual methods,
and they can effortlessly mimic human languages to communicate with human beings in a
human-like way. A chatbot is considered one of the best applications of natural languages
processing.

 Chatbot in present Generation:
Today, we have smart Chatbots powered by Artificial Intelligence that utilize natural language
processing (NLP) in order to understand the commands from humans (text and voice) and learn
from experience. Chatbots have become a staple customer interaction utility for companies and
brands that have an active online existence (website and social network platforms).
With the help of Python, Chatbots are considered a nifty utility as they facilitate rapid messaging
between the brand and the customer. Let us think about Microsoft's Cortana, Amazon's Alexa,
and Apple's Siri. Aren't these chatbots wonderful? It becomes quite interesting to learn how to
create a chatbot using the Python programming language.

 Creating a Chatbot using Python:
We will follow a step-by-step approach and break down the procedure of creating a Python chat.
We will begin building a Python chatbot by importing all the required packages and modules
necessary for the project. We will also initialize different variables that we want to use in it.
Moreover, we will also be dealing with text data, so we have to perform data preprocessing on
the dataset before designing an ML model.
This is where tokenizing supports text data - it converts the large text dataset into smaller,
readable chunks (such as words). Once this process is complete, we can go for lemmatization to
transform a word into its lemma form. Then it generates a pickle file in order to store the objects
of Python that are utilized to predict the responses of the bot.
Another major section of the chatbot development procedure is developing the training and
testing datasets.

 Benefits of using Chatbots:
 24×7 availability.
 Instant answers to queries.
 Support multi-language to enhance businesses.
 Simple and Easy to Use UI to engage more customers.
 Cost effective and user interactive.
 Avoid communication with call agents thereby reducing the time consuming tasks.
 Understand the Customer behavior
 Increase sales of business by offering promo codes or gifts.

Conclusion: Thus we have developed an elementary chatbot for any suitable customer interaction
application.
'''
