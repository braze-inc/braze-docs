---
nav_title: Guide de mise à jour iOS 17
article_title: Guide de mise à jour iOS 17
page_order: 7
platform: 
  - iOS
description: "Cet article fournit des informations sur la version iOS 17 pour vous aider à mettre à jour votre SDK sans heurts."
hidden: true
noindex: true
---

# Guide de mise à jour d'iOS 17

> Vous souhaitez savoir comment Braze se prépare à la prochaine version d’iOS ? Cet article résume nos informations sur la version 17 d'iOS pour vous aider à créer une expérience fluide pour vous et pour vos utilisateurs.

## Compatibilité iOS 17 et Xcode 15

Le SDK Swift et le SDK Objective-C de Braze sont tous deux rétrocompatibles avec Xcode 14 et Xcode 15, et ils sont compatibles avec les appareils iOS 17.

## Changements dans iOS 17

### Suivi des liens et dépouillement des paramètres UTM

L'un des changements importants d'iOS 17 est le blocage des paramètres UTM dans Safari. Les paramètres UTM sont des morceaux de code ajoutés aux URL, qui sont fréquemment utilisés dans les campagnes de communication pour mesurer l'efficacité des e-mails, des SMS et d'autres canaux d'envoi de messages. 

Ce changement n'a pas d'incidence sur le suivi des clics dans les e-mails de Braze et sur les envois de raccourcis de liens par SMS.

### Transparence du suivi des applications

Apple a annoncé sa volonté d'étendre le champ d'application de la [transparence du suivi publicitaire (ATT)](https://support.apple.com/en-us/HT212025), qui permet aux utilisateurs de contrôler si une application peut accéder à leur activité sur des applications et des sites web appartenant à d'autres entreprises. iOS 17 contient deux fonctionnalités ATT clés : les manifestes de confidentialité et la signature de code.

#### Manifeste de confidentialité

Apple exige désormais un fichier de manifeste de confidentialité qui décrit la raison pour laquelle votre application et les SDK tiers collectent des données, ainsi que leurs méthodes de collecte de données. À partir d'iOS 17.2, Apple bloquera tous les endpoints de suivi déclarés dans votre application jusqu'à ce que l'utilisateur final accepte l'invite ATT.

Braze a publié son propre manifeste de confidentialité, ainsi que de nouvelles API flexibles qui redirigent automatiquement les données de suivi déclarées vers des endpoints `-tracking` dédiés. Pour plus d'informations, consultez le [manifeste de confidentialité de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/privacy_manifest).

#### Signature du code

La signature de code permet aux développeurs qui utilisent un SDK tiers dans leur application de confirmer que le même développeur l'a signé comme les versions précédentes dans Xcode. 

### SDK de Braze et protection de la vie privée

Apple a également annoncé la publication d’une liste de SDK tiers considérés comme « ayant un impact sur la vie privée » à la fin de l'année 2023. Ces SDK devraient avoir un impact particulièrement important sur la vie privée des utilisateurs d'Apple.

Contrairement aux SDK de suivi traditionnels qui sont conçus pour surveiller les utilisateurs sur plusieurs sites Web et applications, le SDK de Braze se concentre sur l'envoi de données first-party et les expériences des utilisateurs.

Bien que nous ne nous attendions pas à ce que le SDK de Braze soit inclus dans cette liste, nous avons l'intention de suivre cette situation de près et de publier toutes les mises à jour nécessaires.
