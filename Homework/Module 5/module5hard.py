class User:
    users = []

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        self.users.append([nickname, password, age])

    def __str__(self):
        return f'{self.nickname}'

    def __eq__(self, other):
        return self.password == other


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title


class UrTube:
    def __init__(self, videos=[], current_user=None, users=User.users):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, login, password):
        for i in self.users:
            if login in i and password in i:
                self.current_user = login
            else: print('Такого пользователя не существует')

    def register(self, nickname, password, age):
        if self.users == []:
            User(nickname, password, age)
        else:
            for i in self.users:
                if nickname in i:
                    print(f'Пользователь {nickname} уже существует')
                else:
                    User(nickname, password, age)

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            if self.videos == []:
                self.videos.append([i])
                continue
            for j in self.videos:
                if i not in j:
                    self.videos.append(i)
                    break
                else:
                    print('Такое видео уже существует')





    def get_videos(self):
        pass

    def watch_video(self):
        pass

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = Video('Лучший язык программирования 2024 года', 200)

# Добавление видео
ur.add(v1, v2, v3)
print(ur.videos)


