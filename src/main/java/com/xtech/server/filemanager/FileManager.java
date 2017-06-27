package com.xtech.server.filemanager;

import com.xtech.server.filemanager.model.FileModel;

import java.io.File;

public class FileManager implements IFileManager {
    public static final String ROOT_PATH = "./src/assets/client";
    public static final String CURRENT_DIR_PATH = ".";
    public static final String EMPTY_STRING = "";
    public FileManager() {
    }

    @Override
    public FileModel[] getCurrentDirFiles() {
        return new FileModel[0];
    }

    @Override
    public FileModel getCurrentDir() {
        return null;
    }

    @Override
    public FileModel[] getFiles(String path) {
        if(path.equals(CURRENT_DIR_PATH)) {
            path = EMPTY_STRING;
        }

        File folder = new File(ROOT_PATH + path);
        File[] listOfFiles = folder.listFiles();
        FileModel[] result = new FileModel[listOfFiles.length];

        for (int i = 0; i < listOfFiles.length; i++) {
            result[i] = new FileModel(listOfFiles[i]);
            if (listOfFiles[i].isFile()) {
                System.out.println("File " + listOfFiles[i].getName());
            } else if (listOfFiles[i].isDirectory()) {
                System.out.println("Directory " + listOfFiles[i].getName());
            }
        }
        return result;
    }
}
