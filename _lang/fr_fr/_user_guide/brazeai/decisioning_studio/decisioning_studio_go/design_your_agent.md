---
nav_title: créez votre agent
article_title: créez votre agent
page_order: 3
description: "Découvrez comment concevoir un agent Go de BrazeAI Decisioning Studio, notamment la définition de l'audience, les dimensions et les limitations spécifiques à Go."
---

# créez votre agent

> Cet article explique comment concevoir votre agent Decisioning Studio Go, notamment en définissant votre audience, en sélectionnant les dimensions et en comprenant les capacités et les limites spécifiques à Go.

Pour les concepts fondamentaux des agents décisionnels, notamment les indicateurs de réussite, les dimensions, les banques d'actions et les contraintes, voir [Conception d'agents décisionnels]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/getting_started/designing_decisioning_agents/).

## Capacités Go versus Pro

Decisioning Studio Go est une plateforme en libre-service dont les fonctionnalités sont simplifiées par rapport à Decisioning Studio Pro. Comprendre ces différences vous aide à concevoir un agent efficace dans le cadre de Go.

| Capacité | Décisions Studio Go | Decisioning Studio Pro |
|-----------|----------------------|------------------------|
| **Indicateurs de réussite** | Clics uniquement | Toute mesure commerciale (chiffre d'affaires, conversions ou ARPU) |
| **Dimensions** | Banque d'action limitée | Dimensions illimitées |
| **PEC soutenus** | Braze, SFMC, Klaviyo | Toute CEP (native et personnalisée) |
| **Données client** | Engagement uniquement | Toutes les données 1P |
| **Configuration** | Libre service | Soutien aux services d'aide à la décision de l'intelligence artificielle |
| **Groupes expérimentaux** | Go + contrôle aléatoire + BAU optionnel | Entièrement personnalisable |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Conception de votre agent Go

Lorsque vous concevez un agent Decisioning Studio Go, vous prenez des décisions dans les domaines suivants :

### Étape 1 : Définissez votre audience

Votre audience est l'ensemble des clients avec lesquels l'agent va entrer en contact. Dans Go, les audiences sont définies dans votre CEP :

{% tabs %}
{% tab Braze %}

**Définir l'audience dans Braze :**

1. Créez un segment dans Braze qui définit les clients que vous souhaitez que l'agent cible.
2. Lors de la configuration de votre expérimentateur dans le portail Decisioning Studio Go, sélectionnez ce segment comme audience cible.

{% alert tip %}
Envisagez de créer un segment dédié à votre expérimentateur Decisioning Studio Go pour que vos tests restent isolés et mesurables.
{% endalert %}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

**Définition de l'audience dans le SFMC :**

1. Configurez une extension de données contenant votre audience cible.
2. Veillez à ce que cette extension de données soit actualisée quotidiennement avec les données les plus récentes sur les clients.
3. Faites référence à cette extension de données dans le portail Decisioning Studio Go lorsque vous configurez votre expérimentateur.

{% endtab %}
{% tab Klaviyo %}

**Définition de l'audience dans Klaviyo :**

1. Créez dans Klaviyo un segment qui définit votre audience cible.
2. Lors de la configuration de votre expérimentateur dans le portail Decisioning Studio Go, sélectionnez ce segment.

{% endtab %}
{% endtabs %}

### Étape 2 : Sélectionnez vos dimensions

Les dimensions sont les "leviers" que l'agent peut actionner pour personnaliser l'expérience client. Il s'agit notamment de dimensions créatives telles que la ligne d'objet et l'image du héros, ainsi que de dimensions de type d'envoi telles que la fréquence des e-mails ou l'heure de la journée. 

{% alert note %}
Les dimensions spécifiques disponibles dépendent de votre CEP et de la manière dont vos campagnes sont configurées. Travaillez avec les modèles et le contenu que vous avez mis en place dans votre CEP.
{% endalert %}

### Étape 3 : Configurez votre banque d'actions

La banque d'actions définit les options spécifiques que l'agent peut choisir pour chaque dimension. Par exemple :

- **Modèles d'e-mail**: Sélectionnez les modèles que l'agent peut utiliser (ceux-ci doivent d'abord être configurés dans votre CEP).
- **Lignes d'objet**: Définissez les variantes de la ligne d'objet que l'agent peut tester.
- **Envoyer les heures**: Spécifiez les fenêtres temporelles parmi lesquelles l'agent peut choisir

### Étape 4 : Constituer des groupes d'expérimentation

Decisioning Studio Go crée automatiquement des groupes d'expérimentation pour mesurer les performances :

| Groupe | Description |
|-------|-------------|
| **Décisions Studio Go** | Les clients qui reçoivent des recommandations optimisées par l'intelligence artificielle. |
| **Contrôle aléatoire** | Clients recevant des options sélectionnées de manière aléatoire (comparaison de base) |
| **Les affaires courantes (facultatif)** | Les clients qui reçoivent votre campagne existante (si vous comparez avec les performances actuelles) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
Pour une comparaison précise, assurez-vous qu'aucun client ne peut appartenir à plus d'un groupe d'expérience et que les clients sont répartis de manière aléatoire dans les groupes, sans parti pris.
{% endalert %}

## Limites à prendre en compte

Lorsque vous concevez votre agent Go, gardez ces limites à l'esprit :

- **Clics uniquement**: Go optimise le taux de clics. Si vous avez besoin d'optimiser le chiffre d'affaires, les conversions ou d'autres indicateurs commerciaux, envisagez Decisioning Studio Pro.
- **Dimensions limitées**: Go prend en charge un ensemble prédéfini de dimensions. Pour des dimensions personnalisées ou une personnalisation complexe, envisagez Decisioning Studio Pro.
- **Trois CEP**: Go ne s'intègre qu'avec Braze, Salesforce Marketing Cloud et Klaviyo. Pour d'autres plateformes, envisagez Decisioning Studio Pro.

## Bonnes pratiques

- **Commencez simplement**: Commencez par 2 ou 3 modèles ou variantes de ligne d'objet. L'agent dispose ainsi de suffisamment d'options pour apprendre tout en gardant l'expérience gérable.
- **Donnez-lui du temps**: L'agent a besoin de suffisamment de données pour apprendre. Attendez au moins 2 à 4 semaines avant de tirer des conclusions sur les performances.
- **Veillez à ce que le contenu soit varié**: Veillez à ce que vos options soient significativement différentes. Tester des variations mineures peut ne pas apporter d'informations significatives.
- **Contrôler régulièrement**: Consultez le portail Decisioning Studio Go pour suivre la progression de l'expérience et les indicateurs d'engagement.

## Étapes suivantes

Une fois que vous avez conçu votre agent et que vous l'avez configuré dans le portail Decisioning Studio Go, vous êtes prêt à le lancer :

- [Lancez votre agent]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/launch_your_agent/)
