---
nav_title: Vizbee
article_title: Vizbee pour création de liens profonds TV
alias: /partners/vizbee_for_tv_deeplinking/
page_type: partner
description: "Cet article de référence décrit le partenariat entre Braze et Vizbee et la façon de l’utiliser pour prendre en charge la création de liens profonds TV."
search_tag: Partenaire

---
# Vizbee {#vizbee}

> [Vizbee][1] permet à tous les smartphones et TV connectées de votre maison de fonctionner ensemble comme un seul appareil pour une expérience utilisateur exceptionnelle. Vizbee vous permet d’exploiter les canaux de marketing des applications mobiles existantes, tels que les notifications, les liens profonds et les e-mails, afin d’acquérir et d’engager le public de manière harmonieuse sur tous les appareils de télévision connectés (comme Roku, FireTV, Samsung TV, LG TV, etc.).

L’intégration de Braze et de Vizbee vous permet d’utiliser une console unique pour planifier vos campagnes de marketing pour l’acquisition et la fidélisation des téléspectateurs dans les applications de streaming sur les appareils mobiles et télévisions connectées. Grâce à cette intégration, vous pouvez :
- Planifier une notification mobile pour les utilisateurs ciblés, qui, lorsqu’elle est envoyée, peut entraîner la consultation de l’application mobile ou déclencher de manière harmonieuse la lecture sur un appareil de streaming ou un téléviseur à proximité.
- Planifier une campagne de marketing par e-mail à l’intention d’utilisateurs ciblés, qui, une fois lancée, peut entraîner l’installation automatique de l’application de TV connectée et l’inscription de l’utilisateur sur un appareil TV connecté comme Roku ou FireTV.

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Vizbee | Un compte [Vizbee][1] est nécessaire pour profiter de ce partenariat. Vous devez enregistrer votre application dans Vizbee et avoir un ID Vizbee attribué. |
| Application iOS ou Android | Cette intégration prend en charge les applications iOS et Android. Selon votre plateforme, les extraits de code peuvent être requis dans votre application. |
| SDK Vizbee | En plus du SDK Braze requis, vous devez installer le SDK Vizbee. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

Suivez le [guide d’intégration SDK][2] de Vizbee pour mettre en service votre intégration de Vizbee et Braze. Vous y trouverez des conseils sur la création de liens profonds entre mobile et télévision, les installations d’applications TV et l’attribution de l’audience. 

### Affichage des rapports d’installation et d’attribution {#vizbee-tv-app-installs-viewership-attribution}

Vizbee et Braze vous permettent également de visualiser les performances globales de vos campagnes sur les appareils mobiles et TV connectées. Le SDK Vizbee envoie au SDK Braze des événements personnalisés qui peuvent être consultés dans vos rapports de campagne depuis le Tableau de bord de Braze.

[1]: https://vizbee.tv/
[2]: https://console.vizbee.tv/app/vzb1765003429/develop/guides/ios-promote/swift
[3]: https://console.vizbee.tv/app/vzb1765003429/develop/guides/ios-promote/objc