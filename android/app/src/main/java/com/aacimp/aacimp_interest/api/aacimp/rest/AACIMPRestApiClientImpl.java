package com.aacimp.aacimp_interest.api.aacimp.rest;

import retrofit.RestAdapter;

/**
 * @author Victor Kifer
 */
public class AACIMPRestApiClientImpl implements RestApiClient {
  private AACIMPRestApiService apiService;

  public AACIMPRestApiClientImpl(String apiUrl) {
    RestAdapter restAdapter = new RestAdapter.Builder()
        .setLogLevel(RestAdapter.LogLevel.FULL)
        .setEndpoint(apiUrl)
        .setConverter(new JacksonConverter())
        .setRequestInterceptor(new SessionRequestInterceptor())
        .build();

    apiService = restAdapter.create(AACIMPRestApiService.class);
  }

  @Override
  public AACIMPRestApiService getApiService() {
    return apiService;
  }
}
