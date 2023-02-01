---
nav_title: Raccourcissement de lien
article_title: Raccourcissement de lien
page_order: 5
description: "Cet article de référence explique comment activer le raccourcissement de lien dans vos messages SMS ainsi que certaines questions fréquentes."
page_type: reference
tool:
  - Campagnes
channel:
  - SMS
---

# Raccourcissement de lien

> Le raccourcissement de lien et le suivi des clics vous permettent de raccourcir automatiquement les URL contenues dans les messages SMS et de recueillir des analyses du taux de clics, fournissant ainsi des indicateurs d’engagement supplémentaires pour comprendre le comportement des utilisateurs dans le cadre de vos campagnes SMS. 

## Overview

Le raccourcissement de lien et le suivi des clics peuvent être activés au niveau de la [variante de message]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#step-1-create-your-campaign) dans les campagnes et les Canvas. Les liens sont raccourcis avec un domaine court partagé spécifique à Braze ([brz.ai](http://brz.ai)), d’une longueur d’environ 20-21 caractères. Une URL exemple peut ressembler à ceci : `https://brz.ai/8jshX`

Les URL raccourcies seront valides pendant un an à compter de la date de création.

Pour activer le raccourcissement de lien, assurez-vous que la fonctionnalité est activée dans le l’éditeur de message.

![][1]

Pour que Braze reconnaisse les URL, elles doivent commencer par _http://_  ou  _https://_. Lorsqu’une URL est reconnue, le volet **Aperçu** est mis à jour avec une URL fictive. Notez que le nombre de caractères dans l’onglet **Composition** exclut toute personnalisation du raccourcissement de lien.

![][3]

## Test

Nous vous recommandons toujours de prévisualiser et de tester votre message avant de lancer une campagne ou un Canvas. 

Naviguez jusqu’a l’onglet **Test** pour afficher un aperçu et envoyer un SMS à des [groupes de test de contenu]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab#content-test-groups) ou à un seul utilisateur. L’aperçu sera mis à jour avec la personnalisation pertinente et l’URL raccourcie. Le nombre de caractères et les [segments facturables]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/) seront également mis à jour pour refléter la personnalisation rendue et l'URL raccourcie. 

Assurez-vous d’enregistrer la campagne ou le Canvas avant d’envoyer un message test pour recevoir l’URL raccourcie qui sera expédiée dans votre message. Si la campagne ou le Canvas n’est pas enregistré avant un envoi test, ce dernier comportera une URL fictive.

![][2]

{% alert note %}
La personnalisation de Liquid et les URL raccourcies permettent de créer des modèles dans l’onglet **Test** après avoir sélectionné un utilisateur. Assurez-vous que l’utilisateur est sélectionné pour recevoir un nombre de caractères précis !
{% endalert %}

## Suivi des clics

Lorsque le raccourcissement de lien est activé, le tableau des performances relatif aux SMS et MMS comprend alors une colonne intitulée **Total des clics**, correspondant au nombre total d’événements de clic par variante et au taux de clics associé. Pour plus d’informations sur les métriques SMS, consultez les [performances de message SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/#message-performance).

![][4]

Le graphique de présentation des SMS et de l’historique des performances comprend également une option **Nombre total de clics** et affiche le nombre d’événements de clic par jour.

## Foire aux questions

#### Combien de temps les URL raccourcies sont-elles valides ?

Les URL raccourcies font entre 20 et 21 caractères.

#### Le raccourcissement des liens fonctionne-t-il avec les URL contenant Liquid ?

Non. Actuellement, seules les URL statiques font l’objet d’un raccourcissement.

#### Les liens que je reçois lors des tests sont-ils de vraies URL ?

Si la campagne a été enregistrée comme ébauche avant l’envoi test, alors oui ! Sinon, il s’agit d’une URL fictive. 

#### Le SDK Braze doit-il être installé pour raccourcir des liens ?

Non, le raccourcissement de lien fonctionne indépendamment de toute intégration SDK.

#### Est-ce que je peux indiquer mon propre domaine de raccourcisseur de liens personnalisé ?

Pas encore, bien que nous prévoyions de proposer davantage d’options de personnalisation à l’avenir.

#### Est-il possible de savoir quels utilisateurs cliquent sur une URL ?

Pas encore. Cela fera partie d’une mise à jour concernant le suivi des clics pour les utilisateurs.

#### Est-il possible d’ajouter des paramètres UTM à une URL avant qu’elle ne devienne courte ?

Oui ! Tous les paramètres d’URL statiques peuvent être ajoutés. 

#### Combien de temps les URL raccourcies restent-elles valides ?

Un an.

#### Le raccourcissement de lien fonctionne-t-il avec les liens profonds ou les liens universels ?

Le raccourcissement de lien ne fonctionnera que pour les URL statiques commençant par  _http://_  ou  _https://_. Il n’est pas conseillé de raccourcir plus les liens universels générés (par des fournisseurs comme Branch ou Firebase), car l’attribution ou la redirection de ces outils pourrait cesser de fonctionner.

[1]: {% image_buster /assets/img/link_shortening/shortening1.png %} 
[2]: {% image_buster /assets/img/link_shortening/shortening2.png %} 
[3]: {% image_buster /assets/img/link_shortening/shortening3.png %} 
[4]: {% image_buster /assets/img/link_shortening/shortening4.png %} 
