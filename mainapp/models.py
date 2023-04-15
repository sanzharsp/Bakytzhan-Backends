
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)

from .Manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    # Каждому пользователю нужен понятный человеку уникальный идентификатор,
    # который мы можем использовать для предоставления User в пользовательском
    # интерфейсе. Мы так же проиндексируем этот столбец в базе данных для
    # повышения скорости поиска в дальнейшем.
    email = models.EmailField(db_index=True, verbose_name='электрондық пошта', unique=True)
    date_create = models.DateTimeField(auto_now_add=True)
    # Когда пользователь более не желает пользоваться нашей системой, он может
    # захотеть удалить свой аккаунт. Для нас это проблема, так как собираемые
    # нами данные очень ценны, и мы не хотим их удалять :) Мы просто предложим
    # пользователям способ деактивировать учетку вместо ее полного удаления.
    # Таким образом, они не будут отображаться на сайте, но мы все еще сможем
    # далее анализировать информацию.
    is_active = models.BooleanField(default=True)

    # Этот флаг определяет, кто может войти в административную часть нашего
    # сайта. Для большинства пользователей это флаг будет ложным.
    is_staff = models.BooleanField(default=False, verbose_name='жүйе администраторы')

    # Временная метка создания объекта.
    created_at = models.DateTimeField(auto_now_add=True)

    # Временная метка показывающая время последнего обновления объекта.
    updated_at = models.DateTimeField(auto_now=True)

    # Дополнительный поля, необходимые Django
    # при указании кастомной модели пользователя.

    # Свойство USERNAME_FIELD сообщает нам, какое поле мы будем использовать
    # для входа в систему. В данном случае мы хотим использовать почту.
    USERNAME_FIELD = 'email'


    # Сообщает Django, что определенный выше класс UserManager
    # должен управлять объектами этого типа.
    objects = UserManager()

    class Meta:
        ordering = ['id']
        verbose_name = 'қолданушы'
        verbose_name_plural = 'Қолданушылар'

    def __str__(self):
        return "{}".format(self.email)

    @property
    def token(self):
        """
        Позволяет получить токен пользователя путем вызова Author.token, вместо
        user._generate_jwt_token(). Декоратор @property выше делает это
        возможным. token называется "динамическим свойством".
        """
        return self._generate_jwt_token()

    def get_full_name(self):
        """
        Этот метод требуется Django для таких вещей, как обработка электронной
        почты. Обычно это имя фамилия пользователя, но поскольку мы не
        используем их, будем возвращать email.
        """
        return self.email

    def get_short_name(self):
        """ Аналогично методу get_full_name(). """
        return self.email


class Logo(models.Model):
    logo = models.ImageField(verbose_name="Лого")
    def __str__(self) -> str:
        return "Лого"
    
    class Meta:
        ordering = ['id']
        verbose_name = 'лого'
        verbose_name_plural = 'Лого'


class Parking(models.Model):
    id_Parking = models.IntegerField(verbose_name='Деректер базасындағы паркинг номері')
    number = models.IntegerField(verbose_name='Паркингтегі бос орын саны')
    class Meta:
        ordering = ['id']
        verbose_name = 'Паркинг'
        verbose_name_plural = 'Паркинг'