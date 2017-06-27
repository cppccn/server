package com.xtech.server;

import com.xtech.server.command.Commands;
import com.xtech.tools.Tools;
import fi.iki.elonen.NanoHTTPD;
import java.io.IOException;
import java.util.HashMap;
import static fi.iki.elonen.NanoHTTPD.newFixedLengthResponse;

public class PostHandler {
    Commands mCommandsModule;

    public PostHandler() {
        mCommandsModule = new Commands();
    }

    public NanoHTTPD.Response handlePost(NanoHTTPD.IHTTPSession session) {
        try {
            session.parseBody(new HashMap<String, String>());
            System.out.println( session.getMethod() + " " + session.getParameters().toString() );

            Tools.log("TEST", "executing commands module");
            String json = mCommandsModule.executeCommand(session);
            Tools.log("TEST", "AFTER executing commands module");
            return newFixedLengthResponse(NanoHTTPD.Response.Status.OK, "text/json" , json);
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        } catch (NanoHTTPD.ResponseException e) {
            e.printStackTrace();
            return null;
        }
    }
}
