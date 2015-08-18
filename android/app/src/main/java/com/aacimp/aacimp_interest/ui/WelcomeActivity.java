package com.aacimp.aacimp_interest.ui;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.EditText;
import android.widget.Toast;

import com.aacimp.aacimp_interest.R;
import com.aacimp.aacimp_interest.api.aacimp.AACIMPApi;
import com.aacimp.aacimp_interest.api.aacimp.entities.ApiError;
import com.aacimp.aacimp_interest.api.aacimp.entities.ImagesList;
import com.aacimp.aacimp_interest.api.aacimp.rest.RestCallback;

import butterknife.Bind;
import butterknife.ButterKnife;
import butterknife.OnClick;

public class WelcomeActivity extends AppCompatActivity {

  @Bind(R.id.etNickname)
  EditText etNickname;

  @Bind(R.id.etBoardname)
  EditText etBoardName;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_pinterest_login);

    ButterKnife.bind(this);
  }

  @OnClick(R.id.btnGetRecommendations)
  public void getRecommendations() {
    String nickname = etNickname.getText().toString().trim();
    String boardName = etBoardName.getText().toString().trim();

    AACIMPApi.getClient().recommend(nickname, boardName, new RestCallback<ImagesList>() {
      @Override
      public void failure(ApiError restError) {
        Toast.makeText(AACIMPApi.getContext(), restError.getMessage(), Toast.LENGTH_SHORT).show();
      }

      @Override
      public void success(ImagesList data) {
        Intent intent = new Intent(AACIMPApi.getContext(), MainActivity.class);
        intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
        intent.putExtra(MainActivity.KEY_IMAGES, data);
        AACIMPApi.getContext().startActivity(intent);

        finish();
      }
    });
  }

}
