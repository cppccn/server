package com.xtech.server.command;

import java.util.List;
import java.util.Map;

public class Model {
    public static final String EXTRA_COMMAND = "EXTRA_COMMAND";
    public static final String EXTRA_ARGS = "EXTRA_ARGS";
    private String mArgs;
    private String mCommand;

    public Model(Map<String, List<String>> params) {
        mCommand = params.get(EXTRA_COMMAND).get(0);
        mArgs = params.get(EXTRA_ARGS).get(0);
    }
    
    public String getArgs() {
        return mArgs;
    }

    public void setArgs(String mArgs) {
        this.mArgs = mArgs;
    }

    public String getCommand() {
        return mCommand;
    }

    public void setCommand(String mCommand) {
        this.mCommand = mCommand;
    }
}
