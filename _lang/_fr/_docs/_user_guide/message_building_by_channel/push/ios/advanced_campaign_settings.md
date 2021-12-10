---
nav_title: "Paramètres avancés de la campagne Push"
article_title: Paramètres avancés de la campagne Push
page_type: Référence
page_order: 6
description: "Cet article de référence couvre plusieurs paramètres avancés de campagne Push tels que les options d'alerte, les drapeaux, les sons, l'expiration et plus encore."
platform: iOS
channel:
  - Pousser
tool:
  - Campagnes
---

# Paramètres avancés de la campagne de push

> Cet article de référence couvre plusieurs paramètres avancés de campagne Push tels que les options d'alerte, les drapeaux, les sons, l'expiration et plus encore.

Lors de la création de l'engagement push, à l'étape « Composer », vous pouvez sélectionner l'icône « engrenage » pour afficher les paramètres avancés disponibles.

!\[Paramètres avancés\]\[1\]

## Options d'alerte

En cliquant sur la case à cocher ici, vous remarquerez une liste déroulante des valeurs clés disponibles pour ajuster comment la notification apparaîtra sur les appareils.

## Ajout du drapeau disponible sur le contenu

Le drapeau `Content-available` indique aux périphériques de télécharger du nouveau contenu en arrière-plan. Le plus souvent, cela peut être vérifié si vous êtes intéressé à envoyer [des notifications silencieuses][2].

## Ajout de l'indicateur de contenu mutable

L'indicateur `contenu mutable` permet des personnalisations avancées des récepteurs sur les appareils iOS 10+. Ce drapeau sera automatiquement envoyé lors de la rédaction d'une [notification riche][3], quelle que soit la valeur de cette case à cocher.

## Sons

ici vous pouvez entrer un chemin vers un fichier son dans votre paquet d'application pour spécifier un son à jouer lorsque le message push est reçu. si le fichier son spécifié n'existe pas ou si le mot clé 'default' doit être saisi, braze utilisera le son d'alerte par défaut.

## Réduire l'id
Spécifier un ID de Collapse pour regrouper les notifications similaires. Si vous envoyez plusieurs notifications avec le même identifiant de récupération, l'appareil n'affichera que la dernière notification reçue. Pour plus d'informations, veuillez trouver la documentation d'Apple [ici][4].

## Expiry

cliquez sur la case à cocher ici vous offrira la possibilité de définir une date d'expiration pour votre message. si le périphérique d'un utilisateur perd sa connectivité, braze continuera à essayer d'envoyer le message jusqu'à l'heure spécifiée. si cette option n'est pas définie, la plate-forme prendra par défaut 30 jours. Veuillez noter que les notifications push qui expirent avant la livraison ne sont pas considérées comme un échec et ne seront pas enregistrées comme un rebond.
[1]: {% image_buster /assets/img_archive/ios_advanced_settings.gif %}

[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/silent_push_notifications/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#ios-10-rich-notifications
[4]: https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1
