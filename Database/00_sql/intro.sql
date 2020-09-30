-- 모든 컬럼 가져오기
SELECT *
FROM table_name;

-- 특정 컬럼 가져오기
SELECT column1, column2
FROM table_name;

-- 원하는 개수만큼 가져오기
SELECT column1, column2
FROM table_name LIMIT num;

-- 특정 위치에서부터 원하는 개수만큼 가져오기
SELECT column1, column2
FROM table_name LIMIT my_num OFFSET num;

-- 특정한 값만 가져오기 (조건 설정)
SELECT column1, column2
FROM table_name
WHERE column=value;

-- 중복 없이 가져오기
SELECT DISTINCT column
FROM table_name;

-- 데이터 삭제하기
DELETE FROM table_name
WHERE condition;

-- AUTOINCREMENT
CREATE TABLE table_name (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL
);

-- 수정하기
UPDATE table_name
SET column1=value1, column2=value2
WHERE condition;

-- WHERE 조건 심화
SELECT *
FROM users
WHERE age>=30;

SELECT first_name
FROM users
WHERE age>=30;

SELECT last_name, age
FROM users
WHERE age>=30 AND last_name='김';

-- COUNT 표현식
SELECT COUNT(*)
FROM users;

-- AVG, SUM, MIN, MAN 표현식
SELECT AVG(age)
FROM users
WHERE age>=30;

SELECT MAX(balance), forst_name
FROM users;

SELECT AVG(balance)
FROM users
WHERE age>=30;

-- LIKE
-- users에서 20대인 사람?
SELECT *
FROM users
WHERE age LIKE '6_';

SELECT *
FROM users
WHERE phone LIKE '02-%';

SELECT *
FROM users
WHERE first_name LIKE '%준';

SELECT *
FROM users
WHERE phone LIKE '%-5114-%';

-- ORDER
SELECT *
FROM users
ORDER BY age ASC LIMIT 10;

SELECT *
FROM users
ORDER BY age ASC, last_name ASC LIMIT 10;

SELECT last_name, first_name, balance
FROM users
ORDER BY balance DESC LIMIT 10;

-- GROUP BY
SELECT COUNT(last_name), last_name
FROM users
GROUP BY last_name;

-- AS
SELECT COUNT(last_name) AS name_count, last_name
FROM users
GROUP BY last_name;

--테이블 이름 변경
ALTER TABLE articles
RENAME TO news;

-- 새로운 컬럼 추가
ALTER TABLE news
ADD COLUMN created_at TEXT NOT NULL;

-- datetime()
INSERT INTO news
VALUES ('글', '내용', datetime('now'));

-- 새로운 컬럼 추가 (Default 값 추가)
ALTER TABLE news
ADD COLUMN subtitle TEXT NOT NULL DEFAULT 1;