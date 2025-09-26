---
nav_title: Paramètres de notifications push
article_title: Paramètres de notifications push
page_order: 16
page_type: reference
description: "Cet article donne un aperçu des paramètres de poussée dans le tableau de bord de Braze."
channel: push

---

# Paramètres de notifications push

> La page **Paramètres de push** vous permet de configurer les paramètres clés de vos notifications push, notamment la durée en ligne/en production/instantanée (TTL) et la priorité FCM par défaut pour les campagnes Android. Ces paramètres permettent d'optimiser la réception/distribution de vos notifications push et leur efficacité, garantissant ainsi une meilleure expérience à vos utilisateurs.

## Qu'est-ce que le TTL notifications push ?

Push Time to Live (TTL) contrôle la durée pendant laquelle Braze tentera de délivrer une notification push aux appareils qui sont hors ligne au moment de l'envoi de la campagne. Si un appareil se reconnecte après l'expiration du TTL, le message ne sera pas envoyé. Ce paramètre ne supprime pas une notification si elle a déjà été reçue par l'appareil de l'utilisateur. Il contrôle uniquement la durée pendant laquelle le fournisseur push tente de délivrer une notification.

## Réglage des valeurs TTL push push par défaut

Par défaut, Braze définit le TTL des notifications push au maximum pour chaque service d'envoi de messages push. 

| Service d'envoi de messages en mode push | Maximum TTL |
| --- | --- |
| Web (par le biais des services FCM ou Web Push) | 28 jours |
| Firebase Cloud Messaging (FCM) | 28 jours |
| Kindle (ADM) | 31 jours |
| Huawei (HMS) | 15 jours |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Ces paramètres généraux s'appliquent à toutes les campagnes push, sauf si un TTL différent est défini pour un message spécifique. Pour ajuster le TTL d'un message, reportez-vous à la section [Paramètres avancés de la campagne.]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/advanced_campaign_settings/#ttl)

Pour définir un autre TTL des notifications push par défaut :

1. Allez dans **Paramètres** > **Gérer les paramètres** > **Paramètres de poussée**.
2. Pour chaque plateforme Android, définissez une valeur de durée en ligne/instantanée par défaut. Vous pouvez définir des incréments plus petits, comme les heures ou les secondes, pour un contrôle plus précis.
3. Sélectionnez **Enregistrer** pour appliquer vos modifications.

![Les notifications TTL push pour les appareils Firebase, Web, Kindle et Huawei.]({% image_buster /assets/img/push_ttl.png %})

## Priorité par défaut du FCM pour les campagnes Android

Vous pouvez définir la priorité par défaut de l'envoi de messages dans le nuage Firebase (FCM) pour toutes les campagnes de communication Android. Cette priorité détermine la manière dont la notification push est délivrée aux appareils des utilisateurs.

Les options prioritaires de la FCM sont les suivantes :

| Priorité | Description | Cas d’utilisation |
| --- | --- | --- |
| Normale | Priorité à la réception/distribution standard qui optimise l'utilisation de la batterie. | Contenu ne nécessitant pas une attention immédiate |
| Élevée | Les messages sont envoyés immédiatement | Notifications urgentes nécessitant une réception/distribution rapide |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Pour définir la priorité par défaut du FCM :

1. Allez dans **Paramètres** > **Gérer les paramètres** > **Paramètres de poussée**.
2. Dans la section Priorité du FCM, sélectionnez "Normal" ou "Haut" comme réglage par défaut.
3. Sélectionnez **Enregistrer** pour appliquer vos modifications.

![Paramètres de priorité de réception/distribution Android.]({% image_buster /assets/img/push_fcm_priority_settings.png %})

Ce paramètre s'applique globalement à toutes les nouvelles campagnes push Android, sauf si une priorité différente est sélectionnée lors de la création d'une campagne spécifique. 

{% alert note %}
Si la FCM détecte que votre application envoie fréquemment des messages à priorité élevée qui ne donnent pas lieu à des notifications visibles par l'utilisateur ou à un engagement de sa part, ces messages peuvent être automatiquement dépriorisés et revenir à une priorité normale.
{% endalert %}

Pour plus d'informations sur les niveaux de priorité et la suppression des priorités du FCM, voir [Paramètres avancés de la campagne]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/advanced_campaign_settings/#fcm-priority).

