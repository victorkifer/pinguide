package com.aacimp.aacimp_interest.api.aacimp.rest;

/**
 * @author Victor Kifer
 * @since 5/17/15
 *
 * Retrofit API Client
 * @see AACIMPRestApiClientImpl
 */
public interface RestApiClient {
  AACIMPRestApiService getApiService();
}
