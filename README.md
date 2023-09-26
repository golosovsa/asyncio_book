# Книга "Asyncio и конкурентное программирование на Python" Мэтью Фаулер
Ф28: Asyncio и конкурентное программирование на Python/пер. с англ. А.А. Слинкина. -М.: ДМК Пресс, 2022. - 398 с.: ил.
ISBN 978-5-93700-166-5

## Прогресс

* 25.09.2023: 75 страница (+18,8%)
* 26.09.2023: 132 страница (+14,3%)

## Примечания

### Обновление от 26.09.2023

Для взаимодействия с базой данных в 5 части книге, был добавлен Makefile с командами

* `make run-postgres` - запустить базу данных postgres
* `make stop-postgres` - остановить и удалить контейнер с базой данных

При этом необходимо создать файл `secrets.env` 
и записать туда переменную окружения `POSTGRES_PASSWORD=<придумайте пароль>`