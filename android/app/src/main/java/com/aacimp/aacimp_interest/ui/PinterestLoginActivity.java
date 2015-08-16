package com.aacimp.aacimp_interest.ui;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;

import com.aacimp.aacimp_interest.R;
import com.aacimp.aacimp_interest.utils.Logger;
import com.pinterest.android.pdk.PDKCallback;
import com.pinterest.android.pdk.PDKClient;
import com.pinterest.android.pdk.PDKException;
import com.pinterest.android.pdk.PDKResponse;

import java.util.ArrayList;
import java.util.List;

import butterknife.ButterKnife;
import butterknife.OnClick;

public class PinterestLoginActivity extends AppCompatActivity {

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_pinterest_login);

    ButterKnife.bind(this);
  }

  @OnClick(R.id.btnPinterestLogin)
  public void loginWithPinterest() {
    PDKClient.configureInstance(this, "1446534");
    PDKClient.getInstance().onConnect(this);

    List<String> scopes = new ArrayList<>();
    scopes.add(PDKClient.PDKCLIENT_PERMISSION_READ_PUBLIC);
    scopes.add(PDKClient.PDKCLIENT_PERMISSION_WRITE_PUBLIC);

    PDKClient.getInstance().login(this, scopes, new PDKCallback() {
      @Override
      public void onSuccess(PDKResponse response) {
        Logger.d(getClass().getName(), response.getData().toString());
        //user logged in, use response.getUser() to get PDKUser object
      }

      @Override
      public void onFailure(PDKException exception) {
        Logger.e(getClass().getName(), exception);
      }
    });
  }

  @Override
  protected void onActivityResult(int requestCode, int resultCode, Intent data) {
    super.onActivityResult(requestCode, resultCode, data);
    PDKClient.getInstance().onOauthResponse(requestCode, resultCode, data);
  }
}
