---
nav_title: "Conception d'agents décisionnels"
article_title: "Conception d'agents décisionnels"
page_order: 4
page_type: reference
description: "Cet article de référence couvre les concepts clés et les meilleures pratiques pour concevoir et configurer votre agent décisionnel."
---

# Conception d'agents décisionnels

> Cet article de référence couvre les concepts clés et les meilleures pratiques pour concevoir et configurer votre agent décisionnel.

## À propos des agents décisionnels

La conception de votre agent décisionnel est la première étape de l'installation de Decisioning Studio. Pour que l'agent décisionnel puisse prendre des décisions, vous devez définir le résultat que vous souhaitez maximiser et les actions que l'agent peut entreprendre pour y parvenir.

### Concepts clés

Les termes suivants sont référencés dans le guide Decisioning Studio.

| Terme | Définition |
| --- | --- |
| **Agent décisionnaire** | Un agent décisionnel est une configuration personnalisée pour BrazeAI Decisioning Studio™, conçue sur mesure pour répondre à un objectif métier spécifique. Celle-ci est définie par l'indicateur de réussite, les indicateurs et les options que vous choisissez. |
| **Indicateurs de réussite** | Le chiffre d'affaires, les conversions ou le revenu moyen par utilisateur (ARPU). Il s'agit de l'indicateur que l'agent décisionnaire cherchera à maximiser par ses actions. |
| **Dimensions** | Les dimensions peuvent être considérées comme les *types de leviers* que l'agent décisionnaire peut actionner pour maximiser l'indicateur de réussite. Les dimensions typiques sont l'offre, la ligne d'objet, la création, le canal ou l'heure d'envoi. |
| **Banque d'action** | La banque d'actions définit les *options spécifiques* auxquelles l'agent décisionnaire a accès pour chaque dimension "levier". Par instance, pour une dimension de canal, vous définirez les canaux spécifiques auxquels l'agent décisionnel a accès. Pour une dimension d'offre, vous définissez les offres spécifiques que l'agent décisionnaire peut tester. 
| **Contraintes** | En général, l'agent décisionnaire peut prendre n'importe quelle combinaison d'actions que vous avez placées dans la banque d'actions. Cependant, vous pouvez également définir des contraintes pour limiter les actions de l'agent décisionnel afin de respecter les règles métier essentielles. Il peut s'agir, par exemple, d'empêcher qu'une offre spécifique soit sélectionnée pour les clients d'une zone géographique non éligible, ou de fixer un budget maximum à dépenser par l'agent décisionnaire. 
{: .reset-td-br-1 .reset-td-br-2}

![Un aperçu de haut niveau d'un agent décisionnel]({% image_buster /assets/img/decisioning_studio/decisioning_studio_high_level_agent.png %})

{% alert important %}
L'agent décisionnel ne peut entreprendre que les actions que *vous* configurez et ajoutez à la banque d'actions. Cela signifie que toutes les actions possibles sont définies par les combinaisons de ce que vous mettez dans la banque d'actions.
{% endalert %}

## Comment concevoir votre agent de décision

Lors de la mise en place d'un agent décisionnel, vous devrez réfléchir à quatre éléments de conception principaux :

### Le "but" : Définissez vos indicateurs de réussite

> Quel résultat voulez-vous que l'agent maximise ?

Votre indicateur de réussite est le résultat commercial que l'agent optimisera. Cela doit correspondre directement à vos objectifs commerciaux, et non à des indicateurs de substitution tels que les clics ou les ouvertures, mais à des résultats commerciaux réels tels que le chiffre d'affaires, les conversions, l'ARPU ou la valeur vie client.

### Le « qui » : Sélectionnez votre audience

> Qui l'agent décisionnaire engagera-t-il ?

Définissez l'audience de votre agent. Il peut s'agir de tous les clients, d'un segment spécifique (comme les membres d'un programme de fidélisation) ou de clients à un stade particulier de leur cycle de vie (comme les acheteurs récents ou les abonnés à risque).

### Le « quoi » : Configurez votre banque d'actions

> Quelles sont les options que l'agent peut choisir pour déterminer le résultat ?

