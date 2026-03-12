{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Définition de la dernière localisation connue

Pour définir manuellement la dernière localisation connue d'un utilisateur, veuillez utiliser la`setLastKnownLocation`méthode. Cette fonctionnalité est utile si vous collectez des données d'emplacement en dehors du SDK Braze.

```javascript
Braze.setLastKnownLocation(LATITUDE, LONGITUDE, ALTITUDE, HORIZONTAL_ACCURACY, VERTICAL_ACCURACY);
```

- Sur Android,`latitude`les éléments et`longitude`sont obligatoires. `altitude`Les éléments `horizontalAccuracy`, et`verticalAccuracy`sont facultatifs.
- Sur iOS, `latitude`,`longitude` et`horizontalAccuracy`sont obligatoires.`altitude`et`verticalAccuracy`sont facultatifs.

Pour assurer la compatibilité entre les différentes plateformes, veuillez fournir au `horizontalAccuracy`minimum`latitude` , `longitude`, et .

## Définition d'un attribut d'emplacement personnalisé

Pour définir un attribut de localisation personnalisé sur un profil utilisateur, veuillez utiliser la`setLocationCustomAttribute`méthode.

```javascript
Braze.setLocationCustomAttribute("favorite_restaurant", 40.7128, -74.0060, optionalCallback);
```

## Demande d'initialisation de l'emplacement/localisation (Android uniquement)

Veuillez appeler cette fonction`requestLocationInitialization` après qu'un utilisateur ait accordé les autorisations d'emplacement afin d'initialiser les fonctionnalités de localisation Braze sur Android. Cette méthode n'est pas prise en charge sur iOS et n'est pas requise pour les fonctionnalités de géorepérage ou de localisation iOS.

```javascript
Braze.requestLocationInitialization();
```

## Géorepérages

Les géorepérages sont pris en charge à la fois sur iOS et Android. Par défaut, le SDK Braze peut automatiquement demander et surveiller les géorepérages lorsque l'emplacement est disponible. Vous pouvez vous fier à cette configuration automatique pour la plupart des intégrations.

### Demander manuellement des géorepérages

Pour demander manuellement une mise à jour du géorepérage pour une coordonnée GPS spécifique, veuillez utiliser `requestGeofences`. Ceci est disponible à la fois sur iOS et Android. Si vous utilisez cette méthode, veuillez désactiver les demandes automatiques de géorepérage dans votre configuration native afin que le SDK ne remplace pas vos demandes manuelles.

```javascript
Braze.requestGeofences(LATITUDE, LONGITUDE);
```
