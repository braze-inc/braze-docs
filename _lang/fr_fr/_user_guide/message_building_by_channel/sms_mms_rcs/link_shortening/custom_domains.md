---
nav_title: Domaines personnalisés en libre-service
article_title: Domaines personnalisés en libre-service
page_order: 0
description: "Cette page explique comment utiliser des domaines personnalisés avec le raccourcissement de liens pour personnaliser l'aspect et la convivialité de vos URL raccourcis."
page_type: reference
alias: "/custom_domains/"
tool:
  - Campaigns
channel:
  - SMS
---

# Domaines personnalisés en libre-service

> Cette page explique comment configurer vos propres domaines personnalisés dans le tableau de bord de Braze. Les domaines personnalisés vous permettent d'utiliser un lien raccourci qui reflète l'identité de votre marque au lieu d'un lien raccourci générique ou du domaine Braze (`brz.ai`), ce qui renforce la confiance des utilisateurs et l'engagement envers les campagnes avec des liens SMS.

Les domaines personnalisés en libre-service vous permettent de configurer et de gérer vos propres domaines personnalisés pour les SMS, les RCS et WhatsApp, directement depuis le tableau de bord de Braze. Vous pouvez facilement ajouter, surveiller et gérer jusqu'à 10 domaines personnalisés en un seul endroit.

## Avantages des domaines personnalisés en libre-service

- **Configuration simplifiée :** Veuillez configurer vos domaines sur la page **Paramètres de l'entreprise** afin de réduire le temps de configuration.
- **Amélioration de la transparence :** Recevez des mises à jour en temps réel sur l'état de configuration de votre domaine grâce à des bannières dans le tableau de bord.
- **Notifications proactives :** Recevez des alertes immédiates lorsque votre domaine personnalisé est connecté ou si des erreurs de configuration surviennent.

## Exigences du domaine

- Les domaines doivent être achetés, détenus et gérés par vous. Cela peut être effectué par l'intermédiaire d'un registraire de domaine, tel que GoDaddy, Amazon Route 53 ou Google Domains.
- Le domaine utilisé pour cette fonctionnalité doit être :
  - Unique (différent du domaine de votre site web)
  - Ne peut être utilisé pour héberger du contenu Web.
    - Vous pouvez également utiliser des sous-domaines uniques. Par exemple, le domaine`braze.com`pourrait avoir des sous-domaines tels que`sms.braze.com`ou `whatsapp.braze.com`.

## Déléguer votre domaine personnalisé

Nous vous demandons de déléguer votre domaine personnalisé à Braze afin que nous puissions faciliter le routage approprié et la compatibilité de l'infrastructure avec nos services de raccourcissement de liens et de suivi des clics. Lorsque vous déléguez votre domaine à Braze, nous nous chargeons automatiquement du renouvellement du certificat afin d'éviter toute interruption de service. 

## Ajouter un domaine personnalisé

1. Dans Braze, veuillez vous rendre dans **Paramètres de l'entreprise** > **SMS/RCS et domaines des applications d'envoi de messages**.
![Page « Domaines SMS/RCS et applications d’envoi de messages » avec plusieurs domaines répertoriés.]({% image_buster /assets/img/main_page.png %})

{: start="2"}
2\. Veuillez sélectionner **Ajouter un domaine** pour commencer la configuration d'un nouveau domaine personnalisé.
3\. Veuillez saisir le domaine personnalisé que vous avez acheté dans notre champ de saisie intégré à l'application, qui utilise notre logique de validation existante pour garantir un formatage correct, puis sélectionnez **Suivant** et **Soumettre**.

![Bouton « Ajouter un domaine » sur la page « Domaines SMS/RCS et applications d’envoi de messages ».]({% image_buster /assets/img/custom_domain_button.png %}){: style="max-width:70%;"}

{: start="4"}
4\. Veuillez demander à votre équipe technique (telle que l'ingénierie ou l'informatique) de mettre à jour votre configuration dns avec les détails de l'enregistrement dns Cloudflare qui s'affichent. Votre équipe technique doit mettre à jour vos enregistrements dns avec ces informations dans un délai de 45 jours.
  - Si vous avez besoin de plus de temps pour mettre à jour vos enregistrements dns, vous pouvez recommencer le processus et générer un nouvel ensemble d'enregistrements dns pour votre domaine.

Braze vérifiera votre configuration dns toutes les 30 minutes environ afin de rechercher les mises à jour.

