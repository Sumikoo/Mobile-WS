package com.example.odrive.ui

// Nur Khafidah | 19090075 | 6C
// Helina Putri | 19090133 | 6D

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.Handler
import com.example.odrive.R

class SplashScreenActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_splash_screen)


        Handler().postDelayed({
            val inten = Intent(this, SignInActivity::class.java)
            startActivity(inten)
            finish()
        }, 3000)
    }
}