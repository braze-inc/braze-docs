---
nav_title: Cartes de contenu
article_title: Cartes de contenu pour Unity
platform: 
  - Unity
  - iOS
  - Android
channel: cartes de contenu
page_order: 4
description: "Cet article de référence couvre les directives d’implémentation des cartes de contenu pour la plateforme Unity."

---

# Cartes de contenu

## Affichage natif des cartes de contenu {#unity-content-cards-native-ui}

Vous pouvez afficher l’interface utilisateur par défaut pour les cartes de contenu à l’aide de l’appel suivant :

```csharp
Appboy.AppboyBinding.DisplayContentCards();
```

## Réception des données de carte de contenu dans Unity

Vous pouvez lister des objets de jeu Unity pour être avertis des cartes de contenu entrantes. Nous recommandons de définir des auditeurs d’objets de jeu à partir de l’éditeur de configuration Braze.

Si vous devez configurer votre auditeur d’objet de jeu lors de l’exécution, utilisez `AppboyBinding.ConfigureListener()` et spécifiez `BrazeUnityMessageType.CONTENT_CARDS_UPDATED`.

Notez que vous devrez également appeler `AppboyBinding.RequestContentCardsRefresh()` pour commencer à recevoir des données dans votre auditeur d’objet de jeu sur iOS.

## Analyse des cartes de contenu

Les messages `string` entrants reçus dans votre fonction de rappel d’objet de jeu de cartes de contenu peuvent être analysés dans notre objet de modèle [`ContentCard`][17] pré-fournis pour plus de commodité.

L’analyse des cartes de contenu nécessite l’analyse Json, consultez l’exemple suivant pour plus de détails :

##### Exemple de fonction de rappel des cartes de contenu

```csharp
void ExampleCallback(string message) {
  try {
    JSONClass json = (JSONClass)JSON.Parse(message);

    // Les données de carte de contenus dans le champ`mContentCards` supérieur de l’objet.
    if (json["mContentCards"] != null) {
      JSONArray jsonArray = (JSONArray)JSON.Parse(json["mContentCards"].ToString());
      Debug.Log(String.Format("Array de cartes de contenu parsé avec {0} cartes", jsonArray.Count));

      // Iterate sur le tableau de carte pour analyser les cartes individuelles.
      for (int i = 0; i < jsonArray.Count; i++) {
        JSONClass cardJson = jsonArray[i].AsObject;
        try {
          ContentCard card = new ContentCard(cardJson);
          Debug.Log(String.Format("Un objet de carte a été créé pour la carte : {0}", card));

          // Exemple de journalisation des métriques des performances d’objet des carte de contenu  
          card.LogImpression();
          card.LogClick();
        } catch {
          Debug.Log(String.Format("Impossible de créer et d'enregistrer des analytiques pour la carte {0}", cardJson));
        }
      }
    }
  } catch {
    throw new ArgumentException("Impossible de parser le message JSON de la carte de contenu.");
  }
}
```

## Rafraîchir les cartes de contenu

Pour actualiser les cartes de contenu de Braze, appelez l’une des méthodes suivantes :

```csharp
// entraîne une requête de réseau à Braze
AppboyBinding.RequestContentCardsRefresh()

AppboyBinding.RequestContentCardsRefreshFromCache()
```

## Analytique

Les clics et les impressions doivent être enregistrés manuellement pour les cartes de contenu non affichées directement par Braze.

Utiliser `LogClick()` et `LogImpression()` sur [ContentCard (Carte de contenu)][17] pour enregistrer des clics et des impressions pour des cartes spécifiques.

[17]: https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Appboy/models/Cards/ContentCard.cs
