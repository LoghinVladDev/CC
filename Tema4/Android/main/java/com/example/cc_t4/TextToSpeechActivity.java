package com.example.cc_t4;

import androidx.appcompat.app.AppCompatActivity;
import com.microsoft.cognitiveservices.speech.AudioDataStream;
import com.microsoft.cognitiveservices.speech.CancellationReason;
import com.microsoft.cognitiveservices.speech.ResultReason;
import com.microsoft.cognitiveservices.speech.SpeechConfig;
import com.microsoft.cognitiveservices.speech.SpeechSynthesisCancellationDetails;
import com.microsoft.cognitiveservices.speech.SpeechSynthesizer;
import com.microsoft.cognitiveservices.speech.SpeechSynthesisOutputFormat;
import com.microsoft.cognitiveservices.speech.SpeechSynthesisResult;
import com.microsoft.cognitiveservices.speech.audio.AudioConfig;

import java.io.*;
import java.util.Scanner;
import java.util.concurrent.Future;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class TextToSpeechActivity extends AppCompatActivity {
    Button button;
    EditText editText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_text_to_speech);

        button = (Button) findViewById(R.id.tts);
        editText = (EditText) findViewById(R.id.text);


        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                SpeechConfig speechConfig = SpeechConfig.fromSubscription("9ccc6173fc454f9c9b0470d6b6ed56e7", "francecentral");
                AudioConfig audioConfig = AudioConfig.fromDefaultSpeakerOutput();

                SpeechSynthesizer synthesizer = new SpeechSynthesizer(speechConfig, audioConfig);
                synthesizer.SpeakText(editText.getText().toString());
            }
        });
    }
}