La banque d'actions définit tous les leviers que l'agent peut actionner - les dimensions (comme le canal, l'offre, le moment et la fréquence) et les options spécifiques à l'intérieur de chaque dimension. L'agent expérimente différentes combinaisons de ces options pour trouver ce qui fonctionne le mieux pour chaque client.

### Le « comment » : Configurez vos contraintes

> Quelles sont les règles à respecter par l'agent ?

Les contraintes sont les règles que l'agent doit respecter. Il peut s'agir d'empêcher qu'une offre spécifique soit sélectionnée pour des clients situés dans une zone géographique non éligible, ou de fixer un budget maximum à dépenser par l'agent décisionnaire.

## Bonnes pratiques et exemples

Pour maximiser l'impact de votre agent de décision, vous devez.. :

- Choisissez un indicateur de réussite qui s'aligne étroitement sur les buts et objectifs de votre métier, comme le chiffre d'affaires, les conversions ou l'ARPU.
- Concentrez-vous sur les dimensions, ou "leviers" à tester, tels que l'offre, la ligne d'objet, la création, le canal ou l'heure d'envoi, qui sont les plus susceptibles d'avoir un impact significatif sur l'indicateur de réussite.
- Sélectionnez les options pour chaque dimension, par exemple e-mail ou SMS, ou fréquence quotidienne ou hebdomadaire, qui sont les plus susceptibles d'avoir un impact significatif sur l'indicateur de réussite.

Voici quelques exemples d'agents décisionnels que vous pourriez créer :

{% tabs %}
{% tab Repeat purchase agent %}
Vous pourriez créer un agent d'achat répété pour augmenter les conversions de suivi après une vente initiale :

- Définir l'audience et le message en Braze
- Decisioning Studio lance automatiquement des expériences quotidiennes, en testant différentes combinaisons d'offres de produits, de moments et de fréquences d'envoi des messages pour chaque client.
- Au fil du temps, BrazeAI™ apprend ce qui fonctionne le mieux pour chaque client
- Orchestrer des envois personnalisés par le biais de Braze pour maximiser les taux de réachat.
{% endtab %}
{% tab Cross-sell or upsell agent %}
Vous pourriez créer un agent de vente croisée ou de vente incitative pour maximiser le chiffre d'affaires moyen par utilisateur (ARPU) des abonnements à l'internet :

- Définir l'audience et le message en Braze
- Decisioning Studio effectue automatiquement des expériences quotidiennes, en testant différentes combinaisons de messages, d'heures d'envoi, de remises et d'offres de plan pour chaque client
- BrazeAI™ apprend quels clients sont susceptibles de bénéficier d'offres de saute-mouton et lesquels ont besoin de remises ou d'autres incitations pour se mettre à niveau.
- Orchestration des envois personnalisés par l'intermédiaire de Braze pour maximiser l'ARPU.
{% endtab %}
{% tab Renewal and retention agent %}
Vous pourriez créer un agent de renouvellement et de fidélisation pour garantir le renouvellement des contrats, en maximisant à la fois la durée des contrats et la valeur actuelle nette (VAN) :

- Définir l'audience et le message en Braze
- Decisioning Studio exécute automatiquement des expériences quotidiennes, en testant différentes offres de renouvellement pour chaque client
- BrazeAI™ identifie les clients qui sont moins sensibles aux prix et qui ont besoin de remises moins importantes pour se renouveler.
- Orchestrer des envois personnalisés via Braze pour maximiser les renouvellements de contrats et la VAN.
{% endtab %}
{% tab Winback agent %}
Vous pourriez créer un agent de reconquête pour augmenter la réactivation en encourageant les anciens abonnés à se réabonner :

- Définir l'audience et le message en Braze
- Decisioning Studio exécute automatiquement des expériences quotidiennes, testant des milliers de variables à la fois, y compris la création, le message, le canal et la cadence.
- BrazeAI™ découvre la meilleure combinaison pour chaque client individuel.
- Orchestrer des envois personnalisés via Braze pour maximiser les taux de réactivation.
{% endtab %}
{% tab Referral agent %}
Vous pourriez créer un agent de recommandation pour maximiser l'ouverture de nouveaux comptes par le biais de recommandations de cartes de crédit professionnelles de la part de clients existants :

- Définir l'audience et le message en Braze
- Decisioning Studio effectue automatiquement des expériences quotidiennes, en testant différents e-mails, créations, heures d'envoi et offres de carte de crédit pour chaque client
- BrazeAI™ détermine la combinaison idéale pour des clients personnalisés.
- Orchestrer des envois personnalisés par le biais de Braze pour maximiser les conversions de recommandations.
{% endtab %}
{% tab Lead nurturing and conversion agent %}
Vous pourriez créer un agent de maturation des prospects et de conversion pour générer des chiffres d'affaires supplémentaires et payer le bon montant pour chaque client :

- Définir l'audience et le message en Braze
- Decisioning Studio exécute automatiquement des expériences quotidiennes, en testant différents segments de clientèle, la méthodologie d'enchère, les niveaux d'enchère et les créations
- BrazeAI™ exploite des données first-party robustes pour optimiser les performances des publicités payantes à mesure que les politiques de confidentialité évoluent.
- Orchestrer des envois personnalisés via Braze pour maximiser les chiffres d'affaires tout en optimisant le coût par client.
{% endtab %}
{% tab Loyalty and engagement agent %}
Vous pourriez créer un agent de fidélisation et d'engagement pour maximiser les achats des nouveaux inscrits à un programme d'engagement client :

- Définir l'audience et le message en Braze
- Decisioning Studio effectue automatiquement des expériences quotidiennes, en testant différentes offres d'e-mail, heures d'envoi et fréquences pour chaque client.
- BrazeAI™ apprend ce qui fonctionne le mieux pour chaque nouvel inscrit au programme de fidélité.
- Orchestrer des envois personnalisés par l'intermédiaire de Braze pour maximiser les taux d'achat et de réachat.
{% endtab %}
{% endtabs %}

## Étapes suivantes

Prêt à créer votre propre agent décisionnel ? Suivez les étapes suivantes pour votre niveau de Decisioning Studio :

- **Décision Studio Go**: [Mise en place de Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/)
- **Decisioning Studio Pro :** [Installer Decisioning Studio Pro]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/)

Ces guides vous accompagnent dans la connexion des sources de données, la configuration de l'orchestration, la conception de votre agent et le lancement en production.
