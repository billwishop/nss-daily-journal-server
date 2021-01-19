CREATE TABLE `Entry` (
    `id`    INTEGER NOT NOT NULL PRIMARY KEY AUTOINCREMENT,
    `date`  Date,
    `subject`   TEXT NOT NULL,
    `entry` TEXT NOT NULL,
    `mood_id`   INTEGER NOT NULL
    FOREIGN KEY(`mood_id`) REFERENCES `Mood`(`id`)
);

CREATE TABLE `Mood` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `mood`  TEXT NOT NULL
)