# system-status-webhook

This is just a little webhook that is meant for Discord.  
Upon a service failure what this would do is post two messages in the Discord channel the webhook is created for.  
The first message tells the user what systemd service has failed & the second message gives the log messages as if the user ran systemctl status <service>.  
(I currently have it setup so that it mentions me in the channel on Discord.)
