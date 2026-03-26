---
nav_title: "Conception d'agents décisionnels"
article_title: "Conception d'agents décisionnels"
page_order: 4
page_type: reference
description: "Cet article de référence présente les concepts clés et les bonnes pratiques pour concevoir et configurer votre agent décisionnel."
---

# Conception d'agents décisionnels

> Cet article de référence présente les concepts clés et les bonnes pratiques pour concevoir et configurer votre agent décisionnel.

## À propos des agents décisionnels

La conception de votre agent décisionnel constitue la première étape de la mise en place de Decisioning Studio. Pour que l'agent décisionnel puisse prendre des décisions, vous devez définir le résultat que vous souhaitez maximiser, ainsi que les actions que l'agent peut entreprendre pour y parvenir.

### Concepts clés

Les termes suivants sont utilisés tout au long du guide Decisioning Studio.

| Terme | Définition |
| --- | --- |
| **Agent décisionnel** | Un agent décisionnel est une configuration personnalisée de BrazeAI Decisioning Studio™, conçue sur mesure pour répondre à un objectif métier spécifique. Il est défini par l'indicateur de réussite, les dimensions et les options que vous choisissez. |
| **Indicateur de réussite** | L'indicateur métier spécifique que vous souhaitez optimiser, tel que le chiffre d'affaires, les conversions ou le revenu moyen par utilisateur (ARPU). C'est l'indicateur que l'agent décisionnel cherchera à maximiser par ses actions. |
| **Dimensions** | Les dimensions représentent les *types de leviers* que l'agent décisionnel peut actionner pour maximiser l'indicateur de réussite. Les dimensions courantes incluent l'offre, la ligne d'objet, le visuel, le canal ou l'heure d'envoi. |
| **Banque d'actions** | La banque d'actions définit les *options spécifiques* auxquelles l'agent décisionnel a accès pour chaque « levier » dimensionnel. Par exemple, pour une dimension de canal, vous définiriez les canaux spécifiques auxquels l'agent décisionnel a accès. Pour une dimension d'offre, vous définiriez les offres spécifiques que l'agent décisionnel peut tester. |
| **Contraintes** | Par défaut, l'agent décisionnel peut utiliser n'importe quelle combinaison d'actions présentes dans la banque d'actions. Toutefois, vous pouvez définir des contraintes pour limiter ses actions et garantir le respect des règles métier essentielles. Par exemple, vous pouvez empêcher la sélection d'une offre spécifique pour des clients situés dans une zone géographique non éligible, ou fixer un budget maximal que l'agent décisionnel est autorisé à dépenser. |
{: .reset-td-br-1 .reset-td-br-2}

