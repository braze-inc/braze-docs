---
nav_title: Centres de données
article_title: Centres de données
page_order: 1
page_type: reference
description: "Cet article de référence fournit des informations sur les centres de données, notamment sur leur emplacement/localisation et sur la manière de s'inscrire à des centres de données spécifiques à une région."
---

# Centres de données

> Les centres de données de Braze sont créés pour vous offrir des options sur l'endroit où les données de vos utilisateurs sont traitées et stockées. Vous pouvez ainsi gérer efficacement vos risques liés à la souveraineté, à la flexibilité et à la gestion des données.

## Comment cela fonctionne-t-il ?

Braze exploite plusieurs centres de données situés dans différents emplacements/localisations à travers le monde. Ces centres de données permettent à nos services d'être fiables et évolutifs. Cette répartition géographique permet de minimiser le temps de latence, c'est-à-dire le temps que mettent les données à voyager entre le serveur et l'utilisateur. 

Cela signifie également que lorsqu'un utilisateur interagit avec votre appli ou votre site web, ses demandes sont dirigées vers le centre de données le plus proche, ce qui optimise les performances et réduit les temps de chargement. En se connectant au centre de données le plus proche, vos utilisateurs peuvent bénéficier de temps de chargement rapides, ce qui est particulièrement important pour l'envoi de messages en temps réel et l'importation d'utilisateurs.

Imaginons que vous ayez une application mobile qui envoie des notifications push aux utilisateurs. Si un utilisateur de Melbourne reçoit une notification, la demande d'envoi de cette notification est acheminée vers le centre de données le plus proche en Australie. Dans le cas où l'application mobile connaîtrait une recrudescence d'utilisateurs lors d'un événement promotionnel, Braze dispose d'une infrastructure évolutive avec plusieurs centres de données capables de gérer l'augmentation de la demande.

## Liste des centres de données

### Australie

{% multi_lang_include data_centers.md datacenters='AU' %}

### Union européenne

{% multi_lang_include data_centers.md datacenters='EU' %}

### Indonésie

{% multi_lang_include data_centers.md datacenters='ID' %}

### États-Unis

{% multi_lang_include data_centers.md datacenters='US' %}

## Inscription à des centres de données spécifiques à une région

Lors de l'inscription à votre compte Braze, vous pouvez vous inscrire à des centres de données spécifiques à une région. Contactez votre gestionnaire de compte pour obtenir des informations et des recommandations sur les centres de données qui vous conviennent le mieux en fonction des régions géographiques de vos utilisateurs.
