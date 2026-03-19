---
nav_title: "Conception d'agents décisionnels"
article_title: "Conception d'agents décisionnels"
page_order: 4
page_type: reference
description: "Cet article de référence présente les concepts clés et les meilleures pratiques pour la conception et la configuration de votre agent décisionnel."
---

# Conception d'agents décisionnels

> Cet article de référence présente les concepts clés et les meilleures pratiques pour la conception et la configuration de votre agent décisionnel.

## À propos des agents décisionnaires

La conception de votre agent décisionnel constitue la première étape de la configuration de Decisioning Studio. Pour que l'agent décisionnel puisse prendre des décisions, il est nécessaire de définir le résultat que vous souhaitez optimiser et les actions que l'agent peut entreprendre pour y parvenir.

### Concepts clés

Les termes suivants sont utilisés tout au long du guide Decisioning Studio.

| Terme | Définition |
| --- | --- |
| **Agent décisionnel** | Un agent décisionnel est une configuration personnalisée pour BrazeAI Decisioning Studio™, conçue sur mesure pour répondre à un objectif métier spécifique. Ceci est déterminé par les indicateurs de réussite, les dimensions et les options que vous sélectionnez. |
| **Indicateur de réussite** | L'indicateur commercial spécifique que vous souhaitez optimiser, tel que le chiffre d'affaires, les conversions ou le revenu moyen par utilisateur (ARPU). Il s'agit de l'indicateur que l'agent décisionnaire cherchera à optimiser par ses actions. |
| **Dimensions** | Les dimensions peuvent être considérées comme les *types de leviers* que l'agent décisionnaire peut actionner pour optimiser l'indicateur du succès. Les dimensions typiques comprennent l'offre, la ligne d'objet, la création, le canal ou l'heure d'envoi. |
| **Action Bank** | La banque d'actions définit les *options spécifiques* auxquelles l'agent décisionnaire a accès pour chaque dimension « levier ». Par exemple, pour une dimension de canal, vous définiriez les canaux spécifiques auxquels l'agent décisionnel a accès. Pour une dimension d'offre, vous devez définir les offres spécifiques que l'agent décisionnel peut tester. 
| **Contraintes** | En général, l'agent décisionnel peut prendre n'importe quelle combinaison d'actions que vous avez enregistrées dans la banque d'actions. Cependant, vous pouvez également définir des contraintes afin de limiter les actions de l'agent décisionnel et garantir ainsi le respect des règles métier essentielles. Par exemple, cela pourrait empêcher une offre spécifique d'être sélectionnée pour les clients situés dans une zone géographique non éligible, ou fixer un budget maximal que l'agent décisionnaire est autorisé à dépenser. 
{: .reset-td-br-1 .reset-td-br-2}

![Aperçu général d'un agent décisionnel]({% image_buster /assets/img/decisioning_studio/decisioning_studio_high_level_agent.png %})

{% alert important %}
L'agent décisionnel ne peut prendre que les mesures que *vous* configurez et ajoutez à la banque d'actions. Cela signifie que toutes les actions possibles sont définies par les combinaisons de ce que vous avez enregistré dans la banque d'actions.
{% endalert %}

## Comment concevoir votre agent décisionnel

Lors de la configuration d'un agent décisionnel, il est nécessaire de prendre en compte quatre éléments de conception principaux :

### L'objectif : Définissez vos indicateurs de réussite

> Quel résultat souhaitez-vous que l'agent optimise ?

Votre indicateur de réussite correspond au résultat commercial que l'agent s'efforcera d'optimiser. Cela devrait correspondre directement à vos objectifs commerciaux, non pas à des indicateurs indirects tels que les clics ou les ouvertures, mais à des résultats commerciaux réels tels que le chiffre d'affaires, les conversions, l'ARPU ou la valeur vie client.

### Le « qui » : Veuillez sélectionner votre audience

> Qui l'agent décisionnaire engagera-t-il ?

Définissez l'audience à laquelle votre agent s'adressera. Il peut s'agir de l'ensemble des clients, d'un segment spécifique (comme les membres d'un programme de fidélité) ou de clients à un stade particulier de leur cycle de vie (comme les acheteurs récents ou les utilisateurs abonnés à risque).

### Le « quoi » : Veuillez configurer votre banque d'actions.

> Quelles options l'agent peut-il choisir pour influencer le résultat ?

