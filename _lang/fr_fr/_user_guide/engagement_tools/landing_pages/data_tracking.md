---
nav_title: Suivi des données
article_title: Suivi des données
description: "Cet article traite des données qui sont suivies sur les pages d'atterrissage."
page_order: 3
alias: /landing_pages/data_tracking/
---

# Suivi des données

> Les pages d'atterrissage de Braze utilisent une version du SDK web de Braze pour suivre les données des utilisateurs uniquement lorsqu'un formulaire de la page d'atterrissage est soumis. Les informations qui ne sont pas associées à un utilisateur spécifique, y compris les pages vues et le nombre global de clics sur les boutons, sont collectées sans le SDK.<br><br>Cette page couvre les données du SDK web et les données anonymes qui sont suivies sur les pages de destination.

## Méthodes de suivi

### Web SDK

Le SDK web de Braze n'est initialisé que lorsqu'un utilisateur soumet un formulaire sur la page de renvoi. Avant la soumission du formulaire, aucune donnée personnelle n'est collectée et le SDK ne suit pas activement les utilisateurs. Une fois l'initialisation terminée, le SDK ne stocke aucune donnée dans le navigateur (comme les cookies, le stockage local ou autres).

Lorsqu'un formulaire est soumis, le SDK recueille les données suivantes :

- Événement de soumission du formulaire (nom de l'événement et heure de soumission)
- Données spécifiées par votre équipe dans le formulaire (telles que le nom, l'e-mail et le numéro de téléphone).
- Heure de début de la session
- ID de l'appareil (un ID unique généré, mais non stocké, pour l'appareil)
- Pays déterminé par l'adresse IP

### Données anonymes

Avant qu'un utilisateur ne soumette un formulaire, les données suivies sur une page de renvoi sont uniquement constituées d'informations anonymes et non identifiables. Il s'agit d'indicateurs globaux standard pour les sites web, comme le nombre de pages vues (impressions) et de clics qu'une page de renvoi reçoit.

Ces données n'étant pas liées à des utilisateurs identifiables, elles ne peuvent pas être utilisées pour recibler ou suivre le comportement d'utilisateurs individuels.

