---
nav_title: "Formulaire d'inscription par e-mail"
article_title: "Formulaire d'inscription par e-mail"
alias: "/email_capture/"
description: "Cette page de référence explique comment créer un formulaire d'inscription par e-mail à l'aide de l'éditeur glisser-déposer de messages in-app."
---

# Formulaire d'inscription par e-mail

> Utilisez le modèle de message in-app d'inscription par e-mail par glisser-déposer pour collecter les adresses e-mail des utilisateurs et développer vos groupes d'abonnement.

## Exigences SDK

### Versions minimales du SDK

Les messages créés à l'aide de l'éditeur par glisser-déposer ne peuvent être envoyés qu'aux utilisateurs des versions minimales suivantes du SDK. Consultez la section [Prérequis][1] de l'article [Création d'un message in-app par glisser-déposer]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/) pour plus de détails et de nuances à connaître.

{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}

### Versions du SDK pour les liens de texte

Si vous souhaitez inclure des liens de texte qui ne ferment pas le message, les utilisateurs doivent disposer des versions minimales suivantes du SDK :

{% sdk_min_versions swift:6.2.0 android:26.0.0 %}

{% alert warning %}
Si vous incluez dans votre message in-app un lien qui redirige vers une URL et que l'utilisateur ne dispose pas des versions minimales du SDK spécifiées, le fait de cliquer sur le lien fermera le message et l'utilisateur ne pourra pas revenir dans le message pour soumettre le formulaire.
{% endalert %}

## Création d'un formulaire d'inscription par e-mail

Lorsque vous créez un message in-app par glisser-déposer, sélectionnez **Inscription par e-mail** pour votre modèle et sélectionnez **Créer un message.** Ce modèle est pris en charge à la fois pour les applications mobiles et les navigateurs web.

### Étape 1 : Définissez les styles de vos messages

Avant de commencer à personnaliser votre modèle, vous pouvez définir des styles au niveau du message pour l'ensemble du message à l'aide du menu latéral. Par exemple, vous pouvez personnaliser la police de tout le texte ou la couleur de tous les liens inclus dans votre message. Vous pouvez également faire en sorte que le message s'affiche sous forme de fenêtre modale ou en plein écran.

### Étape 2 : Personnalisez votre composant d'inscription à l'e-mail

Pour commencer à créer votre formulaire d'inscription par e-mail, sélectionnez l'élément de capture d'e-mail dans l'éditeur. Par défaut, les adresses e-mail collectées auront le groupe d'abonnement global **Abonné**. Pour abonner des utilisateurs à des groupes d'abonnement spécifiques, reportez-vous à la section [Mise à jour des états d'abonnement à l'e-mail.]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#updating-email-subscription-states)

Vous pouvez personnaliser le texte substitutif et le texte de l'étiquette de l'élément de capture d'e-mail.

#### Validation de l’e-mail

Si l'utilisateur saisit une adresse e-mail contenant des caractères spéciaux non acceptés, il verra apparaître un indicateur d'erreur générique et ne pourra pas soumettre le formulaire. Ce message d'erreur n'est pas personnalisable. Vous pouvez visualiser le comportement de l'erreur dans l'onglet **Prévisualisation et test** et sur votre appareil de test. Pour en savoir plus sur la manière dont Braze formate les adresses e-mail, consultez la rubrique [Validation de l'e-mail.]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/email_validation/)

### Étape 3 : Ajouter une clause de non-responsabilité (facultatif)

Nous vous recommandons d'inclure dans votre message des termes d'abonnement et des liens vers la politique de confidentialité et les conditions générales de votre marque. Nous avons fourni une marque substitutive dans le modèle uniquement à titre d'exemple, mais elle ne doit pas être utilisée à des fins de conformité. Veillez à collaborer avec votre équipe juridique pour élaborer un langage adapté à votre marque spécifique.

{% alert note %}
Les meilleures pratiques en matière de livrabilité dépassent souvent les exigences légales, et notre recommandation est de toujours obtenir un consentement explicite pour l'envoi d'e-mails et de permettre aux utilisateurs de refuser facilement.
{% endalert %}

### Étape 4 : Donnez du style à votre message

Vous pouvez personnaliser l'aspect et la convivialité de votre message à l'aide des [composants de messages in-app][3] par glisser-déposer.

## Reporting

Une fois votre campagne lancée, vous pouvez analyser les résultats en temps réel pour savoir combien d'utilisateurs se sont engagés dans votre campagne. Pour savoir combien d'utilisateurs ont opté pour le groupe d'abonnement, vous pouvez [créer un segment][5] des utilisateurs qui se sont abonnés au groupe d'abonnement en filtrant les utilisateurs qui ont reçu le message in-app et qui ont abonné le formulaire.

## Bonnes pratiques

### Double vérification pour les abonnements

Pour vous assurer que toute personne qui s'est inscrite à votre liste voulait s'inscrire à votre liste et a fourni l'adresse e-mail correcte, nous vous recommandons d'obtenir une seconde confirmation de la part de toute personne qui s'est inscrite via votre formulaire d'inscription par e-mail en envoyant un flux de [double-opt-in](https://www.braze.com/resources/articles/embracing-the-email-double-opt-in).

L'une des façons de procéder consiste à utiliser Canvas Flow :

1. Créez un canvas basé sur l'action et configurez-le pour qu'il se déclenche lorsqu'un utilisateur ajoute une adresse e-mail à Braze. Assurez-vous de permettre le ciblage des utilisateurs qui découvrent la plateforme (par exemple, en utilisant un segment sans filtre dans le Canvas).
2. Créez une étape de message e-mail avec un CTA qui comporte un lien hypertexte vers l'étiquette Liquid de {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %}. L'état de l'abonnement à l'e-mail de l'utilisateur passera ainsi à `opted_in` lorsqu'il cliquera sur le bouton.
3. Ajoutez une [étape de parcours d'action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths#action-paths).
4. Pour le premier parcours, déclenchez un e-mail lorsqu'un utilisateur modifie son statut d'abonnement aux e-mails sur `opted_in`. Cet e-mail doit informer les utilisateurs que leur e-mail a été confirmé.
5. Mettez en place l'autre voie de sortie de la toile après l'expiration de la fenêtre.

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/#prerequisites
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/#drag-and-drop-in-app-message-components
[5]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/
