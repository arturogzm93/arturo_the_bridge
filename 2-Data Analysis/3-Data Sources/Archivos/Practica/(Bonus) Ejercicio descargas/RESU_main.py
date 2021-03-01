

# automation.py
import os
from shutil import move


# directory paths
user = os.getlogin()
root_dir = 'C:/Users/{}/Downloads/'.format(user)
image_dir = 'C:/Users/{}/Downloads/images/'.format(user)
documents_dir = 'C:/Users/{}/Downloads/documents/'.format(user)
others_dir = 'C:/Users/{}/Downloads/others/'.format(user)
software_dir = 'C:/Users/{}/Downloads/softwares/'.format(user)

# category wise file types
doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif', '.tif', '.tiff')
software_types = ('.exe', '.pkg', '.dmg')

def get_non_hidden_files_except_current_file(root_dir):
  return [f for f in os.listdir(root_dir) if os.path.isfile(root_dir + f) and not f.startswith('.')]


def move_files(files):

  for file in files:
    # file moved and overwritten if already exists
    if file.endswith(doc_types):
      move(root_dir + file, documents_dir)
      print('file {} moved to {}'.format(file, documents_dir))
    elif file.endswith(img_types):
      move(root_dir + file, image_dir)
      print('file {} moved to {}'.format(file, image_dir))
    elif file.endswith(software_types):
      move(root_dir + file, software_dir)
      print('file {} moved to {}'.format(file, others_dir))
    else:
      move(root_dir + file, others_dir)
      print('file {} moved to {}'.format(file, others_dir))


if __name__ == "__main__":
  files = get_non_hidden_files_except_current_file(root_dir)
  move_files(files)