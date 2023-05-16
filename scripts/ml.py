import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


df = pd.read_csv('../datasets/movies_ml.csv', low_memory=False)
data = df.copy()
data = data.drop_duplicates(subset = 'title')

C = data['vote_average'].mean()
print(C)

m = data['vote_count'].quantile(0.90)
print(m)

m = data['vote_count'].quantile(0.90)
print(m)

data = data.loc[data['vote_count'] >= m]

def weighted_rating(x, m=m, C=C):
    v = x['vote_count']
    R = x['vote_average']
    # Calculation based on the IMDB formula
    return (v/(v+m) * R) + (m/(m+v) * C)

data['score'] = data.apply(weighted_rating, axis=1)

data = data.sort_values('score', ascending = False)

tfidf = TfidfVectorizer(stop_words='english')

data['overview'] = data['overview'].fillna('')

tfidf_matrix = tfidf.fit_transform(data['overview'])

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

data.reset_index(drop = True, inplace = True)

index = pd.Series(data.index, index = data['title']).drop_duplicates()

















