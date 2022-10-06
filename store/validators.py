

from asyncore import file_dispatcher
from django.core.exceptions import ValidationError


def validate_file_size(file):
    max_size_kb = 1024
    file_old_size = file.size
    print(f'siz   {file_old_size}')

    if file.size > max_size_kb*1024:
        raise ValidationError(
            f'Files cannon be larger than{max_size_kb}KB and filesize {file_old_size}KB')
