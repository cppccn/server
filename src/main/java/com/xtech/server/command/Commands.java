package com.xtech.server.command;

import com.google.gson.Gson;
import com.xtech.server.command.response_models.ErrorResponse;
import com.xtech.server.command.response_models.JsonResponse;
import com.xtech.server.filemanager.FileManager;
import com.xtech.server.filemanager.IFileManager;
import com.xtech.tools.Tools;
import fi.iki.elonen.NanoHTTPD;
import java.util.List;
import java.util.Map;

public class Commands {
    IFileManager mFileManager;

    public Commands() {
        mFileManager = new FileManager();
    }

    public String executeCommand(NanoHTTPD.IHTTPSession session) {
        Map<String, List<String>> params = session.getParameters();
        String json = this.parseParameters(params);
        return json;
    }

    public String parseParameters(Map<String, List<String>> params) {
        Tools.log("TEST", "params received : " + params.toString());
        Model receivedCommand = new Model(params);
        String command = receivedCommand.getCommand();

        Tools.log("TEST", "Command is: " + command);

        switch (command) {
            case CommandsContansts.LS_COMMAND:
                Tools.log("TEST", "comamnds module inside LS_COMMAND CASE");
                String json = new Gson().toJson(mFileManager.getFiles("."));
                return json;
            default:
                return Tools.toJson(new ErrorResponse("Error executing the response"));
        }
    }
}
