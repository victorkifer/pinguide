package com.aacimp.aacimp_interest.api.aacimp.rest;

import com.aacimp.aacimp_interest.api.aacimp.entities.ApiEntity;
import com.aacimp.aacimp_interest.api.aacimp.entities.ApiError;
import com.aacimp.aacimp_interest.utils.Logger;
import com.fasterxml.jackson.databind.ObjectMapper;

import retrofit.Callback;
import retrofit.RetrofitError;
import retrofit.client.Response;

/**
 * @author Victor Kifer
 */
public abstract class RestCallback<T extends ApiEntity> implements Callback<T> {
  private static final String LOG_TAG = Logger.getLogTag(RestCallback.class);

  public abstract void failure(ApiError restError);

  public abstract void success(T data);

  @Override
  public final void failure(RetrofitError error) {
    ObjectMapper objectMapper = JacksonConverter.objectMapper;

    ApiError restError = null;
    try {
      restError = objectMapper.readValue(error.getMessage(), ApiError.class);
    } catch (Exception e) {
      restError = ApiError.build(error.getMessage());
    }

    failure(restError);
  }

  @Override
  public final void success(T t, Response response) {
    success(t);
  }
}