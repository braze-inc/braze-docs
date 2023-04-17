---
nav_title: Recueil de l’IDFV
article_title: Recueil de l’IDFV
platform: iOS
page_type: reference
description: "Cet article de référence décrit comment renseigner le champ facultatif IDFV pour le SDK Swift"

---

# Recueil de l’IDFV - Swift

## Historique

Dans les versions antérieures du SDK iOS de Braze, le champ IDFV (identifiant du vendeur) était renseigné automatiquement à partir de l’ID de l’appareil de l’utilisateur. À partir du SDK Swift v5.7.0, le champ IDFV peut être désactivé facultativement et, à la place, Braze générera un UUID aléatoire en tant qu’ID de l’appareil.

La fonctionnalité facultative `useUUIDAsDeviceId` configure le [SDK Swift](https://github.com/braze-inc/braze-swift-sdk) pour définir l’ID de l’appareil en tant qu’UUID. Traditionnellement, le SDK iOS attribuerait un ID d’appareil égal à la valeur IDFV générée par Apple. Lorsque cette fonctionnalité est activée sur votre application iOS, tous les nouveaux utilisateurs créés via le SDK se verront attribuer un ID d’appareil équivalent à un UUID.

Si vous souhaitez toujours recueillir l’IDFV, en ayant l’option UUID activée, vous pouvez toujours le faire via le SDK Swift comme indiqué [ici](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifiantforvendor:)).

## Démarrage

Pour définir l’ID de l’appareil en tant qu’UUID au lieu de l’IDFV, dans l’`Braze.Configuration`instance de votre application iOS, définissez `useUUIDAsDeviceId` sur `true`.

## Considérations

### Version du SDK

Lorsque vous activez `useUUIDAsDeviceId`, tous les nouveaux utilisateurs créés se verront attribuer un ID d’appareil aléatoire. Tous les utilisateurs existants auparavant conserveront la même valeur d’ID d’appareil, qui peut avoir été un IDFV.

Lorsque cette fonctionnalité n’est pas activée (par défaut), les appareils continueront à se voir attribuer un IDFV lors de la création.

Le diagramme ci-dessous décrit quand un UUID ou un IDFV sera attribué comme ID d’appareil. Notez que le champ IDFV ne peut être lu que depuis les appareils qui prennent en charge cette fonctionnalité (p. ex., iOS, tvOS, macCatalyst)

![Organigramme pour les scénarios de configuration de l’ID d’appareil Swift v5.7. Description complète de l’organigramme incluse sous « Description du processus »]({% image_buster /assets/img/swift_idfv.png %}){: style="max-width:80%"}

{% details Process description %}
1. L’utilisateur initialise le SDK v5.7 ou ultérieur
2. L’utilisateur est-il mis à niveau à partir d’une version antérieure du SDK ?
	- Si Obj-C ou antérieur à v5.7, passez à l’étape 3
	- Si v5.7 ou ultérieur, passez à l’étape 4
3. Utiliser IDFV comme `device_id`
	- **Fin du processus**
4. L’utilisateur a-t-il déjà un `device_id` ?
	- Si oui, passez à l’étape 5
	- Si non (nouvel utilisateur), passez à l’étape 6
5. Utiliser le `device_id`existant
	- **Fin du processus**
6. Le paramètre UUID est-il activé ?
	- Si oui, passez à l’étape 7
	- Si non, revenez à l’étape 3
7. Attribuez l’UUID comme `device_id`
	- **Fin du processus**
{% enddetails %}

### En aval 

**Technology Partners** : Si cette fonctionnalité est activée, tous les partenaires technologiques qui tirent la valeur IDFV de l’ID d’appareil Braze n’auront plus accès à cette donnée. Si la valeur IDFV dérivée de l’ID d’appareil est nécessaire pour l’intégration de votre partenaire, nous vous recommandons de ne pas activer cette fonctionnalité.

**Currents** : Activer l’option `useUUIDAsDeviceId` signifiera que l’ID d’appareil envoyé dans Currents ne sera plus équivalent à l’IDFV.

## Foire aux questions

#### Ce changement aura-t-il un impact sur mes utilisateurs existants dans Braze ?
Non. Lorsqu’elle est activée, cette fonctionnalité n’écrase aucune donnée utilisateur dans Braze. Seuls les périphériques nouvellement créés, ou après l’appel `wipedata()`, généreront de nouveaux ID d’appareil UUID.

#### Puis-je désactiver cette fonctionnalité après l’avoir activée ?
Oui, cette fonctionnalité peut être activée et désactivée à votre discrétion. Les ID d’appareil précédemment stockés ne seront jamais écrasés.

#### Puis-je toujours recueillir ailleurs la valeur IDFV via Braze ? 
Oui, vous pouvez toujours facultativement recueillir l’IDFV via le SDK Swift (la collecte est désactivée par défaut). 
