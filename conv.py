import html
import os
import glob
import pypandoc
import shutil
import codecs


# создаем папку, в которую будут перенесены обработнные файлы
if not os.path.isdir("Обработано"):
     os.mkdir("Обработано")

# Открываем файлы формата *.html, имеющиеся в текущей папке. Конвертируем его в *.md
for infile in glob.glob("*.html"):
    new_name = '{}_{}'.format(os.path.basename(os.path.dirname(infile)), os.path.basename(infile))  # Присваиваем новове имя файлу
    print('Файл', infile, 'обрабатывается')
    doc = pypandoc.convert_file(infile, 'md', outputfile= new_name + ".md")   # Конвертируем файл в формат *.md

# После конвертации убираем артефакты, не нужные строки
    for infile in glob.glob("*.md"):
        with open(infile, "r", encoding='utf-8') as file:
             lines = file.readlines()
             if not lines:
                break

        print('Файл', infile, 'редактируется')

        with open(infile, 'w') as f:
             for line in lines:
                 if ":::" not in line:
                     if "div" not in line:
                         f.write(line)


        print('Файл', infile, 'перенесен в папку "Обработано"')

        # После всех обработок файл переносим в папку "Обработано"

        for a in glob.glob('*.md'):
            new_name = '{}_{}'.format(os.path.basename(os.path.dirname(a)), os.path.basename(a))
            shutil.move(a, os.path.join('Обработано', new_name))


print('Готово')