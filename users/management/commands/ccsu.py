import os
from django.core.management import BaseCommand

from users.models import User, UserRoles


class Command(BaseCommand):
    def handle(self, *args, **options):
        admin = User.objects.create(
            email="admin@web.top",
            role=UserRoles.MODERATOR,
            first_name="Admin",
            last_name="Adminov",
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )
        admin.set_password(os.getenv("SUPERUSER_PASSWORD"))
        admin.save()
        print("Админ создан")

        moderator = User.objects.create(
            email="moderator@web.top",
            role=UserRoles.MODERATOR,
            first_name="Moderator",
            last_name="Moderatorov",
            is_staff=True,
            is_superuser=False,
            is_active=True,
        )
        moderator.set_password(os.getenv("MODERATOR_PASSWORD"))
        moderator.save()
        print("Модератор создан")

        member = User.objects.create(
            email="member@web.top",
            role=UserRoles.MODERATOR,
            first_name="Member",
            last_name="Memberov",
            is_staff=False,
            is_superuser=False,
            is_active=True,
        )
        member.set_password(os.getenv("MEMBER_PASSWORD"))
        member.save()
        print("Пользователь создан")
