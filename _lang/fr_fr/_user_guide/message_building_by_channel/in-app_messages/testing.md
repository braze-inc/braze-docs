---
nav_title: Essais
article_title: Test des messages in-app
page_order: 4.5
description: "Cet article de référence explique la valeur des messages in-app, comment les tester, ainsi qu'une liste de contrôle des éléments à prendre en compte avant l'envoi."
channel:
  - in-app messages
  
---

# Tests des messages in-app

> Il est extrêmement important de toujours tester vos messages in-app avant d'envoyer vos campagnes. Nos fonctionnalités de prévisualisation et de test offrent deux façons de jeter un coup d'œil à vos messages in-app. Vous pouvez prévisualiser votre message, pour vous aider à le visualiser pendant que vous le composez, et envoyer un message test à votre appareil ou à celui d'un utilisateur spécifique. Nous vous recommandons de profiter des deux.

## Avant-première

Vous pouvez prévisualiser votre message in-app au fur et à mesure que vous le rédigez. Cela devrait vous aider à visualiser ce à quoi ressemblera votre message final du point de vue de l'utilisateur.

{% alert warning %}
Dans l **'aperçu**, l'affichage de votre message peut ne pas être identique à son rendu réel sur l'appareil de l'utilisateur. Nous vous recommandons toujours d'envoyer un message test à un appareil pour vous assurer que vos médias, votre texte, votre personnalisation et vos attributs personnalisés sont générés correctement.
{% endalert %}

### Aperçu de la génération de messages in-app

Prévisualisez l'aspect de votre message pour un utilisateur aléatoire, un utilisateur spécifique ou un utilisateur personnalisé. Ces deux dernières options sont particulièrement utiles si votre message contient des éléments de personnalisation ou plusieurs langues. Vous pouvez également prévisualiser les messages pour les appareils mobiles ou les tablettes afin d'avoir une meilleure idée de l'expérience des utilisateurs.

!L'onglet Composer lors de la création d'un message in-app affiche un aperçu de ce à quoi ressemblera le message. Un utilisateur n'est pas sélectionné, de sorte que le Liquid ajouté dans la section body s'affiche comme is.]({%image_buster /assets/img/in-app-message-preview.png %})

Braze propose trois générations d'envois de messages in-app. Vous pouvez déterminer avec précision les appareils auxquels vos messages doivent être envoyés, en fonction de la génération qu'ils prennent en charge.

!Passage d'une génération à l'autre lors de la prévisualisation d'un message in-app.]({% image_buster /assets/img/iam-generations.gif %}){: height="50%" width="50%"}

## Test

{% alert warning %}
Pour envoyer un test à des [groupes de test de contenu]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) ou à des utilisateurs individuels, la fonction push doit être activée sur vos appareils de test avant l'envoi. <br><br>Par exemple, vous devez avoir activé le push sur votre appareil iOS pour pouvoir appuyer sur la notification avant l'affichage du message de test.
{% endalert %}

### Prévisualisation du message en tant qu'utilisateur

Vous pouvez également prévisualiser les messages à partir de l'onglet **Test**, comme si vous étiez un utilisateur. Vous pouvez sélectionner un utilisateur spécifique, un utilisateur aléatoire ou créer un utilisateur personnalisé.

!Tester l'onglet lorsque vous créez un message in-app. L'option "Prévisualiser le message en tant qu'utilisateur" est réglée sur "Utilisateur personnalisé", les champs de profil disponibles apparaissant sous forme d'options configurables.]({% image_buster /assets/img/iam-user-preview.png %})

{% alert important %}
Les envois test peuvent entraîner l'envoi de plusieurs messages in-app à chaque destinataire.
{% endalert %}

### Liste de contrôle des tests

- Les images et les médias apparaissent-ils et agissent-ils comme prévu ?
- Le liquide fonctionne-t-il comme prévu ? Avez-vous prévu une [valeur d'attribut par défaut]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values) au cas où le liquide ne renverrait aucune information ?
- Votre texte est-il clair, concis et correct ?
- Vos boutons indiquent-ils à l'utilisateur la direction à prendre ?

## Scanner d'accessibilité

Pour soutenir les meilleures pratiques en matière d'accessibilité, Braze analyse automatiquement le contenu des messages in-app créés à l'aide de l'éditeur HTML traditionnel par rapport aux normes d'accessibilité. Ce scanner permet d'identifier les contenus susceptibles de ne pas répondre aux normes[WCAG (](https://www.w3.org/WAI/standards-guidelines/wcag/)Web Content Accessibility Guidelines). Les WCAG sont un ensemble de normes techniques internationalement reconnues, élaborées par le World Wide Web Consortium (W3C) pour rendre le contenu des sites web plus accessible aux personnes handicapées.

\![Résultats de l'analyse d'accessibilité]({% image_buster /assets/img/Accessibilty_Scanner_IAM.png %})

{% alert note %}
L'analyseur d'accessibilité des messages in-app ne fonctionne que sur les messages créés avec du HTML personnalisé.
{% endalert %}

### Comment cela fonctionne-t-il ?

Le scanner s'exécute automatiquement sur les messages HTML personnalisés et évalue l'ensemble de votre message HTML par rapport à l'[ensemble des règles WCAG 2.1 AA.](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.1&currentsidebar=%23col_customize&levels=aaa) Pour chaque problème signalé, il indique

- L'élément HTML spécifique concerné
- Une description du problème d'accessibilité
- Un lien vers un contexte supplémentaire ou des conseils de remédiation

### Comprendre les tests d'accessibilité automatisés

{% multi_lang_include accessibility/automated_testing.md %}





