# Site-card
-------

### Frontend part
-------

Для реализации главной страницы сайта был создан файл [home.html] с дальнейшим написанием кода верстки.

**Скриншот главной страницы сайта**

![alt-текст](https://github.com/Basharov1210/Test_intern/blob/master/readme_photos/First_page.png "Главная страница сайта")

-------

Для реализации страницы 'Обо мне' был создан файл [about.html] с дальнейшим написанием кода верстки.

**Скриншот страницы 'Обо мне'**

![alt-текст](https://github.com/Basharov1210/Test_intern/blob/master/readme_photos/about_page.png "Страница обо мне")

-------

При нажатии на кнопку 'Список дел' открывается встроенная страница Django REST framework с доступом просмотра API и выполнения дальнейших манипуляций с ними, такими как: GET,POST,PUT,DELETE.

**Скриншот страницы 'Список дел'**

![alt-текст](https://github.com/Basharov1210/Test_intern/blob/master/readme_photos/todo_page.png "Страница список дел")

### Backend part

Для реализации простого REST-сервиса был использована библиотека Django REST framework.

Сперва была создана [модель] для описания структуры храненимых данных для списка задач.

Следующим шагом был создан [сериализатор] для выполнения конвертирования объектов в JSON формат.

В файле [views.py] были реазилованы GET,POST,PUT,DELETE-запросы.


[views.py]: https://github.com/Basharov1210/Test_intern/blob/master/todo/views.py
[сериализатор]: https://github.com/Basharov1210/Test_intern/blob/master/todo/serializers.py
[модель]: https://github.com/Basharov1210/Test_intern/blob/master/todo/models.py
[home.html]: https://github.com/Basharov1210/Test_intern/blob/master/main/templates/main/home.html
[about.html]: https://github.com/Basharov1210/Test_intern/blob/master/main/templates/main/about.html
