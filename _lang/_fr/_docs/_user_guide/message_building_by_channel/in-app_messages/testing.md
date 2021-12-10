---
nav_title: Tests en cours
article_title: Tester les messages In-App
page_order: 3
description: "Il est extrêmement important de toujours tester vos messages dans l'application avant d'envoyer vos campagnes. Nos capacités de prévisualisation et de test offrent deux façons de regarder vos messages dans l'application."
channel:
  - messages intégrés à l'application
---

# Tests en cours

Il est extrêmement important de toujours tester vos messages dans l'application avant d'envoyer vos campagnes. Nos capacités de prévisualisation et de test offrent deux façons de regarder vos messages dans l'application. Vous pouvez prévisualiser votre message pour vous aider à le visualiser au fur et à mesure que vous le composez, en plus d'envoyer un message de test à votre appareil ou à celui d'un utilisateur spécifique. Nous vous recommandons de profiter des deux.

## Aperçu

Vous pouvez prévisualiser votre message dans l'application lorsque vous le composez. Cela devrait vous aider à visualiser à quoi ressemblera votre message final du point de vue de votre utilisateur.

{% alert warning %}
Dans __Aperçu__, la vue de votre message peut ne pas être identique à son affichage réel sur l'appareil de l'utilisateur. Nous vous recommandons toujours d'envoyer un message de test à un appareil afin de vous assurer que vos supports, copies, personnalisations et attributs personnalisés génèrent correctement.
{% endalert %}

### Aperçu de la génération des messages dans l'application

Prévisualiser à quoi ressemblera votre message à un utilisateur aléatoire, un utilisateur spécifique, ou un utilisateur personnalisé - les deux derniers sont particulièrement utiles si votre message contient une personnalisation ou plusieurs langues. Vous pouvez également prévisualiser les messages pour les appareils mobiles ou les tablettes pour avoir une meilleure idée de ce que les utilisateurs vont vivre.

!\[In-App_Message_Preview\]\[1\]

Braze a trois générations de messages dans l'application disponibles. Vous pouvez affiner les appareils sur lesquels vos messages doivent être envoyés, en fonction de la génération qu'ils supportent.

!\[In-App_Messages_Generations\]\[2\]{: height="50%" width="50%"}

## Tester

{% alert warning %}
  Pour envoyer un test à [groupes de test de contenu]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) ou à des utilisateurs individuels, le push doit être activé sur vos appareils de test avant l'envoi.
{% endalert %}

### Aperçu du message en tant qu'utilisateur

Vous pouvez également prévisualiser les messages de l’onglet **Test** comme si vous étiez un utilisateur. Vous pouvez sélectionner un utilisateur spécifique, un utilisateur au hasard, ou créer un utilisateur personnalisé.

!\[Custom_User_Preview\]\[3\]

### Test checklist

- Est-ce que les images et les médias apparaissent et agissent comme prévu?
- Est-ce que le Liquid fonctionne comme prévu ? Avez-vous comptabilisé une [valeur d'attribut par défaut]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values) dans le cas où le Liquid ne renvoie aucune information ?
- Votre copie est-elle claire, concise et correcte?
- Est-ce que vos boutons dirigent l'utilisateur où il devrait aller ?
[1]: {%image_buster /assets/img/in-app-message-preview.png %} [2]: {% image_buster /assets/img/iam-generations.gif %} [3]: {% image_buster /assets/img/iam-user-preview.png %}
