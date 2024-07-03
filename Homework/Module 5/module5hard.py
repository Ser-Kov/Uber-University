from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __eq__(self, other):
        return self.password == other


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self, videos=[], current_user=None, users=[]):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, login, password):
        for i in self.users:
            if login in i.nickname and hash(password) == i.password:
                self.current_user = login
                print(f'Добро пожаловать, {self.current_user}!')
                continue
            elif login not in i.nickname:
                print('Такого пользователя не существует')
            elif login in i.nickname and hash(password) != i.password:
                print('Неверный пароль')

    def register(self, nickname, password, age):
        if any(nickname == i.nickname for i in self.users):
            print(f'Пользователь {nickname} уже существует')
        else:
            self.users.append(User(nickname, password, age))
            self.current_user = self.users[-1].nickname
            print(f'Добро пожаловать, {self.current_user}!')

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            if all(i.title != j for j in self.videos):
                self.videos.append(i)
            else:
                print(f'Видео "{i.title}" уже было добавлено!')

    def get_videos(self, search_word):
        list_ = []
        for i in self.videos:
            word = search_word.lower()
            title = i.title.lower()
            if word in title:
                list_.append(i.title)
                continue
        return list_

    def watch_video(self, name_video):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for i in self.videos:
                if i.title != name_video:
                    continue
                else:
                    for user in self.users:
                        if self.current_user != user.nickname:
                            continue
                        elif i.adult_mode is True and user.age < 18:
                            print('Вам нет 18 лет, пожалуйста покиньте страницу')
                        elif i.adult_mode is True and user.age >= 18:
                            count_time = 0
                            while count_time < i.duration:
                                count_time += 1
                                i.time_now += 1
                                print(i.time_now, end=' ')
                                sleep(1)
                            print('Конец видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

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
