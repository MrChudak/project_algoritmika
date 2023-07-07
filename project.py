# --------v1
# pip install markdown
# почитать о расширениях можно здесь: https://python-markdown.github.io/extensions/
import markdown

# f_md = open("h.md", "r", encoding="UTF-8")  # открытие на чтение
# text_md = f_md.read()  # получить содержимое md файла
# text_html = markdown.markdown(text_md, extensions=["extra"])  # получить содержимое html
# f_html = open("h.html", "w", encoding="UTF-8")  # результирующий файл html
# f_html.write(text_html)
# f_html.close()

with open("h.md", 'r', encoding = "UTF-8") as f_md:
    text_md = f_md.read()
    text_html = markdown.markdown(text_md, extendions = ['extra'])
with open('h.html', 'w', encoding = 'UTF-8') as f_html:
    f_html.write(text_html)
print(text_html)
# --------v2
# pip install md-to-html

import os

# os.system(
#     'md-to-html --input "h.md" --output "h2.html"'
# )  # с помощью метода system выполняется команда terminal