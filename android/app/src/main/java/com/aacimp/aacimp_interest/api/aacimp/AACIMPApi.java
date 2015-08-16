package com.aacimp.aacimp_interest.api.aacimp;

import android.content.Context;

/**
 * @author Victor Kifer
 * @since 8/11/15
 */
public class AACIMPApi {
  private static AACIMPApi sInstance;

  public static void init(Context context) {
    if (sInstance == null) {
      synchronized (AACIMPApi.class) {
        sInstance = new AACIMPApi();

        sInstance.context = context;
      }
    }
  }

  public static AACIMPApi getInstance() {
    return sInstance;
  }

  private Context context;
  private String apiKey;

  public static Context getContext() {
    if (sInstance == null) {
      throw new IllegalStateException("Api wasn't initialized");
    }
    return sInstance.context;
  }

  public String getApiKey() {
    return apiKey;
  }

  public void setApiKey(String apiKey) {
    this.apiKey = apiKey;
  }
}
