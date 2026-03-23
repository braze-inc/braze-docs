---
nav_title: créez votre agent
article_title: créez votre agent
page_order: 3
description: "Découvrez comment concevoir votre agent Decisioning Studio Pro avec l'équipe de service à l'intelligence artificielle Decisioning, notamment en matière de définition d'audience, d'indicateurs de réussite et de dimensions."
---

# créez votre agent

> La première étape de la configuration de l'agent consiste à collaborer avec notre équipe des services de prise de décision par intelligence artificielle afin de concevoir votre agent. Cet article traite des principales décisions en matière de conception et explique comment définir votre audience.

Pour les concepts fondamentaux relatifs aux agents décisionnels, notamment les indicateurs de réussite, les dimensions, les banques d'actions et les contraintes, veuillez consulter [la section Conception d'agents décisionnels]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/getting_started/designing_decisioning_agents/).

## Principales décisions en matière de conception

En collaboration avec l'équipe des services de prise de décision par intelligence artificielle, vous prendrez les décisions suivantes :

| Décision | Description | Exemples |
|----------|-------------|----------|
| **Indicateur de réussite** | Quels éléments l'agent optimisera-t-il lors de la personnalisation de l'engagement client ? | Chiffre d'affaires, LTV, ARPU, conversions, fidélisation |
| **Audience** | Pour qui l'agent Decisioning Studio prendra-t-il des décisions en matière d'engagement client ? | Tous les clients, membres fidèles, utilisateurs abonnés à risque |
| **Groupes expérimentaux** | Comment les essais contrôlés randomisés de Decisioning Studio devraient-ils être structurés ? | Studio de prise de décision, contrôle aléatoire, BAU, holdout |
| **Dimensions** | Quelles décisions l'agent devrait-il réaliser en termes de personnalisation ? | Heure de la journée, ligne d'objet, fréquence, offres, canal |
| **Options** | Quelles sont les options dont dispose l'agent pour travailler ? | Modèles spécifiques, offres, délais |
| **Contraintes** | Quelles décisions l'agent *ne* devrait-il *jamais* prendre ? | Restrictions géographiques, limites budgétaires, règles d'admissibilité |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Chacune de ces décisions a des implications sur l'augmentation potentielle que l'agent peut générer et sur la rapidité avec laquelle il peut y parvenir. Notre équipe chargée des services de prise de décision basés sur l'intelligence artificielle collaborera avec vous afin de concevoir un agent qui génère une valeur maximale tout en respectant l'ensemble de vos règles commerciales.

![Diagramme décisionnel Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_pro_agent_design.png %})

## Définir votre audience

Les audiences des cas d'utilisation sont généralement définies dans une plateforme d'engagement client (telle que Braze ou Salesforce Marketing Cloud), puis transmises à l'agent Decisioning Studio. L'agent répartit ensuite les clients en groupes de traitement afin de mener des essais contrôlés randomisés.

### Groupes de traitement

