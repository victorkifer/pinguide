package com.aacimp.aacimp_interest;

import android.app.Application;

import com.aacimp.aacimp_interest.api.aacimp.AACIMPApi;

/**
 * @author Victor Kifer
 * @since 8/10/15
 */
public class AACIMPApp extends Application {

  @Override
  public void onCreate() {
    super.onCreate();

    AACIMPApi.init(this);
  }
}
