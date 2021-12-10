---
nav_title: Prep Guide
article_title: Guide de préparation des messages dans l'application
page_order: 0.5
page_type: Référence
description: "Cet article couvre certaines questions et pratiques exemplaires que vous devriez considérer avant de construire vos messages dans l'application."
channel: messages intégrés à l'application
---

# Guide de préparation des messages dans l'application

Avant de commencer à créer votre message dans l'application, vous devriez considérer certains des sujets suivants, de sorte que la création de votre message est rapide et facile.

## Considérations générales

- Si vous construisez en campagne, combien de variantes de ce message souhaitez-vous afficher ? Pour les idées de test de variantes, consultez [Conseils pour différents canaux]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#tips-different-channels).
- Si vous construisez en Canvas, ce message sera-t-il jumelé à d'autres canaux de messagerie à cette étape?
- Quand souhaitez-vous que [votre message expire]({{site.baseurl}}/canvas_in-app_messages/)?

## Considérations ciblées

- Les messages intégrés sont les meilleurs pour les utilisateurs qui visitent régulièrement votre application – incluez-vous ce public ?
- Où voulez-vous que vos utilisateurs rencontrent votre message ? Dans votre application Web ? Dans votre application mobile ?
- Quel événement déclenche ce message ?
- Est-ce que certains de vos utilisateurs utilisent des versions plus anciennes de votre application ? Dans l'affirmative, ils pourraient ne pas pouvoir voir certains éléments de votre message. En savoir plus sur les [générations]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/generations/).
- Pour quel type d'appareil ou d'appareils êtes-vous en train de construire ce message ? N'oubliez pas que vous pouvez prévisualiser votre message en utilisant l'onglet **Aperçu** ou **Tester**. Reportez-vous à [Tester]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) pour plus d'informations.

## Considérations de contenu

- Quelles langues utiliserez-vous dans ce message ?
- Quelle est la copie de votre en-tête et de votre corps? Sont-ils attirants et pertinents pour votre utilisateur?
- Les messages dans l'application n'apparaissent que pour un temps défini. Votre copie est-elle concise et mémorable?
- Allez-vous utiliser [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) pour construire une copie plus personnalisée ?
- Pour les messages en plein écran dans l'application, votre image ou tout autre média se trouve dans la [zone sûre]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/#image-safe-zone).

## Considérations de conversion

- Quel est votre objectif pour ce message ? Comment pouvez-vous représenter cela dans votre message ?
- Est-ce que vos boutons offrent des options qui ont un sens pour votre utilisateur? Quel est votre appel principal [à l'action]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#buttons)?
- Êtes-vous [profondément lié à un autre contenu dans l'application][1]? Utilisez-vous ce message dans l'application pour envoyer et accepter une [demande d'autorisation ou d'amorçage push][21]?
- Avez-vous une option de sortie de message ? Sinon, vous pouvez toujours copier et coller ce snippet pour créer un bouton rapide :
    ```html
    <a href="appboy://close">X</a>
    ```


[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content
[21]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
