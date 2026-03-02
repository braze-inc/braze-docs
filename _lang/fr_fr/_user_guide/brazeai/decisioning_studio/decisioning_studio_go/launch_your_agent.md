---
nav_title: Lancez votre agent
article_title: Lancez votre agent
page_order: 4
description: "Découvrez comment lancer votre agent BrazeAI Decisioning Studio Go et configurer le reporting Business as Usual (BAU) pour la comparaison des performances."
---

# Lancez votre agent

> Une fois que vous avez connecté vos sources de données, configuré l'orchestration et conçu votre agent, vous êtes prêt à vous lancer. Cet article traite de l'activation de votre agent et de la configuration des rapports BAU facultatifs.

## Lancement de votre agent

Après avoir effectué toutes les étapes de configuration dans le portail Decisioning Studio Go :

1. Vérifiez la configuration de votre agent pour vous assurer que tous les paramètres sont corrects.
2. Vérifiez que votre intégration CEP est active et que l'orchestration est prête.
3. Sélectionnez **Lancer** (ou une action équivalente) dans le portail Decisioning Studio Go pour activer votre agent.

Une fois lancé, votre agent sera :
- Commencez à recevoir des données d'audience de votre CEP
- Commencez à faire des recommandations personnalisées pour chaque client.
- Orchestrer les envois via votre CEP configuré
- Recueillir des données sur l'engagement pour apprendre et s'améliorer au fil du temps.

## Mise en place du reporting BAU

Par défaut, le rapport du portail Decisioning Studio Go compare le groupe Decisioning Studio Go au groupe de contrôle aléatoire. Si vous disposez d'une campagne "Business as Usual" (BAU) existante que vous souhaitez comparer, vous pouvez configurer le reporting BAU pour visualiser les trois groupes en un seul endroit.

### Avantages du rapport BAU

Le principal avantage de la mise en place de rapports BAU est l'application du filtrage des clics non valides de Decisioning Studio Go. Appliquée aux trois groupes expérimentaux, cette méthode permet de comparer les performances des clics de la manière la plus précise et la plus juste ("pommes à pommes") en éliminant le bruit des clics :
- Clics de machine suspectés
- Cliquez sur le lien de désinscription

### Exigences en matière de rapports BAU

Avant de mettre en place le reporting BAU, assurez-vous d'une comparaison "apples-to-apples" entre le groupe de traitement BAU, le groupe Decisioning Studio Go et le groupe de contrôle aléatoire :

- **Pas de chevauchement**: Aucun destinataire ne peut appartenir à plus d'un groupe pendant toute la durée de l'expérience
- **Assignation aléatoire**: Les destinataires sont répartis de manière aléatoire dans les groupes, sans aucun parti pris
- **Options égales**: Toutes les options disponibles pour le groupe BAU (créativité, fréquence, temps, incitation ou offre) sont disponibles pour les groupes Decisioning Studio Go et Random Control.

{% alert warning %}
En l'absence d'un plan d'expérience "pommes à pommes", les rapports sur le BAU peuvent prêter à confusion ou induire en erreur.
{% endalert %}

### Informations requises

Après avoir validé votre plan d'expérience, rassemblez les informations suivantes pour mettre en place le reporting BAU :

**ID de campagne de votre CEP :**

| CEP | Types acceptés |
|-----|---------------|
| **Braze** | Campagnes et canvas |
| **Salesforce Marketing Cloud** | Trajets uniquement |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

**ID de l'audience de votre CEP :**

| CEP | Types acceptés |
|-----|---------------|
| **Braze** | Segments uniquement |
| **Salesforce Marketing Cloud** | Extensions de données uniquement |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Si vous ne disposez pas d'une audience existante qui suit votre audience BAU, vous devez en créer une.

### Considérations

- **Cliquez uniquement sur les ICP**: À l'instar de Decisioning Studio Go plus généralement, le reporting BAU ne couvre que les KPI de clics, et non de conversion.
- **Limites de la toile**: Nous ne prenons pas actuellement en charge le filtrage vers des ID d'étapes du canvas spécifiques. Les événements de toutes les étapes du canvas seront inclus dans les données du BAU. Cela peut invalider les comparaisons avec le BAU si seules certaines étapes du canvas doivent être prises en compte.

### Mise en place du reporting BAU

Suivez les instructions de votre portail Decisioning Studio Go. Vous devez avoir :
- Un ou plusieurs ID de campagne où toutes les communications sont des communications BAU
- Un ID d'audience qui permet de suivre chaque jour les destinataires de l'audience BAU.

## Suivi de votre agent

Après le lancement, surveillez les performances de votre agent sur le portail Decisioning Studio Go :

- **Indicateurs d'engagement**: Suivez les taux de clics dans les différents groupes d'expérience.
- **Progression de l'apprentissage**: Observer l'évolution des recommandations de l'agent dans le temps
- **Comparaisons de groupes**: Comparez les performances de Decisioning Studio Go à celles de Random Control et de BAU (si configuré).

{% alert tip %}
Prévoyez au moins 2 à 4 semaines de collecte de données avant de tirer des conclusions sur les performances. L'agent a besoin de suffisamment d'interactions pour apprendre et optimiser efficacement.
{% endalert %}

## Résolution des problèmes

Si votre agent ne donne pas les résultats escomptés :

1. **Vérifiez l'orchestration**: Confirmez que votre intégration CEP est active, que les campagnes et les parcours sont en cours d'exécution et qu'aucun plafond global ou règle similaire n'interfère avec l'orchestration.
2. **Vérifiez le flux de données**: Confirmez que les données d'audience et d'engagement sont correctement saisies.
3. **Passez en revue les groupes d'expérience**: Veillez à ce que la répartition aléatoire soit correcte et qu'il n'y ait pas de chevauchement entre les groupes.
4. **Contacter le support**: Contactez le service d'assistance de Braze pour obtenir de l'aide.
