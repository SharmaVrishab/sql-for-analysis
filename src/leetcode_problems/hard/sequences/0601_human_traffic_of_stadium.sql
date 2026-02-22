WITH ranked AS (
  SELECT
    id,
    visit_date,
    people,
    id - ROW_NUMBER() OVER (ORDER BY id) AS grp
  FROM Stadium
  WHERE people >= 100
),
valid_groups AS (
  SELECT grp
  FROM ranked
  GROUP BY grp
  HAVING COUNT(*) >= 3
)
SELECT r.id, r.visit_date, r.people
FROM ranked r
JOIN valid_groups g
  ON r.grp = g.grp
ORDER BY r.visit_date;
