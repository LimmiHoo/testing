# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: MovieQueue
TEMPLATE_REGISTRY = {
    'action_movie': {'priority': 1, 'rating': 0, 'genres': ['Action', 'Thriller']},
    'comedy_drama': {'priority': 2, 'rating': 0, 'genres': ['Comedy', 'Drama']},
    'sci_fi': {'priority': 1, 'rating': 0, 'genres': ['Sci-Fi', 'Adventure']},
}

def add_from_template(name, template_name='action_movie'):
    tmpl = TEMPLATE_REGISTRY.get(template_name)
    if not tmpl:
        return None
    record = {
        'name': name or f'{template_name.replace("_", " ")}',
        'priority': tmpl['priority'],
        'rating': 0,
        'genres': list(tmpl['genres']),
        'watched': False,
        'history': [],
        'date_added': datetime.now().strftime('%Y-%m-%d'),
    }
    return record

if __name__ == '__main__':
    m1 = add_from_template('Fast-Paced Action', 'action_movie')
    print(m1)
    m2 = add_from_template('Funny Drama', 'comedy_drama')
    print(m2)
