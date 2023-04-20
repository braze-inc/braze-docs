---
nav_title: Préférences de notification push détaillées
article_title: Préférences de notification push détaillées
page_order: 1.5
page_type: reference
description: "Le présent article couvre les bonnes pratiques pour la création de préférences de notification push détaillées pour vos utilisateurs."
channel: push

---

# Préférences de notification push détaillées

> Les notifications push doivent être traitées avec précaution pour cibler les utilisateurs avec des notifications opportunes et pertinentes. Braze collectera des informations utiles sur l’appareil et l’utilisation qui peuvent être utilisées pour cibler les segments pertinents. Elles doivent être complétées par des événements personnalisés et des attributs spécifiques à votre application. À l’aide de ces données, vous pouvez cibler soigneusement les messages pour augmenter les taux d’ouverture et réduire le nombre d’utilisateurs désactivant les notifications push.

De plus, vous pouvez créer une page de paramètres dans votre application qui permet aux utilisateurs de vous dire directement quelles notifications ils souhaitent recevoir. Cela peut être défini en tant qu’attribut booléen dans Braze correspondant au statut de paramétrage l’application. Par exemple, une application d’actualités peut avoir des paramètres d’abonnement pour les éditions spéciales, les actualités sportives ou politiques.

Lorsque l’application d’actualités souhaite créer une campagne ciblant uniquement les utilisateurs intéressés par la politique, il suffit d’ajouter le filtre d’attribut « Abonné aux actualités politiques » au segment. Lorsqu’il est défini sur « vrai », seuls les utilisateurs qui s’abonnent aux notifications les recevront.

Les statistiques générales que vous voyez pour l’activation des notifications push se rapportent au fait que l’utilisateur a approuvé ou non les notifications avec le système d’exploitation. Si les utilisateurs désactivent les notifications sur iOS, ils seront automatiquement supprimés de notre système, car Apple ne permettra pas l’envoi du jeton de notification push. Android 13 et ultérieurs demandent d’obtenir une autorisation avant que les notifications push puissent être affichées. Les versions plus anciennes d’Android abonneront par défaut les utilisateurs aux notifications.

Reportez-vous aux articles suivants pour définir des attributs personnalisés basés sur votre plate-forme :
- [iOS][4]
- [Android][5]
- [API REST][10]

[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_custom_attributes/
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/#setting-custom-attributes
[10]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-attributes-object-specification
[46]:{% image_buster /assets/img_archive/Push_Window8_Toast.png %}
[47]:{% image_buster /assets/img_archive/Push_Windows_Universal_Toast.png %}
