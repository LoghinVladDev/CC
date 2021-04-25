package com.example.cc_t4;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class StudentReview extends AppCompatActivity {

    Button button;
    TextView textView;
    RequestQueue queue;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_student_review);

        button = findViewById(R.id.reviews_button);
        textView = findViewById(R.id.reviews_text);
        queue = Volley.newRequestQueue(StudentReview.this);

        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) { String url ="https://apicc.azurewebsites.net/translate/";
                Map<String, String> params = new HashMap<String, String>();
                params.put("LanguageFrom", "en");
                params.put("LanguageTo", "ro");
                params.put("Text", "hello");

                JSONObject json =  new JSONObject(params);
                JsonObjectRequest jsonObjReq = new JsonObjectRequest(Request.Method.POST,
                        url, json,
                        new Response.Listener<JSONObject>() {

                            @Override
                            public void onResponse(JSONObject response) {
                                textView.setText(response.toString());
                                //pDialog.hide();
                            }
                        }, new Response.ErrorListener() {

                    @Override
                    public void onErrorResponse(VolleyError error) {
                        //VolleyLog.d("JSONPost", "Error: " + error.getMessage());
                        //pDialog.hide();
                        textView.setText(error.toString());
                    }
                });
                queue.add(jsonObjReq);
            }
        });
    }
}