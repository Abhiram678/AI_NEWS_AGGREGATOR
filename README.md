# 🤖 AI News Aggregator

An intelligent news aggregator that curates personalized AI news digests using Google Gemini API and sends daily email summaries.

## ✨ Features

- 📰 **Multi-Source Scraping**: Aggregates news from OpenAI blog, Anthropic blog, and YouTube AI channels
- 🤖 **AI-Powered Curation**: Uses Google Gemini 2.5 Flash to analyze and rank articles
- 📧 **Email Delivery**: Automated daily digest sent via Gmail
- 🎯 **Personalized**: Ranks content based on user profile and interests
- 💾 **SQLite Database**: Lightweight local storage with no setup required
- 🆓 **100% Free**: Uses free-tier APIs (Google Gemini, Gmail)

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Google Gemini API key (free at [Google AI Studio](https://aistudio.google.com/app/apikey))
- Gmail account with app password

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Abhiram678/AI_NEWS_AGGREGATOR.git
cd AI_NEWS_AGGREGATOR
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment**
```bash
cp app/example.env app/.env
```

Edit `app/.env` with your credentials:
```env
GEMINI_API_KEY=your-gemini-api-key
MY_EMAIL=your-email@gmail.com
APP_PASSWORD=your-gmail-app-password
SQLITE_DB_PATH=ai_news_aggregator.db
```

5. **Run the aggregator**
```bash
python main.py
```

## 📋 Configuration

### User Profile
Edit `app/profiles/user_profile.py` to customize:
- Name and background
- Interests and preferences
- Expertise level

### Content Sources
Edit `app/config.py` to add/remove YouTube channels:
```python
YOUTUBE_CHANNELS = [
    "UCawZsQWqfGSbCI5yjkdVkTA",  # Matthew Berman
]
```

## 🔧 How It Works

1. **Scraping**: Fetches latest content from configured sources (last 24 hours)
2. **Processing**: Extracts transcripts and converts markdown to structured data
3. **Digest Creation**: AI generates concise summaries for each article
4. **Ranking**: Curator agent ranks articles based on user profile (0-10 score)
5. **Email Generation**: Creates personalized email with top 10 articles
6. **Delivery**: Sends digest via Gmail SMTP

## 🌐 Deploy to Render

### One-Click Deploy

1. **Connect GitHub**
   - Go to [Render Dashboard](https://render.com)
   - New → Blueprint
   - Connect your `AI_NEWS_AGGREGATOR` repository

2. **Configure Environment Variables**
   - `GEMINI_API_KEY`: Your Google Gemini API key
   - `MY_EMAIL`: Your Gmail address
   - `APP_PASSWORD`: Your Gmail app password

3. **Deploy**
   - Render will automatically deploy using `render.yaml`
   - Cron job runs daily at midnight UTC
   - Persistent disk stores SQLite database

### Cost: **100% FREE**
- Render: Free cron job (750 hours/month)
- Google Gemini: Free tier (1M tokens/day)
- Gmail: Free SMTP
- Storage: 1GB free persistent disk

## 📊 Project Structure

```
AI_NEWS_AGGREGATOR/
├── app/
│   ├── agent/              # AI agents (curator, digest, email)
│   │   ├── gemini_helper.py    # Google Gemini API wrapper
│   │   ├── curator_agent.py    # Content ranking
│   │   ├── digest_agent.py     # Summary generation
│   │   └── email_agent.py      # Email composition
│   ├── database/           # SQLite models and connection
│   ├── profiles/           # User preference profiles
│   ├── scrapers/           # Content scrapers (OpenAI, Anthropic, YouTube)
│   ├── services/           # Processing pipelines
│   └── .env                # Environment configuration
├── main.py                 # Entry point
├── requirements.txt        # Python dependencies
└── render.yaml            # Render deployment config
```

## 🎯 Usage Examples

**Process last 24 hours (default)**
```bash
python main.py
```

**Process last 48 hours, get top 15 articles**
```bash
python main.py 48 15
```

## 🔑 Getting API Keys

### Google Gemini API Key
1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with Google account
3. Click "Create API Key"
4. Copy and save the key

### Gmail App Password
1. Enable 2-Step Verification: [Google Security](https://myaccount.google.com/security)
2. Go to [App Passwords](https://myaccount.google.com/apppasswords)
3. Select "Mail" and "Windows Computer"
4. Generate and copy the 16-character password

## 🛠️ Technologies Used

- **Python 3.11+**
- **Google Gemini 2.5 Flash** - AI content analysis
- **SQLAlchemy** - Database ORM
- **SQLite** - Lightweight database
- **BeautifulSoup4** - Web scraping
- **Pydantic** - Data validation
- **yt-dlp** - YouTube metadata extraction
- **youtube-transcript-api** - Transcript fetching

## 📝 License

MIT License - Feel free to use and modify!

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📧 Support

For issues or questions:
- Open a GitHub issue
- Check existing issues for solutions

## 🙏 Acknowledgments

- Google Gemini for free AI API
- OpenAI and Anthropic for excellent AI content
- YouTube creators for educational AI content

---

Made with ❤️ by [Abhiram678](https://github.com/Abhiram678)
