---
nav_title: Veuillez lancer votre agent.
article_title: Veuillez lancer votre agent.
page_order: 4
description: "Découvrez comment lancer votre agent BrazeAI Decisioning Studio Go et configurer les rapports Business as Usual (BAU) pour comparer les performances."
---

# Veuillez lancer votre agent.

> Une fois que vous avez connecté vos sources de données, configuré l'orchestration et conçu votre agent, vous êtes prêt à démarrer. Cet article traite de l'activation de votre agent et de la configuration du rapport BAU facultatif.

## Lancement de votre agent

Après avoir effectué toutes les étapes de configuration dans le portail Decisioning Studio Go :

1. Veuillez vérifier la configuration de votre agent afin de vous assurer que tous les paramètres sont corrects.
2. Veuillez vérifier que votre intégration CEP est active et que l'orchestration est prête.
3. Veuillez sélectionner **Lancer** (ou une action équivalente) dans le portail Decisioning Studio Go afin d'activer votre agent.

Une fois lancé, votre agent procédera comme suit :
- Commencez à recevoir les données d'audience de votre CEP
- Commencez à formuler des recommandations personnalisées pour chaque client.
- L'orchestration transmet via votre CEP configuré.
- Collectez des données sur l'engagement afin d'apprendre et de vous améliorer au fil du temps.

## Configuration des rapports BAU

Par défaut, les rapports du portail Decisioning Studio Go comparent le groupe Decisioning Studio Go au groupe de contrôle. Si vous disposez d'une campagne Business as Usual (BAU) existante que vous souhaitez comparer, vous pouvez configurer le reporting BAU afin de visualiser les trois groupes en un seul endroit.

### Avantages des rapports BAU

Le principal avantage de la mise en place du reporting BAU réside dans l'application du filtrage des clics non valides de Decisioning Studio Go. Lorsqu'il est appliqué aux trois groupes expérimentaux, cela permet une comparaison des performances en matière de clics la plus précise et la plus équitable possible (« comparer ce qui est comparable ») en éliminant les interférences provenant :
- Clics suspects provenant de la machine
- Clics sur le lien de désabonnement

### Exigences relatives aux rapports BAU

Avant de configurer le reporting BAU, veuillez vous assurer que la comparaison entre le groupe de traitement BAU, le groupe Decisioning Studio Go et le groupe de contrôle aléatoire est équitable :

- **Pas de chevauchement** : Aucun destinataire ne peut appartenir à plus d'un groupe pendant toute la durée de l'expérience.
- **Attribution aléatoire** : Les destinataires sont répartis de manière aléatoire dans des groupes, sans aucun biais.
- **Options équivalentes** : Toutes les options disponibles pour le groupe BAU (créativité, fréquence, durée, incitation ou offre) sont également disponibles pour les groupes Decisioning Studio Go et de contrôle.

{% alert warning %}
Sans une conception expérimentale comparative, les rapports BAU peuvent être confus ou trompeurs.
{% endalert %}

### Informations requises

Après avoir validé la conception de votre expérience, veuillez rassembler les informations suivantes afin de configurer les rapports BAU :

**ID de campagne provenant de votre CEP :**

| CEP | Types acceptés |
|-----|---------------|
| **Braze** | Campagnes et canvas |
| **Salesforce Marketing Cloud** | Voyages uniquement |
| **Klaviyo** | Flux uniquement |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

**ID d'audience provenant de votre CEP :**

| CEP | Types acceptés |
|-----|---------------|
| **Braze** | Segments uniquement |
| **Salesforce Marketing Cloud** | Extensions de données uniquement |
| **Klaviyo** | Segments uniquement |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Si vous ne disposez pas d'une audience existante qui suit votre audience BAU, il est nécessaire d'en créer une.

### Considérations

- **Cliquez uniquement sur les indicateurs clés de performance** : À l'instar de Decisioning Studio Go de manière plus générale, les rapports BAU ne couvrent que les indicateurs clés de performance (KPI) liés aux clics, et non ceux liés à la conversion.
- **Limites du canvas** : Nous ne prenons actuellement pas en charge le filtrage par ID d'étape du canvas spécifique. Les événements de toutes les étapes du canvas seront inclus dans les données BAU. Cela pourrait invalider les comparaisons avec le scénario BAU si seules certaines étapes du canvas devaient être incluses.

### Configuration des rapports BAU

Veuillez suivre les instructions fournies dans votre portail Decisioning Studio Go. Vous devez disposer de :
- Un ou plusieurs ID de campagne pour lesquels toutes les communications sont des communications BAU
- Un ID d'audience qui suit quotidiennement les destinataires dans l'audience BAU.

## Surveillance de votre agent

Après le lancement, veuillez surveiller les performances de votre agent dans le portail Decisioning Studio Go :

- **Indicateurs d'engagement** : Suivre les taux de clics parmi les groupes participant à l'expérience
- **Progrès dans l'apprentissage** : Veuillez observer comment les recommandations de l'agent évoluent au fil du temps.
- **Comparaisons entre les groupes** : Veuillez comparer les performances de Decisioning Studio Go par rapport au contrôle aléatoire et au BAU (si configuré).

{% alert tip %}
Veuillez prévoir au moins deux à quatre semaines de collecte de données avant de tirer des conclusions sur les performances. L'agent a besoin d'interactions suffisantes pour apprendre et s'optimiser efficacement.
{% endalert %}

## Résolution des problèmes

Si votre agent ne répond pas à vos attentes :

1. **Vérifier l'orchestration** : Veuillez vérifier que votre intégration CEP est active, que les campagnes et les parcours sont en cours d'exécution et qu'aucune limite globale ou règle similaire n'interfère avec l'orchestration.
2. **Veuillez vérifier le flux de données** : Veuillez vérifier que les données relatives à l'audience et à l'engagement sont correctement enregistrées.
3. **Veuillez examiner les groupes expérimentaux** : Veuillez vous assurer que la répartition aléatoire est correcte et qu'il n'y a pas de chevauchement entre les groupes.
4. **Veuillez contacter le service d'assistance** : Veuillez contacter le service d'assistance Braze pour obtenir de l'aide.
