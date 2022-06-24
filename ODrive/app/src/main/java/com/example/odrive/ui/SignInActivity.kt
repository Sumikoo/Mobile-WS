package com.example.odrive.ui

// Nur Khafidah | 19090075 | 6C
// Helina Putri | 19090133 | 6D

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import com.example.odrive.R
import com.example.odrive.utilities.lightStatusBar
import com.example.odrive.utilities.setFullscreen
import kotlinx.android.synthetic.main.activity_sign_in.*

class SignInActivity : AppCompatActivity() {
    var inten = Intent()
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_sign_in)

        btn_continue.setOnClickListener {
            val intent = Intent(this, FaceLockActivity::class.java)
            val user = et_sgn_mail.text.toString()
            val pass = et_sgn_pass.text.toString()
            if ((user == "admin" && pass == "admin")){
                startActivity(intent)
            } else {
                Toast.makeText(this, "Email or Password wrong", Toast.LENGTH_SHORT).show()
            }
        }


        tv_sgn_signup.setOnClickListener {
            inten = Intent(this, SignUpActivity::class.java)
            startActivity(inten)
        }
    }
}