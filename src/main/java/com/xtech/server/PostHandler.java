package com.xtech.server;

import fi.iki.elonen.NanoHTTPD;

import java.io.IOException;
import java.util.HashMap;
import static fi.iki.elonen.NanoHTTPD.newFixedLengthResponse;

public class PostHandler {
    public static NanoHTTPD.Response handlePost(NanoHTTPD.IHTTPSession session) {
        try {
            session.parseBody(new HashMap<String, String>());
            System.out.println( session.getMethod() + " " + session.getParameters().toString() );
            return newFixedLengthResponse("Some response.");
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        } catch (NanoHTTPD.ResponseException e) {
            e.printStackTrace();
            return null;
        }
    }
}
