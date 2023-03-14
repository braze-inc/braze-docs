---
nav_title: Collecte de l’IDFV
article_title: Collecte de l’IDFV
platform: iOS
page_type: reference
description: "Cet article de référence décrit comment collecter le champ IDFV facultatif pour le SDK Swift."

---

# Collecte de l’IDFV - Swift

## Historique

Dans les versions antérieures du SDK iOS de Braze, le champ IDFV (identifiant du vendeur) était renseigné automatiquement à partir de l’ID de l’appareil de l’utilisateur. À partir du SDK Swift v5.7.0, le champ IDFV peut être désactivé facultativement et, à la place, Braze générera un UUID aléatoire en tant qu’ID de l’appareil.

La fonctionnalité `useUUIDAsDeviceId` facultative configure le [SDK Swift](https://github.com/braze-inc/braze-swift-sdk) pour définir l’ID de l’appareil en tant qu’UUID. Normalement, le SDK iOS attribuerait l’ID de l’appareil qui est égal à la valeur IDFV générée par Apple. Lorsque cette fonctionnalité est activée sur votre application iOS, tous les nouveaux utilisateurs créés via le SDK se verront attribuer un ID d’appareil égal à un UUID.

Si vous souhaitez toujours collecter l’IDFV, avec l’option UUID activée, vous pouvez toujours le faire via le SDK Swift comme indiqué [ici](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforvendor:)).

## Démarrage

Pour définir l’ID de l’appareil en tant qu’UUID au lieu de l’IDFV, dans l’instance `Braze.Configuration` de votre application iOS, définissez `useUUIDAsDeviceId` sur `true`.

## Considérations

### Version du SDK

Lorsque vous activez `useUUIDAsDeviceId`, tous les nouveaux utilisateurs créés se verront attribuer un ID d’appareil aléatoire. Tous les utilisateurs précédemment existants conserveront leur même valeur d’ID d’appareil, qui peut avoir été IDFV.

Lorsque cette fonctionnalité n’est pas activée (par défaut), les appareils continueront à recevoir un IDFV lors de la création.

Le diagramme ci-dessous montre quand un UUID ou un IDFV sera attribué comme ID d’appareil. Notez que le champ IDFV peut uniquement être lu depuis les appareils qui prennent en charge cette fonctionnalité (par ex., iOS, tvOS et macCatalyst).

![Organigramme des scénarios de configuration de l’ID d’appareil Swift v5.7 : la description complète de l’organigramme est incluse sous « Description du processus »]({% image_buster /assets/img/swift_idfv.png %}){: style="max-width:80%"}

{% details Description du processus %}
1. L’utilisateur initialise le SDK version 5.7 ou ultérieure.
2. L’utilisateur est-il mis à niveau à partir d’une version précédente du SDK ?
	- Si Obj-C ou une version antérieure à 5.7, passez à l’étape 3.
	- Si version 5.7 ou ultérieure, passer à l’étape 4.
3. Utiliser l’IDFV en tant que `device_id`
	- **Fin du processus**
4. L’utilisateur a-t-il déjà un `device_id` ?
	- Si oui, passez à l’étape 5.
	- Si ce n’est pas le cas (nouvel utilisateur), passez à l’étape 6.
5. Utiliser un `device_id` existant
	- **Fin du processus**
6. Le paramètre UUID est-il activé ?
	- Si oui, passez à l’étape 7.
	- Si non, revenez à l’étape 3.
7. Attribuer l’UUID en tant que `device_id`
	- **Fin du processus**
{% enddetails %}

### En aval 

**Technology Partners** : Si cette fonctionnalité est activée, tous les partenaires technologiques qui tirent la valeur IDFV de l’ID d’appareil Braze n’auront plus accès à ces données. Si la valeur IDFV dérivée de l’ID de l’appareil est nécessaire pour intégrer votre partenaire, nous vous recommandons de ne pas activer cette fonctionnalité.

**Currents** : En activant l’option `useUUIDAsDeviceId`, l’ID d’appareil envoyé dans Currents ne sera plus égal à l’IDFV.

## FAQ

#### Ce changement aura-t-il un impact sur mes utilisateurs actuels dans Braze ?
Non. Lorsqu’elle est activée, cette fonctionnalité n’écrase aucune donnée utilisateur dans Braze. Seuls les appareils nouvellement créés (ou après l’appel de `wipedata()`), généreront de nouveaux ID d’appareil UUID.

#### Puis-je désactiver cette fonctionnalité après l’avoir activée ?
Oui, cette fonctionnalité peut être activée et désactivée lorsque vous en avez besoin. Les ID d’appareil précédemment stockés ne seront jamais écrasés.

#### Puis-je toujours collecter la valeur IDFV autre part dans Braze ? 
Oui, vous pouvez toujours collecter l’IDFV via le SDK Swift (la collecte est désactivée par défaut). 
