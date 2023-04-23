import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from random import randint, choice
import datetime as dt
from time import sleep


class Coin:
    """Класс для подбрасывания монетки."""
    def __init__(self):
        self.variants = ["Выпал орёл!", "Выпала решка!"]

    def drop(self):
        return choice(self.variants)


def days(number):
    """
    Функция возвращает слово "ltym" в нужной форме, согласуя его с
    поступившим на вход числом.
    """
    number = int(number)
    if number == 0:
        text = "дней"
    elif number >= 1 and number <= 9:
        if number == 1:
            text = 'день'
        elif number >= 2 and number <= 4:
            text = 'дня'
        else:
            text = 'дней'
    elif int(str(number)[-2:]) in [11, 12, 13, 14, 15, 16, 17, 18, 19]:
        text = 'дней'
    elif number % 10 == 0:
        text = 'дней'
    elif number % 10 == 1:
        text = 'день'
    elif number % 10 in [2, 3, 4]:
        text = 'дня'
    else:
        text = 'дней'
    return text


def get_start_text():
    """Функция генерирует стандартную стартовую реплику бота."""
    text = ("Привет! Меня зовут Аркадий, я - бот-помощник по ЕГЭ." +
            " Я пока умею не очень много вещей, но мой создатель обещал" +
            " добавить мне новых функций так быстро, как это возможно!" +
            " Чтобы посмотреть список всех доступных команд, введите:\n" +
            "'!Аркадий' (можно в некоторых других формах, в разном РеГиСтРе" +
            " и с запятой на конце), затем пробел и 'команды'. Я выведу" +
            " список всех доступных сейчас команд с описаниями!)")
    return text


def get_random_hello(user_id):
    global admin_id
    """Функция возвращает случайное приветствие из списка."""
    words = ["Привет-привет! :)", "Здравствуйте!", "Рад Вас видеть.",
             "Рад Вас видеть вновь.", "Отлично выглядите сегодня!",
             "Привет! Я скучал по Вам!", "И Вам не хворать!"]
    if admin_id == user_id:
        words.append("Это же мой создатель! Привет)")
    return choice(words)


def get_motivation():
    """Функция открывает файл с мотивирующими цитатами, записывает его
    содержимое в переменную, разделяя строки, и возвращает
    одну строку-цитату."""
    global motivation_path
    file = open(motivation_path, "r", encoding='utf-8').readlines()
    return choice(file)


def cleaner(text):
    """Функция, возвращающая текст без всех находящихся в списке
    strip_symbols символов в начале и конце."""
    global strip_symbols
    bool_go = False
    if text == "":
        return ""
    if text[0] in strip_symbols or text[-1] in strip_symbols:
        bool_go = True
    while bool_go:
        for element in strip_symbols:
            text = text.rstrip(element).lstrip(element)
        if text[0] in strip_symbols or text[-1] in strip_symbols:
            bool_go = True
        else:
            bool_go = False
    return text


admin_id_path = "data/text/admin_id.txt"  # Путь к файлу с id администратора
token_path = "data/text/token.txt"  # Путь к файлу с токеном доступа
command_path = "data/group_media/text/Ссылка на документ.txt"
prepare_path = "data/text/prepare.txt"
"""Путь к файлу с ссылкой на документ со всеми командами бота."""
motivation_path = "data/text/motivation.txt"  # Путь к файлу с цитатами
command_link = open(command_path, "r").readlines()[0]
admin_id = int(open(admin_id_path, "r").readlines()[0])
token = open(token_path, "r").readlines()[0]
prepare = open(prepare_path, "r", encoding="utf-8").readlines()
"""Для проверки кода токен полного доступа необходимо скрывать, например,
заменять его объектом None, для предотвращения чужого доступа к боту."""
messages_list = [VkBotEventType.MESSAGE_NEW, VkBotEventType.MESSAGE_REPLY]
path_to_id = "data/text/id-s.txt"
list_of_id = open(path_to_id, "r").readlines()
list_of_id = [int(x.rstrip("\n")) for x in list_of_id]
community_id = "220001989"  # id сообщества, в котором находится бот
session_bot = vk_api.VkApi(token=token)
connection = VkBotLongPoll(session_bot, community_id)

