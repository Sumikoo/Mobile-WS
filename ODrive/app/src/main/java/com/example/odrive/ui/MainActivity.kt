package com.example.odrive.ui

// Nur Khafidah | 19090075 | 6C
// Helina Putri | 19090133 | 6D

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.fragment.app.Fragment
import com.example.odrive.R
import com.example.odrive.ui.fragment.DashboardFragment
import com.example.odrive.ui.fragment.MyDriveFragment
import com.example.odrive.ui.fragment.ProfileFragment
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        makeCurrentFragment(DashboardFragment())
        bot_nav.setOnItemSelectedListener {
            when(it.itemId){
                R.id.menu_dashboard -> { makeCurrentFragment(DashboardFragment()) }
                R.id.menu_files -> { makeCurrentFragment(MyDriveFragment()) }
                R.id.menu_profile -> { makeCurrentFragment(ProfileFragment()) }
            }
            true
        }
    }

    private fun makeCurrentFragment(fragment: Fragment){
        supportFragmentManager.beginTransaction().apply {
            replace(R.id.frame_main, fragment)
            commit()
        }
    }
}