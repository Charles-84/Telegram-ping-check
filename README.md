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
json```

Remplacer TOKEN_TELEGRAM, ID_CHAT_TELEGRAM et IP_DU_SERVEUR par les valeurs correspondantes.

##Utilisation

Le script peut être exécuté en utilisant la commande suivante : python ping.py. Il peut être lancé en arrière-plan en ajoutant & à la fin de la commande.

##Support
###Linux
Le script peut être utilisé sur Linux. Assurez-vous d'avoir les privilèges suffisants pour exécuter la commande ping.

###Windows 11 (français)
Le script a été testé sur Windows 11 en français. La commande ping est utilisée pour vérifier l'état du serveur.

###Windows 11 (anglais)
Le script a été testé sur Windows 11 en anglais. La commande ping est utilisée pour vérifier l'état du serveur.