bot_names = ["!аркадий", "!аркаша", "!каша", "!кашка", "!arcady",
             "!arcadiy", "!arkasha", "!arkash", "!арк", "!каш", "!аркаш",
             "!аркашка", "!кадий", "!кашенька", "!кот", "!котик", "!аркашенька",
             "!аркашуля", "!кашкандра", "!кашуленька", "!кашак", "!кашакендра",
             "!кашандра", "!арка", "!аркашня", "!арканя", "!аркан",
             "!аркашенко", "!аркашноб", "!аркашноид", "!арканоид", "!аркашмили",
             "!кашуля", "!аркадиллер", "!аркадилер"]
boofer_list = []
for x in bot_names:
    boofer_list.append(x.lstrip("!"))
bot_names += boofer_list
remove_id_names = ["стереть", "сотри", "удали", "удалить", "забыть", "забудь",
                   "вычеркни", "вычеркнуть"]
user_self_names = ["я", "меня", "мне"]
user_all_names = ["всех", "все", "чат", "всё"]
help_command_names = ["команды", "помощь", "помоги"]
dates_names = ["даты", "сроки", "когда", "егэ"]
dates = ["2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020",
         "2021", "2022", "2023"]
stages = ["досрочный", "основной", "дополнительный"]
say_hello = ["прив", "привет", "привки", "приветик", "приветики", "салют",
             "хай", "здравствуй", "здравствуйте", "здарова", "пиривет",
             "пурвет", "тевирп", "тивирп", "йоу", "дароу", "даров", "здаров",
             "хой", "алё", "ало", "алло", "але", "дарова", "датути", "хеллоу",
             "доброе", "добрый", "доброй", "дратути", "утречко", "утро",
             "приветули", "приветуль", "приветульки", "драсте", "драсьте",
             "привет-привет"]
bad_words = ["иди", "пошёл", "пошел", "дурак", "мудак", "придурок", "овощ",
             "гад", "гадёныш", "гаденыш", "идиот", "бяка", "тугодум", "негодяй",
             "противный", "ненавижу", "глупый", "гадкий", "слабый", "лох",
             "позер", "слит"]
motivate_words = ["мотивация", "мотивируй", "замотивируй", "поддержи",
                  "цитаты", "процитируй", "цитируй", "цитировать",
                  "протицировать", "мотивировать", "поддержать",
                  "замотивируйте", "мотивируйте", "цитируйте", "процитируйте",
                  "поддержите", "поддержка"]
panic_words = ["тревога", "паника", "напугайся", "испугайся", "сирена"]
stop_work_words = ["выключись", "выключить", "спи", "усни", "засни",
                   "отключись", "отдохни", "выключитесь", "спите", "усните",
                   "засните", "отключитесь", "отдохните", "вырубись",
                   "вырубитесь", "оффнись", "оффнитесь", "off", "выкл",
                   "офф", "спать", "выключи", "офнись", "оффнись"]
get_clock_words = ["счёт", "отсчёт", "таймер", "осталось"]
subjects = [("математика", "матека", "матика", "матеша", "база", "профиль"),
            ("география", "географ", "гео"),
            ("литература", "литра", "лит-ра", "литера"),
            ("химия", "химик"),
            ("русский", "русиш", "руский", "русич"),
            ("история", "историк", "истори", "хистори", "history"),
            ("физика", "физик"),
            ("обществознание", "общество", "общага"),
            ("иностранные", "иностраные", "иностранный", "иностраный", "иняз",
             "английский", "китайский", "китайский", "немецкий", "француский",
             "инглиш", "англ"),
            ("информатика", "инфа", "ИКТ", "программирование",
             "програмирование", "кодинг", "код")]
ege_marks = ["егэ", "экзамена", "экзаменов", "сдача", "сдачи", "аттестация",
             "аттестации", "атестация", "атестации", "гиа"]
coin_words = ["орёл", "орел", "решка", "монетка", "монета", "подбрось",
              "подбросить", "брось", "бросьте", "подбросьте", "подкинь",
              "подкиньте", "бросай", "бросайте", "монетку", "монету", "coin", ]
