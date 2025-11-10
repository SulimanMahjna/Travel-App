
CREATE TABLE "users" (
  "id" uuid PRIMARY KEY,
  "username" varchar,
  "email" varchar,
  "password" text,
  "created_at" timestamp DEFAULT 'now()',
  "udated_at" timestamp DEFAULT 'now()'
);

CREATE TABLE "places" (
  "id" uuid PRIMARY KEY,
  "name" varchar,
  "descreption" text,
  "location" text,
  "features" text,
  "created_at" timestamp DEFAULT 'now()',
  "udated_at" timestamp DEFAULT 'now()'
);

CREATE TABLE "favorite" (
  "id" uuid PRIMARY KEY,
  "user_id" uuid,
  "place_id" uuid,
  "created_at" timestamp DEFAULT 'now()',
  "udated_at" timestamp DEFAULT 'now()'
);

CREATE TABLE "recommended" (
  "id" uuid PRIMARY KEY,
  "place_id" uuid,
  "name" varchar,
  "descreption" text,
  "location" text,
  "features" text,
  "created_at" timestamp DEFAULT 'now()',
  "udated_at" timestamp DEFAULT 'now()'
);

ALTER TABLE "favorite" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "favorite" ADD FOREIGN KEY ("place_id") REFERENCES "places" ("id");

ALTER TABLE "recommended" ADD FOREIGN KEY ("place_id") REFERENCES "places" ("id");