interface EventListProps {
  events: any[];
}

export default function EventList({ events }: EventListProps) {
  if (!events || events.length === 0) {
    return <p>No events found. Try another search.</p>;
  }

  return (
    <ul className="space-y-4">
      {events.map((event, idx) => (
        <li
          key={idx}
          className="border p-4 rounded shadow-sm hover:shadow-md transition"
        >
          <p className="font-semibold">{event}</p>
        </li>
      ))}
    </ul>
  );
}
