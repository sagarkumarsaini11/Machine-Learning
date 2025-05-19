import ast

def parse_features(text):
    return [i['name'] for i in ast.literal_eval(text)]

def parse_cast(text):
    return [i['name'] for i in ast.literal_eval(text)][:3]

def parse_crew(text):
    return [i['name'] for i in ast.literal_eval(text) if i['job'] == 'Director']


def combine_tags(row):
    return row['overview'] + ' ' + ' '.join(row['genres']) + ' ' + ' '.join(row['keywords']) + \
           ' ' + ' '.join(row['cast']) + ' ' + ' '.join(row['crew'])