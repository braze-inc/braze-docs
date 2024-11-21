---
nav_title: "Paramètres avancés de campagne de notifications push"
article_title: Paramètres avancés de campagne de notifications push
page_type: reference
page_order: 6
description: "Cet article de référence couvre les paramètres avancés de campagne de notifications push pour iOS tels que les options d’alerte, les indicateurs, les sons, l’expiration, etc."
platform: iOS
channel:
  - push
tool:
  - Campaigns

---

# Paramètres avancés de campagne de notifications push

> Cet article de référence couvre les paramètres avancés de campagne de notifications push pour iOS tels que les options d’alerte, les indicateurs, les sons, l’expiration, etc.

Lors de la création d'un engagement push, à l'étape **Composer**, vous pouvez sélectionner l'icône en forme de roue dentée <i class="fas fa-cog"></i> pour afficher les paramètres avancés de votre message.

![][1]

## Options d’alerte

En cochant la case ici, vous remarquerez un menu déroulant de valeurs clés disponibles pour ajuster la façon dont la notification apparaîtra sur les appareils.

## Ajouter un indicateur de contenu disponible

L’indicateur `content-available` indique aux appareils de télécharger le nouveau contenu en arrière-plan. Le plus souvent, vous pouvez cocher cette case si vous souhaitez envoyer des [notifications silencieuses][2].

## Ajouter un indicateur de contenu mutable

L’indicateur `mutable-content` permet une personnalisation avancée du récepteur sur les appareils iOS 10+. Cet indicateur sera automatiquement envoyé lors de la composition d'une [notification enrichie][3], quelle que soit la valeur de cette case à cocher.

## Sons

Vous pouvez entrer ici un chemin d’accès à un fichier audio dans votre lot d’applications afin de spécifier un son à lire lorsque la notification push est reçue. Si le fichier audio spécifié n’existe pas ou si le mot-clé « par défaut » est saisi, Braze utilisera le son d’alerte par défaut de l’appareil.

## ID de réduction
Spécifiez un ID de réduction pour fusionner les notifications similaires. Si vous envoyez plusieurs notifications avec le même ID de réduction, l’appareil affichera uniquement la notification la plus récemment reçue. Pour plus d'informations, reportez-vous à la [documentation][4] d’Apple.

## Expiration

Cochez la case **Expiration** pour définir un délai d’expiration pour votre message. Si l’appareil d’un utilisateur perd sa connexion, Braze continuera d’essayer d’envoyer le message jusqu’à l’heure spécifiée. Si cette option n’est pas définie, la plateforme établit par défaut un délai d’expiration de 30 jours. Notez que les notifications push expirant avant la livraison ne sont pas considérées comme ayant échoué et ne seront pas enregistrées comme une non-remise.

[1]: {% image_buster /assets/img_archive/ios_advanced_settings.gif %}
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#ios-10-rich-notifications
Il y a [4]: https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1
