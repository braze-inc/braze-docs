---
nav_title: créez votre agent
article_title: créez votre agent
page_order: 3
description: "Découvrez comment concevoir un agent Go BrazeAI Decisioning Studio, y compris la définition de l'audience, les dimensions et les limitations spécifiques à Go."
---

# créez votre agent

> Cet article explique comment concevoir votre agent Decisioning Studio Go, notamment comment définir votre audience, sélectionner des dimensions et comprendre les capacités et les limites spécifiques à Go.

Pour les concepts fondamentaux relatifs aux agents décisionnels, notamment les indicateurs de réussite, les dimensions, les banques d'actions et les contraintes, veuillez consulter [la section Conception d'agents décisionnels]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/getting_started/designing_decisioning_agents/).

## Fonctionnalités Go et Pro

Decisioning Studio Go est une plateforme de service dotée de fonctionnalités simplifiées par rapport à Decisioning Studio Pro. Comprendre ces différences vous aide à concevoir un agent efficace dans le cadre de Go.

| Capacité | Studio de prise de décision Go | Studio de prise de décision Pro |
|-----------|----------------------|------------------------|
| **Indicateur de réussite** | Clics uniquement | Tout indicateur commercial (chiffre d'affaires, conversions ou ARPU) |
| **Dimensions** | Banque d'actions restreinte | Dimensions illimitées |
| **CEP pris en charge** | Braze, SFMC, Klaviyo | Tout CEP (natif et personnalisé) |
| **Données client** | Engagement uniquement | Toutes les données 1P |
| **Configuration** | Libre-service | Services d'aide à la décision basés sur l'intelligence artificielle |
| **Groupes expérimentaux** | Aller + Contrôle aléatoire + BAU facultatif | Entièrement personnalisable |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Conception de votre agent Go

Lors de la conception d'un agent Decisioning Studio Go, vous prendrez des décisions dans les domaines suivants :

### Étape 1 : Définissez votre audience

Votre audience est l'ensemble des clients avec lesquels l'agent interagira. Dans Go, les audiences sont définies dans votre CEP :

{% tabs %}
{% tab Braze %}

**Définition de l'audience dans Braze :**

1. Veuillez créer un segment dans Braze qui définit les clients que vous souhaitez que l'agent cible.
2. Lors de la configuration de votre expérimentateur dans le portail Decisioning Studio Go, veuillez sélectionner ce segment comme audience cible.

{% alert tip %}
Envisagez de créer un segment dédié pour votre expérimentateur Decisioning Studio Go afin de garantir l'isolation et la mesurabilité de vos tests.
{% endalert %}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

**Définition de l'audience dans SFMC :**

1. Veuillez configurer une extension de données qui inclut votre audience cible.
2. Veuillez vous assurer que cette extension de données est actualisée quotidiennement avec les dernières données clients.
3. Veuillez vous référer à cette extension de données dans le portail Decisioning Studio Go lors de la configuration de votre expérimentateur.

{% endtab %}
{% tab Klaviyo %}

**Définition de l'audience dans Klaviyo :**

1. Veuillez créer un segment dans Klaviyo qui définit votre audience cible.
2. Lors de la configuration de votre expérimentateur dans le portail Decisioning Studio Go, veuillez sélectionner ce segment.

{% endtab %}
{% endtabs %}

### Étape 2 : Veuillez sélectionner vos dimensions

Les dimensions sont les « leviers » que l'agent peut actionner pour réaliser la personnalisation de l'expérience client. Il s'agit notamment de dimensions créatives telles que la ligne d'objet et l'image principale, ainsi que de dimensions liées au type d'envoi, telles que la fréquence des e-mails ou l'heure de la journée. 

{% alert note %}
Les dimensions spécifiques disponibles dépendent de votre CEP et de la configuration de vos campagnes. Veuillez utiliser les modèles et le contenu que vous avez configurés dans votre CEP.
{% endalert %}

### Étape 3 : Veuillez configurer votre banque d'actions.

La banque d'actions définit les options spécifiques parmi lesquelles l'agent peut choisir pour chaque dimension. Par exemple :

- **Modèles d'e-mails** : Veuillez sélectionner les modèles que l'agent est autorisé à utiliser (ceux-ci doivent d'abord être configurés dans votre CEP).
- **Ligne d'objet** : Définissez les variantes de ligne d'objet que l'agent peut tester.
- **Heures d'envoi** : Veuillez indiquer les plages horaires parmi lesquelles l'agent peut faire son choix.

### Étape 4 : Constituer des groupes expérimentaux

Decisioning Studio Go crée automatiquement des groupes d'expérimentation afin de mesurer les performances :

| Groupe | Description |
|-------|-------------|
| **Studio de prise de décision Go** | Les clients qui reçoivent des recommandations personnalisées optimisées par l'intelligence artificielle |
| **Contrôle aléatoire** | Les clients qui reçoivent des options sélectionnées de manière aléatoire (comparaison de référence) |
| **Activités habituelles (facultatif)** | Les clients qui reçoivent votre campagne actuelle (si l'on compare avec les performances actuelles) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
Pour une comparaison précise, veuillez vous assurer qu'aucun client ne peut appartenir à plus d'un groupe d'expérimentation et que les clients sont répartis de manière aléatoire dans les groupes, sans partialité.
{% endalert %}

## Restrictions à prendre en considération

Lors de la conception de votre agent Go, veuillez tenir compte des contraintes suivantes :

- **Clics uniquement** : Go optimise les taux de clics. Si vous avez besoin d'optimiser votre chiffre d'affaires, vos conversions ou d'autres indicateurs commerciaux, envisagez d'utiliser Decisioning Studio Pro.
- **Dimensions restreintes** : Go prend en charge un ensemble prédéfini de dimensions. Pour des dimensions personnalisées ou une personnalisation complexe, envisagez l'utilisation de Decisioning Studio Pro.
- **Trois CEP** : Go propose une intégration avec Braze, Salesforce Marketing Cloud et Klaviyo. Pour les autres plateformes, veuillez envisager Decisioning Studio Pro.

## Bonnes pratiques

- **Commencez par des choses simples** : Commencez par 2 ou 3 modèles ou variantes de ligne d'objet. Cela offre à l'agent suffisamment d'options pour apprendre tout en conservant une expérience gérable.
- **Veuillez patienter** : L'agent a besoin de données suffisantes pour apprendre. Veuillez prévoir au moins deux à quatre semaines avant de tirer des conclusions sur les performances.
- **Veuillez veiller à la diversité du contenu** : Veuillez vous assurer que vos options sont réellement différentes. Tester des variations mineures peut ne pas fournir d'informations significatives.
- **Veuillez surveiller régulièrement** : Veuillez consulter le portail Decisioning Studio Go pour suivre la progression des expériences et les indicateurs d'engagement.

## Étapes suivantes

Une fois que vous avez conçu votre agent et l'avez configuré dans le portail Decisioning Studio Go, vous êtes prêt à le lancer :

- [Veuillez lancer votre agent.]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/launch_your_agent/)
