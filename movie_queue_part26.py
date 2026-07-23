# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: MovieQueue
def demo():
    print("=== MovieQueue Demo ===")
    q = Queue()
    for title in ["Inception", "The Dark Knight", "Interstellar", "Dune", "Arrival"]:
        m = Movie(title, genre="Sci-Fi", priority=3, rating=0)
        q.add(m)
    print(f"Queue size: {q.size()}")
    print("Top 5:", [f"{m.title}(P{m.priority})" for m in q.top(5)])
    m = q.get_top()
    m.rate(8.5, notes="Mind-blowing visuals")
    print(f"After rating: {m.title} -> {m.rating}")
    seen = m.mark_seen()
    print(f"Seen: {seen}, History: {len(m.history)}")
    q.save("demo.db")
    print("Saved demo.db")

    from sqlite3 import connect as sq_connect
    conn = sq_connect("demo_out.db")
    cur = conn.cursor()
    for t in ["Titanic", "The Godfather", "Pulp Fiction"]:
        m2 = Movie(t, genre="Drama", priority=5, rating=0)
        q2 = Queue()
        q2.add(m2); m2.rate(9.0); m2.mark_seen()
    q2.save("demo_out.db")
    cur.execute("SELECT * FROM movies ORDER BY pri DESC LIMIT 3")
    rows = cur.fetchall()
    print("Top drama movies:", [(r[1], r[4]) for r in rows])

demo()
