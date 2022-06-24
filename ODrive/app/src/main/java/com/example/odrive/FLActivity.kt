package com.example.odrive

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.google.mlkit.common.model.CustomRemoteModel
import com.google.mlkit.common.model.DownloadConditions
import com.google.mlkit.common.model.LocalModel
import com.google.mlkit.common.model.RemoteModelManager
import com.google.mlkit.linkfirebase.FirebaseModelSource

class FLActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_flactivity)
    }

    private fun setPredict(){
        val localModel = LocalModel.Builder()
            .setAssetFilePath("src/main/assets/mobilenet_v1_1.0_224_quantized_1_metadata_1.tflite")
            // or .setAbsoluteFilePath(absolute file path to model file)
            // or .setUri(URI to model file)
            .build()
        // Specify the name you assigned in the Firebase console.
        val remoteModel =
            CustomRemoteModel
                .Builder(FirebaseModelSource.Builder("mobilenet_v1_1.0_224_quantized_1_metadata_1.tflite").build())
                .build()
        val downloadConditions = DownloadConditions.Builder()
            .requireWifi()
            .build()
        RemoteModelManager.getInstance().download(remoteModel, downloadConditions)
            .addOnSuccessListener {
                // Success.
            }
    }
}