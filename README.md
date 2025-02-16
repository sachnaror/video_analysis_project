# 🎥 AI-Powered Video Analysis System




🚀 **AI-based Video Processing & Analysis System** with **Django, Celery, WebSockets, OpenAI GPT-4, Whisper, OCR, and YOLOv8** for **video transcript generation, object detection, speech-to-text, and AI-powered chat**.

## 📌 Features
✅ **Upload & Process Videos** – Extract audio, text, and objects
✅ **Real-time Progress Updates** – WebSockets for instant feedback
✅ **AI Chat** – Ask questions about the processed video
✅ **Multi-user API Key Support** – Users enter their own OpenAI API key
✅ **Database Storage** – Save transcripts & analysis reports
✅ **WebSocket-powered Chat** – Realtime AI Q&A
✅ **Download Reports** – Transcripts & analysis reports available

---

## 🏗️ Directory Structure
```
├── video_analysis_project/
│   ├── dump.rdb
│   ├── requirements.txt
│   ├── yolov8n.pt
│   ├── db.sqlite3
│   ├── README.md
│   ├── database.env
│   ├── docker-compose.yml
│   ├── manage.py
│   ├── celery_tasks.py
│   ├── app/
│   │   ├── video_processing.py
│   │   ├── tasks.py
│   │   ├── models.py
│   │   ├── database.py
│   │   ├── chat_processor.py
│   │   ├── consumers.py
│   │   ├── apps.py
│   │   ├── admin.py
│   │   ├── routing.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── config/
│   │   ├── asgi.py
│   │   ├── celery.py
│   │   ├── settings.py
│   │   └── urls.py
│   └── Dockerfile/
│   ├── staticfiles/
│   │   ├── styles.css
│   │   └── script.js
│   │   ├── admin/
│   │   │   ├── css/
│   │   │   ├── js/
│   │   │   │   ├── admin/
│   │   │   │   ├── vendor/
│   │   │   ├── img/
│   │   │   │   ├── gis/
│   │   ├── rest_framework/
│   │   │   ├── css/
│   │   │   ├── js/
│   │   │   ├── docs/
│   │   │   │   ├── css/
│   │   │   │   ├── js/
│   │   │   │   ├── img/

│   │   │   ├── img/
│   │   │   ├── fonts/
│   ├── static/
│   │   ├── styles.css
│   │   └── script.js
│   ├── templates/
│   │   ├── index.html
│   │   └── reports.html
│   ├── media/
│   │   └── progress.json
│   │   ├── transcripts/
│   │   │   ├── Screen Recording 2025-02-08 at 9.49.34PM.mov_transcript.txt
│   │   │   └── Screen Recording 2025-02-13 at 2.04.42AM.mov_transcript.txt
│   │   ├── analysis/
│   │   │   ├── Screen Recording 2025-02-13 at 2.04.42AM.mov_analysis.txt
│   │   │   └── Screen Recording 2025-02-08 at 9.49.34PM.mov_analysis.txt
│   │   └── frames/
│   │   ├── uploads/
│   │   │   ├── Screen Recording 2025-02-08 at 9.49.34PM.mov
│   │   │   └── Screen Recording 2025-02-13 at 2.04.42AM.mov
│   │   └── chunks/
│   │   └── audio/

```

---

## 🛠️ **Installation & Setup**
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/sachinarora/video_analysis_project.git
cd video_analysis_project
```

### 2️⃣ Setup Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scriptsctivate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Setup PostgreSQL Database
- **DB Name:** `postgres`
- **User:** `postgres`
- **Password:** `password`

Update `DATABASES` in `config/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5️⃣ Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Start Redis Server (For Celery)
```bash
redis-server
```

### 7️⃣ Start Celery Worker
```bash
celery -A config worker --loglevel=info
```

### 8️⃣ Run Django ASGI Server (For WebSockets)
```bash
daphne -b 0.0.0.0 -p 8000 config.asgi:application
```

---

## 📖 API Endpoints
| Method | Endpoint         | Description                         |
|--------|-----------------|-------------------------------------|
| POST   | `/upload_video/` | Upload & process a new video      |
| GET    | `/progress/`     | Get real-time processing progress |
| POST   | `/chat/`         | Ask AI questions about the video  |
| GET    | `/reports/`      | View past analysis reports        |

---

## 🔧 **Usage**
### **1️⃣ Upload & Process a Video**
1. Open `http://127.0.0.1:8000/`
2. Click **Upload Video** → Select a `.mp4` file
3. Processing starts & progress is updated in real-time

### **2️⃣ View Live Progress**
- **WebSockets** update UI dynamically
- Shows **current processing step**: "Extracting Audio", "Running OCR" etc.

### **3️⃣ Ask AI Questions**
- **Enter an OpenAI API Key**
- Use chat box to ask **"What objects are in this video?"**, etc.
- AI responds using transcript, OCR, & detected objects

### **4️⃣ Download Report**
- Once **processing is complete**, download:
  - **Transcript (`media/transcripts/`)**
  - **Analysis Report (`media/analysis/`)**

---

## 📞 Contact & Support
📧 **Email:** sachnaror@gmail.com
🌍 **GitHub:** [github.com/sachnaror](https://github.com/sachnaror)
🌐 **Website:** [https://about.me/sachin-arora](https://about.me/sachin-arora)

🚀 **Happy Coding!** 🎬💡

## Commands:

First, stop existing processes, run:

```bash
pkill -f runserver
pkill -f redis
pkill -f celery

### and then..

redis-server &
python manage.py runserver &
celery -A config worker --loglevel=info &
```
