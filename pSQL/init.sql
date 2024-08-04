CREATE TABLE partition (
  Id SERIAL PRIMARY KEY,
  name CHARACTER VARYING(150),
  description CHARACTER VARYING(150),
  color CHARACTER VARYING(150)
);

CREATE TABLE priority (
    Id SERIAL PRIMARY KEY,
    name CHARACTER VARYING(150),
    color CHARACTER VARYING(150),
);

CREATE TABLE task (
    Id SERIAL PRIMARY KEY,
    partition_id INTEGER REFERENCES partition (Id),
    priority_id INTEGER REFERENCES priority (Id),
    name CHARACTER VARYING(150),
    description CHARACTER VARYING(150),
    preview_file_id INTEGER REFERENCES file (Id),

    status INTEGER CHECK(0 >= status AND status <= 2)
    --0 - просто сделать 
    --1 - сделать до...
    --2 - делать каждый день в...
);

CREATE TABLE file (
    Id SERIAL PRIMARY KEY,
    file_path CHARACTER VARYING(150),
    task_id INTEGER REFERENCES task (Id)
);