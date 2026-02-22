WITH dept AS (
  SELECT
    DATE_FORMAT(pay_date, '%Y-%m') AS pay_month,
    e.department_id,
    AVG(amount) AS dept_avg
  FROM Salary s
  JOIN Employee e
    ON s.employee_id = e.employee_id
  GROUP BY DATE_FORMAT(pay_date, '%Y-%m'), e.department_id
),
comp AS (
  SELECT
    DATE_FORMAT(pay_date, '%Y-%m') AS pay_month,
    AVG(amount) AS comp_avg
  FROM Salary
  GROUP BY DATE_FORMAT(pay_date, '%Y-%m')
)
SELECT
  d.pay_month,
  d.department_id,
  CASE
    WHEN d.dept_avg > c.comp_avg THEN 'higher'
    WHEN d.dept_avg < c.comp_avg THEN 'lower'
    ELSE 'same'
  END AS comparison
FROM dept d
JOIN comp c
  ON d.pay_month = c.pay_month
ORDER BY d.pay_month, d.department_id;
