---
nav_title: créez votre agent
article_title: créez votre agent
page_order: 3
description: "Découvrez comment concevoir votre agent Decisioning Studio Pro avec l'équipe Decisioning Services de l'intelligence artificielle, notamment en ce qui concerne la définition de l'audience, les indicateurs de réussite et les dimensions."
---

# créez votre agent

> La première étape de la configuration de l'agent consiste à travailler avec notre équipe de services d'intelligence artificielle décisionnelle pour concevoir votre agent. Cet article traite des principales décisions en matière de conception et de la manière de définir votre audience.

Pour les concepts fondamentaux des agents décisionnels, notamment les indicateurs de réussite, les dimensions, les banques d'actions et les contraintes, voir [Conception d'agents décisionnels]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/designing_decisioning_agents/).

## Décisions clés en matière de conception

En collaboration avec l'équipe des services décisionnels de l'intelligence artificielle, vous prendrez les décisions suivantes :

| Décision | Description | Exemples |
|----------|-------------|----------|
| **Indicateurs de réussite** | Qu'est-ce que l'agent maximisera lors de la personnalisation de l'engagement client ? | Chiffre d'affaires, LTV, ARPU, conversions, fidélisation |
| **Audience** | Pour qui l'agent du Decisioning Studio prendra-t-il des décisions en matière d'engagement client ? | Tous les clients, les membres du programme de fidélisation, les abonnés à risque |
| **Groupes expérimentaux** | Comment les essais contrôlés randomisés de Decisioning Studio doivent-ils être structurés ? | Studio de décision, contrôle aléatoire, BAU, Holdout |
| **Dimensions** | Quelles décisions l'agent doit-il personnaliser ? | Moment de la journée, ligne d'objet, fréquence, offres, canal |
| **Options** | Quelles sont les options dont dispose l'agent ? | Modèles, offres et fenêtres de temps spécifiques |
| **Contraintes** | Quelles sont les décisions que l'agent *ne* doit *jamais* prendre ? | Restrictions géographiques, limites budgétaires, règles d'éligibilité |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Chacune de ces décisions a des implications sur la quantité d'augmentation que l'agent peut être en mesure de générer, et sur la rapidité de cette augmentation. Notre équipe de services d'intelligence artificielle décisionnelle travaillera avec vous pour concevoir un agent qui génère une valeur maximale tout en respectant l'ensemble de vos règles métier.

![Diagramme Decisioning Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_pro_agent_design.png %})

## Définir votre audience

Les audiences des cas d'utilisation sont généralement définies dans une plateforme d'engagement client (comme Braze ou Salesforce Marketing Cloud), puis envoyées à l'agent Decisioning Studio. L'agent répartit ensuite les clients en groupes de contrôle afin de réaliser des essais contrôlés randomisés.

### Groupes de traitement

| Groupe | Description |
|-------|-------------|
| **Studio de décision** | Les clients qui reçoivent des recommandations optimisées par l'intelligence artificielle. |
| **Contrôle aléatoire** | Clients recevant des options sélectionnées de manière aléatoire (comparaison de base) |
| **Business-as-Usual (facultatif)** | Les clients qui reçoivent le parcours marketing actuel (pour une comparaison avec les performances existantes). |
| **Retenue (facultative)** | Clients ne recevant aucune communication (pour mesurer l'impact global de la campagne) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Configurer votre audience

{% tabs %}
{% tab Braze %}

**Configurez l'audience dans Braze :**

1. Créez un segment de votre audience que vous souhaitez cibler.
2. Communiquez l'ID du segment à votre équipe de services d'aide à la décision en matière d'intelligence artificielle.

{% alert note %}
Pour Braze, nous pouvons ingérer plusieurs segments et les combiner pour créer l'audience. Decisioning Studio peut ingérer un segment pour une campagne de comparaison Business-as-Usual. Tous ces modèles sont acceptables.
{% endalert %}

{% endtab %}
{% tab SFMC %}

**Configurez l'audience dans Salesforce Marketing Cloud :**

1. Configurez une ou plusieurs extensions de données SFMC pour votre audience et fournissez l'ID de l'extension de données.
2. Configurez SFMC Installed Package pour l'intégration API avec les autorisations appropriées requises par Decisioning Studio.
3. Veillez à ce que cette extension de données soit actualisée quotidiennement, car Decisioning Studio utilisera les données incrémentielles les plus récentes.

Fournissez l'ID de l'extension et la clé API à l'équipe de services de Braze. Ils vous assisteront dans les prochaines étapes de l'ingestion des données personnalisées.

{% endtab %}
{% tab Klaviyo %}

**Définissez l'audience dans Klaviyo :**

1. Créer une segmentation de l'audience
2. Générez une clé API privée et fournissez-la à l'équipe de Braze chargée de la prise de décision en matière d'intelligence artificielle.
3. Fournissez l'ID du segment et la clé API à l'équipe des services de Braze.

Consultez la [documentation de Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005237908) pour plus d'informations sur la manière de procéder.

{% endtab %}
{% tab Other Platforms %}

**Google Cloud Storage**

Si l'audience n'est pas actuellement stockée dans Braze, SFMC ou Klaviyo, la meilleure étape suivante consiste à configurer une exportation automatisée directement vers un compartiment Google Cloud Services contrôlé par Braze.

Pour savoir si cela est possible, reportez-vous à la documentation de votre plateforme Martech. Par exemple, mParticle propose une [intégration native avec Google cloud storage.](https://www.mparticle.com/integration/google-cloud-storage/) Si c'est le cas, nous pouvons vous fournir un compartiment GCS vers lequel exporter les données d'audience.

Il existe des pages similaires pour :
- [Segmentation de Twilio](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [Treasure Data](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [Adobe Experience Platform](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

{% endtab %}
{% endtabs %}

## Capacités professionnelles

Decisioning Studio Pro offre toute la puissance de l'intelligence artificielle :

| Capacité | Détails |
|------------|---------|
| **Tout indicateur de réussite** | Optimisez pour le chiffre d'affaires, les conversions, l'ARPU, le LTV ou tout autre indicateur clé de performance. |
| **Dimensions illimitées** | Personnalisez en fonction de l'offre, du canal, du moment, de la fréquence, de la création, etc. |
| **Tout CEP** | Intégrations natives avec Braze, SFMC, Klaviyo + intégrations personnalisées pour n'importe quelle plateforme. |
| **Services d'intelligence artificielle pour la prise de décision** | Un soutien dédié de la part de l'équipe de science des données de Braze. |
| **Conception d'expériences avancées** | Des groupes de traitement et des groupes d'attente entièrement personnalisables |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Bonnes pratiques

Quelques bonnes pratiques pour la conception d'agents Decisioning Studio :

1. **Maximiser la richesse des données**: Plus les agents disposent d'informations sur vos clients, plus ils seront performants.
2. **Diversifier les actions**: Plus l'ensemble des actions que l'agent peut entreprendre est diversifié, plus il peut personnaliser sa stratégie pour chaque utilisateur.
3. **Minimiser les contraintes**: Moins il y a de contraintes pour vos agents, mieux c'est. Les contraintes doivent être conçues de manière à respecter les règles de l'entreprise tout en libérant autant que possible l'expérimentation menée par les agents.

## Étapes suivantes

Une fois que les décisions clés en matière de conception ont été prises, nous pouvons procéder au lancement :

- [Lancez votre agent]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/launch_your_agent/)