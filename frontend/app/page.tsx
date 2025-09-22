"use client";

import { useState } from "react";
import SearchForm from "../components/SearchForm";
import EventList from "../components/EventList";

export default function HomePage() {
  const [events, setEvents] = useState<string[]>([]);

  const handleSearch = async (keyword: string, location: string) => {
    try {
      const res = await fetch(
        `http://127.0.0.1:8000/events?keyword=${keyword}&location=${location}`
      );
      const data = await res.json();
      setEvents(data.results.documents[0]); // adjust depending on your backend JSON
    } catch (err) {
      console.error("Error fetching events:", err);
    }
  };

  return (
    <main className="max-w-3xl mx-auto p-6">
      <h1 className="text-3xl font-bold mb-6">Event & Meetup Mapper</h1>
      <SearchForm onSearch={handleSearch} />
      <EventList events={events} />
    </main>
  );
}
