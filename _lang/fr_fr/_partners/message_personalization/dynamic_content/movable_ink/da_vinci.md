---
title: "Encre mobile Da Vinci"
article_title: Encre mobile Da Vinci
alias: "/partners/movable_ink_da_vinci/"
description: "L'intégration de Braze et Movable Ink Da Vinci permet aux marques de diffuser des messages hautement personnalisés en s'appuyant sur le moteur de décision de contenu piloté par l'intelligence artificielle de Da Vinci. Da Vinci sélectionne le contenu le plus pertinent pour chaque utilisateur et déploie les messages de façon fluide/sans heurts/de façon homogène, etc."
page_type: partner
search_tag: Partner

---

# Encre mobile Da Vinci

> L'intégration de Braze et Movable Ink [Da Vinci](https://movableink.com/da-vinci) permet aux marques de diffuser des messages hautement personnalisés en s'appuyant sur le moteur de décision de contenu piloté par l'intelligence artificielle de Da Vinci. Da Vinci sélectionne le contenu le plus pertinent pour chaque utilisateur et déploie les messages de façon fluide/sans heurts/de façon homogène, etc.

## Conditions préalables

| Condition | Description |
|------------|-------------|
| Encre mobile Da Vinci | Un compte Movable Ink Da Vinci est nécessaire pour bénéficier de ce partenariat. |
| Braze Currents - événements d'engagement lié aux messages | Une exportation Braze Custom Currents est nécessaire pour envoyer les données des événements d'engagement aux messages à Movable Ink. |
| Clé d'API REST Braze | Une clé API REST de Braze avec les autorisations `messages.send`, `sends.id.create`, et `campaigns.details` est nécessaire. Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres***> **Clés API**. <br><br>Votre équipe de compte Movable Ink vous fournira directement d'autres instructions de configuration. Reportez-vous à la section [Intégration](#integration).|
| L'instance de l'application Da Vinci en Braze | Créez une instance dédiée à l'application Da Vinci dans Braze. Une nouvelle app peut être créée dans le tableau de bord de Braze en allant dans **Paramètres** > **Paramètres des apps** > **\+ Ajouter une app.** Nommez l'application "**Movable Ink - Da Vinci**" et sélectionnez n'importe quelle plate-forme (la sélection d'une plate-forme est nécessaire mais le type n'a pas d'impact sur la fonctionnalité). En savoir plus sur l ['ajout d'une nouvelle application]({{site.baseurl}}/user_guide/administrative/app_settings/workspaces/#step-3-add-your-app-instances). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

Pour commencer l'intégration, contactez votre équipe de compte Movable Ink pour obtenir de l'aide. Movable Ink vous fournira des instructions d'accès et de configuration en conséquence. Vous devrez fournir à Movable Ink un ensemble d'identifiants API Braze pour permettre à Da Vinci d'envoyer des déploiements d'e-mails via l'API de messagerie de Braze.

Une fois connecté, Movable Ink va :

- Travaillez avec le client et Braze pour configurer le compte Da Vinci de la marque afin de réussir le déploiement avec Braze.
- Capturez des configurations spécifiques à votre marque pour les aligner sur les cas d'utilisation de vos messages.
- Effectuez des tests complets et une assurance qualité pour valider que les e-mails sont livrés comme prévu et qu'ils répondent à toutes les normes de performance et d'exploitation.
