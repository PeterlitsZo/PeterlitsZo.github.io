from docx import Document, shared
from pdf2image import convert_from_path
from pathlib import Path

print(Path.cwd())
print('-' * 50)
list_file = list(Path.cwd().iterdir())
for i_index, i in enumerate(list_file):
    print(i_index, i.name)
index = int(input('> '))
print(list_file[index])
print('-' * 50)
images = convert_from_path(list_file[index], dpi = 720)
Path.mkdir(Path.cwd() / (list_file[index].name + '.dir'), exist_ok=True)

path = Path.cwd() / (list_file[index].name + '.dir')
if path.exists():
    print(f'there is {path}')

for i_index, i in enumerate(images):
    i_path = path / f'{i_index}.jpg'
    i_path.touch(exist_ok=True)
    print(i_path)
    # 1654 * 2339 -> 5953 * 8419
    i_crop = i.crop((720, 846, 5233, 7580))
    i_crop.save(path / f'{i_index}.jpg')

doc = Document()
for i in range(len(images)):
    doc.add_picture(str(path / f'{i}.jpg'), width=shared.Mm(152.3))
    print(f'add pic {i}')
doc.save(Path.cwd() / (list_file[index].name + '.docx'))