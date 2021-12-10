---
nav_title: Localisation d'une campagne
article_title: Localisation d'une campagne
page_order: 3
page_type: Référence
description: "Cet article de référence décrit comment la locale de l'utilisateur est récupérée et consultée par la plateforme Braze."
tool:
  - Campagnes
---

# Localisation d'une campagne

> Cet article de référence passe brièvement sur les informations que Braze recueille à partir de l'intégration SDK et comment il est utilisé pour classer la locale et personnaliser l'expérience d'un utilisateur.

Braze collecte automatiquement des données pertinentes pour vous aider à localiser des campagnes. Nos clients envoient quotidiennement du contenu localisé à leur public afin de garder le contenu pertinent et accessible.

## Détails techniques

Braze collecte automatiquement les informations locales des périphériques utilisateur après que le SDK a été intégré. La locale contient un identifiant de langue et de région.

Par exemple, un utilisateur qui a mis son appareil en français (US) aura une langue `EN`. Le pays des utilisateurs est collecté à partir de l'adresse IP de leur appareil. Ces filtres seront disponibles dans l'outil de segmentation de Braze sous Pays et Langue.

!\[Filtre Select Screenshot\]\[7\]

Plus de détails techniques sur la façon dont la locale est récupérée peut être accédée par la plateforme :

- [iOS][1]
- [Android][2]
- [Magasin Windows][3]
- [Windows Phone][4]

## Internationaliser les campagnes

Vous pouvez profiter de cet identifiant de langue et de nos capacités de personnalisation pour internationaliser les campagnes. Pour plus d'informations sur l'internationalisation, voir [Campagnes dans plusieurs langues][12]

Braze collecte automatiquement la position la plus récente des appareils des utilisateurs (si l'autorisation de localisation est accordée à votre application). Vous pouvez utiliser ces informations pour lancer une campagne localisée ciblant les utilisateurs dans une zone géographique spécifique. Pour plus d'informations, voir [ciblage de l'emplacement][13].
[7]: {% image_buster /assets/img_archive/language-filter-select.png %}

[1]: https://developer.apple.com/library/ios/documentation/MacOSX/Conceptual/BPInternational/LanguageandLocaleIDs/LanguageandLocaleIDs.html
[2]: http://developer.android.com/reference/java/util/Locale.html
[3]: http://msdn.microsoft.com/en-us/library/windows/apps/dd373814.aspx
[4]: http://msdn.microsoft.com/en-us/library/windowsphone/develop/dd373814(v=vs.85).aspx
[12]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages
[13]: {{site.baseurl}}/user_guide/engagement_tools/segments/location_targeting/#location-targeting
