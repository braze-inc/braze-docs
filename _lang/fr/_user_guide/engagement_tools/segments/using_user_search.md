---
nav_title: Utilisation de la fonction User Search
article_title: Utilisation de la fonction User Search
page_order: 5
page_type: reference
tool: 
  - Tableau de bord
description: "Cet article de référence explique comment utiliser la fonction User Search (Recherche d’utilisateurs) de votre tableau de bord et présente quelques cas d’utilisation de cette fonction."

---

# Utilisation de la fonction User Search

> Cet article de référence explique comment utiliser la fonction User Search (Recherche d’utilisateurs) de votre tableau de bord et quels sont différents composants impliqués dans un profil utilisateur. Vous découvrirez également quelques exemples de la manière dont cette fonctionnalité peut être utilisée pour résoudre des problèmes liés aux campagnes. 

## Présentation de la fonction User Search

La fonction **User Search (Recherche d’utilisateurs)** vous permet de consulter des profils d’utilisateur. Les profils d’utilisateurs sont un excellent moyen de trouver des informations sur des utilisateurs spécifiques. Cette fonction se trouve dans la section **Users (Utilisateurs)** du tableau de bord de Braze.

![][7]

Vous pouvez effectuer une recherche dans votre base d’utilisateurs en vous servant de l’adresse e-mail ou de l’ID d’un utilisateur. La plupart du temps, la fonction User Search (Recherche d’utilisateurs) renverra un résultat, mais notez que si vous saisissez une adresse e-mail non unique dans la recherche (autrement dit, une adresse e-mail appartenant à plus d’un utilisateur), les résultats incluront plus d’un profil utilisateur. Après avoir saisi une adresse e-mail ou un ID utilisateur dans la fonction **User Search (Recherche d’utilisateurs)**, vous pourrez afficher les informations que vous avez enregistrées sur cet utilisateur avec le SDK de Braze. Si vous saisissez une adresse e-mail non unique, cliquez sur **Next (Suivant)** pour afficher les autres profils associés à cette adresse e-mail.

![][14]

## Cas d’utilisation

La fonction **User Search (Recherche d’utilisateurs)** est une excellente option pour résoudre des problèmes ou effectuer des tests, car elle permet d’accéder facilement à des informations sur l’historique d’engagement d’un utilisateur, son appartenance à un segment, son appareil et son système d’exploitation.

Par exemple, si un utilisateur signale un problème et que vous n’êtes pas sûr de l’appareil et du système d’exploitation qu’il utilise, vous pouvez utiliser l’onglet [Overview (Aperçu)](#overview-tab) pour trouver ces informations (tant que vous connaissez leur adresse e-mail ou leur ID utilisateur). Vous pouvez également afficher la langue d’un utilisateur, ce qui pourrait être utile si vous résoudre des problèmes avec une [campagne multilingue][13] qui ne se comporte pas comme prévu.

Vous pouvez utiliser l’onglet [Engagement](#engagement-tab) pour vérifier si un utilisateur a bien reçu une campagne. De plus, si cet utilisateur a effectivement reçu la campagne, vous pouvez voir quand il l’a reçue. Vous pouvez également vérifier si un utilisateur se trouve dans un certain segment, et si un utilisateur s’est abonné aux notifications push, aux communications par e-mail ou les deux. Ces informations sont utiles pour la résolution des problèmes. Par exemple, vous devez vérifier ces informations si un utilisateur n’a pas reçu une campagne qu’il devait recevoir ou s’il reçoit une campagne qui ne lui était pas destinée.

## Onglet Overview {#overview-tab}

Dans l’onglet **Overview (Aperçu)**, vous pouvez voir des informations sur le profil utilisateur, l’utilisation de l’application, les attributs personnalisés, les événements personnalisés, les achats et le dernier appareil avec lequel il s’est connecté. Pour plus d’informations sur ces données, consultez l’article [Collecte des données utilisateur][12].

![][8]

## Onglet Engagement {#engagement-tab}

Vous pouvez cliquer sur l’onglet **Engagement** pour afficher des informations sur les paramètres de contact de l’utilisateur, les campagnes reçues, les segments, les statistiques de communication, l’attribution d’installation, les cartes de fil d’actualité et le numéro de compartiment aléatoire.

![][9]

## Onglet Social {#social-tab}

L’onglet **Social** vous permet de voir les comptes de réseaux sociaux qu’un utilisateur a connectés à votre application. Vous pouvez également afficher l’activité d’un utilisateur sur ces comptes sociaux connectés.

![][11]

[7]: {% image_buster /assets/img_archive/user_search2.png %}
[8]: {% image_buster /assets/img_archive/user_profile2.png %}
[9]: {% image_buster /assets/img_archive/User_Profile_Engagement.png %}
[11]: {% image_buster /assets/img_archive/User_Profile_Social.png %}
[12]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/
[13]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages
[14]: {% image_buster /assets/img_archive/User_Search_Nonunique.png %}
