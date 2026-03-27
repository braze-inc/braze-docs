---
nav_title: Messages push rapides
article_title: Messages push rapides
alias: "/quick_push/"
description: "Cet article décrit les points à connaître lors de la création d'une campagne push ou d'un canvas avec l'expérience d'édition quick push."
---

# Messages push rapides

Lorsque vous créez une campagne push ou un canvas dans Braze, vous pouvez sélectionner plusieurs plateformes et appareils afin de rédiger un seul message pour toutes les plateformes dans une expérience d'édition unifiée appelée quick push.

## Cas d'utilisation

Cette expérience d'édition est idéale pour les cas d'utilisation suivants :

- Les campagnes push mobiles et les étapes de message dans un canvas qui doivent être envoyées à plusieurs types d'appareils (par exemple iOS et Android).
- Les notifications push urgentes qui doivent cibler plusieurs plateformes rapidement et avec précision, lorsque le contenu est identique d'une plateforme à l'autre (comme les alertes d'actualité ou les mises à jour de scores en direct).

## Créer une campagne quick push ou un canvas

Pour créer une campagne ciblant plusieurs plateformes et appareils :

1. Créez une campagne ou ajoutez une [étape Message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) à un canvas.  
2. Sélectionnez **Notification push**.
3. Sélectionnez les plateformes souhaitées (Appareil mobile, Web, Kindle) et les appareils mobiles (iOS, Android). Si vous sélectionnez plusieurs appareils, le test multivarié ne sera pas disponible pour votre campagne.

### Sélection des plateformes pour une campagne
![Options permettant de sélectionner plusieurs plateformes pour une campagne de notifications push, telles que Appareil mobile, Web et Kindle, et plusieurs appareils, tels que iOS et Android.]({% image_buster /assets/img_archive/quick_push_1.png %})

### Sélection des plateformes pour une étape du canvas
![Options permettant de sélectionner plusieurs plateformes pour une étape de message push, telles que Appareil mobile, Web et Kindle, et plusieurs appareils, tels que iOS et Android.]({% image_buster /assets/img_archive/quick_push_4.png %})

{:start="4"}
4. Sélectionnez **Confirmer**. Une fois que vous avez sélectionné **Confirmer**, vous ne pourrez plus modifier les plateformes ou appareils sélectionnés.
5. Poursuivez la configuration de votre campagne ou de votre canvas.

L'éditeur aura un aspect légèrement différent de l'habitude. Poursuivez votre lecture pour découvrir ce qui change.

### Ce qui change

Dans l'onglet **Rédiger**, vous pouvez définir un titre, un message et un comportement au clic communs à toutes les plateformes et tous les appareils sélectionnés.

Le volet de prévisualisation affiche un aperçu de votre message tel qu'il apparaîtra sur chaque plateforme. Il vous donne une bonne indication des endroits où vous pourriez atteindre les limites de caractères, mais pensez à toujours tester vos messages sur un appareil réel avant d'envoyer votre campagne.

![Vue d'édition unique avec un seul champ de titre, de message et de comportement au clic pour trois types de notifications push : iOS, Android et Web.]({% image_buster /assets/img_archive/quick_push_2.png %})

Dans la section **Actifs**, sélectionnez ou téléchargez les images que vous souhaitez afficher pour chaque plateforme. Gardez à l'esprit que les spécifications d'images et les limites de caractères varient selon les appareils. Pour en savoir plus, consultez [Spécifications des images et du texte pour les notifications push]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#push).

![Section Actifs de la vue d'édition unique avec des champs pour l'image de l'icône push, l'image de notification iOS, l'image de notification Android et l'image de notification Web.]({% image_buster /assets/img_archive/quick_push_3.png %}){:style="max-width:50%"}

Terminez ensuite la configuration de votre campagne push comme d'habitude. Pour plus de détails, consultez [Créer une campagne push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/).

## Bon à savoir

### Type de notification

Le type de notification est défini par défaut sur « Standard Push » et ne peut pas être modifié. Si vous souhaitez créer un autre type de push, comme du contenu push ou une image intégrée (Android), créez des campagnes distinctes pour chaque type d'appareil.

### Test multivarié

Si vous sélectionnez plusieurs appareils pour les plateformes mobiles (par exemple iOS et Android), le test multivarié ne sera pas disponible pour votre campagne. Pour effectuer un test multivarié, créez des campagnes distinctes pour chaque type d'appareil.

### Paramètres spécifiques à l'appareil

Vous pouvez modifier les paramètres propres à chaque plateforme dans l'éditeur. Cela inclut notamment les [boutons d'action push]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_action_buttons/), les canaux et groupes de notification, le TTL, la priorité d'affichage, les sons, etc. 

Notez que les boutons d'action push ne sont pas pris en charge lorsque vous ciblez à la fois iOS et Android via des campagnes quick push. Pour plus d'informations sur les paramètres spécifiques aux appareils, consultez les collections d'articles suivantes :

- [Options iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios)
- [Options Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android)