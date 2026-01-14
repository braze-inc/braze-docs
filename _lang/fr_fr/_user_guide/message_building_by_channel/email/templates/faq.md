---
nav_title: FAQ
article_title: "FAQ sur les modèles d'e-mails et de liens"
page_order: 10

page_type: FAQ
description: "Cette page répond aux questions fréquemment posées sur les modèles d'e-mail et les modèles de lien."
tool:
  - Templates
channel: email

---

# Questions fréquemment posées

> Cette page apporte des réponses à certaines questions fréquemment posées sur les modèles d'e-mail et les modèles de lien.

## Modèles d'e-mail

### Puis-je ajouter un lien "afficher cet e-mail dans un navigateur" à mes e-mails ?

Non, Braze n'offre pas cette fonctionnalité. En effet, une majorité croissante d'e-mails est ouverte sur des appareils mobiles et des clients de messagerie modernes, qui restituent les images et le contenu sans problème.

**Solution de contournement :** Pour obtenir le même résultat, vous pouvez héberger le contenu de votre e-mail sur une page de renvoi externe (votre site web, par exemple), à laquelle vous pouvez ensuite vous connecter à partir de la campagne d'e-mails que vous créez à l'aide de l'outil **Lien** lorsque vous modifiez le corps de l'e-mail.

### Comment créer un lien de désabonnement personnalisé pour mes modèles d'e-mail ?

Il existe une option de redirection pour la page de désinscription.

Vous pourriez modifier le lien de désabonnement dans le pied de page personnalisé de {% raw %} `{{${set_user_to_unsubscribed_url}}}` {% endraw %} en un lien vers votre propre site web avec un paramètre de requête qui inclut l'ID de l'utilisateur. En voici un exemple :
{% raw %} 
> https://www.braze.com/unsubscribe?user_id={{${user_id}}}
{% endraw %}

Ensuite, vous pouvez appeler l' [endpoint`/email/status` ]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/) pour mettre à jour le statut de l'abonnement de l'utilisateur. Pour plus de détails, consultez notre documentation sur la [modification de l'état de l'abonnement aux e-mails.]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions)

Pour enregistrer ce nouveau lien, l'étiquette de désabonnement par défaut de Braze {%raw%}(``${set_user_to_unsubscribed_url}``){%endraw%} doit se trouver dans le pied de page. Cela signifie que vous devrez inclure le lien par défaut en le "cachant", soit en plaçant la balise dans un commentaire, soit dans une étiquette cachée `<div>`.

- **Exemple de tags** dans un **commentaire :** mise en place d'un tag dans un commentaire : `<!-- ${set_user_to_unsubscribed_url} -->`
- **Commentaire dans l'exemple de l'étiquette cachée `<div>`:** {%raw%}`<div style="display:none;max-height:0px;overflow:hidden;">${set_user_to_unsubscribed_url}</div>`{%endraw%}

### Que se passe-t-il si je modifie un modèle d'e-mail utilisé dans une campagne ?

Les modifications apportées à un modèle existant ne seront pas répercutées dans les campagnes créées à l'aide de versions antérieures de ce modèle. Pour les campagnes API qui utilisent un modèle dans le corps de l'API REST, Braze utilisera la dernière version du modèle au moment de l'envoi.  

## Modèles de liens

### Puis-je télécharger plusieurs modèles de liens dans mon e-mail ?

Oui, vous pouvez insérer autant de modèles que vous le souhaitez dans vos messages e-mail. En guise de bonne pratique, vous devriez tester vos e-mails pour vous assurer que les liens ne dépassent pas 2 000 caractères, car la plupart des navigateurs raccourcissent ou coupent les liens.

### Comment puis-je prévisualiser mes liens avec toutes les étiquettes appliquées ?

Il existe plusieurs façons de prévisualiser vos liens. Après avoir appliqué le [modèle de lien]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_template/), vous pouvez vous envoyer un [e-mail de test]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages/) pour visualiser tous les liens. 

Depuis le volet de prévisualisation dans un nouvel onglet, vous pouvez également ouvrir les liens pour les visualiser. Vous pouvez également survoler les liens dans le volet de prévisualisation et les voir apparaître en bas de votre navigateur.

### Comment fonctionne le modèle de lien avec Liquid ?

Les modèles de liens sont développés et ajoutés à chaque URL avant toute expansion de liquide. Si une partie de votre URL est générée à l'aide d'un extrait de code Liquid, nous vous recommandons de coder en dur la base de l'URL et le point d'interrogation ( ?) pour que les modèles de liens soient correctement développés. 

Évitez d'ajouter le point d'interrogation ( ?) à votre liquide, car les modèles de liens ajouteront d'abord un point d'interrogation ( ?), puis le processus d'expansion du liquide ajoutera un deuxième point d'interrogation ( ?).

## Aliasage de lien

### Quel sera l'impact de l'activation de l'aliasage de lien sur mes blocs de contenu et mes modèles de liens ?

Pour tous les nouveaux blocs de contenu créés, l'aliasage de lien est appliqué à tous les espaces de travail puisqu'il s'agit d'une fonctionnalité au niveau de l'entreprise. 

Les blocs de contenu existants ne seront pas modifiés lorsque l'aliasage de lien est activé. Les modèles de liens existants ne seront pas modifiés, mais la section du modèle de lien existant dans un message sera supprimée. Pour plus d'informations, consultez la rubrique [Aliasage de liens dans les blocs de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_aliasing/#link-aliasing-in-content-blocks).

### Puis-je utiliser la logique conditionnelle Liquid entièrement à l'intérieur d'une étiquette d'ancrage HTML ?

Non, l'aliasage de lien de Braze ne reconnaîtra pas correctement le HTML. 

Lorsque ce type de logique est utilisé en tandem avec des fonctionnalités qui doivent analyser le code HTML (telles qu'un accroche ou un modèle de lien), la bibliothèque utilisée pour analyser le code HTML peut modifier l'étiquette d'ancrage d'une manière qui empêchera la création du modèle `href` approprié. La bibliothèque déterminera alors que le code HTML n'est pas valide parce qu'elle est indifférente au code Liquid. 

Au lieu de cela, utilisez une logique Liquid qui contient une étiquette d'ancrage complète à chaque étape. Cela n'interférera pas avec l'analyse HTML car la logique comprend plusieurs instances de HTML valide. Vous pouvez également simplifier votre logique en assignant puis en plaçant une variable dans l'étiquette d'ancrage appropriée.
