CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
)
DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Mayra', 33);
INSERT INTO Ages (name, age) VALUES ('Honie', 28);
INSERT INTO Ages (name, age) VALUES ('Benjamin', 34);
INSERT INTO Ages (name, age) VALUES ('Connal', 14);

SELECT hex(name || age) AS X FROM Ages ORDER BY X
