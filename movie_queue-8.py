# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: MovieQueue
def print_menu():
    print("\n=== MovieQueue Menu ===")
    print("1. Add movie/series (title, type, genre)")
    print("2. View queue with priorities and ratings")
    print("3. Update rating or priority for an item")
    print("4. Mark as watched / add to history")
    print("5. Filter by genre")
    print("6. Exit")

def main():
    while True:
        print_menu()
        choice = input("\nSelect action (1-6): ").strip()
        if choice == "1":
            title = input("Title: ")
            item_type = input("Type (movie/series): ").lower()
            genre = input("Genre: ")
            priority = int(input("Priority (higher is more urgent): "))
            rating = float(input("Rating (0-10, 0 if not rated): "))
            movie_queue.add_item(title, item_type, genre, priority, rating)
        elif choice == "2":
            print("\n--- Current Queue ---")
            for i, item in enumerate(movie_queue.items, 1):
                status = "[Watched]" if item.watched else "[Pending]"
                print(f"{i}. [{item.type}] {status} | {item.title} ({item.genre}) | Priority: {item.priority} | Rating: {item.rating}/10")
        elif choice == "3":
            idx = int(input("Item number to update (from list above): ")) - 1
            if movie_queue.items and idx < len(movie_queue.items):
                item = movie_queue.items[idx]
                print(f"Current: {item.title} | Rating: {item.rating}")
                new_rating = input(f"New rating ({'keep current' if not item.watched else 'N/A'}): ").strip()
                if new_rating.lower() != "n/a":
                    movie_queue.items[idx].rating = float(new_rating)
        elif choice == "4":
            idx = int(input("Item number to mark as watched: ")) - 1
            if movie_queue.items and idx < len(movie_queue.items):
                item = movie_queue.items[idx]
                item.watched = True
                print(f"Marked '{item.title}' as watched.")
        elif choice == "5":
            genre_filter = input("Filter by genre: ").lower()
            filtered = [i for i, item in enumerate(movie_queue.items) if genre_filter.lower() in item.genre]
            if filtered:
                print("\n--- Filtered Results ---")
                for idx in filtered:
                    print(f"{idx+1}. {movie_queue.items[idx].title} ({movie_queue.items[idx].genre})")
        elif choice == "6":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
