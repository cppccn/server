package com.xtech.server.filemanager;

import com.xtech.server.filemanager.model.FileModel;

public interface IFileManager {
    FileModel[] getCurrentDirFiles();
    FileModel getCurrentDir();
    FileModel[] getFiles(String path);
}
