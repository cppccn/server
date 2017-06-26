package com.xtech.server;

import com.xtech.tools.Network;
import com.xtech.tools.Tools;
import fi.iki.elonen.NanoHTTPD;

import java.io.File;
import java.io.IOException;

public class GetHandler {
    public static final String BASE_RES_DIR = "./src/assets/client";
    public static final String ROOT_PAGE = "/";
    public static final String APP_FILE = "/sample.html";

    public static NanoHTTPD.Response handleGet(NanoHTTPD.IHTTPSession session) {
        String uri = session.getUri();
        File file;
        if(uri.equals(ROOT_PAGE)) {
            file = new File(BASE_RES_DIR + APP_FILE);
        } else {
            file = new File(BASE_RES_DIR + uri); //path exists and its correct
        }
        try {
            Tools.log("file path is : ", file.getCanonicalPath());
            return Network.sendFile(file.getCanonicalPath());
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
