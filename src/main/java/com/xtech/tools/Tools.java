package com.xtech.tools;

import com.google.gson.Gson;

public class Tools {
    public static void log(String tag, String message) {
        System.out.println(tag + ": " + message);
    }

    public static String toJson(Object o) {
        Gson gson = new Gson(); // Or use new GsonBuilder().create();
        String json = gson.toJson(o); // serializes target to Json
        return json;
    }
}
