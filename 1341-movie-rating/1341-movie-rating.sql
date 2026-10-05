WITH UserRank AS (
    SELECT
        u.name,
        COUNT(*) AS rating_count,
        RANK() OVER (
            ORDER BY COUNT(*) DESC, u.name ASC
        ) AS rnk
    FROM Users u
    JOIN MovieRating mr
        ON u.user_id = mr.user_id
    GROUP BY u.user_id, u.name
),

MovieRank AS (
    SELECT
        m.title,
        AVG(mr.rating) AS avg_rating,
        RANK() OVER (
            ORDER BY AVG(mr.rating) DESC, m.title ASC
        ) AS rnk
    FROM Movies m
    JOIN MovieRating mr
        ON m.movie_id = mr.movie_id
    WHERE mr.created_at >= '2020-02-01'
      AND mr.created_at < '2020-03-01'
    GROUP BY m.movie_id, m.title
)

SELECT name AS results
FROM UserRank
WHERE rnk = 1

UNION ALL

SELECT title AS results
FROM MovieRank
WHERE rnk = 1;