package com.aacimp.aacimp_interest.api.aacimp.entities;

import com.google.gson.annotations.SerializedName;

import java.io.Serializable;
import java.util.List;

/**
 * Created by viktor on 8/18/15.
 */
public class ImagesList extends ApiEntity implements Serializable {
  @SerializedName("data")
  private List<Image> images;

  public List<Image> getImages() {
    return images;
  }

  @Override
  public boolean isValid() {
    return images != null;
  }

  public static class Image implements Serializable {
    @SerializedName("id")
    private String id;

    @SerializedName("img_id")
    private String imgId;

    @SerializedName("url")
    private String url;

    public String getId() {
      return id;
    }

    public void setId(String id) {
      this.id = id;
    }

    public String getImgId() {
      return imgId;
    }

    public void setImgId(String imgId) {
      this.imgId = imgId;
    }

    public String getUrl() {
      return url;
    }

    public void setUrl(String url) {
      this.url = url;
    }
  }

}
