---
nav_title: Octobre
page_order: 3
noindex: true
page_type: update
description: "Cet article contient les notes de version d’octobre 2016."
---

# Octobre 2016

## Nouveaux paramètres de sécurité
Nous avons ajouté des fonctions de sécurité améliorées dans Braze, notamment des règles d’expiration, de longueur et de complexité des mots de passe, une liste blanche d’adresses IP pour se connecter au tableau de bord et une authentification à deux facteurs.

> Mise à jour : Les **Security Settings** (Paramètres de sécurité) de Braze, accessibles depuis votre page **Company Settings** (Paramètres de l’entreprise), comprennent également des règles pour la réutilisation et l’expiration des mots de passe.

## Téléchargement d’un CSV après importation
Les utilisateurs de Braze peuvent désormais télécharger un CSV des utilisateurs récemment importés. Cela vous donne plus de visibilité sur la synchronisation des données dans vos systèmes. En savoir plus sur les [Importations CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/).

## Filtre d’anniversaire
En plus du [filtre basé sur le jour de naissance]({{site.baseurl}}/user_guide/Engagement_Tools/Segments/Segmentation_Filters/), Braze prend désormais en charge un filtre d’anniversaire qui vous donne la possibilité de cibler les utilisateurs en fonction d’une date de calendrier pour les jalons de fidélité, les avis de remplacement et bien plus encore ! Accédez à cette fonction en sélectionnant le filtre « Date of Custom Attribute » (Date de l’attribut personnalisé) sur la page Segments. En savoir plus sur les [filtres]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#segmentation-filters).

## Mises à jour des limites de fréquence
Auparavant, une campagne ou un Canvas qui ignorait les limites de fréquence était toujours comptabilisé dans les limites de fréquence. Nous avons apporté une modification pour que, par défaut, les nouvelles campagnes et les nouveaux Canvas qui n’obéissent pas aux limites de fréquence ne soient pas comptabilisés dans ces limites. Ceci est configurable pour chaque campagne et Canvas. En savoir plus sur les [limites de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#frequency-capping).

## Profils de couleurs pour les messages in-app
Nous avons ajouté des [profils de couleurs]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#color-profile) pour les messages in-app afin de permettre aux clients de réutiliser des thèmes de couleurs de leur marque lors de la création de nouveaux messages dans Braze.