La banque d'actions définit tous les leviers que l'agent peut actionner : les dimensions (telles que le canal, l'offre, le timing et la fréquence) et les options spécifiques au sein de chaque dimension. L'agent teste différentes combinaisons de ces options afin de déterminer celle qui convient le mieux à chaque client.

### Le « comment » : Veuillez configurer vos contraintes.

> Quelles règles l'agent doit-il respecter ?

Les contraintes sont les règles que l'agent doit respecter. Cela pourrait empêcher une offre spécifique d'être sélectionnée pour les clients situés dans une zone géographique non éligible, ou fixer un budget maximal que l'agent décisionnaire est autorisé à dépenser.

## Meilleures pratiques et exemples

Afin de maximiser l'impact de votre agent décisionnel, il est recommandé de :

- Veuillez sélectionner un indicateur de réussite qui correspond étroitement à vos objectifs métier, tels que le chiffre d'affaires, les conversions ou l'ARPU.
- Concentrez-vous sur les dimensions ou les « leviers » à tester, tels que l'offre, la ligne d'objet, la création, le canal ou l'heure d'envoi, qui sont les plus susceptibles d'avoir un impact significatif sur l'indicateur de réussite.
- Veuillez sélectionner les options pour chaque dimension, telles que l'e-mail par rapport au SMS, ou la fréquence quotidienne par rapport à la fréquence hebdomadaire, qui sont les plus susceptibles d'avoir un impact significatif sur l'indicateur de réussite.

Voici quelques exemples d'agents décisionnels que vous pourriez créer :

{% tabs %}
{% tab Repeat purchase agent %}
Vous pourriez créer un agent de réachat afin d'augmenter les conversions de suivi après une vente initiale :

- Définissez l'audience et le message dans Braze.
- Decisioning Studio exécute automatiquement des expériences quotidiennes, testant différentes combinaisons d'offres de produits, de timing des messages et de fréquence pour chaque client.
- Au fil du temps, BrazeAI™ identifie les solutions les plus efficaces pour chaque client.
- Effectuez l'orchestration des envois personnalisés via Braze afin d'optimiser les taux de réachat.
{% endtab %}
{% tab Cross-sell or upsell agent %}
Vous pourriez créer un agent de vente croisée ou incitative afin de maximiser le chiffre d'affaires moyen par utilisateur (ARPU) provenant des abonnements Internet :

- Définissez l'audience et le message dans Braze.
- Decisioning Studio exécute automatiquement des expériences quotidiennes, testant différentes combinaisons de messages, d'heures d'envoi, de remises et d'offres de forfaits pour chaque client.
- BrazeAI™ identifie les clients susceptibles d'accepter des offres exceptionnelles et ceux qui ont besoin de remises ou d'autres incitations pour passer à un niveau supérieur.
- Effectuez l'orchestration des envois personnalisés via Braze afin d'optimiser l'ARPU.
{% endtab %}
{% tab Renewal and retention agent %}
Vous pourriez créer un agent de renouvellement et de fidélisation afin de garantir le renouvellement des contrats, en maximisant à la fois la durée des contrats et la valeur actuelle nette (VAN) :

- Définissez l'audience et le message dans Braze.
- Decisioning Studio exécute automatiquement des expériences quotidiennes, testant différentes offres de renouvellement pour chaque client.
- BrazeAI identifie les clients qui sont moins sensibles au prix et qui ont besoin de remises moins importantes pour renouveler leur abonnement.
- Orchestration des envois personnalisés via Braze afin de maximiser les renouvellements de contrats et la valeur actuelle nette.
{% endtab %}
{% tab Winback agent %}
Vous pourriez créer un agent de reconquête afin d'augmenter le taux de réactivation en encourageant les anciens utilisateurs abonnés à s'abonner à nouveau :

- Définissez l'audience et le message dans Braze.
- Decisioning Studio exécute automatiquement des expériences quotidiennes, testant simultanément des milliers de variables, notamment la créativité, le message, le canal et la cadence.
- BrazeAI™ identifie la combinaison optimale pour chaque client personnalisé.
- Effectuez l'orchestration des envois personnalisés via Braze afin d'optimiser les taux de réactivation.
{% endtab %}
{% tab Referral agent %}
Vous pourriez créer un programme de recommandation afin de maximiser le nombre de nouveaux comptes ouverts grâce aux recommandations de cartes de crédit professionnelles par vos clients existants :

- Définissez l'audience et le message dans Braze.
- Decisioning Studio exécute automatiquement des expériences quotidiennes, testant différents e-mails, créations, heures d'envoi et offres de cartes de crédit pour chaque client.
- BrazeAI™ détermine la combinaison idéale pour chaque client personnalisé.
- Effectuez l'orchestration des envois personnalisés via Braze afin d'optimiser les conversions de recommandation.
{% endtab %}
{% tab Lead nurturing and conversion agent %}
Vous pourriez créer un agent de conversion et de maturation des prospects afin de générer un chiffre d'affaires supplémentaire et de payer le montant adéquat pour chaque client :

- Définissez l'audience et le message dans Braze.
- Decisioning Studio exécute automatiquement des expériences quotidiennes, testant différents segments de clientèle, différentes méthodologies d'enchères, différents niveaux d'enchères et différentes créations.
- BrazeAI™ exploite des données first-party fiables pour optimiser les performances des publicités payantes à mesure que les politiques de confidentialité évoluent.
- Effectuez l'orchestration des envois personnalisés via Braze afin de maximiser le chiffre d'affaires tout en optimisant le coût par client.
{% endtab %}
{% tab Loyalty and engagement agent %}
Vous pourriez créer un agent de fidélisation et d'engagement afin de maximiser les achats des nouveaux inscrits à un programme de fidélisation de la clientèle :

- Définissez l'audience et le message dans Braze.
- Decisioning Studio exécute automatiquement des expériences quotidiennes, testant différentes offres par e-mail, différents moments d'envoi et différentes fréquences pour chaque client.
- BrazeAI™ identifie les stratégies les plus efficaces pour chaque nouveau membre du programme de fidélité.
- Effectuez l'orchestration des envois personnalisés via Braze afin d'optimiser les taux d'achat et de réachat.
{% endtab %}
{% endtabs %}

## Étapes suivantes

Êtes-vous prêt à créer votre propre agent décisionnel ? Veuillez suivre les étapes suivantes pour votre niveau Decisioning Studio :

- **Studio de prise de décision Go** : [Configurer Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/)
- **Studio Pro de prise de décision** : [Configurer Decisioning Studio Pro]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/)

Ces guides vous accompagnent tout au long du processus de connexion des sources de données, de configuration de l'orchestration, de conception de votre agent et de lancement en production.
