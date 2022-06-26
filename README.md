# HyperBotka

HyperBotka is a bot capable of formatting messages and defining custom commands.

## QuickStart

```console
$ cat <<EOF > .env
DISCORD_TOKEN="<your-bot-access-token>"
GUILD_ADM="<your-server-adm-user-id>"
GUILD_ABOUT_CHANNEL="<about-channel-id>"
EOF
$ ./build.sh
$ source ./bin/activate
$ ./bin/python hyperbotka.py
```
