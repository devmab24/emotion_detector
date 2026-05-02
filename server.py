import streamlit as st
from EmotionDetection.emotion_detection import emotion_detector

st.set_page_config(page_title="Emotion Detector", page_icon="😊")

st.title("😊 Emotion Detector")
st.write("Enter some text below to analyze its emotional content.")

text = st.text_area("Text to analyze:", placeholder="Type something here...")

if st.button("Analyze Emotions"):
    if not text or not text.strip():
        st.error("Invalid input! Please provide some text to analyze.")
    else:
        response = emotion_detector(text)

        if response is None or response.get('dominant_emotion') is None:
            st.error("Invalid input! Try again.")
        else:
            # Dominant emotion
            dominant = response['dominant_emotion']
            st.success(f"Dominant Emotion: **{dominant.upper()}**")

            # Emotion scores
            st.subheader("Emotion Scores")
            emotions = {k: v for k, v in response.items() 
                       if k != 'dominant_emotion'}

            for emotion, score in emotions.items():
                st.progress(float(score), text=f"{emotion.capitalize()}: {score:.4f}")
# from flask import Flask, render_template, request, jsonify
# from EmotionDetection.emotion_detection import emotion_detector

# """
# Executing this function initiates the application of emotion
# analysis to be executed over the Flask channel and deployed on
# localhost:5000.
# """

# # Initiating app
# app = Flask(__name__)

# @app.route("/emotionDetector")
# def sent_analyzer():
#     """
#     Receives text from frontend, runs emotion analysis,
#     and returns the full emotions dictionary including dominant_emotion.
#     """
#     text_to_analyze = request.args.get('textToAnalyze')
    
#     # Check if text is provided and not empty
#     if not text_to_analyze or text_to_analyze.strip() == "":
#         return jsonify({"error": "Invalid input! Please provide some text to analyze."}), 400

#     # Pass the text to the emotion_detector function
#     response = emotion_detector(text_to_analyze)

#     # If invalid input or API error, handle gracefully
#     if response is None or response.get('dominant_emotion') is None:
#         return jsonify({"error": "Invalid input! Try again."}), 400

#     # Return the structured JSON with success status
#     return jsonify({
#         "status": "success",
#         "emotions": response
#     })


# @app.route("/")
# def render_index_page():
#     """ 
#     This function initiates the rendering of the main application
#     page over the Flask channel
#     """
#     return render_template('index.html')


# if __name__ == "__main__":
#     """
#     This function executes the flask app and deploys it on localhost:5000
#     """
#     app.run(host="0.0.0.0", port=5000, debug=True)
    
# # from flask import Flask, render_template, request, jsonify
# # from EmotionDetection.emotion_detection import emotion_detector

# # """
# # Executing this function initiates the application of emotion
# # analysis to be executed over the Flask channel and deployed on
# # localhost:5000.
# # """

# # # Initiating app
# # app = Flask(__name__)

# # @app.route("/emotionDetector")
# # def sent_analyzer():
# #     """
# #     Receives text from frontend, runs emotion analysis,
# #     and returns the full emotions dictionary including dominant_emotion.
# #     """
# #     text_to_analyze = request.args.get('textToAnalyze')

# #     # Pass the text to the emotion_detector function
# #     response = emotion_detector(text_to_analyze)

# #     # If invalid input, handle gracefully
# #     if response['dominant_emotion'] is None:
# #         return jsonify({"error": "Invalid input! Try again."}), 400

# #     # Return the structured JSON
# #     return jsonify(response)


# # @app.route("/")
# # def render_index_page():
# #     """ 
# #     This function initiates the rendering of the main application
# #     page over the Flask channel
# #     """
# #     return render_template('index.html')


# # if __name__ == "__main__":
# #     """
# #     This function executes the flask app and deploys it on localhost:5000
# #     """
# #     app.run(host="0.0.0.0", port=5000)
