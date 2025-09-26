---
nav_title: "Pied de page personnalisé pour l'e-mail"
article_title: "Pied de page personnalisé pour l'e-mail"
page_order: 6.5
description: "Cet article explique comment configurer un pied de page d'e-mail personnalisé à l'échelle de l'espace de travail."
channel:
  - email

---

# Pied de page personnalisé pour les e-mails

> Vous pouvez définir un pied de page d'e-mail personnalisé pour l'ensemble de votre espace de travail, que vous pouvez intégrer dans chaque e-mail à l'aide de l'attribut Liquid {% raw %}`{{${email_footer}}}`{% endraw %}.

En utilisant des pieds de page d'e-mail personnalisés, vous n'avez plus besoin de créer un nouveau pied de page pour chaque modèle d'e-mail ou campagne d'e-mail que vous utilisez. Les modifications apportées à votre pied de page personnalisé seront reflétées dans toutes les campagnes par e-mail existantes et nouvelles. N'oubliez pas que le respect de la [loi CAN-SPAM de 2003](https://www.ftc.gov/tips-advice/business-center/guidance/can-spam-act-compliance-guide-business) vous oblige à inclure une adresse physique pour votre entreprise et un lien de désabonnement dans vos e-mails.

{% alert warning %}
Il est de votre responsabilité de vous assurer que votre pied de page personnalisé répond aux exigences susmentionnées.
{% endalert %}

## Création de votre pied de page personnalisé

Pour créer ou modifier votre pied de page personnalisé, procédez comme suit :

1. Allez dans **Paramètres** > **Préférences e-mail.**
2. Allez dans la section **Pied de page personnalisé** et activez les pieds de page personnalisés.
3. Modifiez votre pied de page dans la section **Composer**.
4. Envoyez un message test. 

![Exemple de pied de page personnalisé.]({% image_buster /assets/img_archive/custom_footer.png %})

Le pied de page par défaut utilise l'attribut {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} et notre adresse postale. Si vous utilisez cette option par défaut, veillez à sélectionner **<autre>** pour le **protocole**.

{% alert important %}
Pour être conforme à la réglementation CAN-SPAM, votre pied de page personnalisé doit inclure {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %}. Vous ne pourrez pas enregistrer un pied de page personnalisé sans cet attribut.
{% endalert %}

![Valeurs de protocole et d'URL nécessaires pour le pied de page personnalisé.]({% image_buster /assets/img_archive/email_unsub_protocol.png %}){: style="max-width:50%;"}

## Pieds de page sans liens de désabonnement

Soyez très prudent lorsque vous utilisez un modèle avec le pied de page personnalisé {% raw %}`{{${email_footer}}}` mais sans l'étiquette de lien de désabonnement `{{${set_user_to_unsubscribed_url}}}`{% endraw %}. Un avertissement apparaîtra, mais vous aurez le choix d'envoyer un e-mail avec ou sans lien de désabonnement.

Voici un avertissement dans le compositeur de l'e-mail :

![Exemple d'e-mail composé sans pied de page.]({% image_buster /assets/img_archive/no_unsub_link_warning.png %})

Voici un avertissement dans le compositeur de la campagne :

![Composition de la campagne No-Footer.]({% image_buster /assets/img_archive/no_footer_test.png %})

### Ajouter un lien de désinscription personnalisé

Pour ajouter un lien de désabonnement personnalisé, vous pouvez modifier le lien de désabonnement dans le pied de page personnalisé de {% raw %} `{{${set_user_to_unsubscribed_url}}}` {% endraw %} en un lien vers votre propre site web avec un paramètre de requête qui inclut l'ID de l'utilisateur. Voici un exemple :
{% raw %} 
> https://www.braze.com/unsubscribe?user_id={{${user_id}}}
{% endraw %}

Ensuite, appelez l' [endpoint`/email/status` ]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/) pour mettre à jour le statut de l'abonnement de l'utilisateur. Pour plus de détails, consultez notre documentation sur [la modification du statut d'abonnement par e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions).

Ensuite, enregistrez ce nouveau lien. L'étiquette de désabonnement par défaut de Braze {%raw%}(``${set_user_to_unsubscribed_url}``){%endraw%} doit se trouver dans le pied de page. Cela signifie que vous devez inclure le lien par défaut en le "cachant", soit en plaçant la balise dans un commentaire, soit dans une étiquette cachée `<div>`.

## Bonnes pratiques

Nous vous conseillons de suivre les meilleures pratiques suivantes lors de la création et de l'utilisation de pieds de page personnalisés.

### Personnalisation avec des attributs

Lors de la création d'un pied de page personnalisé, Braze suggère d'utiliser des [attributs pour la personnalisation]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/). L’ensemble complet des attributs personnalisés et par défaut est disponible, mais en voici quelques-uns que vous pourriez trouver utiles :

| Attribut | Balise |
| --------- | --- |
| Adresse e-mail de l’utilisateur | {% raw %}`{{${email_address}}}`{% endraw %} |
| URL personnalisée de désabonnement de l’utilisateur | {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} <br><br>Cette étiquette remplace l'ancienne étiquette {% raw %}`{{${unsubscribe_url}}}`{% endraw %}. Nous vous recommandons d'utiliser plutôt l'étiquette plus récente {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %}. |
| URL personnalisée d’abonnement de l’utilisateur | {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %} |
| URL personnalisée d’abonnement de l’utilisateur | {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}|
| URL personnalisé du centre de préférences de Braze de l'utilisateur | {% raw %}`{{${preference_center_url}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Insertion d’un lien de désabonnement et d’un lien d'abonnement

{% raw  %}
En tant que meilleure pratique, Braze recommande d'inclure à la fois un lien de désabonnement (tel que ``{{${set_user_to_unsubscribed_url}}}``) et un lien d'abonnement (tel que ``{{${set_user_to_opted_in_url}}}``) dans votre pied de page personnalisé. De cette façon, les utilisateurs pourront s’abonner ou se désabonner, et vous pourrez collecter de façon passive les données d’abonnement pour une partie de vos utilisateurs.
{% endraw %}

### Définition de pieds de page personnalisés pour les e-mails en texte clair

Vous pouvez également choisir de définir un pied de page personnalisé pour les e-mails en texte clair à partir de l'onglet **Pages et pieds de page d'abonnement** de la page **Préférences d'e-mail**, qui suit les mêmes règles que le pied de page personnalisé pour les e-mails HTML. 

Si vous n’ajoutez pas de pied de page en texte brut, Braze en créera automatiquement un à partir du pied de page HTML. Lorsque vos pieds de page personnalisés sont à votre goût, sélectionnez **Enregistrer.**

![E-mail avec l'option Set Custom Plaintext Footer sélectionnée.]({% image_buster /assets/img_archive/custom_footer_save_changes.png %}){: style="max-width:70%" }

