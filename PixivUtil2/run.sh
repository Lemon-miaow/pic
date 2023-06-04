python3 PixivUtil2.py

expect {
    "*Pixiv*" {
        send "16\r"
        exp_continue
    }
    "*Valid Modes are*" {
        send "daily\r"
        exp_continue
    }
    "*Valid Content Types are:" {
        send "illust\r"
        exp_continue
    }
    "*Specify the ranking date*" {
        send "\r"
        exp_continue
    }
    "*Start Page*" {
        send "1\r"
        exp_continue
    }
    "*End Page*" {
        send "2\r"
        exp_continue
    }
    eof {
        exit
    }
}
