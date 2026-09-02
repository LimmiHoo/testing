# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: MovieQueue
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="MovieQueue CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    # add
    p_add = sub.add_parser("add", help="Add movie/series")
    p_add.add_argument("--title", required=True)
    p_add.add_argument("--priority", type=int, default=1)
    p_add.add_argument("--rating", type=float, default=0.0)
    p_add.add_argument("--genre", required=True)
    p_add.add_argument("--watched", action="store_true")
    p_add.add_argument("--watched-date", type=str, default="")

    # list
    sub.add_parser("list", help="List all items")

    # show
    p_show = sub.add_parser("show", help="Show details of one item")
    p_show.add_argument("--title", required=True)

    # remove
    p_rm = sub.add_parser("remove", help="Remove an item")
    p_rm.add_argument("--title", required=True)

    # done
    p_done = sub.add_parser("done", help="Mark as watched")
    p_done.add_argument("--title", required=True)
    p_done.add_argument("--rating", type=float, default=0.0)

    return parser.parse_args()
