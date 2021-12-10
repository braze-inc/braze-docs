---
nav_title: Segment Personas
article_title: Segment Personas
page_order: 1.3
alias: /fr/partners/segment_personas/
description: "Cet article décrit le partenariat entre Braze et Segment, une plateforme de données client qui collecte et achemine des informations entre les sources de votre pile marketing."
page_type: partenaire
search_tag: Partenaire
---

# Segment Personas

{% include video.html id="RfOHfZ34hYM" align="right" %}

> Cet article donnera un aperçu de [la connexion entre Braze et Segment Personas](https://segment.com/docs/destinations/braze/#personas), en plus de décrire les exigences et les processus de mise en œuvre et d'utilisation appropriées.

Si vous recherchez des informations sur l'intégration des courants avec Segment, reportez-vous à [Segment for Currents]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents/). Si vous recherchez notre intégration régulière (côte à côte ou serveur-à-serveur) avec Segment, reportez-vous à [Segment]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/).

## À propos de Segment Personas

[Personas](https://segment.com/docs/personas/) est le constructeur d'audience intégré de Segment. Vous pouvez aller sur votre tableau de bord de segment et créer des segments d'utilisateurs en fonction des données que vous avez déjà collectées à travers différentes sources.

De là, ces segments seront assignés à un attribut [personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/) dans un profil utilisateur Braze (uniquement pour les utilisateurs qui ont déjà des identifiants d'utilisateur) qui indique s'ils tombent dans un certain public ou non.

## Exigences

Avant de pouvoir accéder et utiliser les Personas de Segment, vous devez avoir déjà [configuré Braze comme destination]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/) votre intégration de Segment, y compris en entrant les bons "Appboy Data Center" et "Braze REST API Key" dans votre destination [Paramètres de connexion]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/#connection-settings).

## Temps de synchronisation

Bien que le paramètre par défaut pour la connexion Braze à Segment Personas soit `en temps réel`, il y a des filtres qui empêcheront la personne de se synchroniser en temps réel, y compris certains filtres basés sur le temps qui restreignent la taille de votre public au moment de l'envoi du message.

## Test du débogueur de segment

Le tableau de bord du segment fournit une fonctionnalité "Debugger" qui permet aux clients de vérifier si les données d'une "ource" sont transférées vers une "Destination" comme prévu.

Cette fonctionnalité se connecte aux [utilisateurs/terminaux de Braze]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint), ce qui signifie qu'il ne peut être utilisé que pour les utilisateurs identifiés (utilisateurs qui ont déjà un identifiant utilisateur pour leur profil utilisateur Braze).

Avant de pouvoir accéder et utiliser les Personas de Segment, vous devez avoir déjà [configuré Braze comme destination]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/) votre intégration de Segment, y compris en entrant les bons "Appboy Data Center" et "Braze REST API Key" dans votre destination [Paramètres de connexion]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/#connection-settings)


Cela ne fonctionnera pas pour une intégration de Braze côte à côte. Si vous n'avez pas saisi les informations correctes de Braze REST API, alors aucune donnée de serveur ne passera par là.
