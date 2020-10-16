--Initial Viewing

-- View first 20 lines of stream table
SELECT *
FROM stream
LIMIT 20;

-- view first 20 lines of chat table
SELECT *
FROM chat
LIMIT 20;

-- Unique games in stream table
SELECT DISTINCT game
FROM stream;

-- Unique channels in the stream table
SELECT DISTINCT channel
FROM stream;

-- Aggregate Functions

-- Most popular streamed games
SELECT game, COUNT(*)
FROM stream
GROUP BY game
ORDER BY COUNT(*) DESC;

-- LoL viewership origin
SELECT country, COUNT(*)
FROM stream
WHERE game == "League of Legends"
GROUP BY country
ORDER BY COUNT(*) DESC;

-- Source the user view by
SELECT player, COUNT(*)
FROM stream
GROUP BY player
ORDER BY COUNT(*) DESC;

-- Group games into a new column 'genre'
SELECT game,
  CASE
    WHEN game = 'League of Legends'
      THEN 'MOAB'
    WHEN game = 'Dota 2'
      THEN 'MOAB'
    WHEN game = 'Heroes of the Storm'
      THEN 'MOAB'
    WHEN game = 'DayZ'
      THEN 'Survival'
    WHEN game = 'Survival Evolved'
      THEN 'Survival'
    WHEN game = 'Counter-Strike: Global Offensive'
      THEN 'FPS'
    ELSE 'Other'
  END AS 'genre',
  COUNT(*)
FROM stream
GROUP BY game
ORDER BY COUNT(*) DESC;

-- How does view count change in the course of a day?

SELECT time
FROM stream
LIMIT 10;
-- format is YYYY-MM-DD HH:MM:SS

SELECT time,
  strftime('%S', time)
FROM stream
GROUP BY 1
LIMIT 20;
-- grab the number of seconds from the time

-- Return hours of time, view count for each hour, for UK
SELECT strftime('%H', time), COUNT(*)
FROM stream
WHERE country = 'GB'
GROUP BY 1;

-- Joining the two tables

SELECT *
FROM stream
JOIN chat
  ON stream.device_id = chat.device_id;
