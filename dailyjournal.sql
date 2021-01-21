CREATE TABLE `Entry` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `date`  Date,
    `subject`   TEXT NOT NULL,
    `entry` TEXT NOT NULL,
    `mood_id`   INTEGER NOT NULL,
    FOREIGN KEY(`mood_id`) REFERENCES `Mood`(`id`)
);

CREATE TABLE `Mood` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `mood`  TEXT NOT NULL
);

INSERT INTO `Mood` VALUES (null, 'happy');
INSERT INTO `Mood` VALUES (null, 'sad');
INSERT INTO `Mood` VALUES (null, 'angry');
INSERT INTO `Mood` VALUES (null, 'content');

INSERT INTO `Entry` VALUES (null, '1/1/21', 'Python', 'New year, new language', '1');
INSERT INTO `Entry` VALUES (null, '1/2/21', 'SQL', 'New year, new language', '2');
INSERT INTO `Entry` VALUES (null, '1/3/21', 'Python', 'New year, new language', '3');
INSERT INTO `Entry` VALUES (null, '1/4/21', 'SQL', 'New year, new language', '4');


