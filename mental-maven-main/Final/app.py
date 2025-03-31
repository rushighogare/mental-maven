# from flask import Flask, request, jsonify, render_template
# import speech_recognition as sr
# from datetime import datetime

# app = Flask(__name__)

# def recognize_speech_from_microphone():
#     recognizer = sr.Recognizer()

#     with sr.Microphone() as source:
#         print("Adjusting for ambient noise...")
#         recognizer.adjust_for_ambient_noise(source, duration=1)
#         print("Listening...")
#         try:
#             # Allow up to 15 seconds of silence before ending the recording
#             audio = recognizer.listen(source, timeout=None, phrase_time_limit=15)
#             print("Processing audio...")

#             # Recognize speech
#             text = recognizer.recognize_google(audio)
#             return {"success": True, "text": text}
#         except sr.UnknownValueError:
#             return {"success": False, "error": "Could not understand audio"}
#         except sr.RequestError as e:
#             return {"success": False, "error": f"Error: {str(e)}"}

# def save_text_to_file(text):
#     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#     file_name = f"user_response_{timestamp}.txt"
#     with open(file_name, "w") as file:
#         file.write(text)
#     return file_name

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/contact")
# def contact():
#     return render_template("contact.html")

# @app.route("/about")
# def about():
#     return render_template("about.html")

# @app.route("/profile")
# def profile():
#     return render_template("profile.html")

# @app.route("/record-response", methods=["POST"])
# def record_response():
#     response = recognize_speech_from_microphone()
#     if response["success"]:
#         save_text_to_file(response["text"])
#     return jsonify(response)

# if __name__ == "__main__":
#     app.run(debug=True)



# from flask import Flask, request, jsonify, render_template
# import speech_recognition as sr
# from datetime import datetime
# import os

# app = Flask(__name__)

# # File to store responses
# RESPONSE_FILE = "user_responses.txt"

# def recognize_speech_from_microphone():
#     recognizer = sr.Recognizer()
    
#     with sr.Microphone() as source:
#         print("Adjusting for ambient noise...")
#         recognizer.adjust_for_ambient_noise(source, duration=1)
#         print("Listening...")

#         try:
#             audio = recognizer.listen(source, timeout=None, phrase_time_limit=15)
#             print("Processing audio...")
#             text = recognizer.recognize_google(audio)
#             return {"success": True, "text": text}
#         except sr.UnknownValueError:
#             return {"success": False, "error": "Could not understand audio"}
#         except sr.RequestError as e:
#             return {"success": False, "error": f"Error: {str(e)}"}

# def save_text_to_file(question, response):
#     """Appends question and response to a single file."""
#     with open(RESPONSE_FILE, "a") as file:
#         file.write(f"Q: {question}\nA: {response}\n\n")

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/record-response", methods=["POST"])
# def record_response():
#     data = request.get_json()
#     question = data.get("question", "Unknown Question")

#     response = recognize_speech_from_microphone()
    
#     if response["success"]:
#         save_text_to_file(question, response["text"])

#     return jsonify(response)

# if __name__ == "_main_":
#     app.run(debug=True)




# from flask import Flask, request, jsonify, render_template
# import speech_recognition as sr
# from datetime import datetime
# import openai  # Import OpenAI API
# import os

# app = Flask(__name__)

# # OpenAI API Key (Replace with your API key)
# OPENAI_API_KEY = "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"

# # File to store responses
# FILE_NAME = "user_responses.txt"

# def recognize_speech_from_microphone():
#     recognizer = sr.Recognizer()

#     with sr.Microphone() as source:
#         print("Adjusting for ambient noise...")
#         recognizer.adjust_for_ambient_noise(source, duration=1)
#         print("Listening...")

#         try:
#             audio = recognizer.listen(source, timeout=None, phrase_time_limit=15)
#             print("Processing audio...")
#             text = recognizer.recognize_google(audio)
#             return {"success": True, "text": text}
#         except sr.UnknownValueError:
#             return {"success": False, "error": "Could not understand audio"}
#         except sr.RequestError as e:
#             return {"success": False, "error": f"Error: {str(e)}"}

# def save_text_to_file(question, text):
#     """Append question-response pairs to a single text file."""
#     with open(FILE_NAME, "a") as file:
#         file.write(f"Question: {question}\nResponse: {text}\n\n")

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/record-response", methods=["POST"])
# def record_response():
#     """Handles the recording and saving of user responses."""
#     data = request.get_json()
#     question = data.get("question", "Unknown Question")
#     response = recognize_speech_from_microphone()

#     if response["success"]:
#         save_text_to_file(question, response["text"])

#     return jsonify(response)

# @app.route("/interpret-results")
# def interpret_results():
#     """Reads user responses from file, sends them to ChatGPT, and displays the analysis."""
#     if not os.path.exists(FILE_NAME):
#         return "No responses recorded yet."

#     # Read responses from file
#     with open(FILE_NAME, "r") as file:
#         user_responses = file.read()

#     # Prepare ChatGPT prompt
#     chatgpt_prompt = f"""
#     You are a psychologist analyzing a person's responses to mental health questions. 
#     Below are their responses:

#     {user_responses}

#     Based on these answers:
#     - Summarize the person's emotional state.
#     - Identify any patterns in their responses.
#     - Suggest possible mental well-being insights.

#     Provide a structured analysis.
#     """

#     # Send to OpenAI API
#     try:
#         openai.api_key = OPENAI_API_KEY
#         response = openai.ChatCompletion.create(
#             model="gpt-4",
#             messages=[{"role": "system", "content": chatgpt_prompt}]
#         )
#         chatgpt_output = response["choices"][0]["message"]["content"]

#     except Exception as e:
#         return f"Error processing AI response: {str(e)}"

