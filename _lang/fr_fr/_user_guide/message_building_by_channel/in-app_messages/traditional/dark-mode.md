---
nav_title: Thèmes en mode sombre
article_title: Mode sombre pour les messages in-app
page_order: 5
description: "Cet article de référence couvre la prise en charge du mode sombre des messages in-app de Braze, y compris la façon de définir un thème en mode sombre et les considérations de compatibilité."
channel:
  - in-app messages

---

# Thèmes en mode sombre

> Le mode sombre offre aux utilisateurs la possibilité de définir une préférence de couleur à l'échelle du système (introduit sur [Android 10](https://developer.android.com/guide/topics/ui/look-and-feel/darktheme) et [iOS 13](https://developer.apple.com/documentation/appkit/supporting_dark_mode_in_your_interface/)). Les thèmes "sombres" sont destinés à préserver l'autonomie de la batterie et à réduire la fatigue visuelle des utilisateurs, tout en offrant aux développeurs d'applications un moyen plus facile de mettre en œuvre les thèmes de couleurs sombres que les utilisateurs préfèrent.

Les messages in-app de Braze prennent en charge l'ajout d'un thème alternatif Dark pour aider à délivrer le bon message de couleur à vos utilisateurs en fonction de leur préférence, et permet d'assurer la cohérence avec le design de votre application.

## Comment fonctionne le mode sombre ?

Les utilisateurs disposant de versions d'au moins Android 10 ou iOS 13 et ultérieures peuvent basculer le mode sombre dans les paramètres de leur appareil.

Lorsque le mode sombre est activé, les menus et écrans natifs de l'appareil (notifications push, paramètres de l'appareil, etc.) deviennent gris foncé. Les apps peuvent également choisir de prendre en charge le mode sombre en spécifiant les thèmes alternatifs dans le code de l'app.

## Définition d'un thème en mode sombre

La nouvelle option Mode sombre, située dans l'onglet Style lors de la [création d'un message in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/), vous permet d'ajouter facilement un thème de couleur alternatif pour les utilisateurs qui sont en mode sombre sur leur appareil.

L'utilisateur bascule entre le style Mode clair et le style Mode sombre dans l'onglet Style lors de la création d'un message in-app.]({% image_buster /assets/img_archive/iam-dark-mode.gif %})

Lorsque cette option est activée, vous pouvez choisir des couleurs de thème sombres pour votre message in-app à l'aide du sélecteur de couleurs, ou en sélectionnant les [profils de couleurs]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#color-profile) existants pour réutiliser les thèmes sombres ou clairs existants.

{% alert note %}
Vous pouvez toujours utiliser cette fonctionnalité même si votre application ne propose pas son propre thème sombre. Cependant, les appareils qui ne prennent pas en charge le mode sombre afficheront le thème Light par défaut. Changer le thème de l'appareil sur Android pendant l'affichage d'un message in-app ne changera pas le thème utilisé pour ce message in-app.
{% endalert %}

### Utiliser le mode sombre de manière cohérente

Pour utiliser le mode sombre pour tous les messages in-app, accédez à **Modèles** > **Modèles de messages in-app**.

Sélectionnez ensuite [Créer un profil de couleur]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#color-profile) dans la liste déroulante. Créez un profil de couleurs qui s'aligne sur votre thème en mode sombre. Ensuite, chaque fois que vous créez une version en mode sombre d'un message in-app, vous pouvez sélectionner ce profil de couleur et conserver la cohérence de l'aspect de vos messages in-app.

## Compatibilité

- Vos utilisateurs doivent être sur des appareils iOS version 13 ou supérieure, ou des appareils Android version 10 ou supérieure.
- Braze iOS SDK v3.21.0+ Braze Android SDK v3.8.0+ est nécessaire.

{% alert note %}
Les applications en mode sombre ont été introduites avec Android 10 et iOS 13. Les utilisateurs qui n'ont pas mis à jour leur téléphone avec au moins ces versions n'auront accès qu'au thème lumineux. <br><br>Les campagnes seront toujours diffusées à tous les utilisateurs éligibles pour l'audience que vous avez sélectionnée, quel que soit le paramètre du mode sombre des utilisateurs ou la version du système d'exploitation.
{% endalert %}

## Utiliser des messages in-app au format HTML

Pour créer un thème foncé et un thème clair pour les messages HTML in-app, vous pouvez utiliser la fonction [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) CSS pour détecter les préférences de l'utilisateur.

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
    color: #555;
  }
}
```

