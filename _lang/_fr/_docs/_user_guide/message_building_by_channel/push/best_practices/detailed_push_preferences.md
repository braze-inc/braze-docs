---
nav_title: Préférences détaillées des Push
article_title: Préférences détaillées des Push
page_order: 1
page_type: Référence
description: "Cet article couvre les meilleures pratiques pour créer des préférences push détaillées pour vos utilisateurs."
channel: Pousser
---

# Préférences push détaillées

Les notifications push doivent être traitées avec soin aux utilisateurs ciblés avec des notifications opportunes et pertinentes. Braze recueillera des informations utiles sur l'appareil et l'utilisation qui peuvent être utilisées pour cibler les segments pertinents. Ceci doit être complété par des événements personnalisés et des attributs spécifiques à votre application. En utilisant ces données, vous pouvez soigneusement cibler les messages pour augmenter les taux d'ouverture et diminuer les cas de désactivation de push.

De plus, vous pouvez créer une page de paramètres dans votre application qui permet aux utilisateurs de vous dire directement quelles notifications ils veulent recevoir. Cela peut être défini comme un attribut booléen dans Braze qui correspond au statut de réglage de l'application. Par exemple, une application d'actualités pourrait avoir des paramètres d'abonnement pour les suivants :

- Actualités en cours
- Actualités sportives
- Politiques
- Actualités commerciales

Quand l'application de nouvelles veut créer une campagne ciblant uniquement les utilisateurs intéressés par la politique, ils ajoutent simplement le filtre de l'attribut 'S'abonner à la politique' au segment. Quand activé, seuls les utilisateurs qui s'abonnent aux notifications les recevront

Les statistiques générales que vous voyez pour les notifications push activées se rapportent à savoir si l'utilisateur a approuvé les notifications avec l'OS. Si les utilisateurs désactivent les notifications sur iOS, elles seront automatiquement supprimées de notre système car Apple n'autorisera pas l'envoi du jeton push. Android abonne les utilisateurs aux notifications par défaut.

Documentation pour paramétrer les attributs personnalisés :

- [iOS][4]
- [Android][5]
- [Univers Windows][6]
- [API REST][10]
[46]:{% image_buster /assets/img_archive/Push_Window8_Toast.png %} [47]:{% image_buster /assets/img_archive/Push_Windows_Universal_Toast.png %}

[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_custom_attributes/
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/#setting-custom-attributes
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/setting_custom_attributes/
[10]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-attributes-object-specification
