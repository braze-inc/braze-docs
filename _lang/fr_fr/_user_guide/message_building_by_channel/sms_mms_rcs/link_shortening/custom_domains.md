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

> Cette page explique comment configurer vos propres domaines personnalisés dans le tableau de bord de Braze. Les domaines personnalisés vous permettent d'utiliser un lien raccourci de marque qui reflète l'identité de votre marque au lieu d'un lien raccourci générique ou du domaine Braze (`brz.ai`)- ce qui améliore la confiance des utilisateurs et l'engagement de la campagne avec les liens SMS.

Les domaines personnalisés en libre-service vous permettent de configurer et de gérer vos propres domaines personnalisés pour SMS, RCS et WhatsApp, directement depuis votre tableau de bord Braze. Vous pouvez facilement ajouter, surveiller et gérer jusqu'à 10 domaines personnalisés en un seul endroit.

## Avantages des domaines personnalisés en libre-service

- **Configuration simplifiée :** Configurez vos domaines sur la page **Paramètres de l'entreprise**, ce qui réduit le temps de mise en place.
- **Transparence accrue :** Recevez des mises à jour en temps réel sur l'état de la configuration de votre domaine par le biais de bannières dans le tableau de bord.
- **Notifications proactives :** Recevez des alertes immédiates lorsque votre domaine personnalisé est connecté ou en cas d'erreur de configuration.

## Exigences du domaine

- Les domaines doivent être achetés, détenus et gérés par vous. Cela peut se faire par l'intermédiaire d'un bureau d'enregistrement de domaines, comme GoDaddy, Amazon Route 53 ou Google Domains.
- Le domaine utilisé pour cette fonctionnalité doit être :
  - Unique (différent du domaine de votre site web)
  - Ne peut pas être utilisé pour héberger du contenu web
    - Vous pouvez également utiliser des sous-domaines uniques. Par exemple, le domaine `braze.com` peut avoir des sous-domaines `sms.braze.com` ou `whatsapp.braze.com`.

## Déléguer votre domaine personnalisé

Nous vous demandons de déléguer votre domaine personnalisé à Braze afin que nous puissions faciliter le routage et la compatibilité de l'infrastructure avec nos services de raccourcissement de liens et de suivi des clics. Lorsque vous déléguez votre domaine à Braze, nous nous chargeons automatiquement du renouvellement du certificat afin d'éviter toute interruption de service. 

## Ajouter un domaine personnalisé

1. Dans Braze, allez dans **Company Settings** > **SMS/RCS and Messaging Apps Domains**.
!page "Domaines des SMS/RCS et des envois in-app" avec plusieurs domaines répertoriés.]({% image_buster /assets/img/main_page.png %})

{: start="2"}
2\. Sélectionnez **Ajouter un domaine** pour commencer la configuration d'un nouveau domaine personnalisé.
3\. Entrez le domaine personnalisé que vous avez acheté dans notre entrée in-app, qui utilise notre logique de validation existante pour un formatage correct, puis sélectionnez **Suivant** et **Soumettre**.

! bouton "Ajouter un domaine" sur la page "Domaines SMS/RCS et envois in-app".]({% image_buster /assets/img/custom_domain_button.png %}){: style="max-width:70%;"}

{: start="4"}
4\. Demandez à votre équipe technique (comme l'ingénierie ou l'informatique) de mettre à jour votre configuration DNS avec les détails de l'enregistrement DNS Cloudflare qui s'affichent. Votre équipe technique doit mettre à jour vos enregistrements DNS avec ces détails dans un délai de 45 jours.
  - Si vous avez besoin de plus de temps pour mettre à jour vos enregistrements DNS, vous pouvez relancer le processus et générer un nouveau jeu d'enregistrements DNS pour votre domaine.

Braze interroge votre configuration DNS toutes les 30 minutes environ pour vérifier les mises à jour.

!section "enregistrement DNS" avec 3 étapes à compléter pour terminer la configuration de votre domaine.]({% image_buster /assets/img/dns_record.png %})

