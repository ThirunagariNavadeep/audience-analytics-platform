from app.feature_engineering.synthetic_feature_builder import (
    SyntheticFeatureBuilder
)

from app.repository.feature_repository import (
    FeatureRepository
)

from app.recommender.similarity import (
    SimilarityEngine
)

repo = FeatureRepository()

movies = repo.load_analytics_movies()

builder = SyntheticFeatureBuilder()

features = builder.build(movies)

engine = SimilarityEngine()

scaled = engine.fit(

    features,

    [
        "average_rating",
        "rating_count",
        "movie_age",
        "genre_count",
        "rating_confidence"
    ]

)

distances, indices = engine.nearest_movies(
    scaled,
    movie_index=0,
    k=5
)

print(indices)
print(distances)