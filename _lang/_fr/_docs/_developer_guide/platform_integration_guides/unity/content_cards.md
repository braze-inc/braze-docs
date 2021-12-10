---
nav_title: Cartes de contenu
article_title: Cartes de contenu pour l'unité
platform:
  - Unité
  - iOS
  - Android
channel: cartes de contenu
page_order: 4
description: "Cet article de référence couvre les lignes directrices de mise en œuvre de la carte de contenu pour la plate-forme Unity."
---

# Cartes de contenu

## Affichage natif des cartes de contenu {#unity-content-cards-native-ui}

Vous pouvez afficher l'interface par défaut pour les cartes de contenu en utilisant l'appel suivant :

```csharp
Appboy.AppboyBinding.DisplayContentCards();
```

## Réception des données de la carte de contenu dans l'unité

Vous pouvez enregistrer des objets Unity Game pour être averti des cartes de contenu entrantes. Nous vous recommandons de configurer les écouteurs d'objets du jeu à partir de l'éditeur de configuration de Braze.

- Si vous avez besoin de configurer l'écouteur d'objet du jeu à l'exécution, utilisez `AppboyBinding.ConfigureListener()` et spécifiez `BrazeUnityMessageType.CONTENT_CARDS_UPDATED`.

Notez que vous devrez également faire un appel à `AppboyBinding.RequestContentCardsRefresh()` pour commencer à recevoir des données dans votre écouteur d'objet de jeu sur iOS.

## Analyse des cartes de contenu

Les messages entrants de `chaîne` reçus dans la fonction de rappel de l'objet de votre jeu de cartes de contenu peuvent être analysés dans notre objet modèle [`ContentCard`][17] pré-fourni pour plus de commodité.

L'analyse des Cartes de Contenu nécessite l'analyse Json, voir l'exemple suivant pour plus de détails:

##### Exemple de rappel de cartes de contenu

```csharp
void ExampleCallback(string message) {
  // Exemple de logging a Content Card displayed event
  AppboyBinding. ogContentCardsDisplayed();
  essayez {
    JSONClass json = (JSONClass)JSON. arse(message);

    // Les données de la carte de contenu sont contenues dans le champ `mContentCards` de l'objet de niveau supérieur.
    if (json["mContentCards"] != null) {
      JSONArray jsonArray = (JSONArray)JSON.Parse(json["mContentCards"].ToString());
      Debug.Log(String. ormat("Tableau de cartes de contenu analysées avec {0} cartes", jsonArray. ount));

      // Itère sur le tableau de cartes pour analyser les cartes individuelles.
      pour (int i = 0; i < jsonArray. ount; i++) {
        JSONClass cardJson = jsonArray[i]. sObject ;
        essayez {
          ContentCard card = new ContentCard(cardJson);
          Debug. og(String). ormat("Objet de carte créé pour la carte : {0}", carte));

          // Exemple de logging de Content Card analytics sur la carte ContentCard objet 
          . ogImpression(); carte
          . ogClick();
        } attrape {
          Debug.Log(String. ormat("Impossible de créer et de loguer les analytiques pour la carte {0}", cardJson));
        }
      }
    }
  } attrape {
    throw new ArgumentException("Impossible d'analyser le message JSON de la carte de contenu. );
  }
}
```

## Rafraîchissement des cartes de contenu

Pour actualiser les Cartes de Contenu de Braze, appelez l'une des méthodes suivantes :

```csharp
// résulte en une requête réseau à Braze
AppboyBinding.RequestContentCardsRefresh()

AppboyBinding.RequestContentCardsRefreshFromCache()
```

## Analyses

Les clics et les impressions doivent être enregistrés manuellement pour les cartes de contenu non affichées directement par Braze.

Utilisez `LogClick()` et `LogImpression()` sur [ContentCard][17] pour enregistrer les clics et les impressions pour des cartes spécifiques.

To log that the user viewed the feed as a whole, call `AppboyBinding.LogContentCardsDisplayed()`.

[17]: https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Appboy/models/Cards/ContentCard.cs

[17]: https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Appboy/models/Cards/ContentCard.cs
