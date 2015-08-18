package com.aacimp.aacimp_interest.api.aacimp;

import android.content.Context;

import com.aacimp.aacimp_interest.api.aacimp.rest.AACIMPRestApiClientImpl;
import com.aacimp.aacimp_interest.api.aacimp.rest.AACIMPRestApiService;

/**
 * @author Victor Kifer
 * @since 8/11/15
 */
public class AACIMPApi {
  private static AACIMPApi sInstance;

  private AACIMPRestApiClientImpl client;

  public static void init(Context context) {
    if (sInstance == null) {
      synchronized (AACIMPApi.class) {
        sInstance = new AACIMPApi();

        sInstance.context = context;
        sInstance.client = new AACIMPRestApiClientImpl("http://54.75.70.159/api/v1");
      }
    }
  }

  public static AACIMPApi getInstance() {
    return sInstance;
  }

  private Context context;

  public static Context getContext() {
    if (sInstance == null) {
      throw new IllegalStateException("Api wasn't initialized");
    }
    return sInstance.context;
  }

  public static AACIMPRestApiService getClient() {
    if (sInstance == null) {
      throw new IllegalStateException("Api wasn't initialized");
    }
    return sInstance.client.getApiService();
  }
}