you_mark = ["ты", "тебя", "тебе", "вы", "вас"]
prepare_words = ["подготовка", "подготовки", "материалы", "матерьялы",
                 "задания", "варианты", "типовые"]
get_panic = ("А" * 3997) + ("!" * 3)

day_maths = dt.datetime(2023, 6, 1)
day_geo = dt.datetime(2023, 5, 26)
day_chem = dt.datetime(2023, 5, 26)
day_litera = dt.datetime(2023, 5, 26)
day_russian = dt.datetime(2023, 5, 29)
day_history = dt.datetime(2023, 6, 5)
day_fizik = dt.datetime(2023, 6, 5)  # Даты ЕГЭ
day_obs = dt.datetime(2023, 6, 8)
day_bio = dt.datetime(2023, 6, 13)
day_inyaz = dt.datetime(2023, 6, 13)
day_inyaz_gov_1 = dt.datetime(2023, 6, 16)
day_inyaz_gov_2 = dt.datetime(2023, 6, 17)
day_info_1 = dt.datetime(2023, 6, 19)
day_info_2 = dt.datetime(2023, 6, 20)

chats_list = ["1", "2"]
strip_symbols = ["!", "?", ",", ".", ")", "(", "\t", " "]
start_bot_msg = ("Выберите чат для запуска бота." +
                 " Введите 1 для отправки в основной чат" +
                 " и 2 для отправки в тестовый чат:")
coin_dropper = Coin()
print(start_bot_msg)
chat_id = input("Введите 1 или 2 => ")
while chat_id not in chats_list:
    chat_id = input("Ошибка ввода. Повторите попытку => ")
chat_id = int(chat_id)
bot_started = "Бот успешно начал свою работу!\n"
print(bot_started)
vk = session_bot.get_api()
id_to_send = randint(0, 2 ** 64)
text = "Бот начал свою работу."
vk.messages.send(
    chat_id=chat_id,
    message=text,
    random_id=id_to_send)

