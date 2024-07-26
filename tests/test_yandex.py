from unittest import TestCase
import yandex

class TestMain(TestCase):
    token = ''  # https://yandex.ru/dev/disk/poligon/
    ya_disk = yandex.YandexDisk(token)

    def test_create_folder(self):
        response = self.ya_disk.create_folder("new_folder")
        assert response.status_code == 201 # папка создана

    def test_check_folder(self):
        response = self.ya_disk.check_folder("new_folder")
        assert response.status_code == 200  # папка существует
        assert response.status_code == 404  # папки не существует


    def test_delete_folder(self):
        response = self.ya_disk.delete_folder("new_folder")
        assert response.status_code == 204  # папка удалена
        assert response.status_code == 404  # папки не существует

