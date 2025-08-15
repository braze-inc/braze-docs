---
nav_title: Maximiser les notifications push
article_title: Maximiser les notifications push
page_type: reference
description: "L’option Maximiser les notifications push amplifie les notifications push Android en suivant celles qui ont échoué pour les renvoyer lorsque les utilisateurs ont le plus de chances de les recevoir."

permalink: /user_guide/message_building_by_channel/push/android/push_max/
platform: Android
channel:
  - Push

---

# Maximiser les notifications push

> Découvrez Push Max et apprenez comment utiliser cette fonctionnalité pour améliorer la livrabilité des notifications push Android sur les [appareils OEM chinois]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/chinese_push_deliverability/).

## Qu'est-ce que Push Max ?

L’option Maximiser les notifications push amplifie les notifications push Android en suivant celles qui ont échoué pour les renvoyer lorsque les utilisateurs ont le plus de chances de les recevoir.

Certains appareils Android fabriqués par des équipementiers chinois, tels que Xiaomi, OPPO et Vivo, emploient un schéma robuste d'optimisation de la batterie pour prolonger son autonomie. Ce comportement peut avoir pour conséquence involontaire d'arrêter le traitement des applications en arrière-plan, ce qui réduit la livrabilité des notifications push sur ces appareils si l'application n'est pas au premier plan. Cette situation se produit le plus souvent sur les marchés de l'Asie-Pacifique (APAC).

## Disponibilité

- Disponible uniquement pour les notifications push Android
- Non pris en charge pour les messages basés sur une action ou déclenchés par l'API.
- Non pris en charge lorsque l'option d' [envoi uniquement vers le dernier appareil utilisé par l'utilisateur]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#device-options) est sélectionnée.

## Conditions préalables

Les notifications push envoyées à l'aide de Push Max ne seront délivrées qu'aux appareils disposant [au minimum de la version suivante du SDK]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions) :

{% sdk_min_versions android:29.0.1 %}

## Utilisation de Push Max

{% tabs %}
{% tab Campagnes %}

Pour utiliser Push Max dans votre campagne :

1. Créez une campagne de push.
2. Sélectionnez **Android Push** comme plateforme.
3. Passez à l'étape de la **Planifier l’envoi**.
4. Sélectionnez **Envoyer à l'aide de Push Max.**

![Section Livrabilité des notifications push Android de l'étape Planifier l’envoi, avec l'option « Envoyer avec Push Max ».]({% image_buster /assets/img_archive/push_max_campaigns.png %})

{% endtab %}
{% tab Canvas %}

Pour utiliser Push Max dans votre canvas :

1. Ajoutez une étape Message à votre canvas.
2. Sélectionnez **Android Push** comme plateforme.
3. Accédez à l'onglet **Paramètres de réception**.
4. Sélectionnez **Envoyer à l'aide de Push Max.**

![Onglet Paramètres de réception d'une étape Message de notifications push Android, avec l'option « Envoyer avec Push Max ».]({% image_buster /assets/img_archive/push_max_canvas.png %})

{% endtab %}
{% endtabs %}

Les deux fonctionnalités suivantes, le timing intelligent et la durée en vie, peuvent être utilisées en tandem avec Push Max pour augmenter potentiellement la livrabilité de vos notifications push Android.

### Timing intelligent

Push Max fonctionne mieux lorsque le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) est activé. Le timing intelligent peut calculer et envoyer la notification push à un moment où l'utilisateur est le plus susceptible d'utiliser l'application et où le push a le plus de chances d'être délivré.

### Durée en ligne/en vie (TTL)

La durée de vie peut assurer le suivi des échecs des notifications push vers Firebase Cloud Messaging (FCM) et réessayer de renvoyer la notification lorsque l'utilisateur est susceptible de la recevoir.

Par défaut, la durée de vie est fixée à 28 jours, soit le maximum. Vous pouvez réduire la durée TTL par défaut pour tous les nouveaux messages push Android à partir de **Paramètres** > **Paramètres de l'espace de travail** > **Push Time to Live (TTL)**, ou vous pouvez configurer le nombre de jours par message dans l'onglet **Paramètres** lors de la composition d'une notification push Android.

![La durée en ligne/en vie est fixée à 28 jours.]({% image_buster /assets/img_archive/time_to_live.png %}){: style="max-width:60%"}

## Choses à savoir

### Codes de promotion

Nous vous recommandons de ne pas utiliser les [codes de promotion]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/) Braze dans les messages où la fonction Push Max est activée.

En effet, les codes de promotion sont uniques. Si une notification push contenant un code de promotion n'aboutit pas, lorsque cette notification est renvoyée en raison de Push Max, un nouveau code de promotion sera envoyé. Vous risquez ainsi de consommer les codes de promotion plus rapidement que prévu.

### Propriétés d'événement et propriétés d'entrée du canvas

Push Max peut ne pas fonctionner comme prévu si vous incluez dans votre message des références liquides aux [propriétés d'entrée de Canvas ou aux propriétés d'événement]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties). En effet, les propriétés d'entrée et d'événement ne sont pas disponibles lorsque Push Max tente de renvoyer le message.
