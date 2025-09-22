"use client";

import { useState } from "react";

interface SearchFormProps {
  onSearch: (keyword: string, location: string) => void;
}

export default function SearchForm({ onSearch }: SearchFormProps) {
  const [keyword, setKeyword] = useState("AI");
  const [location, setLocation] = useState("San Francisco");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSearch(keyword, location);
  };

  return (
    <form onSubmit={handleSubmit} className="flex gap-4 mb-6">
      <input
        type="text"
        placeholder="Keyword (e.g. AI, ML)"
        value={keyword}
        onChange={(e) => setKeyword(e.target.value)}
        className="border p-2 rounded w-1/3"
      />
      <input
        type="text"
        placeholder="Location (e.g. San Francisco)"
        value={location}
        onChange={(e) => setLocation(e.target.value)}
        className="border p-2 rounded w-1/3"
      />
      <button
        type="submit"
        className="bg-blue-600 text-white px-4 py-2 rounded"
      >
        Search
      </button>
    </form>
  );
}
