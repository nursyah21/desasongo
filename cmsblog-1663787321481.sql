
CREATE TABLE blog
(
  blog_id      serial NOT NULL,
  data         TEXT   NOT NULL,
  release      TEXT   NOT NULL,
  link         TEXT   NOT NULL,
  views        INT    NOT NULL,
  preview_data TEXT   NOT NULL,
  PRIMARY KEY (blog_id)
);

CREATE TABLE comment
(
  comment_id serial NOT NULL,
  url        TEXT   NOT NULL,
  name       TEXT   NOT NULL,
  comment    TEXT   NOT NULL,
  created_at TEXT   NOT NULL,
  PRIMARY KEY (comment_id)
);

CREATE TABLE hidroponik
(
  id_hidroponik serial NOT NULL,
  tangki1       FLOAT  NOT NULL,
  tangki2       FLOAT  NOT NULL,
  tangki3       FLOAT  NOT NULL,
  tds           FLOAT  NOT NULL,
  pompa_1       BOOL   NOT NULL,
  pompa_2       BOOL   NOT NULL,
  pompa_3       BOOL   NOT NULL,
  pompa_4       BOOL   NOT NULL,
  ppm           INT    NOT NULL,
  auto          BOOL   NOT NULL,
  PRIMARY KEY (id_hidroponik)
);

CREATE TABLE shop
(
  shop_id serial NOT NULL,
  url     TEXT   NOT NULL,
  name    TEXT   NOT NULL,
  price   TEXT   NOT NULL,
  img_url TEXT   NOT NULL,
  PRIMARY KEY (shop_id)
);

CREATE TABLE users
(
  users_id   serial NOT NULL,
  name       TEXT   NOT NULL,
  pass       TEXT   NOT NULL,
  created_at TEXT   NULL    ,
  PRIMARY KEY (users_id)
);

CREATE TABLE visited
(
  visited_id serial NOT NULL,
  time       TEXT   NOT NULL,
  counts     INT    NOT NULL,
  PRIMARY KEY (visited_id)
);