![Section « Enregistrement dns » avec trois étapes à suivre pour finaliser la configuration de votre domaine.]({% image_buster /assets/img/dns_record.png %})

{% alert note %}
Les progrès réalisés sur votre domaine sont enregistrés automatiquement. Si vous devez quitter le processus en cours, vous pouvez le reprendre ultérieurement en sélectionnant l'entrée de domaine en attente sur la page **Domaines SMS/RCS et applications d'envoi de messages.**
{% endalert %}

### Gestion et utilisation continues

Une fois votre domaine vérifié, vos domaines personnalisés apparaîtront dans le tableau de la page **Domaines SMS/RCS et applications d'envoi de messages** avec des indicateurs d'état. Vous pouvez immédiatement utiliser les domaines connectés dans plusieurs groupes d'abonnement, espaces de travail et sur les canaux SMS, RCS et WhatsApp.

![Liste des domaines personnalisés et de leurs statuts.]({% image_buster /assets/img/custom_domain_statuses.png %}){: style="max-width:60%;"}

La surveillance en ligne/en production/instantanée vous alertera dans le tableau de bord de Braze si l'un de vos domaines actifs rencontre un problème, afin que vos liens personnalisés restent utilisables. Si vous rencontrez des difficultés, veuillez vous référer aux détails de l'erreur dans l'application ou contacter [le service d'assistance]({{site.baseurl}}/braze_support/) Braze pour obtenir de l'aide.

## Attribution de domaines personnalisés à des groupes d'abonnement

Une fois configurés, les domaines personnalisés peuvent être attribués à un ou plusieurs groupes d'abonnement SMS, RCS et WhatsApp.

1. Veuillez vous rendre dans **Audience** > **Gestion des groupes d'abonnement**.
2. Veuillez rechercher et sélectionner votre groupe d'abonnement dans la liste.
3. Sous **Détails du groupe d'abonnement**, veuillez sélectionner votre domaine personnalisé comme **domaine de raccourcissement de** **lien**.

![Paramètres des groupes d’abonnement vous permettant de sélectionner un domaine de raccourcissement de lien.]({% image_buster /assets/img/custom_domain.png %})

Les campagnes envoyées avec l'option de raccourcissement des liens activée utiliseront le domaine attribué associé à votre groupe d'abonnement SMS, RCS ou WhatsApp.

![Aperçu du compositeur de messages SMS avec un domaine de lien raccourci qui est différent du domaine dans la boîte "Message".]({% image_buster /assets/img/custom_domain2.png %})

## Foire aux questions

### Les domaines délégués peuvent-ils être partagés entre plusieurs groupes d’abonnement ?

Oui. Un seul domaine peut être utilisé avec plusieurs groupes d'abonnement. Pour ce faire, sélectionnez le domaine de chaque groupe d’abonnement auquel il doit être associé.

### Les domaines délégués peuvent-ils être partagés entre plusieurs espaces de travail ?

Oui. Les domaines peuvent être associés à des groupes d'abonnement dans plusieurs espaces de travail, à condition que les espaces de travail soient situés dans la même entreprise.

### Combien de domaines personnalisés puis-je ajouter ?

Vous pouvez ajouter jusqu'à 10 domaines personnalisés par tableau de bord.

### Que se passe-t-il si je ne mets pas à jour mes enregistrements dns dans les 45 jours ?

Bien que les détails de votre enregistrement dns Cloudflare expirent après 45 jours, vous pouvez recommencer le processus de configuration avec le même domaine et Braze générera un ensemble de nouveaux enregistrements dns afin de prolonger votre fenêtre de configuration.

### Serai-je informé en cas d'erreur pendant le processus de mise à jour dns ?

Oui. En cas d'erreur, une bannière s'affichera dans le tableau de bord de Braze, détaillant le problème et les étapes à suivre pour le résoudre. 

### Puis-je utiliser un domaine personnalisé sur plusieurs canaux ?

Oui. Une fois qu'un domaine personnalisé est vérifié, il peut être utilisé dans tous les groupes d'abonnement SMS, RCS et WhatsApp de tous les espaces de travail d'un tableau de bord. 

### Que faire si j'ai des questions ou si j'ai besoin d'une assistance supplémentaire ?

Pour obtenir des conseils plus détaillés sur la configuration et la gestion des domaines personnalisés, y compris les étapes de résolution des problèmes et les exigences techniques, [veuillez contacter le service d'assistance]({{site.baseurl}}/braze_support/).