{% alert note %}
La progression de votre domaine est enregistrée automatiquement. Si vous devez quitter le flux en cours de route, vous pouvez le reprendre plus tard en sélectionnant l'entrée du domaine en attente sur la page **Domaines SMS/RCS et envois de messages.** 
{% endalert %}

### Gestion et utilisation continues

Une fois votre domaine vérifié, vos domaines personnalisés apparaîtront dans le tableau de la page **Domaines SMS/RCS et Messaging Apps** avec des indicateurs d'état. Vous pouvez immédiatement utiliser les domaines connectés dans plusieurs groupes d'abonnement, espaces de travail et sur les canaux SMS, RCS et WhatsApp.

\![Liste des domaines et statuts personnalisés.]({% image_buster /assets/img/custom_domain_statuses.png %}){: style="max-width:60%;"}

La surveillance en direct vous alertera dans le tableau de bord de Braze si l'un de vos domaines actifs présente un problème, de sorte que vos liens personnalisés restent utilisables. Si vous rencontrez des problèmes, reportez-vous aux détails de l'erreur in-app ou contactez l'[assistance de]({{site.baseurl}}/braze_support/) Braze pour obtenir de l'aide.

## Utiliser des domaines personnalisés

Une fois configurés, les domaines personnalisés peuvent être affectés à un ou plusieurs groupes d'abonnement SMS, RCS et WhatsApp.

!Les groupes d'abonnement vous permettent de sélectionner un domaine de raccourcissement des liens.]({% image_buster /assets/img/custom_domain.png %})

Les campagnes envoyées avec le raccourcissement de lien activé utiliseront le domaine attribué associé à votre groupe d'abonnement SMS, RCS ou WhatsApp.

!aperçu du compositeur du message SMS avec un domaine de lien raccourci qui est différent du domaine dans la boîte "Message".]({% image_buster /assets/img/custom_domain2.png %})

## Questions fréquemment posées

### Les domaines délégués peuvent-ils être partagés entre plusieurs groupes d'abonnement ?

Oui. Un seul domaine peut être utilisé avec plusieurs groupes d'abonnement. Pour ce faire, sélectionnez pour chaque groupe d'abonnement le domaine auquel il doit être associé.

### Les domaines délégués peuvent-ils être partagés entre plusieurs espaces de travail ?

Oui. Les domaines peuvent être associés à des groupes d'abonnement dans plusieurs espaces de travail, à condition que les espaces de travail soient situés dans la même entreprise.

### Combien de domaines personnalisés puis-je ajouter ?

Vous pouvez ajouter jusqu'à 10 domaines personnalisés par tableau de bord.

### Que se passe-t-il si je ne mets pas à jour mes enregistrements DNS dans les 45 jours ?

Bien que les détails de votre enregistrement DNS Cloudflare expirent après 45 jours, vous pouvez relancer le processus de configuration avec le même domaine et Braze générera un ensemble de nouveaux enregistrements DNS pour prolonger votre fenêtre de configuration.

### Serai-je averti en cas d'erreur lors du processus de mise à jour du DNS ?

Oui. En cas d'erreur, vous recevrez une bannière dans le tableau de bord de Braze détaillant le problème ainsi que les étapes à suivre pour le résoudre. 

### Puis-je utiliser un domaine personnalisé sur plusieurs canaux ?

Oui. Une fois qu'un domaine personnalisé est vérifié, il peut être utilisé dans tous les groupes d'abonnement SMS, RCS et WhatsApp dans tous les espaces de travail d'un tableau de bord. 

### Que faire si j'ai des questions ou si j'ai besoin d'un soutien supplémentaire ?

Pour obtenir des conseils plus détaillés sur la configuration et la gestion des domaines personnalisés, y compris les étapes de résolution des problèmes et les exigences techniques, [contactez le service d'assistance.]({{site.baseurl}}/braze_support/)