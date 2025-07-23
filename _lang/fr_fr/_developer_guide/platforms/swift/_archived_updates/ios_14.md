---
nav_title: Guide de mise à jour iOS 14
article_title: Guide de mise à jour SDK iOS 14
page_order: 7
platform: iOS
description: "Cet article de référence couvre la mise à jour du SDK iOS 14, mettant en évidence les changements tels que les clôtures géographiques, le ciblage géographique, l’IDFA, etc."
hidden: true
noindex: true
---

# Guide de mise à jour SDK iOS 14

> Ce guide décrit les modifications liées à Braze introduites dans iOS 14 et les étapes de mise à niveau requises pour votre intégration SDK Braze pour iOS. Pour obtenir une liste complète des nouvelles mises à jour d'iOS 14, consultez la [page iOS 14](https://www.apple.com/ios/ios-14/) d’Apple.

{% alert tip %}
À partir d'iOS 14.5, la collecte d'**IDFA** et [certains partages de données](https://developer.apple.com/app-store/user-privacy-and-data-use/#permission-to-track) nécessiteront la nouvelle invite de permission du framework [AppTrackingTransparency](https://developer.apple.com/documentation/apptrackingtransparency) ([en savoir plus](#idfa)).
{% endalert %}

#### Résumé des changements majeurs de l’iOS 14

- Les applications ciblant iOS 14 / Xcode 12 doivent utiliser notre [version officielle d'iOS 14.](https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.27.0)
- Les géorepérages [ne sont plus pris en charge par iOS](https://developer.apple.com/documentation/corelocation/cllocationmanager/3600215-accuracyauthorization) pour les utilisateurs qui choisissent la nouvelle autorisation de _localisation approximative_.
- L’utilisation des fonctions de ciblage « Dernière localisation connue » nécessite une mise à niveau vers le SDK Braze pour iOS v3.26.1+ pour la compatibilité avec l’autorisation de _localisation approximative_. Notez que si vous utilisez XCode 12, vous devrez passer au moins à la mise à jour v3.27.0.
- À partir d'iOS 14.5, la collecte d'IDFA et [certains partages de données](https://developer.apple.com/app-store/user-privacy-and-data-use/#permission-to-track) nécessitent la nouvelle invite de permission du cadre [AppTrackingTransparency.](https://developer.apple.com/documentation/apptrackingtransparency) 
- Si vous utilisez le champ « Suivi des campagnes publicitaires activé » pour le ciblage ou l’analyse de campagne, vous devrez passer à Xcode 12 et utiliser le nouveau framework AppTrackingTransparency pour signaler le statut d’abonnement des utilisateurs.

## Résumé de la mise à jour

<style>
table th:nth-child(1),
table th:nth-child(2),
table td:nth-child(1),
table td:nth-child(2) {
    min-width:230px;
}
table td {
    word-break: break-word;
}
</style>

|Si votre application utilise :|Recommandation de la mise à jour|Description|
|------|--------|---|
|Xcode 12|**Mise à jour vers le SDK iOS v3.27 ou version ultérieure**|Les clients utilisant Xcode 12 doivent utiliser la version v3.27.0+ pour la compatibilité. Si vous rencontrez des problèmes ou si vous avez des questions concernant notre compatibilité avec iOS 14, ouvrez un nouveau [problème dans Github](https://github.com/Appboy/appboy-ios-sdk/issues).|
|La localisation la plus récente| **Mise à jour vers le SDK iOS v3.26.1 ou version ultérieure**|Si vous utilisez la fonctionnalité de ciblage de l'emplacement/localisation le plus récent et que vous utilisez toujours Xcode 11, vous devez passer au moins au SDK iOS v3.26.1 qui prend en charge la nouvelle fonctionnalité d'_emplacement/localisation approximatif_. Les anciens SDK ne pourront pas collecter de manière fiable la localisation lorsqu’un utilisateur passe à iOS 14 _et_ choisit la localisation approximative.<br><br>Même si votre app ne cible pas iOS 14, il se peut que vos utilisateurs passent à iOS 14 et commencent à utiliser la nouvelle option de précision de l'emplacement/localisation. Les applications qui ne passent pas à la version 3.26.1+ du SDK iOS ne pourront pas collecter de manière fiable les attributs de localisation lorsque les utilisateurs fournissent leur _emplacement/localisation approximatif_ sur les appareils iOS 14.|
|ID de suivi des annonces IDFA| **Une mise à jour vers Xcode 12 et le SDK iOS v3.27 peut être nécessaire**|En 2021, Apple commencera à exiger une invite d’autorisation pour la collecte de l’IDFA. À ce moment, les applications doivent être mises à niveau vers Xcode 12 et utiliser la nouvelle infrastructure `AppTrackingTransparency` afin de continuer à recueillir l’IDFA. Si vous transmettez IDFA au SDK Braze, vous devez également mettre à niveau vers v3.27.0+ à ce moment-là.<br><br>Les applis qui n'utilisent pas les nouvelles API d'iOS 14 ne pourront pas collecter d'IDFA, et collecteront à la place un ID vierge (`00000000-0000-0000-0000-000000000000`) après qu'Apple aura commencé à appliquer ce changement en 2021. Pour savoir si cela s'applique ou non à votre application, consultez les [détails sur l’IDFA](#idfa).|


## Changements de comportement iOS 14

### Autorisation de localisation approximative

![Localisation précise]({% image_buster /assets/img/ios/ios14-approximate-location.png %}){: style="float:right;max-width:45%;margin-left:15px;"}

#### Aperçu

Lors de la demande d'autorisation d'emplacement/localisation, les utilisateurs auront désormais le choix entre fournir leur _emplacement précis_ (comportement précédent), ou le nouvel _emplacement approximatif._ La localisation approximative renvoie un rayon plus large dans lequel l’utilisateur se trouve, au lieu de ses coordonnées exactes.

#### Géorepérages {#geofences}

Les géorepérages [ne sont plus pris en charge par iOS](https://developer.apple.com/documentation/corelocation/cllocationmanager/3600215-accuracyauthorization) pour les utilisateurs qui choisissent la nouvelle autorisation de _localisation approximative_. Bien qu'aucune mise à jour ne soit nécessaire pour votre intégration SDK Braze, vous devrez peut-être ajuster votre [stratégie de marketing basé sur l'emplacement](https://www.braze.com/blog/geofencing-geo-targeting-beaconing-when-to-use/) pour les campagnes qui s'appuient sur les géorepérages.

#### Ciblage de localisation {#location-tracking}

Pour continuer à collecter le _dernier emplacement connu_ des utilisateurs lorsque l' _emplacement/localisation approximatif_ est accordé, votre application devra être mise à niveau vers au moins la v3.26.1 du SDK iOS de Braze. Gardez à l’esprit que la localisation sera moins précise et que, d’après nos tests, elle est supérieure à 12 000 mètres (+ de 7 miles). Lorsque vous utilisez les options de ciblage du _dernier emplacement connu_ dans le tableau de bord de Braze, veillez à augmenter le rayon de l'emplacement pour tenir compte des nouveaux _emplacements approximatifs_ (nous recommandons un rayon d'au moins 1 mile/1,6 km).

Les applis qui ne mettent pas à niveau le SDK Braze pour iOS à la version v3.26.1 ou supérieure ne pourront plus utiliser le suivi de la localisation lorsque l’autorisation de _localisation approximative_ est accordée sur les appareils iOS 14.

Les utilisateurs qui ont déjà autorisé l'accès à l'emplacement/localisation continueront à fournir un _emplacement précis_ après la mise à niveau.

Notez que si vous utilisez XCode 12, vous devrez passer au moins à la mise à jour v3.27.0.

Pour plus d'informations sur l'emplacement/localisation approximatif, consultez la vidéo WWDC d'Apple sur [les nouveautés en matière d'emplacement/localisation](https://developer.apple.com/videos/play/wwdc2020/10660/).

### Transparence du suivi des applications et IDFA {#idfa}

#### Aperçu

L’IDFA (Identifiant pour les annonceurs) est un identifiant fourni par Apple pour une utilisation avec des partenaires publicitaires et d’attribution pour le suivi inter-appareil et est lié à l’ID Apple d’une personne.

À partir d’iOS 14.5, une nouvelle invite d’autorisation (lancée par la nouvelle infrastructure `AppTrackingTransparency`) doit être affichée pour recueillir le consentement explicite de l’utilisateur pour l’IDFA. Cette invite d’autorisation pour « vous suivre via les applications et les sites Web appartenant à d’autres sociétés » devra être demandée de la même manière que lorsque vous invitez les utilisateurs à partager leur localisation.

Si un utilisateur n’accepte pas l’invite, ou si vous ne procédez pas à la mise à niveau vers l’infrastructure `AppTrackingTransparency` de Xcode 12, alors une valeur IDFA vide (`00000000-0000-0000-0000-000000000000`) sera renvoyée, et votre application ne sera pas autorisée à inviter à nouveau l’utilisateur.

{% alert important %}
Ces mises à jour de l'IDFA prendront effet après que les utilisateurs finaux auront mis à jour leur appareil vers iOS 14.5. Assurez-vous que votre application utilise le nouveau `AppTransparencyFramework` avec Xcode 12 si vous prévoyez de recueillir l’IDFA.
{% endalert %}

#### Modifications apportées au recueil de l’IDFA Braze
![IDFA]({% image_buster /assets/img/ios/ios14-idfa.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

1. Braze continuera à autoriser les applications à fournir la valeur IDFA d'un utilisateur _au_ SDK de Braze.

2. La macro de compilation `ABK_ENABLE_IDFA_COLLECTION`, qui devrait compiler en fonction du recueil automatique facultatif de l’IDFA, ne fonctionnera plus dans iOS 14 et a été supprimée dans la section 3.27.0. 

3. Si vous utilisez le champ « Suivi des campagnes publicitaires activé » pour le ciblage ou l’analyse de campagne, vous devrez passer à Xcode 12 et utiliser le nouveau framework AppTrackingTransparency pour signaler le statut d’abonnement des utilisateurs. La raison de cette modification est que dans iOS 14, l’ancien champ [`advertisingTrackingEnabled`](https://developer.apple.com/documentation/adsupport/asidentifiermanager/1614148-advertisingtrackingenabled) renverra toujours No (Non).

4. Si votre application a utilisé l’IDFA ou l’IDFV comme ID externe Braze, nous vous recommandons vivement de délaisser ces identifiants au profit d’un UUID. Pour plus d'informations sur la migration des ID externes, consultez nos [endpoints d’API de migration des ID externes]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/).

Pour en savoir plus sur les [mises à jour de la protection de la vie privée](https://developer.apple.com/app-store/user-privacy-and-data-use/) et sur le nouveau [framework de transparence du suivi des applications](https://developer.apple.com/documentation/apptrackingtransparency), consultez le site d'Apple.

### Autorisation Push {#push-provisional-auth}

{% alert important %}
Aucune modification de l’autorisation Push provisoire n’est incluse dans iOS 14. Dans une version bêta antérieure d’iOS 14, Apple a introduit une modification qui a depuis été rétablie au comportement antérieur.
{% endalert %}

## Nouvelles fonctionnalités iOS 14

### Présentation de la confidentialité et de la collecte de données de l’application {#app-privacy}

Depuis le 8 décembre 2020, toutes les soumissions à l'App Store nécessitent des étapes supplémentaires pour adhérer aux [nouvelles normes d'Apple en matière de confidentialité des applications.](https://developer.apple.com/app-store/app-privacy-details/)

#### Questionnaire sur le portail développeur d’Apple

Sur le _portail des développeurs Apple_:
* Il vous sera demandé de remplir un questionnaire pour décrire comment votre application ou des partenaires tiers collectent des données.
  * Le questionnaire doit toujours être à jour avec votre version la plus récente dans l’App Store.
  * Le questionnaire peut être mis à jour même sans nouvelle soumission d’application.
* Vous devrez coller un lien vers l’URL de la politique de confidentialité de votre application.

Lorsque vous remplissez votre questionnaire, consultez votre équipe juridique et réfléchissez à la manière dont votre utilisation de Braze dans les domaines suivants peut affecter vos exigences de divulgation.

#### Collecte de données par défaut Braze
**Identifiants** \- Un identifiant d'appareil anonyme est toujours collecté par le SDK Braze. Ce paramètre est actuellement défini sur l’IDFV (identifiant du fournisseur).

**Données d'utilisation** \- Il peut s'agir des données de session de Braze, ainsi que de toute collecte d'événements ou d'attributs que vous utilisez pour mesurer l'interaction avec le produit.

#### Collecte de données facultatives
Données que vous pouvez éventuellement collecter via votre utilisation de Braze :

**Localisation** \- La localisation approximative et la localisation précise peuvent être collectées par le SDK Braze (facultatif). Ces fonctionnalités sont désactivées par défaut.

**Coordonnées** \- Il peut s'agir d'événements et d'attributs liés à l'identité de l'utilisateur.

**Achats** \- Il peut s'agir d'événements et d'achats enregistrés au nom de l'utilisateur.

{% alert important %}
Notez qu’il ne s’agit pas d’une liste exhaustive. Si vous collectez manuellement d’autres informations sur vos utilisateurs dans Braze qui s’appliquent à d’autres catégories du questionnaire sur la confidentialité de l’application, vous devrez également les divulguer.
{% endalert %}

Pour en savoir plus sur cette fonctionnalité, consultez [la page Confidentialité et utilisation des données d'Apple](https://developer.apple.com/app-store/user-privacy-and-data-use/).

