# __init__.py
from .read_files import ReadFiles
ReadYAML = ReadFiles.ReadYAML
ReadJSON = ReadFiles.ReadJSON
ReadExcel = ReadFiles.ReadExcel
__version__ = '0.0.1'
__all__ = ['ReadFiles', 'ReadYAML', 'ReadJSON', 'ReadExcel']