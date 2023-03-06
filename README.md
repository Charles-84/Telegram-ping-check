# Telegram-ping-check

Ces script perment de surveiller l'état d'un serveur en effectuant un ping toutes les minutes. Si le serveur est hors ligne ou si le temps de réponse du ping est trop élevé, une notification Telegram est envoyée.

Le script est écrit en Python et utilise la bibliothèque `subprocess` pour effectuer la commande de ping.

## Configuration

Avant d'utiliser le script, vous devez configurer les paramètres dans le fichier `config.json`. Vous devez spécifier le token et le chat ID pour votre bot Telegram, ainsi que l'adresse IP du serveur que vous souhaitez surveiller.

Exemple de fichier de configuration :

```json
{
    "telegram_token": "1234567890:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "telegram_chat_id": "1234567890",
    "server_ip": "192.168.1.1"
}
```

Remplacer TOKEN_TELEGRAM, ID_CHAT_TELEGRAM et IP_DU_SERVEUR par les valeurs correspondantes.

### Linux

- Installer `ping` : `sudo apt install iputils-ping`

### Windows (Français)

- Installer `ping` : `choco install -y ping`

### Windows (Anglais)

- Installer `ping` : `choco install -y winping`

## Utilisation

- Lancer le script : `python ping.py`

## Licence

Ce projet est distribué sous la licence MIT. Voir le fichier `LICENSE` pour plus de détails.

