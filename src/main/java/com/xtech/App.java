package com.xtech;

import com.google.gson.Gson;
import com.xtech.server.GetHandler;
import com.xtech.server.PostHandler;
import com.xtech.tools.Tools;
import fi.iki.elonen.NanoHTTPD;
import java.io.IOException;

public class App extends NanoHTTPD {
    public static final String POST_METHOD = "POST";
    public static final String GET_METHOD = "GET";
    private GetHandler mGetHandler;
    private PostHandler mPostHandler;

    public App() throws IOException {
        super(8080);
        initHandlers();
        start(NanoHTTPD.SOCKET_READ_TIMEOUT, false);
        System.out.println("\nRunning! Point your browsers to http://localhost:8080/ \n");
    }

    public void initHandlers() {
        mGetHandler = new GetHandler();
        mPostHandler = new PostHandler();
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
        Tools.log("METHOD", session.getMethod().toString());
        String method = session.getMethod().toString();
        Tools.log("URI: ", session.getUri());
        if(method.equals(POST_METHOD)) {
            return mPostHandler.handlePost(session);
        } else { // GET_METHOD case
            return mGetHandler.handleGet(session);
        }
    }
}