---
nav_title: Google Gemini
article_title: Google Gemini
description: "Cet article de référence présente le partenariat entre Braze et Google Gemini, qui vous permet de connecter les modèles Gemini à Braze pour les utiliser avec des agents d'intelligence artificielle personnalisés."
alias: /partners/gemini/
page_type: partner
search_tag: Partner

---

# Google Gemini

> [Google Gemini](https://deepmind.google/technologies/gemini/) est la famille de modèles d'intelligence artificielle de Google. Elle combine un raisonnement avancé sur le texte, le code et les images pour aider les marques à offrir des expériences plus intelligentes et plus personnalisées.

{% multi_lang_include alerts/important_alerts.md alert='Braze Agents' %}

_Cette intégration est gérée par Google._

## À propos de l'intégration

L'intégration entre Braze et Google Gemini vous permet de connecter votre clé API Google Gemini ou votre clé Vertex AI à Braze afin d'utiliser les modèles Gemini lors de la création d'agents d'intelligence artificielle personnalisés. Grâce à cette intégration, vos agents peuvent générer des textes personnalisés, prendre des décisions en temps réel ou mettre à jour les champs du Catalogue à l'aide des modèles Gemini de Google.

## Conditions préalables

| Exigences | Description |
|---|---|
| Compte Google Cloud avec clé API Gemini ou clé Vertex AI | Un compte Google Cloud avec une clé API Gemini ou une clé Vertex AI. Pour obtenir de l'aide, contactez votre administrateur ou l'[assistance Google Cloud](https://cloud.google.com/support). |
| Instance Braze | Vous trouverez votre instance Braze sur la [page d'aperçu de l'API]({{site.baseurl}}/api/basics/#endpoints) ou auprès de votre Manager onboarding Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

Pour connecter votre clé API Google Gemini à Braze :

1. Dans le tableau de bord de Braze, accédez à **Intégrations partenaires** > **Partenaires technologiques** et recherchez Google Gemini.
2. Pour le **Type d'API**, sélectionnez **Gemini API** ou **Vertex AI**.
3. Saisissez votre clé API Google. Pour Vertex AI, saisissez l'ID du projet.
4. Sélectionnez **Enregistrer**.

Une fois l'enregistrement effectué, vous pouvez sélectionner les modèles Gemini lors de la [création d'un agent personnalisé]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/) dans la console d'agent.

Contactez l'[assistance Google Cloud](https://cloud.google.com/support) pour tout problème ou toute question concernant votre intégration.