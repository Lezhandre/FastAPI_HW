# FastAPI_HW

HTTP-запросы:

## get /
Базы данных не меняются.
В ответ присылает приветственное сообщение "Welcome to dog service!"

## get /post
Базы данных не меняются.
В ответ присылает id и временную метку последнего запроса на создание записи о собаке

## get /dog[?kind={kind}]
Базы данных не меняются.
В ответ присылает все записи собак, или если задан параметр {kind}, то записи всех собак заданной породы.

## post /dog
Создаётся запись собаки и добавляется метка создания с id={pk}.
В ответ присылается или ошибка, или запись собаки, созданной по телу сообщения.

## get /dog/{pk}
Базы данных не меняются.
В ответ присылается или ошибка, или запись собаки, с заданным ключом {pk}.

## patch /dog/{pk}
Изменяется запись собаки хранящаяся по ключу {pk}.
В ответ присылается или ошибка, или запись собаки, с заданным ключом {pk} до изменения.
