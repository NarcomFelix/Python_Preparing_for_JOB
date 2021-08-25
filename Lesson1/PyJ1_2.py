"""
Дополнить следующую функцию недостающим кодом:
def print_directory_contents(sPath):

Функция принимает имя каталога и распечатывает его содержимое
в виде «путь и имя файла», а также любые другие
файлы во вложенных каталогах.

Эта функция подобна os.walk. Использовать функцию os.walk
нельзя. Данная задача показывает ваше умение работать с
вложенными структурами.

"""

def print_directory_contents(sPath):

    array = str(sPath)
    for i in reversed(array):
        dl = 0
        if i != "/":
            dl += 1
        else:
            break

    mean_index = len(array)- dl
    return
    print(dl)
        #print(mean_index)
        # print(f"Путь: {array[:mean_index]}")
        # print(f"Имя файла: {array[mean_index:]}")

print_directory_contents(adsasdg)



