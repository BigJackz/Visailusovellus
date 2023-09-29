CREATE TABLE questions (id SERIAL PRIMARY KEY, question TEXT);

CREATE TABLE answers (id SERIAL PRIMARY KEY, question_id INTEGER REFERENCES questions, answer1 TEXT, answer2 TEXT, answer3 TEXT, answer4 TEXT);

CREATE TABLE correct (id SERIAL PRIMARY KEY, question_id INTEGER REFERENCES questions, answer TEXT);


