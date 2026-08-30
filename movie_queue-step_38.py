# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: MovieQueue
def test_edge_cases():
    q = MovieQueue()
    q.add_movie("A", 1, 8, "Drama", "2020-01-01", False)
    q.add_movie("B", 1, 9, "Action", "2020-02-01", False)
    q.add_movie("C", 1, 7, "SciFi", "2020-03-01", False)

    assert q.next_movie() == "B"
    assert q.next_movie() == "A"
    assert q.next_movie() == "C"
    assert q.next_movie() is None

    q.add_movie("D", 1, 0, "Drama", "2020-01-01", False)
    q.add_movie("E", 1, 100, "Action", "2020-01-01", False)
    assert q.next_movie() == "E"
    assert q.next_movie() == "D"
    assert q.next_movie() is None

    q.add_movie("F", -5, 5, "Horror", "2020-01-01", False)
    q.add_movie("G", 1, 5, "Horror", "2020-01-01", False)
    q.add_movie("H", 0, 5, "Horror", "2020-01-01", False)
    assert q.next_movie() == "G"
    assert q.next_movie() == "H"
    assert q.next_movie() == "F"
    assert q.next_movie() is None

    q.add_movie("I", 1, 8, "Drama", "2020-01-01", True)
    q.add_movie("J", 1, 8, "Drama", "2020-01-01", False)
    assert q.next_movie() == "J"
    assert q.next_movie() == "I"
    assert q.next_movie() is None

    q.add_movie("K", 1, 8, "Drama", "2020-01-01", True)
    q.add_movie("L", 1, 8, "Drama", "2020-01-01", True)
    assert q.next_movie() is None

    q.add_movie("M", 1, 8, "Drama", "2020-01-01", False)
    q.add_movie("N", 1, 8, "Drama", "2020-01-01", False)
    q.add_movie("O", 1, 8, "Drama", "2020-01-01", False)
    q.add_movie("P", 1, 8, "Drama", "2020-01-01", False)
    q.add_movie("Q", 1, 8, "Drama", "2020-01-01", False)
    q.add_movie("R", 1, 8, "Drama", "2020-01-01", False)
    assert q.next_movie() == "M"
    assert q.next_movie() == "N"
    assert q.next_movie() == "O"
    assert q.next_movie() == "P"
    assert q.next_movie() == "Q"
    assert q.next_movie() == "R"
    assert q.next_movie() is None

    q.add_movie("S", 1, 8, "Drama", "2020-01-01", False)
    assert q.next_movie() == "S"
    assert q.next_movie() is None

    q.add_movie("T", 1, 8, "Drama", "2020-01-01", False)
    q.add_movie("U", 1, 8, "Drama", "2020-01-01", False)
    q.add_movie("V", 1, 8, "Drama", "2020-01-01", False)
    assert q.next_movie() == "T"
    assert q.next_movie() == "U"
    assert q.next_movie() == "V"
    assert q.next_movie() is None
