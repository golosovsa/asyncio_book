# Книга "Asyncio и конкурентное программирование на Python" Мэтью Фаулер
Ф28: Asyncio и конкурентное программирование на Python/пер. с англ. А.А. Слинкина. -М.: ДМК Пресс, 2022. - 398 с.: ил.
ISBN 978-5-93700-166-5

## Прогресс

* 25.09.2023: 75 страница (+18.8%)
* 26.09.2023: 132 страница (+14.3%)
* 27.09.2023: 190 страница (+14.6%)
* 28.09.2023: 240 страница (+12.6%)
* 29.09.2023: 246 страница (+1.5%)
* 01.10.2023: 253 страница (+1.8%)
* 03.10.2023 (до обеда): 262 страница (+2.3%)
* 03.10.2023 (после обеда): 286 страница (+6%)

## Примечания

### Обновление от 03.10.23

Добавил в Makefile команду `make database_for_10` для создания и заполнения 
необходимых для примеров таблиц и данных из 10 раздела книги

### Обновление от 01.10.23

Нашел ошибку (свою) из-за которой пример 8_13 работал некорректно:
Сравнивал байт-строку с константной строкой

### Обновление от 29.09.2023

Примеры, работающие странно.  ~~(TODO: разобраться)~~

*  [src8_13.py](./src8_13.py)

<div id="anchor_29_09_2023">
Найдена ошибка в тексте примеров src8_5.py, src8_7.py-src8_10.py:

В листинге src8_8 (с. 238) ветка else вложенного оператора ветвления должна отрабатывать состояние, 
когда вновь введенный символ не равен символу delete_char (необходимо сдвинуть на один уровень вложенности назад)
</div>
### Обновление от 28.09.2023

Примеры, не захотевшие запуститься правильно с первого раза ~~(TODO: разобраться)~~:
* 
* [src8_5.py](./src8_5.py)
* [src8_7.py](./src8_7.py)
* [src8_8.py](./src8_8.py) <-- Ошибка здесь (см. [примечание от 29.09.2023](#anchor_29_09_2023))
* [src8_9.py](./src8_9.py)
* [src8_10.py](./src8_10.py)

### Обновление от 27.09.2023

Для выполнения примеров из главы 6 была добавлена команда для скачивания большого сжатого текстового файла

* `make download-ngrams` - загрузить и распаковать данные для главы 6
* `make database` - запустить postgres, создать и заполнить таблицы (для примера src6_15.py)

### Обновление от 26.09.2023

Для взаимодействия с базой данных в 5 части книге, был добавлен Makefile с командами

* `make run-postgres` - запустить базу данных postgres
* `make stop-postgres` - остановить и удалить контейнер с базой данных

При этом необходимо создать файл `secrets.env` 
и записать туда переменную окружения `POSTGRES_PASSWORD=<придумайте пароль>`