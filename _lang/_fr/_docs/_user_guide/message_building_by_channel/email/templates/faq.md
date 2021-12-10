---
nav_title: Foire aux questions
article_title: Modèle de courrier électronique et de lien FAQ
page_order: 5
page_type: Foire Aux Questions
description: "Cette page couvre la foire aux questions sur les modèles d'e-mails et de liens."
tool:
  - Modèles
channel: Email
---

# FAQ sur les modèles d'e-mail et de lien

> Cette page fournit des réponses à certaines questions fréquemment posées sur les modèles de courriels et les modèles de liens.

## Modèles d'e-mail

### Puis-je ajouter un lien "Voir cet e-mail dans un navigateur" à mes courriels?

Non, Braze n'offre pas cette fonctionnalité. Ceci est dû au fait qu'une majorité croissante de courriels est ouverte sur les appareils mobiles et les clients de messagerie modernes, qui rendent les images et le contenu sans aucun problème.

**Solution de contournement :** Pour atteindre ce même résultat, vous pouvez héberger le contenu de votre e-mail sur une page de renvoi externe (comme votre site Web), qui peut ensuite être lié à partir de la campagne d'email que vous construisez en utilisant l'outil **Lien** lors de l'édition du corps du courriel.

### Comment créer un lien de désinscription personnalisé pour mes modèles de courriels?

Il y a une option de redirection pour la page de désinscription.

Vous pouvez changer le lien de désinscription dans le pied de page personnalisé de {% raw %} `{{${set_user_to_unsubscribed_url}}}` {% endraw %} en un lien vers votre propre site web avec un paramètre de requête qui inclut l'identifiant d'utilisateur. Par exemple, quelque chose comme : {% raw %}
> https://www.braze.com/unsubscribe?user_id={{${user_id}}} 
> 
> {% endraw %}

Vous pouvez alors appeler le point de terminaison [Statut de l'e-mail]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/) pour mettre à jour le statut d'abonnement de l'utilisateur. Pour plus de détails, consultez notre documentation sur [le changement du statut d'abonnement aux e-mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions).

### Que se passe-t-il si je modifie un modèle de courriel qui est actuellement utilisé dans une campagne ?

Les modifications apportées à un modèle existant ne seront pas reflétées dans les campagnes qui ont été créées en utilisant les versions précédentes de ce modèle.

## Modèles de lien

### Puis-je télécharger plusieurs modèles de liens dans mon email?

Oui, vous pouvez insérer autant de modèles que vous le souhaitez dans vos courriels. Dans les meilleures pratiques, vous devriez tester vos e-mails pour vous assurer que les liens ne dépassent pas 2, 00 caractères, car la plupart des navigateurs raccourciront ou couperont les liens.

### Comment puis-je prévisualiser mes liens avec toutes les balises appliquées ?

Une fois que vous avez appliqué le modèle de lien, vous pouvez vous envoyer un email de test pour voir tous les liens. De plus, vous pouvez ouvrir les liens depuis le volet de prévisualisation dans un nouvel onglet pour afficher les liens. Enfin, vous pouvez survoler les liens du Panneau de Prévisualisation et les voir en bas de votre navigateur.

### Comment fonctionne le modèle de lien avec le liquide?

Les modèles de liens sont étendus et ajoutés à chaque URL avant toute extension Liquid.

En tant que meilleure pratique, si une partie de votre URL est générée à l'aide d'un extrait de Liquid, nous avons recommandé que la base d'URL et le point d'interrogation (? est codé en dur pour que les modèles de liens soient développés correctement. Refuser d'ajouter le point d'interrogation (?) à votre Liquid, car cela provoquera d'abord l'ajout d'un point d'interrogation (? , puis plus tard, le processus d'extension de Liquid ajoutera un deuxième point d'interrogation (?).