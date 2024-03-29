# python-messenger

## Tips

Если мы определим переменную с временем вне роута и передадим в качестве ответа из роута, то при обновлении вкладки браузера, время будет одним и тем же, а конкретно время будет временем когда мы запустили сервер, мы запустили сервер, время один раз вычислилось, записалось в переменную и теперь мы каждый раз его и возвращаем

```python
t = datetime.now()
{"status": "ok", "time": t}
```

Мы же хотим что бы время пересчитывалось каждый раз когда мы обращаемся к роуту

```python
{"status": "ok", "time": datetime.now()}
```

Flask может сам преобразовывать дату в красивый вид, но некоторые другие фреймворки этого не делают, а т.к это выражение изначально является объектом класса datetime, а не строкой, то при сериализации возвращаемого объекта в JSON, была бы ошибка

```python
{
    "time": datetime.now(), # Flask неявно
    "time2": str(datetime.now()), # мы сами приводим дату к строке
    "time3": datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # http://strftime.org/
}
```

## Errors

`TypeError: Object of type function is not JSON serializable`

Здесь у нас был конфликт имён между ф-цией messages и списком messages, и когда мы отправляли из роута "/messages" список messages, на самом деле сервер пытался отправить ф-цию messages, естественно предварительно её сериализовав, поэтому мы переименовали её в messages_view

## PyCharm

`ctrl + alt + L` - форматирование 

`ctrl + клик мышки на название библиотеки` - в коде datetime.now(), при клике на datetime откроется код библиотеки

`alt + enter` - в коде datetime.now(), при фокусе указателя на datetime появится окно в котором мы сможем быстро подключить/импортировать данную библиотеку, если она ещё не подключена

`три ковычки " или ' + enter` - python docstring https://www.python.org/dev/peps/pep-0257/

## requests

[send POST with headers](https://stackoverflow.com/questions/10768522/python-send-post-with-header)

[json parameter](https://requests.kennethreitz.org/en/master/user/quickstart/#more-complicated-post-requests)

## Other

[datetime and time](https://python-scripts.com/datetime-time-python)