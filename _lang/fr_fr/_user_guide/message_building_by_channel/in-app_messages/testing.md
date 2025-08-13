---
nav_title: Test
article_title: Test des messages in-app
page_order: 4.5
description: "Cet article de référence explique pourquoi vous devriez tester vos messages in-app, comment les tester, et présente une liste de points à prendre en compte avant l’envoi."
channel:
  - in-app messages
  
---

# Tester des messages in-app

> Il est extrêmement important de toujours tester vos messages in-app avant d’envoyer vos campagnes. Nos fonctions d’aperçu et de test offrent deux façons de consulter vos messages in-app. Vous pouvez prévisualiser votre message pour vous guider lorsque vous le composez, ainsi qu’envoyer un message test à votre appareil ou à celui d’un utilisateur spécifique. Nous vous recommandons d’utiliser les deux.

## Aperçu

Vous pouvez prévisualiser votre message in-app lorsque vous le composez. Cela devrait vous aider à visualiser à quoi ressemblera votre message final du point de vue de l’utilisateur.

{% alert warning %}
Dans l **'aperçu**, l'affichage de votre message peut ne pas être identique à son rendu réel sur l'appareil de l'utilisateur. Nous vous recommandons toujours d’envoyer un message test à un appareil pour vous assurer que vos données, le texte, la personnalisation et les attributs personnalisés se génèrent correctement.
{% endalert %}

### Aperçu de génération de messages in-app

Prévisualisez l’apparence de votre message pour un utilisateur aléatoire, un utilisateur spécifique ou un utilisateur personnalisé, les deux derniers étant particulièrement utiles si votre message inclut une personnalisation ou plusieurs langues. Vous pouvez également prévisualiser les messages pour les appareils mobiles ou les tablettes afin d’avoir une meilleure idée de l’expérience des utilisateurs.

![Onglet Compose (Composer) lors de la création d’un message in-app montrant l’aperçu de son apparence. Aucun utilisateur n'est sélectionné, de sorte que le liquide ajouté dans la section du corps s'affiche tel quel.]({%image_buster /assets/img/in-app-message-preview.png %})

Braze dispose de trois générations de messages in-app disponibles. Vous pouvez affiner les appareils auxquels vos messages doivent envoyés, en fonction de la génération qu’ils prennent en charge.

![Passage d'une génération à l'autre lors de la prévisualisation d'un message in-app.]({% image_buster /assets/img/iam-generations.gif %}){: height="50%" width="50%"}

## Test

{% alert warning %}
Pour envoyer un test à des [groupes de test de contenu]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) ou à des utilisateurs individuels, la fonction push doit être activée sur vos appareils de test avant l'envoi. <br><br>Par exemple, vous devez avoir activé les notifications push sur votre appareil iOS pour pouvoir appuyer sur la notification avant que le message de test ne s’affiche.
{% endalert %}

### Aperçu du message en tant qu’utilisateur

Vous pouvez également prévisualiser les messages à partir de l'onglet **Test**, comme si vous étiez un utilisateur. Vous pouvez sélectionner un utilisateur spécifique, un utilisateur aléatoire ou créer un utilisateur personnalisé.

![Onglet Test lors de la création d’un message in-app. L'option "Prévisualiser le message en tant qu'utilisateur" est réglée sur "Utilisateur personnalisé" et les champs de profil disponibles apparaissent en tant qu'options configurables.]({% image_buster /assets/img/iam-user-preview.png %})

### Liste de contrôle des tests

- Les images et les données s’affichent-elles et se comportent-elles comme prévu ?
- Le Liquid fonctionne-t-il comme prévu ? Avez-vous prévu une [valeur d'attribut par défaut]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values) au cas où Liquid ne renverrait aucune information ?
- Votre texte est-il clair, concis et correct ?
- Vos boutons dirigent-ils l’utilisateur à l’endroit correct ?

## Scanner d'accessibilité

Pour soutenir les meilleures pratiques en matière d'accessibilité, Braze analyse automatiquement le contenu des messages in-app créés à l'aide de l'éditeur HTML traditionnel par rapport aux normes d'accessibilité. Ce scanner permet d'identifier les contenus susceptibles de ne pas répondre aux normes[WCAG (](https://www.w3.org/WAI/standards-guidelines/wcag/)Web Content Accessibility Guidelines). Les WCAG sont un ensemble de normes techniques internationalement reconnues, élaborées par le World Wide Web Consortium (W3C) pour rendre le contenu des sites web plus accessible aux personnes handicapées.

![Résultats de l'analyse d'accessibilité]({% image_buster /assets/img/Accessibilty_Scanner_IAM.png %})

{% alert note %}
L'analyseur d'accessibilité des messages in-app ne fonctionne que sur les messages créés avec du HTML personnalisé.
{% endalert %}

### Fonctionnement

Le scanner s'exécute automatiquement sur les messages HTML personnalisés et évalue l'ensemble de votre message HTML par rapport à l'[ensemble des règles WCAG 2.1 AA.](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.1&currentsidebar=%23col_customize&levels=aaa) Pour chaque problème signalé, il indique

- L'élément HTML spécifique concerné
- Une description du problème d'accessibilité
- Un lien vers un contexte supplémentaire ou des conseils de remédiation

### Comprendre les tests d'accessibilité automatisés

{% multi_lang_include accessibility/automated_testing.md %}





