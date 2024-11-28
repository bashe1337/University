import os
from pdf2docx import Converter as PDFConverter
from docx2pdf import convert as docxToPdfConvert
from PIL import Image

def fileList(extension):
    return [file for file in os.listdir() if file.lower().endswith(extension)]


def changeDir():
    newDir = input("Введите путь к новому рабочему каталогу: ")
    try:
        os.chdir(newDir)
        print(f"Текущий рабочий каталог: {os.getcwd()}")
    except FileNotFoundError:
        print("Катало не найден.")
    except OSError as e:
        print(f"Произошла ошибка: {e}")


def pdfToDocx():
    pdfFiles = fileList(".pdf")
    print("Выберите PDF-файл для преобразования в Docx:")
    for i, pdfFile in enumerate(pdfFiles, start=1):
        print(f"{i}. {pdfFile}")

    try:
        choice = int(input())
        if 1 <= choice <= len(pdfFiles):
            pdfFile = pdfFiles[choice - 1]

            docxFile = os.path.splitext(pdfFile)[0] + ".docx"

            pdfConverter = PDFConverter(pdfFile)
            pdfConverter.convert(docxFile)
            pdfConverter.close()

            print(f"Преобразование завершено. Результат: {docxFile}")
        else:
            print("Неверный ввод. Пожалуйста, выберите существующий файл.")
    except ValueError:
        print("Неверный ввод. Пожалуйста, введите число.")


def docxToPdf():
    docxFiles = fileList(".docx")
    print("Выберите Docx-файл для преобразования в PDF:")
    for i, docxFile in enumerate(docxFiles, start=1):
        print(f"{i}. {docxFile}")

    try:
        choice = int(input())
        if 1 <= choice <= len(docxFiles):
            docxFile = docxFiles[choice - 1]

            pdfFile = os.path.splitext(docxFile)[0] + ".pdf"

            docxToPdfConvert(docxFile, pdfFile)

            print(f"Преобразование завершено. Результат: {pdfFile}")
        else:
            print("Неверный ввод. Пожалуйста, выберите существующий файл.")
    except ValueError:
        print("Неверный ввод. Пожалуйста, введите число.")


def compressImages():
    imageFiles = fileList((".png", ".jpg", ".jpeg"))
    print("Выберите изображение для сжатия:")
    for i, imageFile in enumerate(imageFiles, start=1):
        print(f"{i}. {imageFile}")

    try:
        choice = int(input())
        if 1 <= choice <= len(imageFiles):
            imageFile = imageFiles[choice - 1]

            print("Введите процент сжатия (от 1 до 85):")
            compression = int(input())

            if not (1 <= compression <= 85):
                print("Неверный ввод. Процент сжатия должен быть от 1 до 85.")
                return

            image = Image.open(imageFile)
            compressedImage = f"compressed_{compression}_{imageFile}"

            image.save(compressedImage, optimize=True, quality=compression)

            print(f"Сжатие завершено. Результат: {compressedImage}")
        else:
            print("Неверный ввод. Пожалуйста, выберите существующий файл.")
    except ValueError:
        print("Неверный ввод. Пожалуйста, введите число.")


def deleteFiles():
    print("Выберите критерий удаления:")
    print("1. Удалить все файлы начинающиеся на определенную подстроку")
    print("2. Удалить все файлы заканчивающиеся на определенную подстроку")
    print("3. Удалить все файлы содержащие определенную подстроку")
    print("4. Удалить все файлы по расширению")

    try:
        choice = int(input())
        if 1 <= choice <= 4:
            substring = input("Введите подстроку: ")

            if choice == 1:
                filesToDelete = [f for f in os.listdir() if f.startswith(substring)]
            elif choice == 2:
                filesToDelete = [f for f in os.listdir() if f.endswith(substring)]
            elif choice == 3:
                filesToDelete = [f for f in os.listdir() if substring in f]
            elif choice == 4:
                filesToDelete = [f for f in os.listdir() if f.endswith(substring)]

            print("Будут удалены следующие файлы:")
            for fileName in filesToDelete:
                print(fileName)

            confirm = input("Вы уверены, что хотите удалить эти файлы? (y/n): ")

            if confirm.lower() == "y":
                for file in filesToDelete:
                    os.remove(file)
                print("Удаление завершено.")
            else:
                print("Удаление отменено.")
        else:
            print("Неверный ввод. Пожалуйста, выберите существующий критерий.")
    except ValueError:
        print("Неверный ввод. Пожалуйста, введите число.")


def main():
    while True:
        print("Главное меню:")
        print("1. Сменить рабочий каталог")
        print("2. Преобразовать PDF в Docx")
        print("3. Преобразовать Docx в PDF")
        print("4. Произвести сжатие изображений")
        print("5. Удалить группу файлов")
        print("6. Выход")

        choice = input("Ваш выбор: ")
        if choice.isdigit() == True:
            choice = int(choice)
        else:
            print("Неверный формат. Введите число.")
            continue

        if choice == 1:
            changeDir()
        elif choice == 2:
            pdfToDocx()
        elif choice == 3:
            docxToPdf()
        elif choice == 4:
            compressImages()
        elif choice == 5:
            deleteFiles()
        elif choice == 6:
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите действие снова.")


if __name__ == "__main__":
    main()
