-- Анализ цен по категориям
SELECT
    category_name,
    COUNT(*) AS item_count,
    AVG(price) AS avg_price,
    MAX(price) AS max_price
FROM ebay
GROUP BY category_name
ORDER BY avg_price DESC;

-- Анализ пропусков
SELECT
    snapshot_dt,
    COUNT(*) AS total_rows,
    SUM(CASE WHEN estimated_delivery_days IS NULL THEN 1 ELSE 0 END) AS null_count
FROM ebay
GROUP BY snapshot_dt;
