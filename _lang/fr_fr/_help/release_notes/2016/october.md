---
nav_title: octobre
page_order: 3
noindex: true
page_type: update
description: "Cet article contient les notes de version d’octobre 2016."
---

# Octobre 2016

## Nouveaux paramètres de sécurité
Nous avons ajouté des fonctionnalités de sécurité améliorées à Braze, notamment des règles d'expiration des mots de passe, des règles de longueur des mots de passe, des règles de complexité des mots de passe, l'autorisation de connexion IP du tableau de bord et l'authentification à deux facteurs.

> Mise à jour : Les **paramètres de sécurité** de Braze, accessibles depuis la page **Paramètres de l’entreprise**, comprennent également des règles de réutilisation et d'expiration des mots de passe.

## Téléchargement d’un CSV après importation
Les utilisateurs de Braze peuvent désormais télécharger un CSV des utilisateurs récemment importés. Cela vous donne plus de visibilité sur la synchronisation des données dans vos systèmes. En savoir plus sur l'[importation de fichiers CSV.]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/)

## Filtre d’anniversaire
En plus du [filtre d'anniversaire]({{site.baseurl}}/user_guide/Engagement_Tools/Segments/Segmentation_Filters/), Braze prend désormais en charge un filtre d'anniversaire qui vous donne la possibilité de cibler les utilisateurs en fonction d'une date de calendrier pour les jalons de fidélité, les avis de recharge, et bien plus encore ! Accédez à cette fonction en sélectionnant le filtre « Date of Custom Attribute » (Date de l’attribut personnalisé) sur la page Segments. En savoir plus sur les [filtres]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#segmentation-filters).

## Mises à jour des limites de fréquence
Auparavant, une campagne ou un canvas qui ignorait les limites de fréquence pouvait toujours être pris en compte dans le calcul des limites de fréquence. Nous avons modifié le comportement de sorte que, par défaut, les nouvelles campagnes et les Canevas qui n'obéissent pas aux limites de fréquence ne compteront pas non plus pour ces dernières. Ceci est configurable pour chaque campagne et Canvas. En savoir plus sur la [limite de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#frequency-capping).

## Profils de couleurs pour les messages in-app
Nous avons ajouté des [profils de couleurs]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#color-profile) pour les messages in-app, ce qui permet aux clients de réutiliser les schémas de couleurs de leur marque lorsqu'ils créent de nouveaux messages dans Braze.
