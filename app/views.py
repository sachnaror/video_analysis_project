import sqlite3
import threading
import time

import openai
from django.http import JsonResponse
from django.shortcuts import render

# Session Storage for Progress Updates
progress = 0

def index(request):
    return render(request, 'index.html')

def process_video(request):
    global progress
    progress = 0

    def update_progress():
        global progress
        for i in range(10):
            progress += 10
            time.sleep(2)

    threading.Thread(target=update_progress).start()
    return JsonResponse({"message": "Processing started."})

def chat(request):
    if request.method == "POST":
        data = request.POST
        question = data.get("question")
        api_key = data.get("api_key")

        if not api_key:
            return JsonResponse({"response": "Error: No API Key provided."}, status=400)

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": question}],
            api_key=api_key
        )

        ai_response = response["choices"][0]["message"]["content"]

        # Save chat history
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO chat_history (user_message, ai_response) VALUES (?, ?)", (question, ai_response))
        conn.commit()
        conn.close()

        return JsonResponse({"response": ai_response})
