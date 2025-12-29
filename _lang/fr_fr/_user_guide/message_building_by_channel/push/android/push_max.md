---
nav_title: Pousser Max
article_title: Pousser Max
page_type: reference
description: "Push Max amplifie les notifications push Android en suivant les notifications push qui ont échoué et en renvoyant le push lorsque l'utilisateur est plus susceptible de le recevoir."

permalink: /user_guide/message_building_by_channel/push/android/push_max/
platform: Android
channel:
  - Push

---

# Pousser Max

> Découvrez Push Max et comment vous pouvez utiliser cette fonctionnalité pour améliorer la livrabilité des notifications push Android sur les [appareils OEM chinois.]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/chinese_push_deliverability/)

## Qu'est-ce que Push Max ?

Push Max amplifie les notifications push Android en suivant les notifications push qui ont échoué et en renvoyant le push lorsque l'utilisateur est plus susceptible de le recevoir.

Certains appareils Android fabriqués par des équipementiers chinois, tels que Xiaomi, OPPO et Vivo, utilisent un schéma d'optimisation de la batterie robuste pour prolonger son autonomie. Ce comportement peut avoir pour conséquence involontaire d'arrêter le traitement des applications en arrière-plan, ce qui réduit la livrabilité des notifications push sur ces appareils si l'application n'est pas au premier plan. Cette situation se produit le plus souvent sur les marchés de l'Asie-Pacifique (APAC).

## Disponibilité

- Disponible uniquement pour les notifications push Android
- Non pris en charge pour les messages basés sur une action ou déclenchés par l'API.
- Non pris en charge lorsque l'option d' [envoi uniquement vers le dernier appareil utilisé par l'utilisateur]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#device-options) est sélectionnée.

## Conditions préalables

Les notifications push envoyées à l'aide de Push Max ne seront délivrées qu'aux appareils disposant au [minimum de la version]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions) suivante [du SDK]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions):

{% sdk_min_versions android:29.0.1 %}

## Utilisation de Push Max

{% tabs %}
{% tab Campaigns %}

Pour utiliser Push Max dans votre campagne :

1. Créez une campagne de push.
2. Sélectionnez **Android Push** comme plateforme.
3. Passez à l'étape de la **planification de la réception/distribution**.
4. Sélectionnez **Envoyer à l'aide de Push Max.**

!section Android Push Deliverability de l'étape Schedule Delivery avec l'option "Send using Push Max".]({% image_buster /assets/img_archive/push_max_campaigns.png %})

{% endtab %}
{% tab Canvas %}

Pour utiliser Push Max dans votre canvas :

1. Ajoutez une étape Message à votre Canvas.
2. Sélectionnez **Android Push** comme plateforme.
3. Accédez à l'onglet **Paramètres de réception/distribution**.
4. Sélectionnez **Envoyer à l'aide de Push Max.**

!onglet Paramètres de réception/distribution d'une étape d'un message Push Android avec l'option "Envoyer à l'aide de Push Max".]({% image_buster /assets/img_archive/push_max_canvas.png %})

{% endtab %}
{% endtabs %}

Les deux fonctionnalités suivantes, le timing intelligent et la durée en vie, peuvent être utilisées en tandem avec Push Max pour augmenter potentiellement la livrabilité de vos notifications push Android.

### Le timing intelligent

Push Max fonctionne mieux lorsque le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) est activé. Le timing intelligent peut calculer et envoyer la notification push à un moment où l'utilisateur est le plus susceptible d'utiliser l'application et où le push a le plus de chances d'être délivré.

### Durée en ligne/en vie (TTL)

La durée en ligne/en production/instantanée (TTL) peut suivre les échecs des notifications push vers Firebase Cloud Messaging (FCM) et réessayer la notification lorsque l'utilisateur est susceptible de la recevoir.

Par défaut, la durée en ligne/en production/instantanée est fixée à 28 jours, ce qui est le maximum. Vous pouvez diminuer le TTL par défaut pour tous les nouveaux messages push Android à partir de **Paramètres** > **Paramètres de l'espace de travail** > **Paramètres Push**, ou vous pouvez configurer le nombre de jours par message dans l'onglet **Paramètres** lors de la composition d'une notification push Android.

!La durée en ligne/en production/instantanée est fixée à 28 jours.]({% image_buster /assets/img_archive/time_to_live.png %}){: style="max-width:60%"}

## Ce qu'il faut savoir

### Codes de promotion

Nous vous recommandons de ne pas utiliser les [codes de promotion]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/) Braze dans les messages où la fonction Push Max est activée.

En effet, les codes de promotion sont uniques. Si une notification push contenant un code de promotion n'aboutit pas, lorsque cette notification est renvoyée en raison de Push Max, un nouveau code de promotion sera envoyé. Vous risquez ainsi de consommer les codes de promotion plus rapidement que prévu.

### Propriétés d'événement et propriétés d'entrée du canvas

Push Max peut ne pas fonctionner comme prévu si vous incluez dans votre message des références liquides aux [propriétés d'entrée de Canvas ou aux propriétés d'événement]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties). En effet, les propriétés d'entrée et d'événement ne sont pas disponibles lorsque Push Max tente de renvoyer le message.
