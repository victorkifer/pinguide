package com.aacimp.aacimp_interest.api.aacimp.rest;

import com.aacimp.aacimp_interest.api.aacimp.AACIMPApi;

import retrofit.RequestInterceptor;

/**
 * @author Victor Kifer
 */
public class SessionRequestInterceptor implements RequestInterceptor {
  @Override
  public void intercept(RequestFacade request) {
    String accessToken = AACIMPApi.getInstance().getApiKey();
    if (accessToken != null) {
      request.addQueryParam("accessToken", accessToken);
    }
  }
}
