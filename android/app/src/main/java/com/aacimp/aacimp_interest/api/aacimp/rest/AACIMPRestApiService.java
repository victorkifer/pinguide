package com.aacimp.aacimp_interest.api.aacimp.rest;

import com.aacimp.aacimp_interest.api.aacimp.entities.ApiEntity;
import com.aacimp.aacimp_interest.api.aacimp.entities.ImagesList;

import retrofit.http.GET;
import retrofit.http.Query;

/**
 * @author Victor Kifer
 *         Retrofit Rest API Service interface
 */
public interface AACIMPRestApiService {

  @GET("/recommend")
  void recommend(@Query("nickname") String nickname, @Query("board_name") String board_name, RestCallback<ImagesList> callback);

}
