package com.aacimp.aacimp_interest.api.aacimp.entities;

import com.fasterxml.jackson.annotation.JsonProperty;

/**
 * @author Victor Kifer
 */
public class ApiError {
  public static final int CODE_UNKNOWN = Integer.MIN_VALUE;

  @JsonProperty("code")
  private int code = CODE_UNKNOWN;

  @JsonProperty("errorMessage")
  private String message;

  public static ApiError build(int code, String message) {
    ApiError error = new ApiError();
    error.code = code;
    error.message = message;
    return error;
  }

  public static ApiError build(String message) {
    return build(CODE_UNKNOWN, message);
  }

  public Integer getCode() {
    return code;
  }

  public void setCode(Integer code) {
    this.code = code;
  }

  public String getMessage() {
    return message;
  }

  public void setMessage(String message) {
    this.message = message;
  }
}
