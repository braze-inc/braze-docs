---
nav_title: Réduire la taille de la charge utile des notifications push
article_title: Réduire la taille de la charge utile des notifications push
page_type: solution
description: "Cet article d'aide fournit quelques conseils pour réduire la taille de la charge utile de vos notifications push si vous n'êtes pas en mesure de lancer une campagne ou une étape de Canvas en raison des limites de taille de la charge utile de push."
channel: push
---

# Réduire la taille de la charge utile des notifications push

Si vous ne pouvez pas lancer une campagne push ou une étape du canvas parce que votre charge utile push est trop importante, consultez ces conseils pour réduire la taille de votre charge utile de notification push.

{% alert note %}
La taille maximale de notre charge utile est de **3 807 octets.** Si votre push dépasse cette taille, le message risque de ne pas être envoyé. La meilleure pratique consiste à limiter votre charge utile à quelques centaines d'octets.
{% endalert %}

## Qu'est-ce qu'une charge utile de poussée ?

Les fournisseurs de services push calculent si votre notification push peut être affichée à un utilisateur en examinant la taille en octets de l'ensemble de la charge utile push. La charge utile est limitée à **4 Ko (4 096 octets)** pour la plupart des services de notifications push, notamment :

- Service de notification push d'Apple (APN)
- Firebase Cloud Messaging (FCM) d'Android
- Push Web
- Notification push Huawei

Ces services push refuseront toute notification dépassant cette limite.

Braze réserve une partie de la charge utile du push à des fins d'intégration et d'analyse/analytique. Dans ces conditions, la taille maximale de notre charge utile est de **3 807 octets.** Si votre push dépasse cette taille, le message risque de ne pas être envoyé. La meilleure pratique consiste à limiter votre charge utile à quelques centaines d'octets.

Les éléments suivants constituent la charge utile de votre push :

- Copie, telle que le titre et le corps du message
- Rendu final de toute personnalisation liquide
- URL des images (mais pas la taille de l'image elle-même)
- URL des cibles des clics
- Noms des boutons
- Paires clé-valeur

## Conseils pour réduire la taille de la charge utile

Pour réduire la taille de la charge utile :

- Veillez à ce que votre message soit bref. Une bonne ligne de conduite générale consiste à faire en sorte que les informations soient exploitables et utiles en moins de 40 caractères.
- Oubliez les espaces blancs et les sauts de ligne dans votre texte.
- Réfléchissez à la manière dont Liquid s'affichera lors de l'envoi. Étant donné que le rendu final de toute personnalisation Liquid varie d'un utilisateur à l'autre, Braze ne peut pas déterminer si une charge utile de push dépassera la limite de taille lorsque Liquid est inclus. Si votre votre code Liquid génère un message plus court, cela ne devrait pas poser de problème. Cependant, si votre Liquid donne lieu à un message plus long, votre push peut dépasser la limite de taille de la charge utile. Testez toujours votre message push sur un appareil réel avant de l'envoyer aux utilisateurs.
- Envisagez de raccourcir les URL à l'aide d'un raccourcisseur d'URL.