#     return render_template("interpret.html", interpretation=chatgpt_output)

# if __name__ == "_main_":
#     app.run(debug=True)




# from flask import Flask, request, jsonify, render_template
# import speech_recognition as sr
# from datetime import datetime
# import openai  # Import OpenAI API
# import os

# app = Flask(__name__)  # Fixed _name

# # OpenAI API Key (Replace with your actual key)
# OPENAI_API_KEY = "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"

# # File to store responses
# FILE_NAME = "user_responses.txt"

# def recognize_speech_from_microphone():
#     recognizer = sr.Recognizer()

#     with sr.Microphone() as source:
#         print("Adjusting for ambient noise...")
#         recognizer.adjust_for_ambient_noise(source, duration=1)
#         print("Listening...")

#         try:
#             audio = recognizer.listen(source, timeout=None, phrase_time_limit=15)
#             print("Processing audio...")
#             text = recognizer.recognize_google(audio)
#             return {"success": True, "text": text}
#         except sr.UnknownValueError:
#             return {"success": False, "error": "Could not understand audio"}
#         except sr.RequestError as e:
#             return {"success": False, "error": f"Error: {str(e)}"}

# def save_text_to_file(question, text):
#     """Append question-response pairs to a single text file."""
#     with open(FILE_NAME, "a") as file:
#         file.write(f"Question: {question}\nResponse: {text}\n\n")

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/record-response", methods=["POST"])
# def record_response():
#     """Handles the recording and saving of user responses."""
#     data = request.get_json()
#     question = data.get("question", "Unknown Question")
#     response = recognize_speech_from_microphone()

#     if response["success"]:
#         save_text_to_file(question, response["text"])

#     return jsonify(response)

# @app.route("/interpret-results")
# def interpret_results():
#     """Reads user responses from file, sends them to ChatGPT, and displays the analysis."""
#     if not os.path.exists(FILE_NAME):
#         return "No responses recorded yet."

#     # Read responses from file
#     with open(FILE_NAME, "r") as file:
#         user_responses = file.read()

#     # Prepare ChatGPT prompt
#     chatgpt_prompt = f"""
#     You are a psychologist analyzing a person's responses to mental health questions. 
#     Below are their responses:

#     {user_responses}

#     Based on these answers:
#     - Summarize the person's emotional state.
#     - Identify any patterns in their responses.
#     - Suggest possible mental well-being insights.

#     Provide a structured analysis.
#     """

#     # Send to OpenAI API
#     try:
#         client = openai.OpenAI(api_key=OPENAI_API_KEY)  # ✅ Fixed API Call
#         response = client.chat.completions.create(
#             model="gpt-4",
#             messages=[
#                 {"role": "system", "content": "You are a psychologist analyzing responses."},
#                 {"role": "user", "content": chatgpt_prompt}
#             ]
#         )
#         chatgpt_output = response.choices[0].message.content  # ✅ Fixed API Response Parsing

#     except Exception as e:
#         return f"Error processing AI response: {str(e)}"

#     return render_template("interpret.html", interpretation=chatgpt_output)

# if __name__ == "_main":  # ✅ Fixed _name
#     app.run(debug=True)





from flask import Flask, request, jsonify, render_template
import speech_recognition as sr
import os
import requests

app = Flask(__name__)

# Hugging Face API Key (replace with your actual key)
HUGGINGFACE_API_KEY = ""

# Model name (use a free model)
MODEL_NAME = "HuggingFaceH4/zephyr-7b-beta"

# File to store responses
FILE_NAME = "user_responses.txt"

def recognize_speech_from_microphone():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")

        try:
            audio = recognizer.listen(source, timeout=None, phrase_time_limit=15)
            print("Processing audio...")
            text = recognizer.recognize_google(audio)
            return {"success": True, "text": text}
        except sr.UnknownValueError:
            return {"success": False, "error": "Could not understand audio"}
        except sr.RequestError as e:
            return {"success": False, "error": f"Error: {str(e)}"}

def save_text_to_file(question, text):
    """Append question-response pairs to a single text file."""
    with open(FILE_NAME, "a") as file:
        file.write(f"Question: {question}\nResponse: {text}\n\n")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/record-response", methods=["POST"])
def record_response():
    """Handles the recording and saving of user responses."""
    data = request.get_json()
    question = data.get("question", "Unknown Question")
    response = recognize_speech_from_microphone()

    if response["success"]:
        save_text_to_file(question, response["text"])

    return jsonify(response)

@app.route("/interpret-results")
def interpret_results():
    """Reads user responses from file, sends them to Hugging Face, and displays the analysis."""
    if not os.path.exists(FILE_NAME):
        return "No responses recorded yet."

    # Read responses from file
    with open(FILE_NAME, "r") as file:
        user_responses = file.read()

    # Prepare prompt for analysis
    prompt = f"""
    You are an AI psychologist analyzing a person's responses to mental health questions. 
    Below are their responses:

    {user_responses}

    Based on these answers:
    - Summarize the person's emotional state.
    - Identify any patterns in their responses.
    - Suggest possible mental well-being insights.

    Provide a structured analysis.
    """

    # Send request to Hugging Face Inference API
    headers = {
        "Authorization": f"Bearer {HUGGINGFACE_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {"inputs": prompt}

    try:
        response = requests.post(f"https://api-inference.huggingface.co/models/{MODEL_NAME}", 
                                 headers=headers, json=data)
        response_data = response.json()

        if isinstance(response_data, list):
            chat_output = response_data[0]["generated_text"]
        else:
            chat_output = response_data.get("error", "Unknown error")

    except Exception as e:
        return f"Error processing AI response: {str(e)}"

    return render_template("interpret.html", interpretation=chat_output)

if __name__ == "_main_":
    app.run(debug=True)
