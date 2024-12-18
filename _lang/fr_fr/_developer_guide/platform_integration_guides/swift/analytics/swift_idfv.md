---
nav_title: Recueil de l’IDFV
article_title: Recueil de l’IDFV
platform: Swift
page_type: reference
description: "Cet article de référence décrit comment collecter le champ facultatif IDFV pour le SDK Swift."
page_order: 4

---

# Recueil de l’IDFV 

## Arrière-plan

Dans les versions antérieures du SDK iOS de Braze, le champ IDFV (identifiant du vendeur) était renseigné automatiquement à partir de l’ID de l’appareil de l’utilisateur. À partir du SDK Swift v5.7.0, le champ IDFV peut être désactivé facultativement et, à la place, Braze générera un UUID aléatoire en tant qu’ID de l’appareil. À partir de la version 7.0.0 du SDK Swift, le champ IDFV ne sera pas collecté par défaut, et un UUID sera défini comme ID de l'appareil à la place.

La fonctionnalité `useUUIDAsDeviceId` configure le [SDK Swift](https://github.com/braze-inc/braze-swift-sdk) pour qu'il définisse l'ID de l'appareil en tant qu’UUID. Traditionnellement, le SDK iOS attribuerait un ID d’appareil égal à la valeur IDFV générée par Apple. Avec cette fonctionnalité activée par défaut sur votre app iOS, tous les nouveaux utilisateurs créés via le SDK se verraient attribuer un ID d'appareil égal à un UUID.

Si vous souhaitez toujours collecter l'IDFV séparément, vous pouvez toujours le faire via le SDK Swift, comme décrit [ici](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforvendor:)).

## Considérations

### Version du SDK

Dans le SDK Swift v7.0.0+, lorsque `useUUIDAsDeviceId` est activé (par défaut), tous les nouveaux utilisateurs créés se verront attribuer un ID d'appareil aléatoire. Tous les utilisateurs existants auparavant conserveront la même valeur d’ID d’appareil, qui peut avoir été un IDFV.

Si cette fonctionnalité n'est pas activée, les appareils continueront à se voir attribuer l'IDFV lors de leur création.

### En aval 

**Partenaires technologiques** : Lorsque cette fonctionnalité est activée, tous les partenaires technologiques qui dérivent la valeur IDFV de l'ID de l'appareil Braze n'auront plus accès à ces données. Si la valeur IDFV dérivée de l'appareil est nécessaire pour l'intégration de votre partenaire, nous vous recommandons de définir cette fonctionnalité sur vrai.

**Currents** : lorsque `useUUIDAsDeviceId` est défini sur « true » (« vrai »), l'ID d'appareil envoyé dans Currents ne sera plus égal à la valeur IDFV.

## Foire aux questions

#### Ce changement aura-t-il un impact sur mes utilisateurs existants dans Braze ?
Non. Lorsqu’elle est activée, cette fonctionnalité n’écrase aucune donnée utilisateur dans Braze. Seuls les appareils nouvellement créés, ou après l’appel `wipedata()`, généreront de nouveaux ID d’appareil UUID.

#### Puis-je désactiver cette fonctionnalité après l’avoir activée ?
Oui, cette fonctionnalité peut être activée et désactivée à votre discrétion. Les ID d’appareil précédemment stockés ne seront jamais écrasés.

#### Puis-je toujours recueillir ailleurs la valeur IDFV via Braze ?
Oui, vous pouvez toujours facultativement recueillir l’IDFV via le SDK Swift (la collecte est désactivée par défaut). 
