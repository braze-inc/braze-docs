---
nav_title: Sons personnalisés
article_title: Sons de notification Push personnalisés pour iOS
platform: iOS
page_order: 3
description: "Cet article couvre les sons personnalisés de vos notifications push iOS."
channel:
  - Notification push

---

# Sons personnalisés

## Étape 1 : Héberger les sons dans l’application

Les sons des notifications push personnalisées doivent être hébergés localement dans le lot principal de l’application client. Les formats de données audio suivants sont acceptés :

- Linear PCM
- MA4
- µLaw
- aLaw

Vous pouvez regrouper les données audio dans un fichier AIFF, WAV ou CAF. Dans Xcode, ajoutez le fichier audio à votre projet comme ressource non localisée du lot d’applications.

Vous pouvez utiliser l’outil afconvert pour convertir les sons. Par exemple, pour convertir le système PCM linéaire de 16 bits sous Submarine.aiff en audio IMA4 dans un fichier CAF, utilisez la commande suivante dans le terminal :

```bash
afconvert /System/Library/Sounds/Submarine.aiff ~/Desktop/sub.caf -d ima4 -f caff -v
```

Vous pouvez inspecter un son pour déterminer son format de données en l’ouvrant dans QuickTime Player et en choisissant **Afficher l'inspecteur du film** dans le menu **Film**.

Les sons personnalisés doivent durer moins de 30 secondes lorsqu’ils sont joués. Si un son personnalisé dépasse cette limite, le son système par défaut est joué à la place.

## Étape 2 : Fournir au tableau de bord une URL de protocole pour le son

Votre son doit être hébergé localement dans l’application. Vous devez spécifier une URL de protocole qui dirige vers l’emplacement du fichier audio dans l’application dans le champ **Sound (Son)** sur le cadran notification push. Spécifier « par défaut » dans ce champ permet de jouer le son de notification par défaut sur l’appareil. Cela peut être spécifié par le biais de notre [messaging API (API de messagerie)][25] ou notre tableau de bord sous **Settings (Paramètres)** dans l’assistant de composition de notification push, comme illustré sur la capture d’écran suivante :

![][8]

Si le fichier son spécifié n’existe pas ou si le mot-clé « default » est saisi, Braze utilisera le son d’alerte par défaut de l’appareil. En dehors de notre tableau de bord, le son peut également être configuré via notre [API de messagerie][12]. Consultez la documentation du développeur Apple concernant la [préparation de sons d’alerte personnalisés][9] pour plus d’informations.

[8]: {% image_buster /assets/img_archive/sound_push_ios.png %}
[9]: https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SupportingNotificationsinYourApp.html
[12]: {{site.baseurl}}/api/endpoints/messaging/
[25]: {{site.baseurl}}/api/endpoints/messaging/
