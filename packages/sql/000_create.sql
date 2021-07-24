drop table if exists notes;
drop table if exists details;
CREATE TABLE details(
    id serial PRIMARY KEY,
    username TEXT,
    email TEXT,
    updated date,
    password VARCHAR(20)
);

CREATE TABLE notes(
    id serial PRIMARY KEY,
    notes TEXT,
    usr INTEGER,
    time date,
    FOREIGN KEY (usr) REFERENCES details(id)
);
