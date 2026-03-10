{% alert important %}
Les géorepérages sont pris en charge **à la fois** sur **iOS et Android** dans le SDK React native. Cette`requestLocationInitialization`méthode est réservée à Android et n'est pas nécessaire pour iOS. Cette`requestGeofences`méthode est disponible sur les deux plateformes. Par défaut, le SDK peut automatiquement demander et surveiller les géorepérages lorsque l'emplacement est disponible ; vous pouvez vous fier à cette configuration automatique ou appeler`requestGeofences`pour effectuer une demande manuellement.
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/react_native.md %} Sur Android, il est nécessaire de [configurer les notifications push silencieuses]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android) pour la synchronisation de géorepérage.

## Configuration des géorepérages {#setting-up-geofences}

### Étape 1 : Activer dans Braze

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

### Étape 2 : Configuration Android native complète

Étant donné que le SDK React native utilise le SDK Android natif de Braze, veuillez effectuer la configuration native du géorepérage Android pour votre projet. L'équivalent iOS de ces étapes est décrit dans le guide des géorepérages du SDK Swift natif ([étapes 2.2 à 3.1]({{site.baseurl}}/developer_guide/geofences/?sdktab=swift#swift_step-21-add-the-brazelocation-module)) ; l'étape 2.1 (Ajouter le module BrazeLocation) n'est pas nécessaire pour React native, car BrazeLocation est déjà inclus implicitement dans le SDK Braze React native.

1. **Mise à jour `build.gradle`:** Veuillez`android-sdk-location`ajouter les services de localisation Google Play pour l'emplacement/la localisation. Veuillez consulter [les géorepérages Android]({{site.baseurl}}/developer_guide/geofences/?sdktab=android).
2. **Veuillez mettre à jour le manifeste :** Veuillez ajouter les autorisations pour les emplacements et le récepteur de démarrage Braze. Veuillez consulter [les géorepérages Android]({{site.baseurl}}/developer_guide/geofences/?sdktab=android).
3. **Activer la collecte de données d’emplacement Braze :** Veuillez mettre à jour votre`braze.xml`fichier. Veuillez consulter [les géorepérages Android]({{site.baseurl}}/developer_guide/geofences/?sdktab=android).

### Étape 3 : Configuration iOS native complète

Étant donné que le SDK React native utilise le SDK iOS natif de Braze, veuillez terminer la configuration native du géorepérage iOS pour votre projet en suivant les instructions du SDK Swift natif à partir de l'étape 2.2 : mettez à jour votre`Info.plist`configuration avec les descriptions d'utilisation des emplacements (étape 2.2) et activez le géorepérage dans votre configuration Braze, y compris`automaticGeofenceRequests = true`les paramètres de géolocalisation (étape 3) ; vous pouvez également activer les rapports en arrière-plan (étape 3.1). L'étape 2.1 (Ajouter le module BrazeLocation) n'est pas nécessaire, car BrazeLocation est déjà inclus implicitement dans le SDK Braze React native. Veuillez vous référer [aux géorepérages iOS, étapes 2.2 à 3.1]({{site.baseurl}}/developer_guide/geofences/?sdktab=swift#swift_step-21-add-the-brazelocation-module).

### Étape 4 : Demander du géorepérage à partir de JavaScript

**Sur Android :** Une fois que l'utilisateur a accordé les autorisations d'emplacement, veuillez appeler`requestLocationInitialization()`pour initialiser les fonctionnalités d'emplacement Braze et demander des géorepérages aux serveurs Braze. Cette méthode n'est pas prise en charge sur iOS et n'est pas requise pour iOS.

**Sur iOS :** L'équivalent consiste à activer la`automaticGeofenceRequests`configuration dans votre configuration native Swift ou Objective-C Braze (voir étape 3). Lorsque cette fonctionnalité est activée, le SDK demande et surveille automatiquement les géorepérages lorsque l'emplacement est disponible ; aucun appel JavaScript équivalent à`requestLocationInitialization`  n'est nécessaire.

```javascript
import Braze from '@braze/react-native-sdk';

// Android only: call this after the user grants location permission
Braze.requestLocationInitialization();
```

### Étape 5 : Demander manuellement des géorepérages (facultatif)

Sur iOS et Android, vous pouvez demander manuellement une mise à jour du géorepérage pour une coordonnée GPS spécifique en utilisant `requestGeofences`. Par défaut, Braze récupère automatiquement l'emplacement de l'appareil et demande des géorepérages. Pour fournir manuellement une coordonnée à la place :

1. Veuillez désactiver les demandes automatiques de géorepérage. Sur Android, veuillez configurer`com_braze_automatic_geofence_requests_enabled`  sur`false`  dans votre `braze.xml`. Sur iOS, veuillez configurer`automaticGeofenceRequests`  sur`false`  dans votre configuration Braze.
2. Veuillez appeler`requestGeofences`en indiquant la latitude et la longitude souhaitées :

```javascript
import Braze from '@braze/react-native-sdk';

Braze.requestGeofences(33.078947, -116.601356);
```

{% alert important %}
Les géorepérages ne peuvent être demandés qu’une seule fois par session, soit automatiquement par le SDK, soit manuellement avec cette méthode.
{% endalert %}
