package com.xtech.tools;

import fi.iki.elonen.NanoHTTPD;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

import static fi.iki.elonen.NanoHTTPD.newFixedLengthResponse;

public class Network {
    public static NanoHTTPD.Response sendFile(String filePath) {
        FileInputStream fis = null;
        File file = null;
        long size = -1;
        try {
            file = new File(filePath); //path exists and its correct
            Tools.log("Canonical path", file.getCanonicalPath());
            size = file.length();
            fis = new FileInputStream(file);
        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException ioe ) {
            ioe.printStackTrace();
        }

        int lastIndex = filePath.lastIndexOf('.');
        String fileType = filePath.substring(lastIndex + 1, filePath.length());

        return newFixedLengthResponse(NanoHTTPD.Response.Status.OK, "text/" + fileType, fis, file.length());
    }
}