for event in connection.listen():  # Главный цикл программы
    if event.type in messages_list:
        msg_text = event.obj['message']['text']
        msg_id = int(event.obj['message']['from_id'])
        log_text = f"Получено сообщение от id {msg_id}. Текст:"
        print(log_text)
        print(msg_text + "\n")
        splitted_text = msg_text.strip().rstrip("\n")
        bool_go = False
        if len(splitted_text):
            if splitted_text[-1] in strip_symbols:
                bool_go = True
        while bool_go:
            for element in strip_symbols:
                splitted_text = splitted_text.rstrip(element)
            if len(splitted_text):
                if splitted_text[-1] in strip_symbols:
                    bool_go = True
                else:
                    bool_go = False
            else:
                bool_go = False
        splitted_text = splitted_text.split()
        if len(splitted_text):
            search_call = splitted_text[0].lower()
        else:
            search_call = "None"
        if (search_call in bot_names or
            (search_call[-1] == "," and
             search_call[0:len(search_call) - 1] in bot_names)):
            if msg_id not in list_of_id:
                text = get_start_text()
                open_file = open(path_to_id, "a")
                string_to_write = f"{msg_id}\n"
                open_file.write(string_to_write)
                open_file.close()
                list_of_id.append(msg_id)
            else:
                if len(splitted_text) == 1:
                    text = "Да-да?"
                elif (len(splitted_text) >= 2 and
                      cleaner(splitted_text[1].lower()) == "паровозов"):
                    text = "Чух-чуууух!"
                elif (len(splitted_text) >= 2 and
                      cleaner(splitted_text[1].lower()) in prepare_words):
                    text = "\n".join(prepare)
                elif (len(splitted_text) >= 2 and
                      cleaner(splitted_text[1].lower()) in coin_words):
                    text = coin_dropper.drop()
                elif (len(splitted_text) >= 5
                        and cleaner(splitted_text[1].lower()) in dates_names
                        and cleaner(splitted_text[2].lower()) in ege_marks):
                    if (splitted_text[3] in dates
                            and splitted_text[4] in stages):
                        n_data = cleaner(splitted_text[3])
                        n_stage = cleaner(splitted_text[4].lower())
                        n_stage = n_stage[0].upper() + n_stage[1:]
                        n_path = f"data/text/dates/{n_data}/{n_stage}.txt"
                        text = (f"Даты ЕГЭ в {n_data} году в "
                                + f"{n_stage} период:\n")
                        boofer = "".join(open(n_path, "r",
                                                encoding='utf-8').readlines())
                        text += boofer
                    else:
                        text = ("Ошибка. Укажите корректные год "
                                + "и период через пробел!")
                elif (len(splitted_text) >= 4
                     and cleaner(splitted_text[1].lower()) in dates_names
                     and cleaner(splitted_text[2].lower()) in ege_marks):
                    if cleaner(splitted_text[3].lower()) in dates:
                        n_data = cleaner(splitted_text[3].lower())
                        text = (f"Даты ЕГЭ в {n_data} году\n\n")
                        text += "Досрочный период:\n***\n"
                        n_path = f"data/text/dates/{n_data}/Досрочный.txt"
                        boofer = "".join(open(n_path, "r",
                                                encoding='utf-8').readlines())
                        text += boofer
                        text += "\n***\nОсновной период:\n"
                        n_path = f"data/text/dates/{n_data}/Основной.txt"
                        boofer = "".join(open(n_path, "r",
                                                encoding='utf-8').readlines())
                        text += boofer
                        text += "\n***\nДополнительный период:\n"
                        n_path = f"data/text/dates/{n_data}/Дополнительный.txt"
                        boofer = "".join(open(n_path, "r",
                                                encoding='utf-8').readlines())
                        text += boofer + "\n***"
                    else:
                        text = ("Ошибка. Укажите корректный год " +
                                "(2013-2023 включительно)!")                       
                elif (len(splitted_text) >= 4
                        and cleaner(splitted_text[1].lower()) in dates_names):
                    if (cleaner(splitted_text[2].lower()) in dates
                            and cleaner(splitted_text[3].lower()) in stages):
                        n_data = cleaner(splitted_text[2].lower())
                        n_stage = cleaner(splitted_text[3].lower())
                        n_stage = n_stage[0].upper() + n_stage[1:]
                        n_path = f"data/text/dates/{n_data}/{n_stage}.txt"
                        text = (f"Даты ЕГЭ в {n_data} году в " +
                                f"{n_stage} период:\n")
                        boofer = "".join(open(n_path, "r",
                                                encoding='utf-8').readlines())
                        text += boofer
                    else:
                        text = ("Ошибка. Укажите корректные год " +
                                "и период через пробел!")
                elif (len(splitted_text) >= 3 and
                     cleaner(splitted_text[1].lower()) in dates_names):
                    if cleaner(splitted_text[2].lower()) in dates:
                        n_data = cleaner(splitted_text[2].lower())
                        text = (f"Даты ЕГЭ в {n_data} году\n\n")
                        text += "Досрочный период:\n***\n"
                        n_path = f"data/text/dates/{n_data}/Досрочный.txt"
                        boofer = "".join(open(n_path, "r",
                                                encoding='utf-8').readlines())
                        text += boofer
                        text += "\n***\nОсновной период:\n"
                        n_path = f"data/text/dates/{n_data}/Основной.txt"
                        boofer = "".join(open(n_path, "r",
                                                encoding='utf-8').readlines())
                        text += boofer
                        text += "\n***\nДополнительный период:\n"
                        n_path = f"data/text/dates/{n_data}/Дополнительный.txt"
                        boofer = "".join(open(n_path, "r",
                                                encoding='utf-8').readlines())
                        text += boofer + "\n***"
                    else:
                        text = ("Ошибка. Укажите корректный год "
                                + "(2013-2023 включительно)!")
                elif (len(splitted_text) >= 3 and
                      cleaner(splitted_text[1].lower()) in remove_id_names):
                    if cleaner(splitted_text[2].lower()) in user_self_names:
                        file = open(path_to_id, "w")
                        boofer = []
                        for ID in list_of_id:
                            if ID != msg_id:
                                file.write(f"{ID}\n")
                                boofer.append(ID)
                            list_of_id = []
                            for element in boofer:
                                list_of_id.append(element)
                            file.close()
                        text = f"Пользователь {msg_id} успешно забыт!"
                    elif cleaner(splitted_text[2].lower()) in user_all_names:
                        if msg_id == admin_id:
                            file = open(path_to_id, "w")
                            file.write("")
                            file.close()
                            list_of_id = []
                            text = "Все id пользователей забыты успешно!"
                        else:
                            text = "Вы не администратор!"
                    else:
                        text = "Не смог обработать запрос. Попробуйте снова."
                elif (len(splitted_text) >= 2
                      and cleaner(splitted_text[1].lower()) in say_hello):
                    text = get_random_hello(msg_id)
                elif (len(splitted_text) >= 3
                      and cleaner(splitted_text[2].lower()) in bad_words
                      and cleaner(splitted_text[1].lower()) in you_mark):
                    text = "Как Вам не стыдно обижать бота?("
                elif (len(splitted_text) >= 2
                      and cleaner(splitted_text[1].lower()) in bad_words):
                    text = "Как Вам не стыдно обижать бота?("
                elif (len(splitted_text) >= 2 and
                      cleaner(splitted_text[1].lower()) in help_command_names):
                    text = ("Вот список всех доступных на " +
                            f"данный момент команд:\n{command_link}")
                elif (len(splitted_text) >= 2
                      and cleaner(splitted_text[1].lower()) in motivate_words):
                    text = get_motivation()
                elif (len(splitted_text) >= 2
                      and cleaner(splitted_text[1].lower()) in panic_words):
                    text = get_panic
                elif (len(splitted_text) >= 2
                      and cleaner(splitted_text[1].lower()) in stop_work_words):
                    if msg_id == admin_id:
                        text = "Прекращаю работу. До свидания!"
                        id_to_send = randint(0, 2 ** 64)
                        vk.messages.send(
                            chat_id=chat_id,
                            message=text,
                            random_id=id_to_send)
                        sleep(1)
                        break
                    else:
                        text = "Вы не администратор!"
                elif (len(splitted_text) >= 3
                      and cleaner(splitted_text[1].lower()) in get_clock_words):
                    now_day = dt.datetime.today()
                    n_subj = "None"
                    delta = None
                    if cleaner(splitted_text[2].lower()) in subjects[0]:
                        delta = (day_maths - now_day).days
                        day = days(delta)
                        n_subj = "базовой и профильной математике"
                    elif cleaner(splitted_text[2].lower()) in subjects[1]:
                        delta = (day_geo - now_day).days
                        day = days(delta)
                        n_subj = "географии"
                    elif cleaner(splitted_text[2].lower()) in subjects[2]:
                        delta = (day_litera - now_day).days
                        day = days(delta)
                        n_subj = "литературе"
                    elif cleaner(splitted_text[2].lower()) in subjects[3]:
                        delta = (day_chem - now_day).days
                        day = days(delta)
                        n_subj = "химии"
                    elif cleaner(splitted_text[2].lower()) in subjects[4]:
                        delta = (day_russian - now_day).days
                        day = days(delta)
                        n_subj = "русскому языку"
                    elif cleaner(splitted_text[2].lower()) in subjects[5]:
                        delta = (day_history - now_day).days
                        day = days(delta)
                        n_subj = "истории"
                    elif cleaner(splitted_text[2].lower()) in subjects[6]:
                        delta = (day_fizik - now_day).days
                        day = days(delta)
                        n_subj = "физике"
                    elif cleaner(splitted_text[2].lower()) in subjects[7]:
                        delta = (day_obs - now_day).days
                        day = days(delta)
                        n_subj = "обществознанию"
                    elif cleaner(splitted_text[2].lower()) in subjects[8]:
                        delta1 = (day_inyaz - now_day).days
                        delta2 = (day_inyaz_gov_1 - now_day).days
                        delta3 = (day_inyaz_gov_2 - now_day).days
                        day1 = days(delta1)
                        day2 = days(delta2)
                        day3 = days(delta3)
                        text = (f"ЕГЭ по иностранным языкам пройдёт через " +
                                f"{delta1} {day1}. До первого срока этапа " +
                                f"'говорение' остаётся {delta2} {day2}, до " +
                                f"второго - {delta3} {day3}.")
                    elif cleaner(splitted_text[2].lower()) in subjects[9]:
                        delta1 = (day_info_1 - now_day).days
                        delta2 = (day_info_2 - now_day).days
                        day1 = days(delta1)
                        day2 = days(delta2)
                        text = (f"ЕГЭ по информатике пройдёт через " +
                                f"{delta1} {day1}. До второго срока " +
                                f"проведения остаётся {delta2} {day2}.")
                    else:
                        text = "Укажите существующий предмет для сдачи ЕГЭ!"
                    if n_subj != "None":
                        text = f"ЕГЭ по {n_subj} пройдёт через {delta} {day}."
                else:
                    text = "Не смог обработать запрос. Попробуйте снова."
            id_to_send = randint(0, 2 ** 64)
            log_text = ("Отправлено сообщение с id " +
                        f"{id_to_send} в чат {chat_id}. Текст:")
            print(log_text)
            print(text + "\n")
            vk.messages.send(
                chat_id=chat_id,
                message=text,
                random_id=id_to_send)
        else:
            if msg_id not in list_of_id:
                text = get_start_text()
                open_file = open(path_to_id, "a")
                string_to_write = f"{msg_id}\n"
                open_file.write(string_to_write)
                open_file.close()
                list_of_id.append(msg_id)
            elif (len(splitted_text) >= 1 and
                      cleaner(splitted_text[0].lower()) == "паровозов"):
                text = "Чух-чуууух!"
            elif (len(splitted_text) >= 1 and
                    cleaner(splitted_text[0].lower()) in prepare_words):
                text = "\n".join(prepare)
            elif (len(splitted_text) >= 1 and
                    cleaner(splitted_text[0].lower()) in coin_words):
                text = coin_dropper.drop()
            elif (len(splitted_text) >= 4
                    and cleaner(splitted_text[0].lower()) in dates_names
                    and cleaner(splitted_text[1].lower()) in ege_marks):
                if (splitted_text[2] in dates
                        and splitted_text[3] in stages):
                    n_data = cleaner(splitted_text[2])
                    n_stage = cleaner(splitted_text[3].lower())
                    n_stage = n_stage[0].upper() + n_stage[1:]
                    n_path = f"data/text/dates/{n_data}/{n_stage}.txt"
                    text = (f"Даты ЕГЭ в {n_data} году в "
                            + f"{n_stage} период:\n")
                    boofer = "".join(open(n_path, "r",
                                            encoding='utf-8').readlines())
                    text += boofer
                else:
                    text = ("Ошибка. Укажите корректные год "
                            + "и период через пробел!")
            elif (len(splitted_text) >= 3
                    and cleaner(splitted_text[0].lower()) in dates_names
                    and cleaner(splitted_text[1].lower()) in ege_marks):
                if cleaner(splitted_text[2].lower()) in dates:
                    n_data = cleaner(splitted_text[2].lower())
                    text = (f"Даты ЕГЭ в {n_data} году\n\n")
                    text += "Досрочный период:\n***\n"
                    n_path = f"data/text/dates/{n_data}/Досрочный.txt"
                    boofer = "".join(open(n_path, "r",
                                            encoding='utf-8').readlines())
                    text += boofer
                    text += "\n***\nОсновной период:\n"
                    n_path = f"data/text/dates/{n_data}/Основной.txt"
                    boofer = "".join(open(n_path, "r",
                                            encoding='utf-8').readlines())
                    text += boofer
                    text += "\n***\nДополнительный период:\n"
                    n_path = f"data/text/dates/{n_data}/Дополнительный.txt"
                    boofer = "".join(open(n_path, "r",
                                            encoding='utf-8').readlines())
                    text += boofer + "\n***"
                else:
                    text = ("Ошибка. Укажите корректный год "
                            + "(2013-2023 включительно)!")
            elif (len(splitted_text) >= 3
                    and cleaner(splitted_text[0].lower()) in dates_names):
                if (cleaner(splitted_text[1].lower()) in dates
                        and cleaner(splitted_text[2].lower()) in stages):
                    n_data = cleaner(splitted_text[1].lower())
                    n_stage = cleaner(splitted_text[2].lower())
                    n_stage = n_stage[0].upper() + n_stage[1:]
                    n_path = f"data/text/dates/{n_data}/{n_stage}.txt"
                    text = (f"Даты ЕГЭ в {n_data} году в " +
                            f"{n_stage} период:\n")
                    boofer = "".join(open(n_path, "r",
                                            encoding='utf-8').readlines())
                    text += boofer
                else:
                    text = ("Ошибка. Укажите корректные год " +
                            "и период через пробел!")
            elif (len(splitted_text) >= 2 and
                    cleaner(splitted_text[0].lower()) in dates_names):
                if cleaner(splitted_text[1].lower()) in dates:
                    n_data = cleaner(splitted_text[1].lower())
                    text = (f"Даты ЕГЭ в {n_data} году\n\n")
                    text += "Досрочный период:\n***\n"
                    n_path = f"data/text/dates/{n_data}/Досрочный.txt"
                    boofer = "".join(open(n_path, "r",
                                            encoding='utf-8').readlines())
                    text += boofer
                    text += "\n***\nОсновной период:\n"
                    n_path = f"data/text/dates/{n_data}/Основной.txt"
                    boofer = "".join(open(n_path, "r",
                                            encoding='utf-8').readlines())
                    text += boofer
                    text += "\n***\nДополнительный период:\n"
                    n_path = f"data/text/dates/{n_data}/Дополнительный.txt"
                    boofer = "".join(open(n_path, "r",
                                            encoding='utf-8').readlines())
                    text += boofer + "\n***"
                else:
                    text = ("Ошибка. Укажите корректный год "
                            + "(2013-2023 включительно)!")
            elif (len(splitted_text) >= 2 and
                    cleaner(splitted_text[0].lower()) in remove_id_names):
                if cleaner(splitted_text[1].lower()) in user_self_names:
                    file = open(path_to_id, "w")
                    boofer = []
                    for ID in list_of_id:
                        if ID != msg_id:
                            file.write(f"{ID}\n")
                            boofer.append(ID)
                        list_of_id = []
                        for element in boofer:
                            list_of_id.append(element)
                        file.close()
                    text = f"Пользователь {msg_id} успешно забыт!"
                elif cleaner(splitted_text[1].lower()) in user_all_names:
                    if msg_id == admin_id:
                        file = open(path_to_id, "w")
                        file.write("")
                        file.close()
                        list_of_id = []
                        text = "Все id пользователей забыты успешно!"
                    else:
                        text = "Вы не администратор!"
                else:
                    text = "Не смог обработать запрос. Попробуйте снова."
            elif (len(splitted_text) >= 1
                    and cleaner(splitted_text[0].lower()) in say_hello):
                text = get_random_hello(msg_id)
            elif (len(splitted_text) >= 2
                    and cleaner(splitted_text[1].lower()) in bad_words
                    and cleaner(splitted_text[0].lower()) in you_mark):
                text = "Как Вам не стыдно обижать бота?("
            elif (len(splitted_text) >= 1
                    and cleaner(splitted_text[0].lower()) in bad_words):
                text = "Как Вам не стыдно обижать бота?("
            elif (len(splitted_text) >= 1 and
                    cleaner(splitted_text[0].lower()) in help_command_names):
                text = ("Вот список всех доступных на " +
                        f"данный момент команд:\n{command_link}")
            elif (len(splitted_text) >= 1
                    and cleaner(splitted_text[0].lower()) in motivate_words):
                text = get_motivation()
            elif (len(splitted_text) >= 1
                    and cleaner(splitted_text[0].lower()) in panic_words):
                text = get_panic
            elif (len(splitted_text) >= 1
                    and cleaner(splitted_text[0].lower()) in stop_work_words):
                if msg_id == admin_id:
                    text = "Прекращаю работу. До свидания!"
                    id_to_send = randint(0, 2 ** 64)
                    vk.messages.send(
                        chat_id=chat_id,
                        message=text,
                        random_id=id_to_send)
                    sleep(1)
                    break
                else:
                    text = "Вы не администратор!"
            elif (len(splitted_text) >= 2
                    and cleaner(splitted_text[0].lower()) in get_clock_words):
                now_day = dt.datetime.today()
                n_subj = "None"
                delta = None
                if cleaner(splitted_text[1].lower()) in subjects[0]:
                    delta = (day_maths - now_day).days
                    day = days(delta)
                    n_subj = "базовой и профильной математике"
                elif cleaner(splitted_text[1].lower()) in subjects[1]:
                    delta = (day_geo - now_day).days
                    day = days(delta)
                    n_subj = "географии"
                elif cleaner(splitted_text[1].lower()) in subjects[2]:
                    delta = (day_litera - now_day).days
                    day = days(delta)
                    n_subj = "литературе"
                elif cleaner(splitted_text[1].lower()) in subjects[3]:
                    delta = (day_chem - now_day).days
                    day = days(delta)
                    n_subj = "химии"
                elif cleaner(splitted_text[1].lower()) in subjects[4]:
                    delta = (day_russian - now_day).days
                    day = days(delta)
                    n_subj = "русскому языку"
                elif cleaner(splitted_text[1].lower()) in subjects[5]:
                    delta = (day_history - now_day).days
                    day = days(delta)
                    n_subj = "истории"
                elif cleaner(splitted_text[1].lower()) in subjects[6]:
                    delta = (day_fizik - now_day).days
                    day = days(delta)
                    n_subj = "физике"
                elif cleaner(splitted_text[1].lower()) in subjects[7]:
                    delta = (day_obs - now_day).days
                    day = days(delta)
                    n_subj = "обществознанию"
                elif cleaner(splitted_text[1].lower()) in subjects[8]:
                    delta1 = (day_inyaz - now_day).days
                    delta2 = (day_inyaz_gov_1 - now_day).days
                    delta3 = (day_inyaz_gov_2 - now_day).days
                    day1 = days(delta1)
                    day2 = days(delta2)
                    day3 = days(delta3)
                    text = (f"ЕГЭ по иностранным языкам пройдёт через " +
                            f"{delta1} {day1}. До первого срока этапа " +
                            f"'говорение' остаётся {delta2} {day2}, до " +
                            f"второго - {delta3} {day3}.")
                elif cleaner(splitted_text[1].lower()) in subjects[9]:
                    delta1 = (day_info_1 - now_day).days
                    delta2 = (day_info_2 - now_day).days
                    day1 = days(delta1)
                    day2 = days(delta2)
                    text = (f"ЕГЭ по информатике пройдёт через " +
                            f"{delta1} {day1}. До второго срока " +
                            f"проведения остаётся {delta2} {day2}.")
                else:
                    text = "Укажите существующий предмет для сдачи ЕГЭ!"
                if n_subj != "None":
                    text = f"ЕГЭ по {n_subj} пройдёт через {delta} {day}."
            else:
                text = "Не смог обработать запрос. Попробуйте снова."
            id_to_send = randint(0, 2 ** 64)
            log_text = ("Отправлено сообщение с id " +
                        f"{id_to_send} в чат {chat_id}. Текст:")
            print(log_text)
            print(text + "\n")
            vk.messages.send(
                chat_id=chat_id,
                message=text,
                random_id=id_to_send)

    elif event.type == VkBotEventType.GROUP_JOIN:
        joined_user_id = event.obj["user_id"]
        text = f"Новый пользователь с id {joined_user_id} присоединился с группе!"
        id_to_send = randint(0, 2 ** 64)
        log_text = ("Отправлено сообщение с id " +
                    f"{id_to_send} в чат {chat_id}. Текст:")
        print(log_text)
        print(text + "\n")        
        vk.messages.send(
            chat_id=chat_id,
            message=text,
            random_id=id_to_send)

    elif event.type == VkBotEventType.GROUP_LEAVE:
        leaved_user_id = event.obj["user_id"]
        text = f"Новый пользователь с id {leaved_user_id} покинул группу!("
        id_to_send = randint(0, 2 ** 64)
        log_text = ("Отправлено сообщение с id " +
                    f"{id_to_send} в чат {chat_id}. Текст:")
        print(log_text)
        print(text + "\n")        
        vk.messages.send(
            chat_id=chat_id,
            message=text,
            random_id=id_to_send)
    else:
        print(event)
        print()
