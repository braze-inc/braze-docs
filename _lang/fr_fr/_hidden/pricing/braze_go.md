---
nav_title: Braze Go
permalink: "/braze_go/"
hidden: true
noindex: true
hide_toc: true
---

# Braze Go

> Braze Go offre un accès simplifié à la plateforme d'engagement client Braze pour aider vos équipes marketing à commencer n'importe où et à aller partout. Conçu pour être simple et efficace, Braze Go est adapté à certains marchés émergents.

{% alert important %}
Braze Go n'est pas disponible sur tous les marchés. Si vous souhaitez en savoir plus sur Braze Go, contactez votre gestionnaire de compte.
{% endalert %}

Braze Go offre toutes les mêmes fonctionnalités que Braze, avec les changements ciblés sur les fonctionnalités suivantes : 

- Vous pouvez avoir jusqu'à 30 campagnes actives.
- Vous pouvez avoir jusqu'à 20 toiles actives.
- La limite de débit totale par défaut de l'API REST est de 50 000 par heure et par espace de travail.
    - Pour une utilisation autre que celle de Braze Go, renseignez-vous sur les [limites de l'API REST.]({{site.baseurl}}/api/api_limits/#rate-limits-by-request-type)
- Les données relatives aux campagnes et aux interactions avec le Canvas sont conservées pendant deux mois, sans possibilité de restauration.
    - Pour une utilisation hors Braze Go, renseignez-vous sur la [disponibilité des données d’interaction de messagerie]({{site.baseurl}}/messaging_interaction_data/).

{% alert note %}
Les données d'interaction pour les campagnes et les Canvases sont différentes des données de Snowflake et n'ont aucun effet.
{% endalert %}

- Les webhooks Braze à Braze ne sont pas pris en charge.
- Les filtres liés aux tags ne sont pas pris en charge, en particulier les filtres suivants :
    - Campagne ou canvas cliqué ou ouvert avec étiquette
    - Dernier message reçu d'une campagne ou d'un canvas avec étiquette
    - Campagne ou Canvas avec balise reçu
- Braze peut également mettre en œuvre une politique de conservation des données pour les événements du profil utilisateur et les données d'achat qui supprime les événements, les achats ou les deux datant de plus d'un an qui n'ont pas été effectués à nouveau dans un délai d'un an. Toutefois, ces données resteront disponibles dans les extensions de segments SQL pendant 2 ans.

Si l'une des fonctionnalités ci-dessus est mise à jour, cela sera reflété dans cet article et indiqué dans nos [notes de version]({{site.baseurl}}/help/release_notes/#most-recent-braze-release-notes).