---
nav_title: Paramètres de notifications push
article_title: Paramètres de notifications push pour iOS
platform: Swift
page_order: 7
description: "Cet article de référence couvre les paramètres avancés de notifications push pour iOS, tels que les options d’alerte, les sons, l’expiration et plus encore pour le SDK Swift."
channel:
  - push

---

# Paramètres de notifications push

> Lorsque vous créez une campagne push via le tableau de bord, cliquez sur l'onglet **Paramètres** à l'étape **Composer** pour afficher les paramètres avancés disponibles.

![]({% image_buster /assets/img_archive/ios_advanced_settings.png %})

## Paires clé-valeur

Braze vous permet d’envoyer des paires clé-valeur définies de manière personnalisée sous forme de chaînes de caractères, appelées `extras`, ainsi qu’une notification push à votre application. Des éléments supplémentaires peuvent être définis via le tableau de bord ou l’API et seront disponibles en tant que paires clé-valeur dans le dictionnaire `notification` transmis à vos implémentations de délégué de notification push.

## Options d’alerte

Sélectionnez la case à cocher **Options d'alerte** pour voir une liste déroulante des paires clé-valeur disponibles pour ajuster l'apparence de la notification sur les appareils.

## Ajouter un indicateur de contenu disponible

Cochez la case **Ajouter un indicateur de contenu disponible** pour indiquer aux appareils de télécharger le nouveau contenu en arrière-plan. Le plus souvent, vous pouvez cocher cette case si vous souhaitez envoyer des [notifications silencieuses]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/).

## Ajouter un indicateur de contenu mutable

Cochez la case **Ajouter un indicateur de contenu mutable** pour activer la personnalisation avancée du récepteur. Cet indicateur sera automatiquement envoyé lors de la composition d'une [notification enrichie]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/rich_notifications/), quelle que soit la valeur de cette case à cocher.

## Mettre à jour le nombre de badges de l’application

Entrez le nombre que vous souhaitez mettre à jour pour le nombre de votre badge ou utilisez la syntaxe Liquid pour définir des conditions personnalisées. Vous pouvez également mettre à jour le nombre de badges de message par programmation : consultez notre article dédié au [nombre de badges]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/badges/).

## Sons

Si vous souhaitez que votre notification push soit accompagnée d'un son personnalisé lorsqu'elle est reçue, utilisez le champ **Sound** pour spécifier l'URL du protocole de votre fichier sonore. Pour plus d'informations sur la personnalisation, consultez notre article sur les [sons personnalisés]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/custom_sounds/).

## ID de réduction

Spécifiez un ID de réduction pour fusionner les notifications similaires. Si vous envoyez plusieurs notifications avec le même ID de réduction, l’appareil affichera uniquement la notification la plus récemment reçue. Reportez-vous à la documentation d'Apple sur les [notifications groupées](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1).

## Expiration

Cocher la case **Expiration** permettra de définir une durée d'expiration pour votre message. Si l’appareil d’un utilisateur perd sa connexion, Braze continuera d’essayer d’envoyer le message jusqu’à l’heure spécifiée. Si cette option n’est pas définie, la plateforme établit par défaut un délai d’expiration de 30 jours. Notez que les notifications push expirant avant la livraison ne sont pas considérées comme ayant échoué et ne seront pas enregistrées comme une non-remise.

