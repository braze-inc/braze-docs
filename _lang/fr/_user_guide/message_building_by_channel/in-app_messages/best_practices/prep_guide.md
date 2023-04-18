---
nav_title: Guide de préparation
article_title: Guide de préparation des messages In-App
page_order: 0.5

page_type: reference
description: "Le présent article couvre quelques questions et meilleures pratiques à prendre en compte avant de créer vos messages In-App."
channel: messages In-App

---

# Guide de préparation des messages In-App

> Avant de créer vos messages In-App, vous devez prendre en compte les sujets suivants pour une création simple et rapide.

## Considérations générales

- Si vous élaborez une campagne, combien de variantes de ce message souhaitez-vous afficher ? Pour des idées de test de variantes, consultez [Conseils pour différents canaux]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/#tips-different-channels).
- Si vous créez un Canvas, ce message sera-t-il associé à d’autres canaux de communication à cette étape ?
- Quand souhaitez-vous que [votre message expire]({{site.baseurl}}/canvas_in-app_messages/) ?

## Considérations relatives au ciblage

- Les messages In-App sont idéaux pour les utilisateurs qui visitent régulièrement votre application. Incluez-vous cette audience ?
- Où souhaitez-vous que vos utilisateurs voient votre message ? Dans votre application Web ? Dans votre application mobile ?
- Quel événement devrait déclencher ce message ?
- Vos utilisateurs emploient-ils des versions plus anciennes de votre application ? Dans ce cas, il risquent de ne pas voir certains éléments de votre message.
- Pour quel type d’appareil créez-vous ce message ? Pour rappel, vous pouvez prévisualiser votre message en utilisant la zone **Preview** (Aperçu) ou l’onglet **Test**. Consultez [Test]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) pour plus d’informations.

## Considérations relatives au contenu

- Quelles langues utiliserez-vous dans ce message ?
- Quel est le texte de l’en-tête et du corps ? Sont-ils accrocheurs et pertinents pour votre utilisateur ?
- Les messages In-App apparaissent uniquement pendant une durée définie. Votre texte est-il concis et mémorable ?
- Utiliserez-vous [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) pour ajouter un texte personnalisé ?
- Pour les messages In-App plein écran, votre image ou d’autres données se trouvent-elles dans la [zone sécurisée]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/#image-safe-zone) ?
- Pour les messages in-app de sondages, désirez-vous enregistrer des attributs ou des saisies ? Avez-vous défini votre page de validation ?

## Considérations relatives à la conversion

- Quel est votre objectif pour ce message ? Comment pouvez-vous le représenter dans votre message ?
- Vos boutons offrent-ils des options pertinentes ? Quel est votre [appel principal à l’action]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#buttons)?
- Établissez-vous un [lien profond vers un autre contenu In-App][1] ? Utilisez-vous ce message In-App pour envoyer et accepter une [demande d’autorisation ou d’amorçage de notification push][21] ?
- Avez-vous une option de sortie de message ? Sinon, vous pouvez copier et coller cet extrait de code pour créer un bouton rapide :
    ```html
    <a href="appboy://close">X</a>
    ```


[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content
[21]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
