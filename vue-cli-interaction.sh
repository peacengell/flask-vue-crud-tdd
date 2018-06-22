#!/usr/bin/expect
set timeout 360

spawn "vue init webpack app"

expect { send "\n" }

