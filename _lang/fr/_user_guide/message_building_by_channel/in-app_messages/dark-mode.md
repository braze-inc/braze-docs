---
nav_title: Thèmes du mode sombre
article_title: Mode sombre pour les messages In-App
page_order: 5.20
description: "Cet article de référence présente la prise en charge du mode sombre des messages in-app de Braze, y compris la manière de définir un thème de mode sombre et des observations sur la compatibilité."
channel:
  - messages In-App

---

# Thèmes du mode sombre

> Le mode sombre offre aux utilisateurs la possibilité de définir une préférence de couleur dans tout le système (introduit dans [Android 10](https://developer.android.com/guide/topics/ui/look-and-feel/darktheme) et [iOS 13](https://developer.apple.com/documentation/appkit/supporting_dark_mode_in_your_interface/)). Les thèmes sombres sont conçus pour préserver la durée de vie de la batterie et réduire la fatigue oculaire des utilisateurs. Les développeurs d’applications disposent aussi d’un moyen plus simple d’implémenter les thèmes de couleur sombre que les utilisateurs préfèrent.

Les messages In-App Braze prennent en charge un thème sombre distinct pour que les messages s’affichent dans la couleur appropriée en fonction des préférences utilisateur, tout en assurant la cohérence avec la conception de votre application.

## Fonctionnement du mode sombre

Les utilisateurs avec des versions à partir d’Android 10 ou iOS 13 peuvent basculer en mode sombre dans les réglages de leur appareil.

Lorsque le mode sombre est activé, les menus et écrans natifs de l’appareil (notifications push, réglages de l’appareil, etc.) s’affichent en gris foncé. Les applications peuvent également prendre en charge le mode sombre si les autres thèmes sont indiqués dans leur code.

## Définition d’un thème du mode sombre

La nouvelle option de mode sombre, située dans l’onglet Style lors de la [création d’un message In-App]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/), vous permet d’ajouter facilement un thème de couleur distinct pour les utilisateurs en mode sombre sur leur appareil.

![Utilisateur basculant entre les modes sombre et clair dans l’onglet Style lors de la création d’un message In-App.]({% image_buster /assets/img_archive/iam-dark-mode.gif %})

Lorsque cette option est activée, vous pouvez choisir les couleurs du thème sombre pour votre message In-App à l’aide d’un sélecteur de couleur, ou en sélectionnant des [profils de couleurs][2] existants pour réutiliser les thèmes clair et sombre existants.

{% alert note %}
Vous pouvez utiliser cette fonctionnalité même si votre application n’offre pas son propre thème sombre. Toutefois, les appareils qui ne prennent pas en charge le mode sombre affichent par défaut le thème clair. Changer le thème de l’appareil sur Android alors qu’un message In-App est affiché ne change pas le thème utilisé pour ce message In-App.
{% endalert %}

### Utilisation continue du mode sombre

Pour utiliser le mode sombre pour tous les messages In-App, allez à **Templates & Media (Modèles et médias)**, puis **Modèles de messages In-App**. Sélectionnez [Create Color Profile (Créer un profil de couleur)][2] dans la liste déroulante. Créez un profil de couleur qui correspond à votre thème du mode sombre. Puis, chaque fois que vous créez une version en mode sombre d’un message In-App, vous pouvez sélectionner ce profil de couleur et conserver la cohérence de l’apparence de vos messages In-App.

## Compatibilité

- Les utilisateurs finaux doivent employer des appareils à partir d’iOS version 13 ou Android version 10.
- SDK iOS Braze v3.21.0+ SDK Android Braze v3.8.0+ requis.

{% alert note %}
Les applications en mode sombre ont été introduites avec Android 10 et iOS 13. Les utilisateurs qui n’ont pas mis à niveau leurs téléphones à ces versions ou ultérieures ne voient que le thème clair. <br><br>Les campagnes sont toujours envoyées à tous les utilisateurs éligibles sélectionnés, quel que soit leur paramètre de mode sombre ou la version du système d’exploitation.
{% endalert %}

## Utilisation de messages In-App HTML

Pour créer des thèmes sombre et clair pour les messages In-App HTML, vous pouvez utiliser la fonction [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) CSS afin de détecter la préférence de l’utilisateur.

Par exemple :

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
    color: #555;
  }
}
```

[2]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#color-profile