| Groupe | Description |
|-------|-------------|
| **Studio de prise de décision** | Les clients qui reçoivent des recommandations personnalisées optimisées par l'intelligence artificielle |
| **Contrôle aléatoire** | Les clients qui reçoivent des options sélectionnées de manière aléatoire (comparaison de référence) |
| **Activités habituelles (facultatif)** | Les clients qui bénéficient du parcours marketing actuel (à des fins de comparaison avec les performances existantes) |
| **Holdout (facultatif)** | Clients qui ne reçoivent aucune communication (pour mesurer l'impact global de la campagne) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Configurer votre audience

{% tabs %}
{% tab Braze %}

**Configurer l'audience dans Braze :**

1. Veuillez créer un segment pour l'audience que vous souhaitez cibler pour le processus de ciblage.
2. Veuillez fournir l'ID du segment à votre équipe chargée des services de prise de décision par intelligence artificielle.

{% alert note %}
Pour Braze, nous pouvons intégrer plusieurs segments et les combiner afin de créer l'audience. Decisioning Studio peut intégrer un segment pour une campagne comparative « Business-as-Usual ». Tous ces modèles sont acceptables.
{% endalert %}

{% endtab %}
{% tab SFMC %}

**Configurer l'audience dans Salesforce Marketing Cloud :**

1. Veuillez configurer une ou plusieurs extensions de données SFMC pour votre audience et fournir l'ID de l'extension de données.
2. Veuillez configurer le package SFMC installé pour l'intégration API avec les autorisations appropriées requises par Decisioning Studio.
3. Veuillez vous assurer que cette extension de données est actualisée quotidiennement, car Decisioning Studio extraira les dernières données incrémentielles disponibles.

Veuillez fournir l'ID d'extension et la clé API à l'équipe des services Braze. Ils vous assisteront dans les prochaines étapes de l'ingestion de données clients.

{% endtab %}
{% tab Klaviyo %}

**Définissez l'audience dans Klaviyo :**

1. Créer un segment d'audience
2. Veuillez générer une clé API privée et la fournir à l'équipe Braze intelligence artificielle Decisioning.
3. Veuillez fournir l'ID du segment et la clé API à l'équipe des services Braze.

Veuillez consulter la [documentation Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005237908) pour plus d'informations sur la manière de procéder.

{% endtab %}
{% tab Other Platforms %}

**Google Cloud Storage**

Si l'audience n'est actuellement pas stockée dans Braze, SFMC ou Klaviyo, la meilleure solution consiste à configurer une exportation automatisée directement vers un compartiment Google Cloud Services contrôlé par Braze.

Pour déterminer si cela est possible, veuillez consulter la documentation de votre plateforme Martech. Par exemple, mParticle propose une [intégration native avec Google cloud storage](https://www.mparticle.com/integration/google-cloud-storage/). Si tel est le cas, nous pouvons fournir un compartiment GCS vers lequel exporter les données d'audience.

Il existe des pages similaires pour :
- [Segment Twilio](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [Treasure Data](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [Adobe Experience Platform](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

{% endtab %}
{% endtabs %}

## Capacités professionnelles

Decisioning Studio Pro offre toute la puissance de la prise de décision basée sur l'intelligence artificielle :

| Capacité | Détails |
|------------|---------|
| **Tout indicateur de réussite** | Optimisez votre chiffre d'affaires, vos conversions, votre ARPU, votre LTV ou tout autre indicateur clé de performance (KPI) de votre entreprise. |
| **Dimensions illimitées** | Effectuez la personnalisation de vos offres, de vos canaux, de votre timing, de votre fréquence, de vos créations, etc. |
| **Tout CEP** | Intégrations natives avec Braze, SFMC, Klaviyo et intégrations personnalisées pour toutes les plateformes. |
| **Services de prise de décision basés sur l'intelligence artificielle** | Assistance dédiée de l'équipe de science des données de Braze |
| **Conception avancée d'expériences** | Groupes de traitement et groupes témoins entièrement personnalisables |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Bonnes pratiques

Quelques bonnes pratiques pour la conception d'agents Decisioning Studio :

1. **Optimisez la richesse des données** : Plus les agents disposent d'informations sur vos clients, plus ils seront performants.
2. **Diversifier les actions** : Plus l'ensemble des actions que l'agent peut entreprendre est varié, plus il peut réaliser la personnalisation de sa stratégie pour chaque utilisateur.
3. **Réduire les contraintes** : Moins vos agents ont de contraintes, mieux c'est. Les contraintes doivent être conçues de manière à respecter les règles commerciales tout en laissant autant de liberté que possible aux agents pour mener leurs expériences.

## Étapes suivantes

Une fois les décisions clés en matière de conception prises, nous pouvons procéder au lancement :

- [Veuillez lancer votre agent.]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/launch_your_agent/)