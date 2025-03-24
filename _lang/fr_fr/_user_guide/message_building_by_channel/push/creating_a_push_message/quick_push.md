---
nav_title: Envoi rapide de messages
article_title: Envoi rapide de messages
alias: "/quick_push/"
description: "Cet article décrit les choses à savoir lors de la création d'une campagne push ou d'un Cavnas en utilisant l'expérience d'édition push rapide."
---

# Envoi rapide de messages

Lorsque vous créez une campagne de push ou un Canvas dans Braze, vous pouvez sélectionner plusieurs plateformes et appareils afin de créer un message pour toutes les plateformes en une seule expérience de communication appelée quick push.

## Cas d’utilisation

Cette expérience de modification est optimale pour les cas d'utilisation suivants :

- Campagnes push mobiles et étapes du canvas message qui doivent être envoyées à plusieurs types d'appareils (par exemple à la fois iOS et Android).
- Les notifications push sensibles à la durée qui doivent cibler plusieurs plateformes rapidement et avec précision, lorsque le contenu est le même d'une plateforme à l'autre (comme les nouvelles de dernière minute ou les mises à jour de jeux en direct).

## Création d'une campagne de push rapide ou d'un canvas

Pour créer une campagne ciblant plusieurs plateformes et appareils :

1. Créez une campagne ou ajoutez une [étape message à]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) un canvas.  
2. Sélectionnez **Notification push**.
3. Sélectionnez les plateformes souhaitées (Mobile, Web, Kindle) et les appareils mobiles (iOS, Android). Si vous sélectionnez plusieurs appareils, les tests multivariés ne seront pas disponibles pour votre campagne.

### Sélection des plateformes pour une campagne
![Options permettant de sélectionner plusieurs plateformes pour une campagne de notifications push, telles que Mobile, Web et Kindle, et plusieurs appareils, tels que iOS et Android.][1]

### Sélection des plates-formes pour une étape du canvas
![Options permettant de sélectionner plusieurs plateformes pour une étape de message push, telles que Mobile, Web et Kindle, et plusieurs appareils, tels que iOS et Android.][8]

{:start="4"}
4\. Sélectionnez **Confirmer**. Après avoir sélectionné **Confirmer**, vous ne pourrez plus modifier les plateformes ou appareils sélectionnés.
5\. Continuez à implémenter votre campagne ou votre Canvas.

Votre compositeur aura un aspect légèrement différent de l'habituel. Poursuivez votre lecture pour découvrir les différences.

### Ce qui est différent

Dans l'onglet **Composer**, vous pouvez spécifier un titre, un message et un comportement au clic pour toutes les plateformes et tous les appareils que vous avez choisis.

Le volet de prévisualisation affiche une approximation de ce à quoi ressemblera votre message pour chaque plateforme. Bien qu'il puisse vous donner un bon indicateur des endroits où vous pourriez atteindre les limites de caractères, n'oubliez pas de toujours tester vos messages sur un appareil réel avant d'envoyer votre campagne.

![Vue d’édition unique avec un seul champ de titre, de message et de comportement lors du clic pour trois types de notifications push : iOS, Android et Web.][2]

Dans la section **Ressources**, sélectionnez ou téléchargez les images que vous souhaitez voir apparaître pour chaque plateforme. Gardez à l'esprit que les appareils ont des spécifications différentes en matière d'images et de nombre de caractères. Pour obtenir de l'aide, reportez-vous à la rubrique [Formats d'envoi de messages et d'images][3].

![Section Ressources de la vue d'édition unique avec des champs pour l'image de l'icône Push, l'image de la notification iOS, l'image de la notification Android et l'image de la notification Web.][4]{:style="max-width:50%"}

Terminez ensuite la création de votre campagne de notifications push comme d'habitude. Pour plus d'informations, consultez la section [Créer une campagne de push][5].

## Choses à savoir

### Type de notification

Le type de notification est par défaut "Standard Push" et ne peut pas être modifié. Si vous souhaitez créer un contenu push différent, tel que Push Stories ou Inline Image (Android), créez des campagnes distinctes pour chaque type d'appareil.

### Tests multivariés

Si vous sélectionnez plusieurs appareils pour les plateformes mobiles, comme iOS et Android, les tests multivariés ne seront pas disponibles pour votre campagne. Si vous souhaitez effectuer des tests multivariés, créez des campagnes distinctes pour chaque type d'appareil.

### Paramètres spécifiques à l'appareil

Vous pouvez modifier les paramètres spécifiques à la plate-forme dans l'éditeur. Cela inclut des paramètres tels que les [boutons d'action push]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_action_buttons/), les canaux et groupes de notification, le TTL, la priorité d'affichage, les sons, etc.

Pour plus d'informations sur les réglages spécifiques aux appareils, reportez-vous aux collections d'articles suivantes :

- [Options iOS][6]
- [Options Android][7]


[1]: {% image_buster /assets/img_archive/quick_push_1.png %}
[2]: {% image_buster /assets/img_archive/quick_push_2.png %}
[4]: {% image_buster /assets/img_archive/quick_push_3.png %}
[8]: {% image_buster /assets/img_archive/quick_push_4.png %}
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/
[6]: {{site.baseurl}}/user_guide/message_building_by_channel/push/ios
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/push/android