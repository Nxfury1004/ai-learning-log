repos = [
    {
        'name': 'transformers',
        'language': 'Python',
        'stars': 130000,
        'topics': ['nlp', 'deep-learning', 'pytorch'],
        'owner': {'login': 'huggingface', 'type': 'Organization'},
    },
    {
        'name': 'react',
        'language': 'JavaScript',
        'stars': 228000,
        'topics': ['ui', 'frontend'],
        'owner': {'login': 'facebook', 'type': 'Organization'},
    },
    {
        'name': 'ohmyzsh',
        'language': 'Shell',
        'stars': 175000,
        'topics': [],
        'owner': {'login': 'ohmyzsh', 'type': 'Organization'},
    },
    {
        'name': 'scikit-learn',
        'language': 'Python',
        'stars': 60000,
        'topics': ['machine-learning', 'data-science'],
        'owner': {'login': 'scikit-learn', 'type': 'Organization'},
    },
    {
        'name': 'pytorch',
        'language': 'Python',
        'stars': 84000,
        'topics': ['deep-learning', 'tensor', 'gpu'],
        'owner': {'login': 'pytorch', 'type': 'Organization'},
    },
]

# TODO 1: print "<name> by <owner login> -- <stars> stars" for every repo

for repo in repos:
    name = repo['name']
    owner_login = repo['owner']['login']
    stars = repo['stars']
    print(f"{name} by {owner_login} -- {stars} stars")

# TODO 2: build a SET of every unique language across all repos (comprehension)
unique_languages = {repo['language'] for repo in repos}

# TODO 3: build a dict counting how many repos use each language
#   e.g. {'Python': 3, 'JavaScript': 1, 'Shell': 1}
counts = {}
for repo in repos:
    counts[repo['language']] = counts.get(repo['language'], 0) + 1
#   (classic pattern: counts[key] = counts.get(key, 0) + 1)
print(counts)

# TODO 4: print only repos with more than 100_000 stars, sorted by stars descending
for repo in sorted(repos, key = lambda r:r['stars'] , reverse=True):
    if repo['stars'] > 100_000:
        print(f"{repo['name']} by {repo['owner']['login']} -- {repo['stars']} stars")

# TODO 5: build a set of every unique topic used across ALL repos (flatten nested lists)
unique_topics = {topic for repo in repos for topic in repo['topics']}
print(unique_topics)