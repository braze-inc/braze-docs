---
nav_title: "Mettre en place l'orchestration"
article_title: "Mettre en place l'orchestration"
page_order: 2
description: "Découvrez comment configurer l'orchestration pour les agents de Decisioning Studio Pro afin de permettre des communications personnalisées."
toc_headers: h2
---

# Mettre en place l'orchestration

> Les agents décisionnels doivent se connecter à une plateforme d'engagement client (CEP) pour orchestrer les communications une fois qu'ils ont ingéré les données client et personnalisé à un niveau 1:1. Cet article explique comment configurer l'intégration pour chaque CEP pris en charge.

## PEC soutenus

Decisioning Studio Pro prend en charge les plateformes d'engagement client suivantes :

| CEP | Type d’intégration | Complexité de la configuration |
|-----|-----------------|------------------|
| **Braze** | Intégration de l'API native | Faible (recommandé) |
| **Salesforce Marketing Cloud** | Événements API natifs + voyages | Moyen |
| **Klaviyo** | Événements de l'API native + flux | Moyen |
| **Autres CEP** | Personnalisé (fichier de recommandation) | Élevée |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Sélectionnez votre CEP ci-dessous pour commencer la configuration de l'intégration.

{% tabs %}
{% tab Braze %}

## Mise en place de l'intégration de Braze

Suivez ces étapes pour intégrer un agent Braze Decisioning Studio aux fonctionnalités d'orchestration de Braze (l'équipe des services de Braze sera à votre disposition pour vous aider) :

### Étape 1 : créez une clé API

Allez dans **Paramètres** > **Clés API**, puis créez une nouvelle clé avec les autorisations suivantes :

{% multi_lang_include decisioning_studio/api_key_permissions.md %}

### Étape 2 : Implanter des campagnes déclenchées par l'API

Implantez une campagne déclenchée par l'API pour chaque modèle de base avec des propriétés de déclenchement de l'API pour toutes les dimensions optimisées.

Un modèle de base est un modèle que l'agent décisionnel peut utiliser pour orchestrer les messages. Un agent décisionnaire peut avoir un ou plusieurs modèles de base, auquel cas le choix du modèle de base approprié pour chaque client sera l'une des décisions que l'agent personnalisera.

### Étape 3 : Configurer la rééligibilité

Assurez-vous que toutes les campagnes déclenchées par l'API permettent aux utilisateurs de redevenir éligibles dans les 15 minutes.

![Diagramme Decisioning Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_frequency_cap.png %})

{% alert note %}
Bien que l'agent de Decisioning Studio n'envoie jamais la même campagne plus d'une fois par jour, vous souhaitez pouvoir envoyer les mêmes campagnes plusieurs fois par jour à des fins de test.
{% endalert %}

### Étape 4 : Ajouter des marques substitutives dynamiques

Ceux-ci servent de marque substitutive dynamique pour les décisions que l'agent du Decisioning Studio est en train d'optimiser.

#### Exemple 1 : Campagne par e-mail

Supposons que l'agent Decisioning Studio optimise une campagne d'e-mailing. La configuration pourrait être la suivante :

![Diagramme Decisioning Pro]({% image_buster /assets/img/decisioning_studio/decisioning_email_example_1.png %})

Supposons que l'agent optimise le choix des modèles et du message d'appel à l'action, une campagne déclenchée par l'API doit être créée pour chaque modèle, et la section d'appel à l'action d'un modèle peut ressembler à ce qui suit :

![Diagramme Decisioning Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_braze_email_example_2.png %})

#### Exemple 2 : Campagne de notification push

Supposons qu'un agent du Decisioning Studio optimise le message d'une campagne de communication. La configuration pourrait être la suivante :

![Diagramme Decisioning Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_1.png %})

![Diagramme Decisioning Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_2.png %})

L'envoi du message suivant apparaît :

![Diagramme Decisioning Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_3.png %})

#### Exemple 3 : Campagne SMS

Supposons que l'agent Decisioning Studio optimise les champs d'une campagne SMS. La configuration pourrait être la suivante :

![Diagramme Decisioning Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_1.png %})

![Diagramme Decisioning Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_2.png %})

L'envoi du message suivant apparaît :

![Diagramme Decisioning Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_3.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## Mise en place de l'intégration du SFMC

Decisioning Studio Pro prend en charge l'intégration native avec Salesforce Marketing Cloud. Decisioning Studio déclenche des événements API dans un parcours avec les données nécessaires pour alimenter les éléments dynamiques.

La configuration de l'orchestration pour SFMC est similaire pour Decisioning Studio Pro et Decisioning Studio Go. Pour connaître les étapes détaillées de la configuration de l'intégration SFMC, suivez les [instructions SFMC]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/) dans la documentation Decisioning Studio Go.

{% endtab %}
{% tab Klaviyo %}

## Mise en place de l'intégration de Klaviyo

Decisioning Studio Pro prend en charge l'intégration native avec Klaviyo. Decisioning Studio déclenche des événements API dans un flux avec les données nécessaires pour alimenter les éléments dynamiques.

La configuration de l'orchestration pour Klaviyo est similaire pour Decisioning Studio Pro et Decisioning Studio Go. Pour connaître les étapes détaillées de la configuration de l'intégration Klaviyo, suivez les [instructions Klaviyo]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/) dans la documentation Decisioning Studio Go.

{% endtab %}
{% tab Other CEPs %}

## Mise en place d'autres intégrations CEP

Decisioning Studio peut s'intégrer à n'importe quelle plateforme d'engagement client. Toutefois, cela peut nécessiter un travail d'ingénierie personnalisé de la part de votre équipe, car Decisioning Studio ne peut pas déclencher de communications directement.

Dans ce scénario, l'agent délivrera un "dossier de recommandation". Ce fichier contient des lignes pour chaque client, avec des colonnes qui indiquent toutes les décisions personnalisées pour ce client.

Par exemple, le fichier de recommandation suivant :

![Diagramme Decisioning Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_2.png %})

Il peut être utilisé pour optimiser une campagne d'e-mail qui ressemble à ce qui suit :

![Diagramme Decisioning Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_1.png %})

{% endtab %}
{% endtabs %}

## Étapes suivantes

Après avoir configuré l'orchestration, passez à la conception de votre agent :

- [créez votre agent]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/design_your_agent/)

