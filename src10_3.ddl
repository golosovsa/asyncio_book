-- Таблица избранных товаров пользователя
-- с. 286

CREATE TABLE IF NOT EXISTS user_favorite(
    user_id INT NOT NULL,
    product_id INT NOT NULL
);

INSERT INTO user_favorite VALUES (1, 1);
INSERT INTO user_favorite VALUES (1, 2);
INSERT INTO user_favorite VALUES (1, 3);
INSERT INTO user_favorite VALUES (3, 1);
INSERT INTO user_favorite VALUES (3, 2);
INSERT INTO user_favorite VALUES (3, 3);
