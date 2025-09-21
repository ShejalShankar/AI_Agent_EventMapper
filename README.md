# Event & Meetup Mapper (RAG + Maps)

## 📌 Introduction
Event & Meetup Mapper is a full-stack application designed to make discovering local tech events smarter and more convenient. This project tackles the problem by combining AI-powered relevance filtering with interactive mapping, helping users quickly find the events that matter most to them and understand how practical it is to attend. It transforms scattered event data into a personalized, location-aware experience.

## 💡 Workflow
**Data Collection** – The backend scrapes raw event details such as titles, descriptions, dates, and locations.

**Intelligent Filtering (AI Agent)** – Events are enriched with embeddings (all-MiniLM-L6-v2) and stored in ChromaDB, allowing the system to filter and rank them by how closely they match user interests.

**Geospatial Mapping** – Event addresses are geocoded into coordinates and plotted on an interactive map, with the option to apply commute-distance filters for practicality.

**Backend Services (FastAPI)** – A clean REST API powers the entire pipeline, exposing endpoints for event search, AI-driven filtering, and map generation.

**User Interface (Next.js + React)** – On the frontend, users can search by keyword and location, browse a ranked list of events, and switch to a map view for a spatial perspective.

## 🛠️ Tech Stack
- **AI/ML** – SentenceTransformers (`all-MiniLM-L6-v2`), ChromaDB  
- **Backend** – FastAPI, Uvicorn  
- **Scraping** – Requests, BeautifulSoup, Regex  
- **Mapping** – Folium, Geopy  
- **Frontend** – Next.js (React + TypeScript), TailwindCSS  

## 🎯 Why This Project
This project demonstrates how to build a practical **AI-powered full-stack application** by combining:  
- Web scraping + NLP (data collection & cleaning)  
- Retrieval-Augmented Generation (intelligent filtering)  
- API design with FastAPI (backend services)  
- Interactive mapping (geospatial visualization)  
- Modern frontend development (React/Next.js UI)  

It highlights skills across **AI, full-stack development, and deployment**, making it a strong showcase for real-world engineering.  
