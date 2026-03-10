{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Désactiver le suivi des données

Pour désactiver la collecte de données, veuillez utiliser la`disableSDK`méthode. Après avoir appelé cette méthode, le SDK Braze cesse d'envoyer des données aux serveurs Braze.

```javascript
Braze.disableSDK();
```

## Reprise du suivi des données

Pour reprendre la collecte de données après l'avoir désactivée, veuillez utiliser la`enableSDK`méthode.

```javascript
Braze.enableSDK();
```

## Effacement des données

Pour supprimer toutes les données Braze SDK stockées localement sur l'appareil, veuillez utiliser la`wipeData`méthode. Après avoir appelé cette méthode, le SDK est désactivé et doit être réactivé à l'aide de `enableSDK`.

```javascript
Braze.wipeData();
```

## Vider les données

Pour demander le transfert immédiat de toutes les données en attente vers les serveurs Braze, veuillez utiliser `requestImmediateDataFlush`.

```javascript
Braze.requestImmediateDataFlush();
```

## Activation du suivi publicitaire

Pour indiquer à Braze si le suivi publicitaire est activé pour cet appareil, veuillez utiliser la`setAdTrackingEnabled`méthode. Le SDK ne collecte pas automatiquement ces données.

```javascript
Braze.setAdTrackingEnabled(true, "GOOGLE_ADVERTISING_ID");
```

Le deuxième paramètre est l'ID publicitaire Google et n'est utilisé que sur Android.

## Mise à jour de la liste blanche des propriétés de suivi (iOS uniquement)

Pour mettre à jour la liste des types de données déclarés pour le suivi, veuillez utiliser `updateTrackingPropertyAllowList`. Cette opération n'a aucun effet sur Android.

```javascript
Braze.updateTrackingPropertyAllowList({
  adding: [Braze.TrackingProperty.EMAIL, Braze.TrackingProperty.FIRST_NAME],
  removing: [],
  addingCustomEvents: ["my_custom_event"],
  removingCustomEvents: [],
  addingCustomAttributes: ["my_custom_attribute"],
  removingCustomAttributes: []
});
```

Pour plus d'informations, veuillez vous référer au [manifeste de confidentialité]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/privacy_manifest/).
