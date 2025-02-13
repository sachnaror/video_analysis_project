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
│   │   │   │   ├── widgets.css
│   │   │   │   ├── dark_mode.css
│   │   │   │   ├── login.css
│   │   │   │   ├── dashboard.css
│   │   │   │   ├── nav_sidebar.css
│   │   │   │   ├── responsive.css
│   │   │   │   ├── autocomplete.css
│   │   │   │   ├── responsive_rtl.css
│   │   │   │   ├── forms.css
│   │   │   │   ├── unusable_password_field.css
│   │   │   │   ├── rtl.css
│   │   │   │   ├── base.css
│   │   │   │   └── changelists.css
│   │   │   │   ├── vendor/
│   │   │   │   │   ├── select2/
│   │   │   │   │   │   ├── select2.min.css
│   │   │   │   │   │   ├── LICENSE-SELECT2.md
│   │   │   │   │   │   └── select2.css
│   │   │   ├── js/
│   │   │   │   ├── urlify.js
│   │   │   │   ├── core.js
│   │   │   │   ├── actions.js
│   │   │   │   ├── prepopulate.js
│   │   │   │   ├── cancel.js
│   │   │   │   ├── theme.js
│   │   │   │   ├── nav_sidebar.js
│   │   │   │   ├── autocomplete.js
│   │   │   │   ├── inlines.js
│   │   │   │   ├── change_form.js
│   │   │   │   ├── filters.js
│   │   │   │   ├── SelectFilter2.js
│   │   │   │   ├── jquery.init.js
│   │   │   │   ├── popup_response.js
│   │   │   │   ├── SelectBox.js
│   │   │   │   ├── calendar.js
│   │   │   │   ├── unusable_password_field.js
│   │   │   │   └── prepopulate_init.js
│   │   │   │   ├── admin/
│   │   │   │   │   ├── RelatedObjectLookups.js
│   │   │   │   │   └── DateTimeShortcuts.js
│   │   │   │   ├── vendor/
│   │   │   │   │   ├── jquery/
│   │   │   │   │   │   ├── jquery.min.js
│   │   │   │   │   │   ├── LICENSE.txt
│   │   │   │   │   │   └── jquery.js
│   │   │   │   │   ├── xregexp/
│   │   │   │   │   │   ├── xregexp.min.js
│   │   │   │   │   │   ├── xregexp.js
│   │   │   │   │   │   └── LICENSE.txt
│   │   │   │   │   ├── select2/
│   │   │   │   │   │   ├── LICENSE.md
│   │   │   │   │   │   ├── select2.full.min.js
│   │   │   │   │   │   └── select2.full.js
│   │   │   │   │   │   ├── i18n/
│   │   │   │   │   │   │   ├── pt.js
│   │   │   │   │   │   │   ├── hsb.js
│   │   │   │   │   │   │   ├── vi.js
│   │   │   │   │   │   │   ├── lv.js
│   │   │   │   │   │   │   ├── gl.js
│   │   │   │   │   │   │   ├── pl.js
│   │   │   │   │   │   │   ├── el.js
│   │   │   │   │   │   │   ├── dsb.js
│   │   │   │   │   │   │   ├── et.js
│   │   │   │   │   │   │   ├── is.js
│   │   │   │   │   │   │   ├── sl.js
│   │   │   │   │   │   │   ├── ko.js
│   │   │   │   │   │   │   ├── hr.js
│   │   │   │   │   │   │   ├── ms.js
│   │   │   │   │   │   │   ├── fi.js
│   │   │   │   │   │   │   ├── th.js
│   │   │   │   │   │   │   ├── ru.js
│   │   │   │   │   │   │   ├── eu.js
│   │   │   │   │   │   │   ├── mk.js
│   │   │   │   │   │   │   ├── sq.js
│   │   │   │   │   │   │   ├── ja.js
│   │   │   │   │   │   │   ├── ka.js
│   │   │   │   │   │   │   ├── he.js
│   │   │   │   │   │   │   ├── bg.js
│   │   │   │   │   │   │   ├── hy.js
│   │   │   │   │   │   │   ├── sr-Cyrl.js
│   │   │   │   │   │   │   ├── ne.js
│   │   │   │   │   │   │   ├── af.js
│   │   │   │   │   │   │   ├── id.js
│   │   │   │   │   │   │   ├── az.js
│   │   │   │   │   │   │   ├── ca.js
│   │   │   │   │   │   │   ├── nb.js
│   │   │   │   │   │   │   ├── zh-CN.js
│   │   │   │   │   │   │   ├── zh-TW.js
│   │   │   │   │   │   │   ├── pt-BR.js
│   │   │   │   │   │   │   ├── da.js
│   │   │   │   │   │   │   ├── fa.js
│   │   │   │   │   │   │   ├── de.js
│   │   │   │   │   │   │   ├── en.js
│   │   │   │   │   │   │   ├── bs.js
│   │   │   │   │   │   │   ├── tk.js
│   │   │   │   │   │   │   ├── sv.js
│   │   │   │   │   │   │   ├── hi.js
│   │   │   │   │   │   │   ├── uk.js
│   │   │   │   │   │   │   ├── cs.js
│   │   │   │   │   │   │   ├── km.js
│   │   │   │   │   │   │   ├── fr.js
│   │   │   │   │   │   │   ├── nl.js
│   │   │   │   │   │   │   ├── sr.js
│   │   │   │   │   │   │   ├── hu.js
│   │   │   │   │   │   │   ├── lt.js
│   │   │   │   │   │   │   ├── ar.js
│   │   │   │   │   │   │   ├── sk.js
│   │   │   │   │   │   │   ├── it.js
│   │   │   │   │   │   │   ├── es.js
│   │   │   │   │   │   │   ├── bn.js
│   │   │   │   │   │   │   ├── ro.js
│   │   │   │   │   │   │   ├── ps.js
│   │   │   │   │   │   │   └── tr.js
│   │   │   ├── img/
│   │   │   │   ├── search.svg
│   │   │   │   ├── icon-calendar.svg
│   │   │   │   ├── icon-clock.svg
│   │   │   │   ├── icon-hidelink.svg
│   │   │   │   ├── icon-no.svg
│   │   │   │   ├── tooltag-add.svg
│   │   │   │   ├── inline-delete.svg
│   │   │   │   ├── LICENSE
│   │   │   │   ├── icon-changelink.svg
│   │   │   │   ├── icon-unknown.svg
│   │   │   │   ├── sorting-icons.svg
│   │   │   │   ├── icon-viewlink.svg
│   │   │   │   ├── icon-yes.svg
│   │   │   │   ├── icon-addlink.svg
│   │   │   │   ├── icon-unknown-alt.svg
│   │   │   │   ├── icon-deletelink.svg
│   │   │   │   ├── README.txt
│   │   │   │   ├── selector-icons.svg
│   │   │   │   ├── calendar-icons.svg
│   │   │   │   ├── tooltag-arrowright.svg
│   │   │   │   └── icon-alert.svg
│   │   │   │   ├── gis/
│   │   │   │   │   ├── move_vertex_on.svg
│   │   │   │   │   └── move_vertex_off.svg
│   │   ├── rest_framework/
│   │   │   ├── css/
│   │   │   │   ├── bootstrap.min.css
│   │   │   │   ├── bootstrap.min.css.map
│   │   │   │   ├── bootstrap-theme.min.css.map
│   │   │   │   ├── prettify.css
│   │   │   │   ├── default.css
│   │   │   │   ├── font-awesome-4.0.3.css
│   │   │   │   ├── bootstrap-tweaks.css
│   │   │   │   └── bootstrap-theme.min.css
│   │   │   ├── js/
│   │   │   │   ├── load-ajax-form.js
│   │   │   │   ├── ajax-form.js
│   │   │   │   ├── prettify-min.js
│   │   │   │   ├── csrf.js
│   │   │   │   ├── bootstrap.min.js
│   │   │   │   ├── default.js
│   │   │   │   ├── coreapi-0.1.1.js
│   │   │   │   └── jquery-3.7.1.min.js
│   │   │   ├── docs/
│   │   │   │   ├── css/
│   │   │   │   │   ├── highlight.css
│   │   │   │   │   ├── base.css
│   │   │   │   │   └── jquery.json-view.min.css
│   │   │   │   ├── js/
│   │   │   │   │   ├── highlight.pack.js
│   │   │   │   │   ├── api.js
│   │   │   │   │   └── jquery.json-view.min.js
│   │   │   │   ├── img/
│   │   │   │   │   ├── favicon.ico
│   │   │   │   │   └── grid.png
│   │   │   ├── img/
│   │   │   │   ├── grid.png
│   │   │   │   ├── glyphicons-halflings.png
│   │   │   │   └── glyphicons-halflings-white.png
│   │   │   ├── fonts/
│   │   │   │   ├── fontawesome-webfont.svg
│   │   │   │   ├── glyphicons-halflings-regular.woff
│   │   │   │   ├── glyphicons-halflings-regular.eot
│   │   │   │   ├── glyphicons-halflings-regular.woff2
│   │   │   │   ├── glyphicons-halflings-regular.ttf
│   │   │   │   ├── fontawesome-webfont.ttf
│   │   │   │   ├── fontawesome-webfont.woff
│   │   │   │   ├── glyphicons-halflings-regular.svg
│   │   │   │   └── fontawesome-webfont.eot
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
│   │   │   ├── Employee Group Mediclaim Insurance Policy-NEW.pdf
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


🚀 **Happy Coding!** 🎬💡
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
video_analysis_project/
│── app/
│   ├── consumers.py      # WebSocket Consumers (Chat & Progress)
│   ├── models.py         # Django Models for storing data
│   ├── tasks.py          # Celery Task for Video Processing
│   ├── views.py          # Django Views (API Endpoints)
│   ├── urls.py           # API URL Routing
│   ├── routing.py        # WebSocket Routing
│── config/
│   ├── settings.py       # Django Settings
│   ├── asgi.py           # ASGI WebSocket Support
│   ├── urls.py           # Main URL Configuration
│── media/                # Video Uploads, Frames, Transcripts, Analysis
│── static/               # Static Files (JS, CSS)
│── templates/            # HTML Templates
│── manage.py             # Django Management Script
│── requirements.txt      # Python Dependencies
│── README.md             # Project Documentation
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
