---
nav_title: Localiser une campagne
article_title: Localiser une campagne
page_order: 3
page_type: reference
description: "Le présent article de référence passe en revue la manière dont l’emplacement de l’utilisateur est récupéré et accessible par la plateforme Braze."
tool:
  - Campagnes

---
# Localiser une campagne

> Le présent article de référence passe brièvement en revue les informations collectées par Braze depuis l’intégration SDK et la manière dont elles sont utilisées pour classifier l’emplacement et personnaliser l’expérience d’un utilisateur. 

SDK Braze recueille automatiquement les données pertinentes pour vous aider à localiser les campagnes. Nos clients envoient quotidiennement du contenu localisé à leur audience afin de garder le contenu pertinent et accessible.

## Détails techniques

Braze recueille automatiquement les informations d’emplacement des appareils de l’utilisateur après l’intégration du SDK. L’emplacement contient un identifiant de langue et de région.

Par exemple, un utilisateur qui a configuré son appareil en anglais (États-Unis) aura la langue `EN`. Le pays de l’utilisateur est obtenu à partir de l’adresse IP de son appareil. Ces filtres seront disponibles dans l’outil de segmentation de Braze sous **Pays et langue**.

![Liste des attributs utilisateur : Âge, Pays, E-mail disponible, Sexe, Langue, Position disponible et Notifications push activées.][7]

Consultez les ressources suivantes pour plus de détails techniques sur la manière dont l’emplacement est récupéré en fonction de votre plate-forme :

- [iOS][1]
- [Android][2]
- [Windows Store][3]
- [Windows Phone][4]

## Internationaliser les campagnes

Vous pouvez profiter de cet identifiant de langue et de nos capacités de personnalisation pour internationaliser les campagnes. Pour plus d’informations sur l’internationalisation, consultez [Campagnes en plusieurs langues][12]

Braze recueille automatiquement la position la plus récente des appareils des utilisateurs (si l’autorisation de positionnement est accordée à votre application). Vous pouvez utiliser ces informations pour exécuter une campagne localisée ciblant les utilisateurs situés dans une zone géographique spécifique. Pour plus d’informations, consultez [Cibler la position][13].

[1]: https://developer.apple.com/library/ios/documentation/MacOSX/Conceptual/BPInternational/LanguageandLocaleIDs/LanguageandLocaleIDs.html
[2]: http://developer.android.com/reference/java/util/Locale.html
[3]: http://msdn.microsoft.com/en-us/library/windows/apps/dd373814.aspx
[4]: http://msdn.microsoft.com/en-us/library/windowsphone/develop/dd373814(v=vs.85).aspx
[7]: {% image_buster /assets/img_archive/language-filter-select.png %}
[12]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages
[13]: {{site.baseurl}}/user_guide/engagement_tools/segments/location_targeting/#location-targeting
