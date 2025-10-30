{% if include.section == "SDK requirements" %}

## Conditions préalables

### Versions minimales du SDK

Les messages créés à l'aide de l'éditeur par glisser-déposer ne peuvent être envoyés qu'aux utilisateurs des versions minimales suivantes du SDK. Pour plus d'informations, voir [Créer un message in-app par glisser-déposer : Prérequis]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/#prerequisites).

{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}

### Versions du SDK pour les liens de texte

Pour inclure des liens de texte qui ne renvoient pas le message, les versions minimales suivantes du SDK sont nécessaires :

{% sdk_min_versions swift:6.2.0 android:26.0.0 %}

{% alert warning %}
Si vous incluez dans votre message in-app un lien qui redirige vers une URL et que l'utilisateur ne dispose pas des versions minimales du SDK spécifiées, le fait de cliquer sur le lien fermera le message et l'utilisateur ne pourra pas revenir dans le message pour soumettre le formulaire.
{% endalert %}

{% endif %}

{% if include.section == "message style" %}

Avant de commencer à personnaliser votre modèle, vous pouvez définir des styles au niveau du message pour l'ensemble du message à l'aide du menu latéral. Par exemple, vous pouvez personnaliser la police de tout le texte ou la couleur de tous les liens inclus dans votre message. Vous pouvez également faire en sorte que le message s'affiche sous forme de fenêtre modale ou en plein écran.

{% endif %}


<!-- Add this below after the disclaimers are added to all email sign-up templates: "We have provided a placeholder disclaimer in the template solely as an example, but this should not be relied upon for compliance purposes."-->

{% if include.section == "email disclaimer" %}

Nous vous recommandons d'inclure dans votre message des termes d'abonnement et des liens vers la politique de confidentialité et les conditions générales de votre marque. Veillez à collaborer avec votre équipe juridique pour élaborer un langage adapté à votre marque spécifique.

{% alert note %}
Les meilleures pratiques en matière de livrabilité dépassent souvent les exigences légales, et notre recommandation est de toujours obtenir un consentement explicite pour l'envoi d'e-mails et de permettre aux utilisateurs de refuser facilement.
{% endalert %}

{% endif %}

{% if include.section == "email validation" %}

Si l'utilisateur saisit une adresse e-mail contenant des caractères spéciaux non acceptés, il verra apparaître un indicateur d'erreur générique et ne pourra pas soumettre le formulaire. Ce message d'erreur n'est pas personnalisable. Vous pouvez visualiser le comportement de l'erreur dans l'onglet **Prévisualisation et test** et sur votre appareil de test. Pour en savoir plus sur la manière dont Braze formate les adresses e-mail, consultez la rubrique [Validation de l'e-mail.]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/email_validation/)

{% endif %}

{% if include.section == "email double opt-in" %}

### Double vérification pour les abonnements

Pour vous assurer que toute personne qui s'est inscrite à votre liste voulait s'inscrire à votre liste et a fourni l'adresse e-mail correcte, nous vous recommandons d'obtenir une seconde confirmation de la part de toute personne qui s'est inscrite via votre formulaire d'inscription par e-mail en envoyant un flux de [double-opt-in](https://www.braze.com/resources/articles/embracing-the-email-double-opt-in).

L'un des moyens d'y parvenir est d'utiliser Canvas :

1. Créez un canvas basé sur l'action et configurez-le pour qu'il se déclenche lorsqu'un utilisateur ajoute une adresse e-mail à Braze. Assurez-vous de permettre le ciblage des utilisateurs qui découvrent la plateforme (par exemple, en utilisant un segment sans filtre dans le Canvas).
2. Créez une étape de message e-mail avec un CTA qui comporte un lien hypertexte vers l'étiquette Liquid de {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %}. L'état de l'abonnement à l'e-mail de l'utilisateur passera ainsi à `opted_in` lorsqu'il cliquera sur le bouton.
3. Ajoutez une [étape de parcours d'action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths#action-paths).
4. Pour le premier parcours, déclenchez un e-mail lorsqu'un utilisateur modifie son statut d'abonnement aux e-mails sur `opted_in`. Cet e-mail doit informer les utilisateurs que leur e-mail a été confirmé.
5. Mettez en place l'autre voie de sortie de la toile après l'expiration de la fenêtre.

{% endif %}

{% if include.section == "reporting" %}

Une fois votre campagne lancée, vous pouvez analyser les résultats en temps réel pour savoir combien d'utilisateurs se sont engagés dans votre campagne. Pour savoir combien d'utilisateurs ont opté pour le groupe d'abonnement, vous pouvez [créer un segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) des utilisateurs qui se sont abonnés au groupe d'abonnement en filtrant les utilisateurs qui ont reçu le message in-app et qui ont abonné le formulaire.

{% endif %}