import os
import uuid
from datetime import datetime


def file_path(instance, filename):
    _, file_extension= os.path.splitext(filename)
    filename= datetime.now().strftime('%Y/%m/%d/')+'file-'+uuid.uuid4().hex
    return '{filename}{ext}'.format( filename= filename, ext= file_extension)
