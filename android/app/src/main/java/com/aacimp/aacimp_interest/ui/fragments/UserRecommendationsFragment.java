package com.aacimp.aacimp_interest.ui.fragments;

import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import com.aacimp.aacimp_interest.R;

import butterknife.ButterKnife;

/**
 * @author Victor Kifer
 * @since 8/11/15
 */
public class UserRecommendationsFragment extends Fragment {

  @Override
  public void onCreate(@Nullable Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setHasOptionsMenu(true);
  }

  @Nullable
  @Override
  public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
    View view = inflater.inflate(R.layout.fragment_user_recommendations, container, false);

    ButterKnife.bind(view);

    return view;
  }
}
