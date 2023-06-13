import re


class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        return context



"""Список cities был образован с помощью парсинга сайта в html-документ"""
# with open("NewTrip/other_files/cities.html", "r", encoding="UTF-8") as f:
#     text = f.read()
#     cities = []
#     match = re.findall(r"\n([а-яА-ЯёЁ\s\-]+)\n", text)
#
#     for x in match:
#       cities.append(x.strip("\n"))

cities = [
  'Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург', 'Нижний Новгород', 'Самара', 'Омск', 'Казань',
  'Челябинск', 'Ростов-на-Дону', 'Уфа', 'Волгоград', 'Пермь', 'Красноярск', 'Воронеж', 'Саратов', 'Краснодар',
  'Тольятти', 'Ижевск', 'Ульяновск', 'Барнаул', 'Владивосток', 'Ярославль', 'Иркутск', 'Тюмень', 'Махачкала',
  'Хабаровск', 'Новокузнецк', 'Оренбург', 'Кемерово', 'Рязань', 'Томск', 'Астрахань', 'Пенза', 'Набережные Челны',
  'Липецк', 'Тула', 'Киров', 'Чебоксары', 'Калининград', 'Брянск', 'Курск', 'Иваново', 'Магнитогорск',
  'Улан-Удэ', 'Тверь', 'Ставрополь', 'Нижний Тагил', 'Белгород', 'Архангельск', 'Владимир', 'Сочи', 'Курган',
  'Смоленск', 'Калуга', 'Чита', 'Орёл', 'Волжский', 'Череповец', 'Владикавказ', 'Мурманск', 'Сургут', 'Вологда',
  'Саранск', 'Тамбов', 'Стерлитамак', 'Грозный', 'Якутск', 'Кострома', 'Комсомольск-на-Амуре', 'Петрозаводск',
  'Таганрог', 'Нижневартовск', 'Йошкар-Ола', 'Братск', 'Новороссийск', 'Дзержинск', 'Шахты', 'Нальчик', 'Орск',
  'Сыктывкар', 'Нижнекамск', 'Ангарск', 'Старый Оскол', 'Великий Новгород', 'Балашиха', 'Благовещенск',
  'Прокопьевск', 'Бийск', 'Химки', 'Псков', 'Энгельс', 'Рыбинск', 'Балаково', 'Северодвинск', 'Армавир',
  'Подольск', 'Королёв', 'Южно-Сахалинск', 'Петропавловск-Камчатский', 'Сызрань', 'Норильск', 'Златоуст',
  'Каменск-Уральский', 'Мытищи', 'Люберцы', 'Волгодонск', 'Новочеркасск', 'Абакан', 'Находка', 'Уссурийск',
  'Березники', 'Салават', 'Электросталь', 'Миасс', 'Рубцовск', 'Альметьевск', 'Ковров', 'Коломна', 'Майкоп',
  'Пятигорск', 'Одинцово', 'Колпино', 'Копейск', 'Хасавюрт', 'Железнодорожный', 'Новомосковск', 'Кисловодск',
  'Серпухов', 'Первоуральск', 'Новочебоксарск', 'Нефтеюганск', 'Димитровград', 'Нефтекамск', 'Черкесск',
  'Орехово-Зуево', 'Дербент', 'Камышин', 'Невинномысск', 'Красногорск', 'Муром', 'Батайск', 'Новошахтинск',
  'Сергиев Посад', 'Ноябрьск', 'Щёлково', 'Кызыл', 'Октябрьский', 'Ачинск', 'Северск', 'Новокуйбышевск',
  'Елец', 'Арзамас', 'Обнинск', 'Новый Уренгой', 'Каспийск', 'Элиста', 'Пушкино', 'Жуковский', 'Артём',
  'Междуреченск', 'Ленинск-Кузнецкий', 'Сарапул', 'Ессентуки', 'Воткинск', 'Ногинск', 'Тобольск', 'Ухта',
  'Серов', 'Великие Луки', 'Мичуринск', 'Киселёвск', 'Новотроицк', 'Зеленодольск', 'Бердск', 'Соликамск',
  'Раменское', 'Домодедово', 'Магадан', 'Глазов', 'Каменск-Шахтинский', 'Железногорск', 'Канск', 'Назрань',
  'Пушкин', 'Гатчина', 'Саров', 'Воскресенск', 'Долгопрудный', 'Бугульма', 'Кузнецк', 'Губкин', 'Кинешма',
  'Ейск', 'Реутов', 'Усть-Илимск', 'Железногорск', 'Новоуральск', 'Усолье-Сибирское', 'Чайковский', 'Азов',
  'Бузулук', 'Озёрск', 'Балашов', 'Юрга', 'Кирово-Чепецк', 'Кропоткин', 'Клин', 'Выборг', 'Ханты-Мансийск',
  'Троицк', 'Бор', 'Шадринск', 'Белово', 'Минеральные Воды', 'Анжеро-Судженск', 'Биробиджан', 'Лобня',
  'Петергоф', 'Чапаевск', 'Георгиевск', 'Черногорск', 'Минусинск', 'Михайловск', 'Елабуга', 'Дубна',
  'Воркута', 'Новоалтайск', 'Егорьевск', 'Асбест', 'Белорецк', 'Белогорск', 'Гуково', 'Ступино',
  'Туймазы', 'Кстово', 'Вольск', 'Ишимбай', 'Кунгур', 'Зеленогорск', 'Лысьва', 'Сосновый Бор', 'Буйнакск',
  'Борисоглебск', 'Ишим', 'Наро-Фоминск', 'Будённовск', 'Донской', 'Полевской', 'Лениногорск',
  'Павловский Посад', 'Славянск-на-Кубани', 'Заречный', 'Туапсе', 'Россошь', 'Кумертау', 'Лабинск', 'Сибай',
  'Клинцы', 'Ржев', 'Ревда', 'Тихорецк', 'Нерюнгри', 'Алексин', 'Александров', 'Дмитров', 'Мелеуз', 'Сальск',
  'Лесосибирск', 'Гусь-Хрустальный', 'Чистополь', 'Павлово', 'Чехов', 'Котлас', 'Белебей', 'Искитим',
  'Верхняя Пышма', 'Краснотурьинск', 'Апатиты', 'Всеволожск', 'Прохладный', 'Михайловка', 'Анапа', 'Тихвин',
  'Свободный', 'Ивантеевка', 'Шуя', 'Когалым', 'Щёкино', 'Крымск', 'Вязьма', 'Горно-Алтайск', 'Видное',
  'Арсеньев', 'Избербаш', 'Выкса', 'Климовск', 'Лиски', 'Волжск', 'Краснокаменск', 'Жигулёвск', 'Фрязино',
  'Узловая', 'Лыткарино', 'Нягань', 'Рославль', 'Геленджик', 'Тимашёвск', 'Белореченск', 'Боровичи',
  'Солнечногорск', 'Назарово', 'Кириши', 'Черемхово', 'Вышний Волочёк', 'Краснокамск', 'Берёзовский',
  'Балахна', 'Ливны', 'Лесной', 'Донецк', 'Североморск', 'Саяногорск', 'Бугуруслан', 'Кимры', 'Мегион',
  'Кизляр', 'Урус-Мартан', 'Снежинск', 'Кингисепп', 'Заринск', 'Отрадный', 'Курганинск', 'Шелехов', 'Можга',
  'Сертолово', 'Ярцево', 'Шали', 'Торжок', 'Рузаевка', 'Волхов', 'Берёзовский', 'Дзержинский', 'Грязи',
  'Чусовой', 'Надым', 'Верхняя Салда', 'Сафоново', 'Осинники', 'Кольчугино', 'Гудермес', 'Канаш', 'Рассказово',
  'Сатка', 'Мончегорск', 'Куйбышев', 'Усть-Кут', 'Тулун', 'Красное Село', 'Шебекино', 'Спасск-Дальний',
  'Камень-на-Оби', 'Белая Калитва', 'Печора', 'Чебаркуль', 'Радужный', 'Усть-Лабинск', 'Мценск', 'Мыски',
  'Ломоносов', 'Кронштадт', 'Амурск', 'Курчатов', 'Салехард', 'Ефремов', 'Стрежевой', 'Аксай',
  'Переславль-Залесский', 'Ахтубинск', 'Кашира', 'Заинск', 'Советск', 'Пугачёв', 'Лангепас', 'Бирск',
  'Урюпинск', 'Моршанск', 'Пыть-Ях', 'Качканар', 'Конаково', 'Ртищево', 'Вязники', 'Кореновск', 'Усинск',
  'Тутаев', 'Красный Сулин', 'Саянск', 'Новодвинск', 'Новозыбков', 'Людиново', 'Изобильный', 'Мариинск',
  'Черняховск', 'Заволжье', 'Апшеронск', 'Троицк', 'Красноуфимск', 'Коряжма', 'Каменка', 'Елизово', 'Фролово',
  'Урай', 'Большой Камень', 'Тосно', 'Алексеевка', 'Коркино', 'Кыштым', 'Лянтор', 'Моздок', 'Партизанск',
  'Шарыпово', 'Светлоград', 'Сокол', 'Ирбит', 'Гай', 'Реж', 'Алатырь', 'Алапаевск', 'Темрюк', 'Южноуральск',
  'Учалы', 'Вичуга', 'Дальнегорск', 'Протвино', 'Мирный', 'Нижнеудинск', 'Лесозаводск', 'Баксан', 'Беслан',
  'Сестрорецк', 'Ялуторовск', 'Миллерово', 'Луга', 'Кизилюрт', 'Фурманов', 'Краснознаменск', 'Зеленокумск',
  'Кулебаки', 'Кандалакша', 'Тында', 'Тайшет', 'Тавда', 'Сердобск', 'Валуйки', 'Гулькевичи', 'Вятские Поляны',
  'Истра', 'Тейково', 'Абинск', 'Азнакаево', 'Новокубанск', 'Сухой Лог', 'Углич', 'Кинель', 'Благовещенск',
  'Югорск', 'Слободской', 'Острогожск', 'Добрянка', 'Трёхгорный', 'Сланцы', 'Корсаков', 'Касимов', 'Муравленко',
  'Чернушка', 'Юбилейный', 'Артёмовский', 'Сосновоборск', 'Кондопога', 'Шатура', 'Щербинка', 'Благодарный',
  'Балтийск', 'Нововоронеж', 'Нурлат', 'Зима', 'Славгород', 'Котельники', 'Приморско-Ахтарск', 'Инта', 'Аша',
  'Богородицк', 'Киров', 'Котовск', 'Старая Русса', 'Ростов', 'Шумерля', 'Гагарин', 'Нарткала', 'Великий Устюг',
  'Маркс', 'Можайск', 'Борзя', 'Ликино-Дулёво', 'Дюртюли', 'Петровск', 'Карабулак', 'Малгобек', 'Удомля',
  'Холмск', 'Городец', 'Богданович', 'Дагестанские Огни', 'Усть-Джегута', 'Верхний Уфалей', 'Малоярославец',
  'Барабинск', 'Скопин', 'Мирный', 'Еманжелинск', 'Кушва', 'Горячий Ключ', 'Киржач', 'Луховицы', 'Десногорск',
  'Сегежа', 'Аргун', 'Алейск', 'Дятьково', 'Кохма', 'Знаменск', 'Дедовск', 'Североуральск', 'Сорочинск',
  'Карталы', 'Карпинск', 'Кудымкар', 'Кировск', 'Топки', 'Карасук', 'Кимовск', 'Костомукша', 'Соль-Илецк',
  'Дивногорск', 'Гусев', 'Похвистнево', 'Сасово', 'Сосногорск', 'Советская Гавань', 'Нефтекумск', 'Морозовск',
  'Полысаево', 'Дальнереченск', 'Губаха', 'Тара', 'Медногорск', 'Октябрьск', 'Бутурлиновка', 'Янаул',
  'Лабытнанги', 'Калач-на-Дону', 'Камышлов', 'Зерноград', 'Уварово', 'Заречный', 'Новоалександровск', 'Майский',
  'Новопавловск', 'Советский', 'Балабаново', 'Родники', 'Красноармейск', 'Унеча', 'Кувандык',
  'Железногорск-Илимский', 'Ипатово', 'Семилуки', 'Озёры', 'Буй', 'Заводоуковск', 'Кировск', 'Аткарск', 'Асино',
  'Киреевск', 'Богородск', 'Обь', 'Тайга', 'Павловск', 'Зея', 'Котельнич', 'Красноуральск', 'Ленск',
  'Северобайкальск', 'Гурьевск', 'Зарайск', 'Гусиноозёрск', 'Невьянск', 'Бежецк', 'Железноводск', 'Исилькуль',
  'Семёнов', 'Красноармейск', 'Татарск', 'Колпашево', 'Котово', 'Давлеканово', 'Строитель', 'Вельск',
  'Семикаракорск', 'Отрадное', 'Карачаевск', 'Фокино', 'Шарья', 'Омутнинск', 'Усть-Катав', 'Калачинск',
  'Бологое', 'Волоколамск', 'Губкинский', 'Таштагол', 'Оленегорск', 'Оха', 'Кубинка', 'Вилючинск', 'Нелидово',
  'Нерехта', 'Николаевск-на-Амуре', 'Нижний Ломов', 'Лосино-Петровский', 'Лермонтов', 'Вихоревка', 'Никольск',
  'Зверево', 'Няндома', 'Дудинка', 'Верещагино', 'Электрогорск', 'Бавлы', 'Менделеевск', 'Нижняя Тура',
  'Тогучин', 'Калтан', 'Лысково', 'Старая Купавна', 'Куровское', 'Ряжск', 'Остров', 'Хотьково', 'Хадыженск',
  'Пикалёво', 'Льгов', 'Ершов', 'Сергач', 'Светлый', 'Онега', 'Ковылкино', 'Нарьян-Мар', 'Алдан', 'Рошаль',
  'Козьмодемьянск', 'Оса', 'Бронницы', 'Данков', 'Лодейное Поле', 'Боготол', 'Кировград', 'Тырныауз', 'Лебедянь',
  'Черноголовка', 'Бакал', 'Алагир', 'Шахунья', 'Суровикино', 'Райчихинск', 'Сысерть', 'Среднеуральск',
  'Котельниково', 'Тарко-Сале', 'Буинск', 'Белоярский', 'Пролетарск', 'Коммунар', 'Пущино', 'Абдулино',
  'Электроугли', 'Калач', 'Кяхта', 'Шимановск', 'Черепаново', 'Бобров', 'Карачев', 'Кизел', 'Юрьев-Польский',
  'Новый Оскол', 'Собинка', 'Никольское', 'Новомичуринск', 'Агрыз', 'Нефтегорск', 'Сортавала', 'Терек', 'Нытва',
  'Стародуб', 'Суворов', 'Приозерск', 'Ковдор', 'Куса', 'Ардон', 'Енисейск', 'Усмань', 'Подпорожье', 'Яровое',
  'Петровск-Забайкальский', 'Инза', 'Слюдянка', 'Апрелевка', 'Рыбное', 'Жуковка', 'Радужный', 'Харабали',
  'Козельск', 'Арск', 'Осташков', 'Чегем', 'Почеп', 'Сельцо', 'Константиновск', 'Туринск', 'Новоаннинский',
  'Шумиха', 'Гаврилов-Ям', 'Ивдель', 'Покров', 'Баймак', 'Поворино', 'Катав-Ивановск', 'Нижняя Салда',
  'Мантурово', 'Голицыно', 'Бородино', 'Ясный', 'Московский', 'Межгорье', 'Галич', 'Пласт', 'Полярный',
  'Яранск', 'Кирсанов', 'Бикин', 'Барыш', 'Абаза', 'Волгореченск', 'Куртамыш', 'Покачи', 'Щигры', 'Новоузенск',
  'Касли', 'Жирновск', 'Ясногорск', 'Приволжск', 'Кондрово', 'Бокситогорск', 'Советск', 'Болотное',
'Мензелинск', 'Калининск', 'Навашино', 'Звенигород', 'Агидель', 'Невель', 'Сухиничи', 'Камызяк', 'Плавск',
  'Талица', 'Кашин', 'Иланский', 'Валдай', 'Поронайск', 'Красновишерск', 'Ужур', 'Павловск', 'Новоульяновск',
  'Краснослободск', 'Палласовка', 'Светогорск', 'Пестово', 'Данилов', 'Заполярный', 'Лакинск', 'Рыльск',
  'Медвежьегорск', 'Грязовец', 'Ленинск', 'Дегтярск', 'Чудово', 'Бодайбо', 'Венёв', 'Жердевка', 'Меленки',
  'Петушки', 'Полярные Зори', 'Николаевск', 'Цимлянск', 'Трубчевск', 'Нерчинск', 'Лукоянов', 'Купино',
  'Карабаново', 'Кодинск', 'Белокуриха', 'Емва', 'Первомайск', 'Вяземский', 'Александровск', 'Сим', 'Мамадыш',
  'Красный Кут', 'Струнино', 'Дубовка', 'Лагань', 'Очёр', 'Арамиль', 'Южа', 'Пересвет', 'Катайск', 'Гороховец',
  'Шилка', 'Горняк', 'Белёв', 'Далматово', 'Гвардейск', 'Фокино', 'Калязин', 'Талдом', 'Сясьстрой', 'Свирск',
  'Байкальск', 'Обоянь', 'Руза', 'Цивильск', 'Ак-Довурак', 'Краснозаводск', 'Шлиссельбург', 'Петров Вал',
  'Яхрома', 'Могоча', 'Карабаш', 'Камешково', 'Хвалынск', 'Кемь', 'Анадырь', 'Торопец', 'Зеленоградск',
  'Зеленогорск', 'Аркадак', 'Новая Ляля', 'Снежногорск', 'Уяр', 'Кораблино', 'Чаплыгин', 'Киренск', 'Удачный',
  'Юрюзань', 'Балей', 'Окуловка', 'Малая Вишера', 'Нязепетровск', 'Гурьевск', 'Сосенский', 'Чкаловск', 'Вуктыл',
  'Урень', 'Боровск', 'Лихославль', 'Адыгейск', 'Долинск', 'Волосово', 'Жуков', 'Сорск', 'Бабаево',
  'Горнозаводск', 'Заволжск', 'Сосновка', 'Звенигово', 'Судогда', 'Верхний Тагил', 'Дрезна', 'Богучар',
  'Неман', 'Михайлов', 'Невельск', 'Сураж', 'Ворсма', 'Кремёнки', 'Называевск', 'Опочка', 'Тетюши', 'Чулым',
  'Закаменск', 'Хилок', 'Питкяранта', 'Завитинск', 'Болхов', 'Эртиль', 'Нариманов', 'Петухово', 'Тюкалинск',
  'Луза', 'Белая Холуница', 'Беломорск', 'Заозёрск', 'Зуевка', 'Печоры', 'Гаджиево', 'Камбарка', 'Пионерский',
  'Щучье', 'Шагонар', 'Змеиногорск', 'Дигора', 'Светлогорск', 'Гремячинск', 'Микунь', 'Дорогобуж', 'Заозёрный',
  'Высоковск', 'Александровск-Сахалинский', 'Порхов', 'Суздаль', 'Вытегра', 'Кола', 'Ожерелье', 'Кирс',
  'Ермолино', 'Углегорск', 'Козловка', 'Нижние Серги', 'Вилюйск', 'Уржум', 'Наволоки', 'Юрьевец', 'Миньяр',
  'Нюрба', 'Краснослободск', 'Каргополь', 'Ельня', 'Сольцы', 'Харовск', 'Южно-Сухокумск', 'Каргат', 'Рудня',
  'Волчанск', 'Кувшиново', 'Володарск', 'Михайловск', 'Нея', 'Ивангород', 'Тотьма', 'Суоярви', 'Пудож',
  'Задонск', 'Таруса', 'Болохово', 'Белозерск', 'Ядрин', 'Городовиковск', 'Сковородино', 'Нолинск', 'Покровск',
          'Олёкминск', 'Устюжна', 'Верхняя Тура', 'Верхнеуральск', 'Ардатов', 'Облучье', 'Западная Двина',
    'Серафимович', 'Перевоз', 'Костерёво', 'Анива', 'Теберда', 'Мариинский Посад', 'Дно', 'Олонец', 'Чадан',
  'Бирюсинск', 'Ветлуга', 'Новая Ладога', 'Верхотурье', 'Починок', 'Липки', 'Комсомольск', 'Инсар', 'Болгар',
  'Старица', 'Пучеж', 'Белинский', 'Никольск', 'Белоусово', 'Шахтёрск', 'Макушино', 'Медынь', 'Малмыж', 'Андреаполь',
  'Салаир', 'Новосокольники', 'Сычёвка', 'Городище', 'Томмот', 'Мглин', 'Бирюч', 'Лахденпохья', 'Мамоново',
  'Спасск-Рязанский', 'Кириллов', 'Лаишево', 'Дмитриев', 'Велиж', 'Полесск', 'Советск', 'Спасск', 'Демидов',
  'Весьегонск', 'Севск', 'Оханск', 'Темников', 'Макарьев', 'Юхнов', 'Сурск', 'Красавино', 'Орлов', 'Сенгилей',
  'Зубцов', 'Сретенск', 'Новохопёрск', 'Курлово', 'Каменногорск', 'Мураши', 'Алзамай', 'Княгинино', 'Макаров',
  'Шацк', 'Солигалич', 'Гаврилов Посад', 'Багратионовск', 'Себеж', 'Грайворон', 'Игарка', 'Приморск', 'Пошехонье',
  'Шиханы', 'Суджа', 'Мышкин', 'Спас-Клепики', 'Короча', 'Сусуман', 'Пыталово', 'Шенкурск', 'Усолье', 'Дмитровск',
  'Красный Холм', 'Жиздра', 'Любим', 'Злынка', 'Билибино', 'Фатеж', 'Верея', 'Чухлома', 'Туран', 'Чердынь',
  'Спас-Деменск', 'Бабушкин', 'Кадников', 'Озёрск', 'Пустошка', 'Славск', 'Нестеров', 'Томари', 'Гдов', 'Духовщина',
  'Правдинск', 'Мосальск', 'Любань', 'Певек', 'Мещовск', 'Чёрмоз', 'Холм', 'Ладушкин', 'Белый', 'Новоржев', 'Новосиль',
  'Малоархангельск', 'Мезень', 'Среднеколымск', 'Краснознаменск', 'Кологрив', 'Северо-Курильск', 'Магас',
  'Сольвычегодск', 'Кедровый', 'Плёс', 'Горбатов', 'Артёмовск', 'Островной', 'Курильск', 'Приморск', 'Верхоянск',
  'Высоцк', 'Чекалин']