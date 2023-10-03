-- Таблица корзины
-- с. 285

CREATE TABLE IF NOT EXISTS user_card(
    user_id INT NOT NULL,
    product_id INT NOT NULL
);

INSERT INTO user_card VALUES (1, 1);
INSERT INTO user_card VALUES (1, 2);
INSERT INTO user_card VALUES (1, 3);
INSERT INTO user_card VALUES (2, 1);
INSERT INTO user_card VALUES (2, 2);
INSERT INTO user_card VALUES (2, 5);
