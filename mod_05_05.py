
from time import sleep

# Каждый объект класса User должен обладать следующими атрибутами и методами:
#   Атриубуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
# Каждый объект класса Video должен обладать следующими атрибутами и методами:
#   Атриубуты: title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки
#       (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))
# Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
#   Атриубты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
#   Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users
#       с такими же логином и паролем. Если такой пользователь существует, то current_user меняется на найденного.
#       Помните, что password передаётся в виде строки, а сравнивается по хэшу.
#   Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список,
#       если пользователя не существует (с таким же nickname). Если существует, выводит на экран:
#       "Пользователь {nickname} уже существует". После регистрации, вход выполняется автоматически.
#   Метод log_out для сброса текущего пользователя на None.
#   Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos,
#       если с таким же названием видео ещё не существует. В противном случае ничего не происходит.
#   Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих
#       поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best'
#       (не учитывать регистр).
#   Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела),
#       то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде
#       ведётся просмотр. После текущее время просмотра данного видео сбрасывается.
# Для метода watch_video так же учитывайте следующие особенности:
#   Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
#   Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. В противном случае
#       выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
#   Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть
#       ограничения 18+. Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
#   После воспроизведения нужно выводить: "Конец видео"

class User:

    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)

        self.password = hash(password)
        if isinstance(password, int):
            self.password = password

        self.age = int(age)

    def __eq__(self, other): # ==
        if isinstance(other, User):
            return self.nickname == other.nickname
        return False

    def __str__(self):
        # return f'Ник: {self.nickname}, пароль: {self.password}, возраст: {self.age}'
        return f'{self.nickname}'

class Video:

    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = str(title)
        self.duration = int(duration)
        self.time_now = int(time_now)
        self.adult_mode = bool(adult_mode)

    def __eq__(self, other): # ==
        if isinstance(other, User):
            return self.title == other.title
        return False

    def __str__(self):
        return f'Название: {self.title}, длительность: {self.duration}'


class UrTube:

    users = []
    videos = []

    def __init__(self, current_user = None):
        self.current_user = None
        if current_user != None and isinstance(current_user, User):
            if not self.log_in(current_user.nickname, current_user.password):
                self.register(current_user.nickname, current_user.password, current_user.age)


    def log_in(self, nickname, password):

        temp_user = User(nickname, password, 1)

        if temp_user not in self.users:
            print(f'Пользователя с ником {nickname} не существует')
            return False

        index_temp_user = self.users.index(temp_user)

        if self.users[index_temp_user].password != temp_user.password:
                print(f'Неверный пароль')
                return False

        self.current_user = self.users[index_temp_user]
        # print(f'Приветствую вас {self.current_user.nickname}')
        return True

    def log_out(self):
        self.current_user = None

    def register(self, nickname, password, age):

        new_user = User(nickname, password, age)
        if new_user in self.users:
            print(f'Пользователь с ником {nickname} уже существует')
            return False

        # print(f'Пользователь {nickname} ещё не существует')
        self.users.append(new_user)
        # print(*self.users)
        self.log_in(nickname, password)
        return True


    def add(self, *args):

        self.videos.extend(item for item in args if isinstance(item, Video) if item not in self.videos)
        # self.videos.extend(args)


    def get_videos(self, substr):
        title_list = []
        for item in self.videos:
            if substr.lower() in item.title.lower():
                title_list.append(item.title)

        return title_list

    def watch_video(self, title_video):

        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return False

        if self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
            return False

        for item in self.videos:
            if title_video == item.title:
                self.player_video(item)
                print('Конец видео')

        return True



    def player_video(self, current_video):

        for sec in range(1, current_video.duration + 1):
            sleep(0.25)
            print(sec, end = ' ')




maxx = User('Макс', '5jjj5dd', 20)
den = User('Деня', '5jjj5ddd5', 25)
UrTube(maxx)
UrTube(den)
print(*UrTube.users)

john = User('Джон', 'j5ddd5', 33)
film = Video('Ролик', 47)
tube = UrTube(john)
print(*tube.users)

tube.register('Деня', '5jjj5ddd5', 25)
tube.register('Ден', '5jjj5ddd5', 25)

tube.log_in('Макс', '5j') # Неверный пароль
tube.log_in('Макс', '5jjj5dd')
print()


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2, v1)
# print(*ur.videos)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

print()
print(*ur.users)
