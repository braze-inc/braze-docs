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

**Contournement :** Pour obtenir ce même résultat, vous pouvez héberger le contenu de votre e-mail sur une page d’accueil externe (comme votre site Internet), qui peut ensuite être lié à la campagne par e-mail que vous construisez à l’aide de l’outil **Link (Lien)** lors de la modification du corps de l’email.

### Comment créer un lien de désabonnement personnalisé pour mes modèles d’e-mail ?

Il existe une option de redirection pour la page de désinscription.

Vous pouvez modifier le lien de désabonnement dans le pied de page personnalisé depuis {% raw %} `{{${set_user_to_unsubscribed_url}}}` {% endraw %} un lien vers votre propre site Internet avec un paramètre de requête incluant l’ID utilisateur. Comme par exemple : 
{% raw %} 
> https://www.braze.com/unsubscribe?user_id={{${user_id}}}
{% endraw %}

Ensuite, vous pouvez appeler l’endpoint [email status (statut de l’e-mail)]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/) pour mettre à jour le statut d’abonnement de l’utilisateur. Pour plus de détails, consultez notre documentation sur la [modification du statut d’abonnement aux e-mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions).

### Que se passe-t-il si je modifie un modèle d’e-mail actuellement utilisé dans une campagne ?

Les modifications apportées à un modèle existant ne seront pas reflétées dans les campagnes créées qui utilisent les versions précédentes de ce modèle.

## Modèles de lien

### Puis-je télécharger plusieurs modèles de lien dans mon e-mail ?

Oui, vous pouvez insérer autant de modèles que vous le souhaitez dans vos e-mails. En tant que meilleure pratique, vous devez tester vos e-mails pour vous assurer que les liens ne dépassent pas 2 000 caractères car la plupart des navigateurs raccourcissent ou coupent les liens.

### Comment puis-je prévisualiser mes liens avec toutes les balises appliquées ?

Plusieurs manières de prévisualiser vos liens existent. Une fois que vous avez appliqué le [modèle de lien]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_template/), vous pouvez vous envoyer un [e-mail de test]({{site.baseurl}}/developer_guide/platform_wide/sending_test_messages/) pour afficher tous les liens. 

Vous pouvez ouvrir les liens depuis le volet d’aperçu dans un nouvel onglet pour les afficher. Enfin, vous pouvez survoler les liens dans le volet d’aperçu et les afficher au bas de votre navigateur.

### Comment le modèle de lien fonctionne-t-il avec Liquid ?

Les modèles de lien sont étendus et ajoutés à chaque URL avant toute extension de Liquid. Si une partie de votre URL est générée à l’aide d’un extrait de code Liquid, nous vous recommandons de coder en dur la base d’URL et le point d’interrogation (?) pour que les modèles de liens soient étendus correctement. 

Évitez d’ajouter un point d’interrogation (?) à votre Liquid, sinon les modèles de liens ajouteront un point d’interrogation (?) et le processus d’extension de Liquid en ajoutera un deuxième.

## Aliasage de lien

### Quel est l’impact de l’activation de l’aliasage de lien sur mes modèles de blocs de contenu et de liens ?

Pour tous les nouveaux blocs de contenu créés, l’aliasage de lien est appliqué sur tous les groupes d’apps étant donné qu’il s’agit d’une fonctionnalité au niveau de l’entreprise. Les blocs de contenu existants ne seront pas modifiés lorsque l’aliasage de lien est activé. Même si les modèles de lien ne seront pas modifiés, la section existante de modèle de lien d’un message sera supprimée. Consultez l’[aliasage de lien dans les blocs de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_aliasing/#link-aliasing-in-content-blocks) pour plus d’informations.

