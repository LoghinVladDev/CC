package com.example.cc_t4;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.os.StrictMode;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.squareup.okhttp.HttpUrl;
import com.squareup.okhttp.OkHttpClient;

import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class TranslatorActivity extends AppCompatActivity {

    EditText editText;
    TextView textView;
    Button button, button2;
    String subscriptionKey = "17f8bc791f754116a1594723b9588d0c";
    String location = "francecentral";
    RequestQueue queue;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_translator);

        button = findViewById(R.id.translate_button);
        editText = findViewById(R.id.text_translate);
        textView = findViewById(R.id.translated_text);
        queue = Volley.newRequestQueue(TranslatorActivity.this);

        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String text = editText.getText().toString();
                String url ="https://apicc.azurewebsites.net/translate/";
                Map<String, String> params = new HashMap<String, String>();
                params.put("LanguageFrom", "en");
                params.put("LanguageTo", "ro");
                params.put("Text", text);

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