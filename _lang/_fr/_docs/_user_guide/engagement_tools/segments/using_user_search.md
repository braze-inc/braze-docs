---
nav_title: Utiliser la recherche d'utilisateur
article_title: Utiliser la recherche d'utilisateur
page_order: 5
page_type: Référence
tool:
  - Tableau de bord
description: "Cet article de référence décrit comment utiliser la recherche utilisateur dans le tableau de bord et présente certains cas d'utilisation de la recherche utilisateur."
---

# Utiliser la recherche utilisateur

> Cet article de référence va comprendre comment utiliser la recherche d'utilisateur dans le tableau de bord, les différents composants impliqués dans un profil d'utilisateur, et présente quelques exemples de comment cette fonctionnalité peut être utilisée pour résoudre des campagnes.

## Aperçu des fonctionnalités

La fonction **Recherche d'utilisateur** vous permet de visualiser les profils d'utilisateurs. Les profils des utilisateurs sont un excellent moyen de trouver des informations sur des utilisateurs spécifiques. La fonction de recherche des utilisateurs se trouve dans la section Utilisateurs du tableau de bord Braze.

!\[User_Search\]\[7\]

Vous pouvez rechercher votre base d'utilisateurs à l'aide de l'e-mail ou de l'identifiant de l'utilisateur. La plupart du temps, la recherche de l'utilisateur retournera un résultat, mais notez que si vous entrez un courriel non unique (i.e. un email qui appartient à plus d'un utilisateur) dans la recherche d'utilisateur, il retournera plus d'un profil d'utilisateur. Une fois que vous avez entré un e-mail ou un identifiant d'utilisateur dans la **Recherche d'utilisateur**, vous pourrez voir les informations que vous avez enregistrées sur cet utilisateur avec le Braze SDK. Si vous entrez un e-mail non unique, cliquer sur le suivant vous permettra de visualiser les autres profils qui sont associés à cet e-mail.

!\[Nonunique_User_Search\]\[14\]

## Cas d'utilisation

La fonctionnalité **Recherche Utilisateur** est une excellente ressource pour le dépannage et le test car vous pouvez facilement accéder à des informations sur l'historique d'engagement d'un utilisateur. l'adhésion au segment, l'appareil et le système d'exploitation.

Par exemple, si un utilisateur signale un problème et que vous n'êtes pas sûr de quel périphérique et système d'exploitation il utilise, vous pouvez utiliser l'onglet [Aperçu](#overview-tab) pour trouver ces informations (à condition que vous ayez leur e-mail ou leur identifiant d'utilisateur). Vous pouvez également voir la langue d'un utilisateur qui pourrait être utile si vous effectuez un dépannage d'une [campagne multilingue][13] qui ne se comportait pas comme prévu.

Vous pouvez utiliser l'onglet [Engagement](#engagement-tab) pour vérifier si un certain utilisateur a reçu une campagne. En outre, si cet utilisateur a reçu la campagne, vous pouvez voir quand il l'a reçue. Vous pouvez également vérifier si un utilisateur est dans un certain segment, et si un utilisateur est choisi pour push, e-mail ou les deux. Ces informations sont utiles à des fins de dépannage. Par exemple, vous devriez vérifier ces informations si un utilisateur ne reçoit pas une campagne que vous attendiez qu'il reçoive ou reçoive une campagne que vous ne vous attendiez pas à recevoir.

## Onglet Aperçu {#overview-tab}

Dans l'onglet **Aperçu** vous pouvez voir des informations sur le profil de l'utilisateur, l'utilisation de l'application, attributs personnalisés, événements personnalisés, achats, et le périphérique le plus récent sur lequel l'utilisateur s'est connecté. Pour plus d'informations sur ces données, voir [Collecte de données utilisateur][12].

!\[User_Search_Overview\]\[8\]

## Onglet Engagement {#engagement-tab}

Vous pouvez cliquer sur l'onglet **Engagement** pour afficher des informations sur les paramètres de contact de l'utilisateur, Campaigns Received, Segments, Communication Stats, Install Attribution, News Feed Cards Clicked and Random Bucket #.

!\[User_Search_Engagement\]\[9\]

## Social tab {#social-tab}

L'onglet **Social** vous permet de voir les comptes sociaux qu'un utilisateur a connectés à l'application. Vous pouvez également voir l'activité d'un utilisateur sur ces comptes sociaux connectés.

!\[User_Search_Social\]\[11\]
[7]: {% image_buster /assets/img_archive/user_search2.png %} [8]: {% image_buster /assets/img_archive/user_profile2.png %} [9]: {% image_buster /assets/img_archive/User_Profile_Engagement. ng %} [11]: {% image_buster /assets/img_archive/User_Profile_Social.png %} [14]: {% image_buster /assets/img_archive/User_Search_Nonunique.png %}

[12]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/
[13]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages
