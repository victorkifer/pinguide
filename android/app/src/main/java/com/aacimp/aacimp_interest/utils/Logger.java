package com.aacimp.aacimp_interest.utils;

import android.util.Log;

public class Logger {
  public static enum LogLevel {
    ALL,
    DEBUG,
    INFO,
    WARN,
    ERR,
    NONE
  }

  private static LogLevel sLogLevel = LogLevel.INFO;

  public static LogLevel getLogLevel() {
    return sLogLevel;
  }

  public static void setLogLevel(LogLevel logLevel) {
    Logger.sLogLevel = logLevel;
  }

  private static boolean isLogEnabled(LogLevel level) {
    return sLogLevel.ordinal() <= level.ordinal();
  }

  public static String getLogTag(Class<?> classObj) {
    return classObj.getName();
  }

  public static void d(String tag, String message) {
    if (isLogEnabled(LogLevel.DEBUG) && message != null) {
      Log.d(tag, message);
    }
  }

  public static void d(String tag, Exception e) {
    if (e.getMessage() == null) {
      if (isLogEnabled(LogLevel.DEBUG)) {
        e.printStackTrace();
      }
    } else {
      d(tag, e.getMessage());
    }
  }

  public static void i(String tag, String message) {
    if (isLogEnabled(LogLevel.INFO) && message != null) {
      Log.i(tag, message);
    }
  }

  public static void i(String tag, Exception e) {
    if (e.getMessage() == null) {
      if (isLogEnabled(LogLevel.INFO)) {
        e.printStackTrace();
      }
    } else {
      i(tag, e.getMessage());
    }
  }

  public static void w(String tag, String message) {
    if (isLogEnabled(LogLevel.WARN) && message != null) {
      Log.w(tag, message);
    }
  }

  public static void w(String tag, Exception e) {
    if (e.getMessage() == null) {
      if (isLogEnabled(LogLevel.WARN)) {
        e.printStackTrace();
      }
    } else {
      w(tag, e.getMessage());
    }
  }

  public static void e(String tag, String message) {
    if (isLogEnabled(LogLevel.ERR) && message != null) {
      Log.e(tag, message);
    }
  }

  public static void e(String tag, Exception e) {
    if (e.getMessage() == null) {
      if (isLogEnabled(LogLevel.ERR)) {
        e.printStackTrace();
      }
    } else {
      e(tag, e.getMessage());
    }
  }

}
