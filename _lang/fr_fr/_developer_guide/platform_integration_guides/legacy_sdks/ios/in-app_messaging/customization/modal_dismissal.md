---
nav_title: Rejet modal
article_title: Rejet de message in-app modal pour iOS
platform: iOS
page_order: 29
description: "Cet article de référence explique le rejet de la messagerie in-app modale dans votre application iOS."
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Rejet modal par touché extérieur

La valeur par défaut est `NO`. Cela détermine si le message in-app modal sera rejeté lorsque l’utilisateur touche à l’extérieur du message in-app.

Pour activer les rejets extérieurs, ajoutez un dictionnaire nommé `Braze` à votre fichier `Info.plist`. À l’intérieur du dictionnaire `Braze`, ajoutez la sous-entrée booléenne `DismissModalOnOutsideTap` et réglez la valeur sur `YES` comme indiqué dans l’extrait de code suivant. Notez qu’avant le SDK Braze pour iOS v4.0.2, la clé du dictionnaire `Appboy` doit être utilisée à la place de `Braze`.

```
<key>Braze</key>
<dict>
  <key>DismissModalOnOutsideTap</key>
  <boolean>YES</boolean>
</dict>
```

Vous pouvez également activer la fonctionnalité lors de l’exécution en définissant `ABKEnableDismissModalOnOutsideTapKey` sur `YES` dans `appboyOptions`.

| `DismissModalOnOutsideTap` | Description |
|----------|-------------|
| `YES`       | Les messages in-app modaux seront rejetés par touche extérieure.     |
| `NO`        | Par défaut, les messages in-app modaux ne seront rejetés par touche extérieure. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }