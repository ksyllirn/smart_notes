from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QWidget, QApplication, QPushButton, QLabel
from PyQt5.QtWidgets import QVBoxLayout, QLineEdit, QTextEdit, QListWidget, QInputDialog
import sys
import json

def show_note():
    text = notes_list.selectedItems()[0].text()
    note = notes[text]['текст']
    note_field.setText(note)
#    tags_list.clear()

def load_notes():
    global notes
    with open('notes_data.json', 'r', encoding='utf-8') as file:
        notes = json.load(file)
    notes_list.addItems(notes)

#def del_note():

def save_note():
    global notes
    text = notes_list.selectedItems()[0].text()
    note = note_field.toPlainText()
    notes[text]['текст'] = note
    with open('notes_data.json','w', encoding='utf-8') as file:
        json.dump(notes, file)

def add_note():
    note_name, result = QInputDialog.getText(window,'Добавить заметку', 'Название заметки:')
    print(note_name, result)

notes = {"Приветствие": {
    'текст': 'Что хотите то и делайте',
    'теги': ['начало', 'приветствие']
}}

#with open('notes_data.json', 'w', encoding= 'utf-8') as file:
#    json.dump(notes, file)

app = QApplication(sys.argv)
window = QWidget()


note_field = QTextEdit()
notes_list = QListWidget()
tags_list = QListWidget()

btn_create_note = QPushButton('Создать заметку')
btn_delete_note = QPushButton('Удалить заметку')
btn_save_note = QPushButton('Сохранить заметку')

btn_add_tag = QPushButton('Добавить к заметке')
btn_remove_tag = QPushButton('Открепить от заметки')
btn_search_by_tag = QPushButton('Искать по тегу')

lbl_for_notes = QLabel('Список заметок')
lbl_for_tags = QLabel('Список тегов')
search_tag_field = QLineEdit()

main_line = QHBoxLayout()
left_side = QVBoxLayout()
right_side = QVBoxLayout()

h_1_line = QHBoxLayout()
h_2_line = QHBoxLayout()
h_3_line = QHBoxLayout()
h_4_line = QHBoxLayout()
h_5_line = QHBoxLayout()
h_6_line = QHBoxLayout()
h_7_line = QHBoxLayout()
h_8_line = QHBoxLayout()
h_9_line = QHBoxLayout()

h_1_line.addWidget(lbl_for_notes)
h_2_line.addWidget(notes_list)
h_3_line.addWidget(btn_create_note)
h_3_line.addWidget(btn_delete_note)
h_4_line.addWidget(btn_save_note)
h_5_line.addWidget(lbl_for_tags)
h_6_line.addWidget(tags_list)
h_7_line.addWidget(search_tag_field)
h_8_line.addWidget(btn_add_tag)
h_8_line.addWidget(btn_remove_tag)
h_9_line.addWidget(btn_search_by_tag)

right_side.addLayout(h_1_line)
right_side.addLayout(h_2_line)
right_side.addLayout(h_3_line)
right_side.addLayout(h_4_line)
right_side.addLayout(h_5_line)
right_side.addLayout(h_6_line)
right_side.addLayout(h_7_line)
right_side.addLayout(h_8_line)
right_side.addLayout(h_9_line)

left_side.addWidget(note_field)

main_line.addLayout(left_side)
main_line.addLayout(right_side)

window.setLayout(main_line)
search_tag_field.setPlaceholderText('Введите тег')

window.setWindowTitle('Smart-notes')
window.resize(900,600)
notes_list.itemClicked.connect(show_note)
btn_save_note.clicked.connect(save_note)
btn_create_note.clicked.connect(add_note)

load_notes()
window.show()
app.exec()
