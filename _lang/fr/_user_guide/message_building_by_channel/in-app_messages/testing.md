---
nav_title: Test
article_title: Test des messages In-App
page_order: 3
description: "Cet article de référence explique pourquoi vous devriez tester vos messages in-app, comment les tester, et présente une liste de points à prendre en compte avant l’envoi."
channel:
  - messages In-App
  
---

# Test

Il est extrêmement important de toujours tester vos messages In-App avant d’envoyer vos campagnes. Nos fonctions d’aperçu et de test offrent deux façons de consulter vos messages In-App. Vous pouvez prévisualiser votre message pour vous guider lorsque vous le composez, ainsi qu’envoyer un message test à votre appareil ou à celui d’un utilisateur spécifique. Nous vous recommandons d’utiliser les deux.

## Aperçu

Vous pouvez prévisualiser votre message In-App lorsque vous le composez. Cela devrait vous aider à visualiser à quoi ressemblera votre message final du point de vue de l’utilisateur.

{% alert warning %}
Dans **Preview** (Aperçu), la vue de votre message peut différer son rendu réel sur l’appareil de l’utilisateur. Nous vous recommandons toujours d’envoyer un message test à un appareil pour vous assurer que vos données, le texte, la personnalisation et les attributs personnalisés se génèrent correctement.
{% endalert %}

### Aperçu de génération de messages In-App

Prévisualisez l’apparence de votre message pour un utilisateur aléatoire, un utilisateur spécifique ou un utilisateur personnalisé, les deux derniers étant particulièrement utiles si votre message inclut une personnalisation ou plusieurs langues. Vous pouvez également prévisualiser les messages pour les appareils mobiles ou les tablettes afin d’avoir une meilleure idée de l’expérience des utilisateurs.

![Onglet Compose (Composer) lors de la création d’un message In-App montrant l’aperçu de son apparence. Aucun utilisateur n’étant sélectionné, la section du corps affiche Liquid tel quel après son ajout.][1]

Braze dispose de trois générations de messages In-App disponibles. Vous pouvez affiner les appareils auxquels vos messages doivent envoyés, en fonction de la génération qu’ils prennent en charge.

![Bascule entre des générations lors de la prévisualisation d’un message In-App.][2]{: height="50%" width="50%"}

## Test

{% alert warning %}
Pour envoyer un test à des [groupes de test de contenu]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) ou des utilisateurs individuels, les notifications push doivent être activées sur vos appareils de test avant envoi. <br><br>Par exemple, vous devez avoir activé les notifications push sur votre appareil iOS pour pouvoir appuyer sur la notification avant que le message de test ne s’affiche.
{% endalert %}

### Aperçu du message en tant qu’utilisateur

Vous pouvez également prévisualiser les messages dans l’onglet **Test** comme si vous étiez un utilisateur. Vous pouvez sélectionner un utilisateur spécifique, un utilisateur aléatoire ou créer un utilisateur personnalisé.

![Onglet Test lors de la création d’un message In-App. L’option « Preview message as user » (Aperçu de message en tant qu’utilisateur) est définie à « Custom User » (Utilisateur personnalisé) avec les champs de profil disponibles apparaissant comme options configurables.][3]

### Liste de contrôle des tests

- Les images et les données s’affichent-elles et se comportent-elles comme prévu ?
- Liquid fonctionne-t-il comme prévu ? Avez-vous pris en compte une [valeur d’attribut par défaut]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values) si Liquid ne renvoie aucune information ?
- Votre copie est-elle claire, concise et correcte ?
- Vos boutons dirigent-ils l’utilisateur à l’endroit correct ?

[1]: {%image_buster /assets/img/in-app-message-preview.png %}
[2]: {% image_buster /assets/img/iam-generations.gif %}
[3]: {% image_buster /assets/img/iam-user-preview.png %}