![Aperçu général d'un agent décisionnel]({% image_buster /assets/img/decisioning_studio/decisioning_studio_high_level_agent.png %})

{% alert important %}
L'agent décisionnel ne peut exécuter que les actions que *vous* configurez et ajoutez à la banque d'actions. Autrement dit, toutes les actions possibles sont déterminées par les combinaisons de ce que vous avez défini dans la banque d'actions.
{% endalert %}

## Comment concevoir votre agent décisionnel

Lors de la configuration d'un agent décisionnel, vous devez réfléchir à quatre éléments de conception principaux :

### L'objectif : définissez votre indicateur de réussite

> Quel résultat souhaitez-vous que l'agent maximise ?

Votre indicateur de réussite correspond au résultat métier que l'agent cherchera à optimiser. Il doit être directement aligné sur vos objectifs métier — non pas des indicateurs indirects comme les clics ou les ouvertures, mais de véritables résultats commerciaux tels que le chiffre d'affaires, les conversions, l'ARPU ou la valeur vie client.

### Le « qui » : sélectionnez votre audience

> À qui l'agent décisionnel s'adressera-t-il ?

Définissez l'audience que votre agent servira. Il peut s'agir de l'ensemble des clients, d'un segment spécifique (comme les membres d'un programme de fidélité) ou de clients à un stade particulier de leur cycle de vie (comme les acheteurs récents ou les utilisateurs abonnés à risque).

### Le « quoi » : configurez votre banque d'actions

> Parmi quelles options l'agent peut-il choisir pour influencer le résultat ?

La banque d'actions définit tous les leviers que l'agent peut actionner : les dimensions (telles que le canal, l'offre, le timing et la fréquence) et les options spécifiques au sein de chaque dimension. L'agent expérimente différentes combinaisons de ces options pour déterminer ce qui fonctionne le mieux pour chaque client.

### Le « comment » : configurez vos contraintes

> Quelles règles l'agent doit-il respecter ?

Les contraintes sont les règles que l'agent doit suivre. Par exemple, empêcher la sélection d'une offre spécifique pour des clients situés dans une zone géographique non éligible, ou fixer un budget maximal que l'agent décisionnel est autorisé à dépenser.

## Bonnes pratiques et exemples

Pour maximiser l'impact de votre agent décisionnel, nous vous recommandons de :

- Choisir un indicateur de réussite étroitement aligné sur vos objectifs métier, comme le chiffre d'affaires, les conversions ou l'ARPU.
- Vous concentrer sur les dimensions, ou « leviers » à tester — offre, ligne d'objet, visuel, canal ou heure d'envoi — les plus susceptibles d'avoir un impact significatif sur l'indicateur de réussite.
- Sélectionner les options pour chaque dimension — par exemple e-mail versus SMS, ou fréquence quotidienne versus hebdomadaire — les plus susceptibles d'influencer significativement l'indicateur de réussite.

Voici quelques exemples d'agents décisionnels que vous pourriez créer :

{% tabs %}
{% tab Repeat purchase agent %}
Vous pourriez créer un agent de réachat pour augmenter les conversions de suivi après une première vente :

- Définissez l'audience et le message dans Braze
- Decisioning Studio lance automatiquement des expériences quotidiennes, testant différentes combinaisons d'offres produit, de timing et de fréquence des messages pour chaque client
- Au fil du temps, BrazeAI<sup>TM</sup> identifie ce qui fonctionne le mieux pour chaque client
- Les envois personnalisés sont orchestrés via Braze pour maximiser les taux de réachat
{% endtab %}
{% tab Cross-sell or upsell agent %}
Vous pourriez créer un agent de vente croisée ou incitative pour maximiser le revenu moyen par utilisateur (ARPU) sur les abonnements Internet :

- Définissez l'audience et le message dans Braze
- Decisioning Studio lance automatiquement des expériences quotidiennes, testant différentes combinaisons de messages, d'heures d'envoi, de remises et d'offres de forfaits pour chaque client
- BrazeAI<sup>TM</sup> identifie les clients réceptifs aux offres premium et ceux qui ont besoin de remises ou d'autres incitations pour monter en gamme
- Les envois personnalisés sont orchestrés via Braze pour maximiser l'ARPU
{% endtab %}
{% tab Renewal and retention agent %}
Vous pourriez créer un agent de renouvellement et de rétention pour sécuriser les renouvellements de contrats, en maximisant à la fois la durée des contrats et la valeur actuelle nette (VAN) :

- Définissez l'audience et le message dans Braze
- Decisioning Studio lance automatiquement des expériences quotidiennes, testant différentes offres de renouvellement pour chaque client
- BrazeAI<sup>TM</sup> identifie les clients moins sensibles au prix, qui n'ont pas besoin de remises importantes pour renouveler
- Les envois personnalisés sont orchestrés via Braze pour maximiser les renouvellements de contrats et la VAN
{% endtab %}
{% tab Winback agent %}
Vous pourriez créer un agent de reconquête pour augmenter la réactivation en encourageant d'anciens utilisateurs abonnés à se réabonner :

- Définissez l'audience et le message dans Braze
- Decisioning Studio lance automatiquement des expériences quotidiennes, testant simultanément des milliers de variables : visuel, message, canal et cadence
- BrazeAI<sup>TM</sup> découvre la combinaison optimale pour chaque client
- Les envois personnalisés sont orchestrés via Braze pour maximiser les taux de réactivation
{% endtab %}
{% tab Referral agent %}
Vous pourriez créer un agent de recommandation pour maximiser le nombre de nouveaux comptes ouverts grâce aux recommandations de cartes de crédit professionnelles par vos clients existants :

- Définissez l'audience et le message dans Braze
- Decisioning Studio lance automatiquement des expériences quotidiennes, testant différents e-mails, visuels, heures d'envoi et offres de cartes de crédit pour chaque client
- BrazeAI<sup>TM</sup> détermine la combinaison idéale pour chaque client
- Les envois personnalisés sont orchestrés via Braze pour maximiser les conversions par recommandation
{% endtab %}
{% tab Lead nurturing and conversion agent %}
Vous pourriez créer un agent de nurturing et de conversion des prospects pour générer du chiffre d'affaires incrémental tout en optimisant le coût d'acquisition par client :

- Définissez l'audience et le message dans Braze
- Decisioning Studio lance automatiquement des expériences quotidiennes, testant différents segments de clientèle, méthodologies d'enchères, niveaux d'enchères et visuels
- BrazeAI<sup>TM</sup> exploite des données first-party fiables pour optimiser les performances des publicités payantes à mesure que les politiques de confidentialité évoluent
- Les envois personnalisés sont orchestrés via Braze pour maximiser le chiffre d'affaires tout en optimisant le coût par client
{% endtab %}
{% tab Loyalty and engagement agent %}
Vous pourriez créer un agent de fidélisation et d'engagement pour maximiser les achats des nouveaux inscrits à un programme de fidélité :

- Définissez l'audience et le message dans Braze
- Decisioning Studio lance automatiquement des expériences quotidiennes, testant différentes offres par e-mail, heures d'envoi et fréquences pour chaque client
- BrazeAI<sup>TM</sup> identifie ce qui fonctionne le mieux pour chaque nouveau membre du programme de fidélité
- Les envois personnalisés sont orchestrés via Braze pour maximiser les taux d'achat et de réachat
{% endtab %}
{% endtabs %}

## Étapes suivantes

Prêt à créer votre propre agent décisionnel ? Suivez les étapes correspondant à votre niveau Decisioning Studio :

- **Decisioning Studio Go** : [Configurer Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/)
- **Decisioning Studio Pro** : [Configurer Decisioning Studio Pro]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/)

Ces guides vous accompagnent dans la connexion des sources de données, la configuration de l'orchestration, la conception de votre agent et le lancement en production.