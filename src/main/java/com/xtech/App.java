package com.xtech;

import fi.iki.elonen.NanoHTTPD;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.HashMap;

public class App extends NanoHTTPD {
    public static final String POST_METHOD = "POST";
    public static final String GET_METHOD = "GET";
    public static final String BASE_RES_DIR = "./src/assets/client";
    public static final String ROOT_PAGE = "/";
    public static final String APP_FILE = "/sample.html";

    public App() throws IOException {
        super(8080);
        start(NanoHTTPD.SOCKET_READ_TIMEOUT, false);
        System.out.println("\nRunning! Point your browsers to http://localhost:8080/ \n");
    }

    public static void main(String[] args) {
        try {
            new App();
        } catch (IOException ioe) {
            System.err.println("Couldn't start server:\n" + ioe);
        }
    }

    @Override
    public Response serve(IHTTPSession session) {
        log("METHOD", session.getMethod().toString());
        String method = session.getMethod().toString();
        String uri = session.getUri();
        log("URI: ", session.getUri());
        if(method.equals(POST_METHOD)) {
            try {
                session.parseBody(new HashMap<String, String>());
                System.out.println( session.getMethod() + " " + session.getParameters().toString() );
                return newFixedLengthResponse("Some response.");
            } catch (IOException e) {
                e.printStackTrace();
                return null;
            } catch (ResponseException e) {
                e.printStackTrace();
                return null;
            }
        } else { // GET_METHOD case
            File file;
            if(uri.equals(ROOT_PAGE)) {
                file = new File(BASE_RES_DIR + APP_FILE);
            } else {
                file = new File(BASE_RES_DIR + uri); //path exists and its correct
            }
            try {
                log("file path is : ", file.getCanonicalPath());
                return sendFile(file.getCanonicalPath());
            } catch (IOException e) {
                e.printStackTrace();
                return null;
            }

/*            log("PARAMS", session.getQueryParameterString());
            log("Getting parameters", session.getParameters().toString());
            String msg = "<html><body><h1>Hello server</h1>\n";
            Map<String, List<String>> parms = session.getParameters();
            if (parms.get("username") == null) {
                msg += "<form action='?' method='get'>\n  <p>Your name: <input type='text' name='username'></p>\n" + "</form>\n";
            } else {
                msg += "<p>Hello, " + parms.get("username").get(0) + "!</p>";
            }
            return newFixedLengthResponse(msg + "</body></html>\n");*/
        }
    }

    public void log(String tag, String message) {
        System.out.println(tag + ": " + message);
    }

    public NanoHTTPD.Response sendFile(String filePath) {
        FileInputStream fis = null;
        File file = null;
        long size = -1;
        try {
            file = new File(filePath); //path exists and its correct
            log("Canonical path", file.getCanonicalPath());
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

        return newFixedLengthResponse(Response.Status.OK, "text/" + fileType, fis, file.length());
    }
}