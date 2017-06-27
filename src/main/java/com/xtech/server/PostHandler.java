package com.xtech.server;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.xtech.tools.Tools;
import fi.iki.elonen.NanoHTTPD;
import java.io.IOException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static fi.iki.elonen.NanoHTTPD.newFixedLengthResponse;

public class PostHandler {
    public static final String EXTRA_COMMAND = "EXTRA_COMMAND";

    public NanoHTTPD.Response handlePost(NanoHTTPD.IHTTPSession session) {
        try {
            session.parseBody(new HashMap<String, String>());
            System.out.println( session.getMethod() + " " + session.getParameters().toString() );

            Map<String, List<String>> params = session.getParameters();
            String command = params.get(EXTRA_COMMAND).get(0);
            Tools.log("Command: ", command);
            JsonResponse jsonResponse = new JsonResponse(command);
            String json = Tools.toJson(jsonResponse);

            return newFixedLengthResponse(NanoHTTPD.Response.Status.OK, "text/json" , json);
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        } catch (NanoHTTPD.ResponseException e) {
            e.printStackTrace();
            return null;
        }
    }

    public class JsonResponse {
        private String mCommand;
        public JsonResponse(String command) {
            mCommand = command;
        }
    }
}
