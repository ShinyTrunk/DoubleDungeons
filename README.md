1. Создание карт 3 уровней, включающих в себя фоновые блоки, блоки препятствий, игрового персонажа, лут и врагов. В одной из карт также должен быть реализован проход на секретный уровень. 
2. Поиск в интернете последовательных изображений для анимации главного персонажа и врагов, картинок для стартового и конечного экранов, картинок для фоновых блоков и блоков препятствий. 
3. Создание классов блоков и врагов, классы врагов включают в себя количество их здоровья и атаку.  
4. На начальном экране разместить кнопку "Играть" для запуска игры. 
5. Сделать автоматический переход между уровнями, по порядку. 
6. Разместить систему характеристик у персонажа и врагов, рядом с ними, таких как здоровье и атака. 
7. Разработка механики игры (каждый ход персонажа равен ходу всех врагов, все враги должны двигаться в сторону персонажа, взаимный урон при коллизии, если враг оказывается на клетке, где персонаж был в предыдущем ходе, то персонаж получает урон). 
8. В случае смерти: выдача сообщения "Вы умерли, повторите попытку", кнопки рестарта и возврата в главное меню. 
9. В случае победы: выдача сообщения "Вы выйграли", кнопка возврата в меню.
10. Отображение количества убитых врагов и собранного лута после каждой смерти и победы. 
11. Организовать механику сбора лута (лут необходимо собрать перед убийством всех врагов, за собранный лут на 4 уровнях предусматривается ачивка). 
12. Добавление секретного уровня с боссом и лутом
<br>
<h2>Пояснительная записка:<h2>
<h3>Название: DoubleDungeons</h3>
<h3>Авторы: Мокрецов Максим, Мальцев Фёдор</h3>
<div class="desription">
  <h3>Описание проекта:</h3>
  <p>Наш проект это 2D игра с видом сверху. В DoubleDungeons ты должен пройти несколько уровней, собрать все сокровища, а может даже найти что-то скрытое от глаз, ведь только в этом случае ты получишь истинную концовку нашей игры.<br>
  На пути к своей к цели ты встретишь множество врагов, над которыми ты должен будешь одержать верх, но не останавливайся и продолжай проходить уровень за уровнем.</p>
  <h3>Реализация:</h3>
  <p>Все спрайты и тайлсеты расположены в директории data и распределены по отдельным директориям sprites, tilesets. Файл main.py отвечает за запуск приложения, файлы level.py, level_1.py, level_2.py, level_3.py отвечают за генерацию уровней и взаимодействие с ними, в файле start_screen.py реализован функционал стартового окна, в файлах final_screen_1.py, final_screen_2.py реализован функционал двух разных финальных окон, в файле death_screen.py реализован функционал окна, всплывающего после смерти аватара, в файл settings.py занесены константы, в файле creatures.py реализованы классы аватара и врагов. Функции, которые отвечают за загрузку карты, изображений и завершение работы программы занесены в отдельный файл secondary_functions.py. Класс, отвечающий за передвижение камеры реализован в файле camera.py.  В фйле surface_to_sprite_transformer.py находится класс Card. Все группы спрайтов создаются в файле sprite_groups.py. В проекте использованы библиотеки pygame, sys, os, pytmx. У нас в игре реализован класс AnimatedSprite, благодаря которому добавлена анимация персонажей, класс Player в котором реализованы передвижение играка и класс Enemy благодаря которому на нашей карте появляются враги, еще реализован класс Camera, который отвечает за передвижение камеры, класс Card отвечат за часть присоединения карты из приложения Tiled Map Editor к нашей игре. Для создания карт мы воспользовались приложением Tiled Map Editor и для того чтобы мы могли использовать карты, созданные в этом приложении, в нашей игре мы воспользовались библиотекой pytmx.</p> 
</div>
<h3>Презентация</h3>
<a href="https://docs.google.com/presentation/d/1wSzkDbbkqwaAtZv0vvi0JJ2dZOzNlZYZ5N1YgG4xrhc/edit?usp=sharing">DoubleDungeons</a>
