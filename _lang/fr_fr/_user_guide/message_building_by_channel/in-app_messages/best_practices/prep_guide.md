---
nav_title: Guide de préparation
article_title: Guide de préparation des messages in-app
page_order: 0.5

page_type: reference
description: "Cet article aborde quelques questions et bonnes pratiques à prendre en compte avant de créer vos messages in-app."
channel: in-app messages

---

# Guide de préparation des messages in-app

> Avant de créer vos messages in-app, vous devriez prendre en compte quelques-uns des sujets suivants afin que la construction de votre message soit rapide et facile.

## Considérations générales

- Si vous créez une campagne, combien de variantes de ce message souhaitez-vous afficher ? Pour des idées de tests variants, consultez la rubrique [Conseils pour les différents canaux.]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/#tips-different-channels)
- Si vous créez un Canvas, ce message sera-t-il associé à d'autres canaux de communication dans cette étape ?
- Quand souhaitez-vous que [votre message expire]({{site.baseurl}}/canvas_in-app_messages/)?

## Considérations relatives au ciblage

- Les messages in-app conviennent mieux aux utilisateurs qui consultent régulièrement votre application. Incluez-vous cette audience ?
- Où voulez-vous que vos utilisateurs voient votre message ? Dans votre application Web ? Dans votre application mobile ?
- Quel événement doit déclencher ce message ?
- Certains de vos utilisateurs utilisent-ils d'anciennes versions de votre application ? Si c'est le cas, il se peut qu'ils ne puissent pas voir certains éléments de votre message.
- Pour quel(s) type(s) d'appareil(s) créez-vous ce message ? N'oubliez pas que vous pouvez prévisualiser votre message à l'aide de la boîte de **prévisualisation** ou de l'onglet **Test.**  Pour plus d'informations, reportez-vous à la section [Tests.]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) 

## Considérations sur le contenu

- Quelles langues utiliserez-vous dans ce message ?
- Quels sont les textes de votre en-tête et de votre corps de texte ? Sont-elles accrocheuses et pertinentes pour votre utilisateur ?
- Les messages in-app ne s'affichent que pendant une durée déterminée. Votre texte est-il concis et mémorable ?
- Utiliserez-vous [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) pour ajouter des textes personnalisés ?
- Pour les messages in-app en plein écran, votre image ou autre média se trouve-t-il dans la [zone de sécurité]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/#image-safe-zone)?
- Pour les messages in-app des enquêtes, voulez-vous enregistrer les attributs ou les soumissions ? Avez-vous créé votre page de confirmation ?

## Considérations relatives à la conversion

- Quel est l'objectif de ce message ? Comment pouvez-vous le conseiller dans votre message ?
- Vos boutons offrent-ils des options qui ont un sens pour l'utilisateur ? Quel est votre [principal appel à l'action]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#buttons)?
- Créez-vous des [liens profonds vers d'autres contenus de l'application]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content)? Utilisez-vous ce message in-app pour envoyer et accepter une [demande de permission ou d'amorçage push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/)?
- Avez-vous une option d'envoi de messages ? Si ce n'est pas le cas, vous pouvez toujours copier et coller cet extrait de code pour créer un bouton rapide :
    ```html
    <a href="appboy://close">X</a>
    ```


