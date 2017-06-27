package com.xtech.server.filemanager.model;

import com.xtech.tools.Tools;

import java.io.File;

public class FileModel {
    private String mFileName, mPath, mAbsPath;
    private long mSize;

    private File mFile;
    private FileType mType;

    public FileModel(File file) {
        mFile = file;
        mFileName = file.getName();
        mSize = file.length();
        mType = file.isFile() ? FileType.FILE : FileType.DIR;
        Tools.log("TEST", "File:  name -> " + mFileName + ", size: " + mSize);
        mPath = file.getPath();
        mAbsPath = file.getAbsolutePath();
    }

    public String getFileName() { return mFileName; }
    public void setFileName(String mFileName) { this.mFileName = mFileName; }
    public String getPath() { return mPath; }
    public void setPath(String mPath) { this.mPath = mPath; }
    public String getAbsPath() { return mAbsPath; }
    public void setAbsPath(String mAbsPath) { this.mAbsPath = mAbsPath; }
    public long getSize() { return mSize; }
    public void setSize(long mSize) { this.mSize = mSize; }
    public File getFile() { return mFile; }
    public void setFile(File mFile) { this.mFile = mFile; }
    public FileType getType() { return mType; }
    public void setType(FileType mType) { this.mType = mType; }

    private enum FileType {
        DIR,
        FILE
    };
}
