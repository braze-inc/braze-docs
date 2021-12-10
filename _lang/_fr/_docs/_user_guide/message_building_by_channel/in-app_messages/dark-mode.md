---
nav_title: Thèmes du mode sombre
article_title: Mode sombre pour les messages In-App
page_order: 5.20
description: "Braze les messages dans l'application prennent en charge l'ajout d'un thème sombre alternatif pour aider à fournir le bon message de couleur à vos utilisateurs, en fonction de leurs préférences, et aide à assurer la cohérence avec le design de votre application."
channel:
  - messages intégrés à l'application
---

# Mode sombre pour les messages dans l'application

Dark Mode offre aux utilisateurs la possibilité de définir une préférence de couleur à l'échelle du système (disponible sur [Android 10](https://developer.android.com/guide/topics/ui/look-and-feel/darktheme) et [iOS 13](https://developer.apple.com/documentation/appkit/supporting_dark_mode_in_your_interface/)). Les thèmes "sombre" sont destinés à économiser la durée de vie de la batterie et à réduire la pression sur les yeux des utilisateurs, tout en fournissant aux développeurs d'applications un moyen plus facile d'implémenter les thèmes de couleurs sombres que les utilisateurs préfèrent.

Braze les messages dans l'application prennent en charge l'ajout d'un thème sombre alternatif pour aider à fournir le bon message de couleur à vos utilisateurs, en fonction de leurs préférences, et aide à assurer la cohérence avec le design de votre application.

## Comment fonctionne le mode sombre

Les utilisateurs avec des versions d'au moins Android 10 ou iOS 13 et plus peuvent activer/désactiver le mode sombre dans les paramètres de leur appareil.

Lorsque le mode sombre est activé, les menus et écrans natifs de l'appareil (notifications push, paramètres de l'appareil, etc.) changeront en gris foncé. Les applications peuvent également choisir de prendre en charge le mode sombre en spécifiant les thèmes alternatifs dans le code de l'application.

## Définir un thème en mode sombre

La nouvelle option Mode Sombre, située dans l'onglet Style lorsque [crée un message dans l'application]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/), vous permet d'ajouter facilement un thème de couleur alternatif pour les utilisateurs qui sont en mode sombre sur leur appareil.

<img src="{% image_buster /assets/img_archive/iam-dark-mode.gif %}" style="width:100%;max-width:800px;" />

Lorsque cette option est activée, vous pouvez choisir les couleurs du thème foncé pour votre message dans l'application en utilisant le sélecteur de couleur, ou en sélectionnant les [profils de couleur][2] existants pour réutiliser les thèmes Dark ou Light existants.

{% alert note %}
Vous pouvez toujours utiliser cette fonctionnalité même si votre application n'offre pas son propre thème sombre. Cependant, les appareils qui ne prennent pas en charge le mode sombre afficheront par défaut le thème _Light_. En outre, le changement du thème des appareils sur Android alors qu'un message intégré est affiché ne changera pas quel thème est utilisé pour ce message dans l'application.
{% endalert %}

### Utilisation constante du mode sombre

Pour utiliser le mode sombre pour tous les messages dans l'application, allez dans Modèles & Médias, puis dans Modèles de message In-App. À partir de là, sélectionnez [`Créer un profil de couleur`][2] dans le menu déroulant. Créez un profil de couleur qui s'aligne sur votre thème Mode foncé. Ensuite, à chaque fois que vous créez une version en mode sombre d'un message dans l'application, vous pouvez sélectionner ce profil de couleur et garder l'apparence de vos messages dans l'application.

## Compatibilité
- Les utilisateurs finaux doivent être sur les appareils iOS version 13 ou supérieure, ou sur les appareils Android version 10 ou supérieure.
- Braze iOS SDK v3.21.0+ Braze Android SDK v3.8.0+ est nécessaire.

{% alert tip %}
Des applications en mode sombre ont été introduites avec Android 10 et iOS 13. Les utilisateurs qui n'ont pas mis à niveau leur téléphone au moins ces versions ne seront montrés que le thème lumineux.

Les campagnes seront toujours servies à tous les utilisateurs éligibles pour le public que vous avez sélectionné, quel que soit le paramètre Dark Mode des utilisateurs ou la version de l'OS.
{% endalert %}

## Utiliser des messages HTML dans l'application

Créer un thème sombre et léger pour les messages HTML dans l'application. vous pouvez utiliser la fonction média CSS [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) pour détecter les préférences de l'utilisateur.

Par exemple :

```css
@media (prefers-color-scheme: dark) {
  body {
    background: #333;
    color: white;
  }
}

@media (prefers-color-scheme: light) {
  body {
    background: white;
    couleur : #555 ;
  }
}
```

[2]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#color-profile

[2]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#color-profile
