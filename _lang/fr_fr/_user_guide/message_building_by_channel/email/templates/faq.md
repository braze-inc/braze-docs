---
nav_title: FAQ
article_title: FAQ sur les modèles d’e-mails et de liens
page_order: 10

page_type: FAQ
description: "Cette page répond aux questions fréquemment posées sur les modèles d’e-mail et de lien."
tool:
  - Templates
channel: email

---

# Foire aux questions

> Cette page répond à certaines questions fréquemment posées sur les modèles d’e-mail et de lien.

## Modèles d'e-mail

### Puis-je ajouter un lien « Afficher cet e-mail dans un navigateur » à mes e-mails ?

Non, Braze n’offre pas cette fonctionnalité. C’est parce qu’une majorité croissante d’e-mails sont ouverts sur des appareils mobiles et des clients par e-mail modernes, qui rendent les images et le contenu sans aucun problème.

**Contournement :** Pour obtenir le même résultat, vous pouvez héberger le contenu de votre e-mail sur une page de destination externe (comme votre site Web), qui peut ensuite être liée à partir de la campagne e-mail que vous construisez en utilisant l'outil **Link** lors de l'édition du corps de l'e-mail.

### Comment créer un lien de désabonnement personnalisé pour mes modèles d’e-mail ?

Il existe une option de redirection pour la page de désinscription.

Vous pourriez changer le lien de désabonnement dans le pied de page personnalisé de {% raw %} `{{${set_user_to_unsubscribed_url}}}` {% endraw %} à un lien vers votre propre site web avec un paramètre de requête qui inclut l'ID de l'utilisateur. Voici un exemple :
{% raw %} 
> https://www.braze.com/unsubscribe?user_id={{${user_id}}}
{% endraw %}

Ensuite, vous pourriez appeler l’endpoint [`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/) pour mettre à jour le statut d'abonnement de l'utilisateur. Pour plus de détails, consultez notre documentation sur [la modification du statut d'abonnement par e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions).

Pour enregistrer ce nouveau lien, le tag de désabonnement Braze par défaut {%raw%}(``${set_user_to_unsubscribed_url}``){%endraw%} doit être dans le pied de page. Cela signifie que vous devrez inclure le lien par défaut en le "cachant" en plaçant soit la balise dans un commentaire, soit dans une balise cachée `<div>`.

- **Exemple de balise dans un commentaire :** mettre une balise dans un exemple de commentaire : `<!-- ${set_user_to_unsubscribed_url} -->`
- **Commentaire dans l'exemple de balise cachée `<div>` :** {%raw%}`<div style="display:none;max-height:0px;overflow:hidden;">${set_user_to_unsubscribed_url}</div>`{%endraw%}

### Que se passe-t-il si je modifie un modèle d’e-mail actuellement utilisé dans une campagne ?

Les modifications apportées à un modèle existant ne seront pas reflétées dans les campagnes créées qui utilisent les versions précédentes de ce modèle. Pour les campagnes API qui utilisent un modèle dans le corps de l'API REST, Braze utilisera la dernière version du modèle au moment de l'envoi.  

## Modèles de lien

### Puis-je télécharger plusieurs modèles de lien dans mon e-mail ?

Oui, vous pouvez insérer autant de modèles que vous le souhaitez dans vos e-mails. En tant que meilleure pratique, vous devez tester vos e-mails pour vous assurer que les liens ne dépassent pas 2 000 caractères car la plupart des navigateurs raccourcissent ou coupent les liens.

### Comment puis-je prévisualiser mes liens avec toutes les balises appliquées ?

Plusieurs manières de prévisualiser vos liens existent. Après avoir appliqué le [modèle de lien]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_template/), vous pouvez envoyer un [e-mail de test]({{site.baseurl}}/developer_guide/sending_test_messages/) à vous-même pour voir tous les liens. 

Vous pouvez ouvrir les liens depuis le volet d’aperçu dans un nouvel onglet pour les afficher. Vous pouvez également survoler les liens dans le volet d'aperçu et les voir en bas de votre navigateur.

### Comment le modèle de lien fonctionne-t-il avec Liquid ?

Les modèles de lien sont étendus et ajoutés à chaque URL avant toute extension de Liquid. Si une partie de votre URL est générée à l'aide d'un extrait de code Liquid, nous vous recommandons de coder en dur la base de l'URL et le point d'interrogation ( ?) pour que les modèles de liens soient correctement développés. 

Évitez d’ajouter un point d’interrogation (?) à votre Liquid, sinon les modèles de liens ajouteront un point d’interrogation (?) et le processus d’extension de Liquid en ajoutera un deuxième.

## Aliasage de lien

### Quel est l’impact de l’activation de l’aliasage de lien sur mes modèles de blocs de contenu et de liens ?

Pour tous les nouveaux blocs de contenu créés, l'alias de lien est appliqué dans tous les espaces de travail, car il s'agit d'une fonctionnalité au niveau de l'entreprise. 

Les blocs de contenu existants ne seront pas modifiés lorsque l’aliasage de lien est activé. Même si les modèles de lien ne seront pas modifiés, la section existante de modèle de lien d’un message sera supprimée. Consultez [l'aliasage de lien dans les blocs de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_aliasing/#link-aliasing-in-content-blocks) pour plus d'informations.

### Puis-je utiliser la logique conditionnelle Liquid entièrement dans une balise d'ancrage HTML ?

Non, l'aliasage de lien Braze ne reconnaîtra pas correctement le HTML. 

Lorsque cette logique est utilisée en tandem avec des fonctionnalités qui doivent analyser le HTML (comme un pré-en-tête ou un modèle de lien), la bibliothèque utilisée pour scanner le HTML peut modifier la balise d'ancrage d'une manière qui empêchera le bon `href` d'être modélisé. La bibliothèque déterminera alors que le HTML est invalide car il est agnostique au code Liquid. 

Au lieu de cela, utilisez une logique Liquid qui contient une balise d'ancrage complète à chaque étape. Cela n'interférera pas avec l'analyse HTML car la logique inclut plusieurs instances de HTML valide. Vous pouvez également simplifier votre logique en assignant puis en modélisant une variable dans la balise d'ancrage appropriée.
