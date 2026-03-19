---
nav_title: "Configurer l'orchestration"
article_title: "Configurer l'orchestration"
page_order: 2
description: "Découvrez comment configurer l'orchestration pour les agents Decisioning Studio Pro afin de permettre la personnalisation des communications."
toc_headers: h2
---

# Configurer l'orchestration

> Les agents décisionnaires doivent se connecter à une plateforme d'engagement client (CEP) afin d'effectuer l'orchestration des communications une fois qu'ils ont intégré les données clients et les ont personnalisées à un niveau individuel. Cet article explique comment configurer l'intégration pour chaque CEP pris en charge.

## CEP pris en charge

Decisioning Studio Pro prend en charge les plateformes d'engagement client suivantes :

| CEP | Type d’intégration | Complexité de la configuration |
|-----|-----------------|------------------|
| **Braze** | Intégration d'API native | Faible (recommandé) |
| **Salesforce Marketing Cloud** | Événements API natifs + Parcours | Moyen |
| **Klaviyo** | Événements API natifs + Flux | Moyen |
| **Autres CEP** | Personnalisé (fichier de recommandations) | Élevée |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Veuillez sélectionner votre CEP ci-dessous pour commencer la configuration de l'intégration.

{% tabs %}
{% tab Braze %}

## Configuration de l'intégration Braze

Veuillez suivre ces étapes pour réaliser l'intégration d'un agent Braze Decisioning Studio aux capacités d'orchestration de Braze (l'équipe des services Braze se tient à votre disposition pour vous assister) :

### Étape 1 : créez une clé API

Veuillez vous rendre dans **Paramètres** > **Clés API**, puis créez une nouvelle clé avec les autorisations suivantes :

{% multi_lang_include decisioning_studio/api_key_permissions.md %}

### Étape 2 : Implémenter des campagnes déclenchées par API

Veuillez configurer une campagne déclenchée par API pour chaque modèle de base avec les propriétés de déclencheur API pour toutes les dimensions optimisées.

Un modèle de base est un modèle que l'agent de décision peut utiliser pour l'orchestration des messages. Un agent décisionnaire peut disposer d'un ou de plusieurs modèles de base. Dans ce cas, le choix du modèle de base approprié pour chaque client constituera l'une des décisions que l'agent personnalisera.

### Étape 3 : Configurer la rééligibilité

Veuillez vous assurer que toutes les campagnes déclenchées par l'API permettent aux utilisateurs de redevenir éligibles dans un délai de 15 minutes.

![Diagramme décisionnel Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_frequency_cap.png %})

{% alert note %}
Bien que l'agent Decisioning Studio n'envoie jamais la même campagne plus d'une fois par jour, il est souhaitable de pouvoir envoyer les mêmes campagnes plusieurs fois par jour à des fins de test.
{% endalert %}

### Étape 4 : Ajouter des marques substitutives dynamiques

Ils servent de marque substitutive pour les décisions que l'agent Decisioning Studio optimise.

#### Exemple 1 : Campagne par e-mail

Supposons que l'agent Decisioning Studio optimise une campagne par e-mail. Cela pourrait être configuré de la manière suivante :

![Diagramme décisionnel Pro]({% image_buster /assets/img/decisioning_studio/decisioning_email_example_1.png %})

En supposant que l'agent optimise le choix des modèles et le message d'appel à l'action (CTA), une campagne déclenchée par API devrait être créée pour chaque modèle, et la section CTA d'un modèle pourrait ressembler à ceci :

![Diagramme décisionnel Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_braze_email_example_2.png %})

#### Exemple 2 : Campagne de notification push

Supposons qu'un agent de Decisioning Studio optimise le message d'une campagne Push. Cela pourrait être configuré de la manière suivante :

![Diagramme décisionnel Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_1.png %})

![Diagramme décisionnel Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_2.png %})

Ceci entraîne l'affichage du message suivant :

![Diagramme décisionnel Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_3.png %})

#### Exemple 3 : Campagne SMS

Supposons que l'agent Decisioning Studio optimise les champs d'une campagne SMS. Cela pourrait être configuré de la manière suivante :

![Diagramme décisionnel Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_1.png %})

![Diagramme décisionnel Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_2.png %})

Ceci entraîne l'affichage du message suivant :

![Diagramme décisionnel Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_3.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## Configuration de l'intégration SFMC

Decisioning Studio Pro prend en charge l'intégration native avec Salesforce Marketing Cloud. Decisioning Studio déclenche des événements API dans un parcours avec les données nécessaires pour remplir les éléments dynamiques.

La configuration de l'orchestration pour SFMC est similaire pour Decisioning Studio Pro et Decisioning Studio Go. Pour obtenir des instructions détaillées sur la configuration de l'intégration SFMC, veuillez suivre les [instructions SFMC]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/) fournies dans la documentation Decisioning Studio Go.

{% endtab %}
{% tab Klaviyo %}

## Configuration de l'intégration Klaviyo

Decisioning Studio Pro prend en charge l'intégration native avec Klaviyo. Decisioning Studio déclenche des événements API dans un flux avec les données nécessaires pour remplir les éléments dynamiques.

La configuration de l'orchestration pour Klaviyo est similaire pour Decisioning Studio Pro et Decisioning Studio Go. Pour obtenir des instructions détaillées sur la configuration de l'intégration Klaviyo, veuillez suivre les [instructions Klaviyo]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/) fournies dans la documentation Decisioning Studio Go.

{% endtab %}
{% tab Other CEPs %}

## Configuration d'autres intégrations CEP

Decisioning Studio peut réaliser l'intégration avec n'importe quelle plateforme d'engagement client. Cependant, cela peut nécessiter un travail d'ingénierie personnalisé de la part de votre équipe, car Decisioning Studio n'est pas un déclencheur direct des communications.

Dans ce scénario, l'agent fournira un « dossier de recommandation ». Ce fichier contient des lignes pour chaque client, avec des colonnes qui indiquent toutes les décisions de personnalisation pour ce client.

Par exemple, le fichier de recommandations suivant :

![Diagramme décisionnel Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_2.png %})

Peut être utilisé pour optimiser une campagne par e-mail qui ressemble à ce qui suit :

![Diagramme décisionnel Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_1.png %})

{% endtab %}
{% endtabs %}

## Étapes suivantes

Après avoir configuré l'orchestration, veuillez procéder à la conception de votre agent :

- [créez votre agent]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/design_your_agent/)

