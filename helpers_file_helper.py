import os
import shutil
from pathlib import Path
from base_app import App

class FileHelper:

    # Returns a list of files in the specified directory
    @staticmethod
    def listFiles(directory):
        files = []

        for (_, _, filenames) in os.walk(directory):
            files.extend(filenames)
            break

        return files

    # Returns a file path based on the specified path
    @staticmethod
    def createFilePath(path, root = False):
        return Path((App.instance.dataPath if not root else App.instance.rootPath) + path)

    # Copies a file. You must pass a Path object.
    # Use createFilePath to create a Path object.
    @staticmethod
    def copyFile(src, dest):
        FileHelper.createParentDirectories(dest)
        shutil.copy(src, dest)

    # Creates the parent directories of a file
    @staticmethod
    def createParentDirectories(file):
        os.makedirs(file.parent, exist_ok=True)