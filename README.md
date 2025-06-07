# 🛡️ TADNS API Vault Server

A clean, secure, and minimal backend server to fetch images, videos, and weather data from external APIs – without the headache of repeating `.env` setups and duplicated API code for every small project.

---

## 🧑‍💻 Who Needs This?

* Are you tired of setting up API keys again and again for Unsplash, Pixabay, or OpenWeatherMap?
* Want a central backend that gives you all this data securely?
* Need a mini UI to test your API even from mobile?

**Then this project is for you.** A mini vault that helps you keep your keys safe, responses cached, and APIs clean — with just Flask, simple HTML, and some GPT-styled magic 💡 (yeah, I’m not an HTML/CSS guy, thanks GPT buddy for the UI and caching logic).

---

## 🚀 What It Does

* 📸Search **Images** from Pixabay and Unsplash
* 🎥Search **Videos** from Pixabay
* 🌦️Fetch **Current Weather** from OpenWeatherMap
* 🚀Cache results with expiry (default 10 mins)
* 🖥️Simple HTML UI for mobile/desktop testing
* 🔐Secure route-level access using headers (so only you can use it!)

---

## 📦 Tech Stack & Libraries

* **Flask** – Web framework
* **requests** – API requests
* **python-dotenv** – Loads API keys
* **hashlib** – Generates MD5 hashed filenames
* **json & os** – Core modules for saving/reading cache
* **Inline CSS/JS** – Mobile-friendly UI

---

## 🗂 Folder Structure

```bash
API-Keys-MiniBackend/
├── app/
│   ├── __init__.py             # App factory setup
│   ├── config.py               # Loads .env
│   ├── core/
│   │   └── error_handlers.py   # Custom 404/500 JSON
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── images.py           # /search/<api>/images/<query>
│   │   ├── videos.py           # /search/pixabay/videos/<query>
│   │   ├── weather.py          # /weather/<city>
│   │   └── ui.py               # /test UI route
│   └── utils/
│       ├── api_helpers.py      # Handles API calls
│       └── cache_helper.py     # Smart cache logic
├── cache/                      # JSON files (auto created)
├── templates/
│   └── index.html              # Minimal UI
├── static/
│   ├── style.css               # CSS for UI
│   └── app.js                  # JS logic for UI
├── tests/                      # (optional tests)
├── .env                        # API keys (ignored)
├── .gitignore                  # Ignore cache, .env, venv
├── requirements.txt            # Flask + requests + dotenv + gunicorn
├── run.py                      # Starts Flask app
└── README.md                   # This doc
```

---

## 🔧 How It Works (Brief)

1. **Frontend or request hits route** → `/search/unsplash/images/cats`
2. **Flask route checks** → is result cached?
3. **If cached & not expired** → return it.
4. **Else** → fetch from API → return → cache result.
5. **Optional Header**: You can add `X-Api-Secret: yourkey` to lock your API.

---

## 💡 Example API Usage

```bash
# Search images from Pixabay
GET /search/pixabay/images/dogs

# Get current weather
GET /weather/delhi

# With force fresh data (bypass cache)
GET /search/unsplash/images/flowers?force=true

# Auth header for protection
X-Api-Secret: your_secret_here
```

Test in browser via:

```
http://localhost:5000/
```

---

## ⚙️ How to Use

1. **Clone + setup**:

```bash
git clone https://github.com/Aditya-Pratap-Bose/tadns-api-vault-server.git
cd tadns-api-vault-server
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. **Add your ****`.env`**** file**:

```
UNSPLASH_ACCESS_KEY=...
PIXABAY_API_KEY=...
OPENWEATHER_API_KEY=...
BACKEND_SECRET_KEY=...
```

3. **Run app**:

```bash
python run.py
```

4. **Hit API or go to** `http://localhost:5000/`

---

## 🛡 Security & Deployment

* Never push `.env` → already added to `.gitignore`
* All secrets pulled from config (Flask `app.config`)
* Secure your routes using `X-Api-Secret` header
* Test UI is open by default (you can obfuscate the URL if needed)

**Deploy on Render:**

* Connect repo
* Add environment variables in dashboard
* Use build command: `pip install -r requirements.txt`
* Start command: `gunicorn run:app`

---

## 🔧 Extend it your way

* Add more APIs → News, YouTube, AI APIs
* Swap file cache with Redis
* Convert UI to React frontend
* Add token-based auth / JWT
* Dockerize it for container use

---

## ✨ In Closing...

> **A small backend that does big things 💥**

If you're like me — juggling small tools, APIs, and frontend/backend glue work — this vault is for you.

**Clone it. Test it. Use it in your projects. Show it off. Or improve it!**  
Just don’t forget to keep your `.env` safe ✌️

Made with ❤️ by **Aditya**

> _“Happy coding! Keep calm and cache on.”_ 😊

If you find bugs or have questions, feel free to **open an issue**.  
Enjoy and make something awesome!

