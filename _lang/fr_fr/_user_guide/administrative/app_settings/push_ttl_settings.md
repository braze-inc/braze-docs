---
nav_title: Paramètres de durée de vie des notifications push
article_title: Paramètres de durée de vie des notifications push
page_order: 16
page_type: reference
description: "Cet article de référence couvre les paramètres de notification Push Time to Live (TTL, durée de vie) du tableau de bord de Braze."
channel: push

---

# Paramètres TTL (Durée de vie) de notification push

> Découvrez la page de paramètres Push Time to Live dans le tableau de bord de Braze.

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

1. Allez dans **Paramètres** > **Gérer les paramètres** > **Paramètres TTL push**.
2. Pour chaque plateforme Android, définissez une valeur de durée en ligne/instantanée par défaut. Vous pouvez définir des incréments plus petits, comme les heures ou les secondes, pour un contrôle plus précis.
3. Sélectionnez **Enregistrer** pour appliquer vos modifications.

![Onglet Paramètres de durée de vie (TTL) des notifications push sous Gérer les paramètres][1]


[1]: {% image_buster /assets/img/push_ttl.png %}
