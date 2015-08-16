package com.aacimp.aacimp_interest.api.aacimp.rest;

import android.support.annotation.StringRes;

import com.aacimp.aacimp_interest.R;
import com.aacimp.aacimp_interest.api.aacimp.AACIMPApi;
import com.aacimp.aacimp_interest.api.aacimp.entities.ApiEntity;
import com.aacimp.aacimp_interest.utils.Logger;
import com.fasterxml.jackson.databind.DeserializationFeature;
import com.fasterxml.jackson.databind.JavaType;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.IOException;
import java.io.OutputStream;
import java.lang.reflect.Type;

import retrofit.converter.ConversionException;
import retrofit.converter.Converter;
import retrofit.mime.TypedInput;
import retrofit.mime.TypedOutput;

/**
 * @author Victor Kifer
 */
public class JacksonConverter implements Converter {
  private static final String LOG_TAG = Logger.getLogTag(JacksonConverter.class);
  static ObjectMapper objectMapper = new ObjectMapper();

  public JacksonConverter() {
    objectMapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
  }

  private String getString(@StringRes int res) {
    return AACIMPApi.getContext().getString(res);
  }

  @Override
  public Object fromBody(TypedInput body, Type type) throws ConversionException {
    JavaType javaType = objectMapper.getTypeFactory().constructType(type);

    String text = null;
    try {
      text = convertStreamToString(body.in());
    } catch (IOException e) {
      Logger.e(LOG_TAG, e);

      throw new ConversionException(getString(R.string.error_invalid_entity));
    }

    Object object;
    try {
      object = objectMapper.readValue(text, javaType);

      if (object instanceof ApiEntity) {
        if (!((ApiEntity) object).isValid()) {
          throw new IOException(getString(R.string.error_invalid_entity));
        }
      }
    } catch (IOException e) {
      Logger.e(LOG_TAG, e);

      throw new ConversionException(text);
    }

    return object;
  }

  static String convertStreamToString(java.io.InputStream is) {
    java.util.Scanner s = new java.util.Scanner(is).useDelimiter("\\A");
    return s.hasNext() ? s.next() : "";
  }

  @Override
  public TypedOutput toBody(Object object) {
    try {
      String charset = "UTF-8";
      return new JsonTypedOutput(objectMapper.writeValueAsString(object).getBytes(charset), charset);
    } catch (IOException e) {
      throw new AssertionError(e);
    }
  }

  private static class JsonTypedOutput implements TypedOutput {
    private final byte[] jsonBytes;
    private final String mimeType;

    public JsonTypedOutput(byte[] jsonBytes, String charset) {
      this.jsonBytes = jsonBytes;
      this.mimeType = "application/json; charset=" + charset;
    }

    @Override
    public String fileName() {
      return null;
    }

    @Override
    public String mimeType() {
      return mimeType;
    }

    @Override
    public long length() {
      return jsonBytes.length;
    }

    @Override
    public void writeTo(OutputStream out) throws IOException {
      out.write(jsonBytes);
    }
  }
}