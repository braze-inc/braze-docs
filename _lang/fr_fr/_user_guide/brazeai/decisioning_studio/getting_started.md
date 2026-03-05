---
nav_title: Démarrage
article_title: Premiers pas avec Decisioning Studio
layout: dev_guide
guide_top_header: "Premiers pas avec Decisioning Studio"
guide_top_text: "Avant de créer un agent décisionnel, utilisez ces articles pour vous aider à planifier et à comprendre Decisioning Studio."
page_order: 0
search_rank: 2
page_type: landing
description: "Cette section présente Decisioning Studio et explique comment l'utiliser pour concevoir et déployer des agents décisionnels qui optimisent n'importe quel indicateur d'entreprise."

guide_featured_title: "Section Articles"
guide_featured_list:
  - name: Préparer vos sources de données
    link: /docs/user_guide/brazeai/decisioning_studio/preparing_your_data_sources/
    image: /assets/img/braze_icons/database-01.svg
  - name: Préparer votre orchestration
    link: /docs/user_guide/brazeai/decisioning_studio/preparing_your_orchestration/
    image: /assets/img/braze_icons/dataflow-04.svg
  - name: "Conception d'agents décisionnels"
    link: /docs/user_guide/brazeai/decisioning_studio/designing_decisioning_agents/
    image: /assets/img/braze_icons/settings-01.svg

guide_menu_title: "Additional resources"
guide_menu_list:
  - name: À propos de Decisioning Studio
    link: /docs/user_guide/brazeai/decisioning_studio/about/
    image: /assets/img/braze_icons/info-circle.svg
  - name: Decisioning Studio FAQ
    link: /docs/user_guide/brazeai/decisioning_studio/faq/
    image: /assets/img/braze_icons/annotation-question.svg
---

# Premiers pas avec Decisioning Studio

> Cette référence donne un aperçu des étapes de configuration de Decisioning Studio, notamment la connexion des sources de données, la configuration de l'orchestration et la conception de votre agent décisionnel.

BrazeAI Decisioning Studio™ vous permet de concevoir et de déployer des agents décisionnels qui optimisent n'importe quel indicateur commercial. Un agent décisionnel est une configuration personnalisée adaptée à un objectif métier spécifique.

Pour ce faire, vous devez connecter les sources de données, mettre en place l'orchestration et concevoir vos agents décisionnels.

{% alert tip %}
Pour les clients de Decisioning Studio Pro, votre équipe d'experts en intelligence artificielle vous aidera à configurer Decisioning Studio pour des performances optimales.
{% endalert %}

## Mise en place de Decisioning Studio

Pour configurer Decisioning Studio, vous devez suivre les étapes suivantes :

### Étape 1 : Connecter les sources de données

Connectez les profils des clients et les données d'engagement afin que les agents décisionnels que vous créez comprennent qui est chaque client et comment il se comporte.

En général, vous ne devez connecter vos sources de données qu'une seule fois, lors de la configuration initiale de Decisioning Studio. Si vous élargissez vos cas d'utilisation par la suite, vous devrez peut-être ajouter de nouvelles sources de données.

{% alert tip %}
Toutes les données déjà présentes dans la [plateforme de données de Braze]({{site.baseurl}}/user_guide/data/braze_data_platform) sont automatiquement disponibles pour Decisioning Studio.
{% endalert %}

Pour obtenir des conseils détaillés, consultez la documentation relative à votre niveau de Decisioning Studio :
- [Décision Studio Go : Connecter les sources de données]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/connect_data_sources/)
- [Decisioning Studio Pro : Connecter les sources de données]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/connect_data_sources/)

### Étape 2 : Mettre en place l'orchestration

Intégrez Decisioning Studio à votre plateforme d'engagement client (CEP) pour permettre à vos agents d'orchestrer des actions. Le CEP est la plateforme utilisée pour offrir des expériences personnalisées à vos clients en fonction des décisions de l'agent.

En général, vous ne devez configurer cette orchestration qu'une seule fois.

Pour obtenir des conseils détaillés, consultez la documentation relative à votre niveau de Decisioning Studio :
- [Décision Studio Go : Mettre en place l'orchestration]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/)
- [Decisioning Studio Pro : Mettre en place l'orchestration]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/set_up_orchestration/)

### Étape 3 : Concevez vos agents

Configurez vos agents décisionnels pour définir les résultats que vous souhaitez maximiser et les actions que l'agent peut entreprendre pour les atteindre. Reportez-vous à la section [Conception d'agents décisionnels]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/designing_decisioning_agents/) pour obtenir des conseils détaillés sur la conception des agents.

Pour des conseils spécifiques à chaque niveau :
- [Décision Studio Go : Concevez votre agent]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/design_your_agent/)
- [Decisioning Studio Pro : Concevez votre agent]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/design_your_agent/)

{% alert tip %}
Pour les clients Decisioning Studio Pro, votre équipe Decisioning Services de l'intelligence artificielle vous aidera à concevoir et à lancer vos agents décisionnels.
{% endalert %}

### Étape 4 : Lancez votre agent décisionnel

Lancez votre agent décisionnel et laissez-le apprendre en permanence et optimiser les résultats de votre entreprise.

Pour obtenir des conseils détaillés, consultez la documentation relative à votre niveau de Decisioning Studio :
- [Décision Studio Go : Lancez votre agent]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/launch_your_agent/)
- [Decisioning Studio Pro : Lancez votre agent]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/launch_your_agent/)

## Étapes suivantes

Maintenant que vous avez une compréhension de base des concepts clés de Decisioning Studio, vous pouvez commencer à concevoir votre agent décisionnel.

- [Conception d'agents décisionnels]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/designing_decisioning_agents/)
