# Event & Meetup Mapper (RAG + Maps)

## 📌 Project Overview
Event & Meetup Mapper is a full-stack application that helps users discover the most relevant tech events in their area.  
Traditional platforms like Meetup or Eventbrite show long lists of events, but they don’t:  
- Filter results intelligently by your interests.  
- Show how far events are from you or how easy they are to attend.  

This project solves that by combining **AI-powered filtering** with **interactive maps**.  

## 💡 How It Works
1. **Scraping Layer** – Collects raw event data (title, description, date, location) from platforms like Eventbrite and Meetup.  
2. **AI Agent (RAG)** – Uses sentence embeddings (`all-MiniLM-L6-v2`) and a vector database (ChromaDB) to filter and rank events by relevance to user interests (e.g., AI, ML, Cloud).  
3. **Mapping Layer** – Converts event addresses into coordinates and plots them on an interactive map, with optional commute-distance filters.  
4. **Frontend (Next.js + React)** – Provides a clean UI where users can:  
   - Enter keywords and a location.  
   - View the most relevant events in a list with dates and links.  
   - Switch to a map view to see event locations visually.  
5. **Backend (FastAPI)** – Exposes REST APIs for event search, relevance filtering, and map generation.  

## 🛠️ Tech Stack
- **AI/ML** – SentenceTransformers (`all-MiniLM-L6-v2`), ChromaDB  
- **Backend** – FastAPI, Uvicorn  
- **Scraping** – Requests, BeautifulSoup, Regex  
- **Mapping** – Folium, Geopy  
- **Frontend** – Next.js (React + TypeScript), TailwindCSS  
- **Deployment** – (Planned) Render / Vercel / Hugging Face Spaces  

## 🎯 Why This Project
This project demonstrates how to build a practical **AI-powered full-stack application** by combining:  
- Web scraping + NLP (data collection & cleaning)  
- Retrieval-Augmented Generation (intelligent filtering)  
- API design with FastAPI (backend services)  
- Interactive mapping (geospatial visualization)  
- Modern frontend development (React/Next.js UI)  

It highlights skills across **AI, full-stack development, and deployment**, making it a strong showcase for real-world engineering.  
