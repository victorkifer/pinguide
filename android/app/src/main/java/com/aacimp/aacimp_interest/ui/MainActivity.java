package com.aacimp.aacimp_interest.ui;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.Toolbar;

import com.aacimp.aacimp_interest.R;
import com.aacimp.aacimp_interest.ui.fragments.SelectImagesFragment;

import butterknife.Bind;
import butterknife.ButterKnife;

public class MainActivity extends AppCompatActivity {

  @Bind(R.id.toolbar)
  Toolbar toolbar;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);

    ButterKnife.bind(this);

    setSupportActionBar(toolbar);
    getSupportActionBar().setTitle(R.string.app_name);
    getSupportActionBar().setLogo(R.mipmap.ic_launcher);

    getSupportFragmentManager().beginTransaction()
        .replace(R.id.container, new SelectImagesFragment())
        .commit();
  }

}
