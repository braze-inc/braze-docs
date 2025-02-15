---
nav_title: Intégration
article_title: Guide d’intégration de messages in-app pour Roku
platform: Roku
page_order: 2
description: "Ce guide de référence explique comment intégrer les messages in-app pour Roku et les considérations de code pertinentes"
channel:
  - in-app messages
---

# Intégration de message in-app

> Ce guide d’implémentation couvre les considérations relatives au code de messages in-app et les extraits de code qui l’accompagnent. Bien que nous fournissions un exemple de code d’intégration, vous devrez ajouter une logique pour gérer et afficher les messages déclenchés dans l’interface utilisateur souhaitée. 

Étant donné que votre code sera unique à votre application, vous n’avez pas besoin de gérer toutes les situations répertoriées si elles ne sont pas pertinentes pour votre cas d’utilisation. Par exemple, si vous n’utilisez pas l’affichage différé des messages in-app, vous n’aurez pas besoin d’implémenter cette logique et ces cas extrêmes.

## Exigences du SDK {#supported-sdk-versions}

Les messages in-app ne seront envoyés qu’aux appareils Roku exécutant la version minimale du SDK prise en charge :

{% sdk_min_versions roku:0.1.2 %}

## Configurer les messages in-app

Pour traiter les messages in-app, vous pouvez ajouter un observateur à `BrazeTask.BrazeInAppMessage` :

```brightscript
m.BrazeTask.observeField("BrazeInAppMessage", "onInAppMessageReceived")
```

Puis, dans votre gestionnaire, vous avez accès au message in-app le plus élevé que vos campagnes ont déclenché :

```brightscript
sub onInAppMessageReceived()
  in_app_message = m.BrazeTask.BrazeInAppMessage
  ...
end sub
```

## Champs de message in-app

Les champs suivants répertorient les champs dont vous aurez besoin pour gérer vos messages in-app :

| Champs | Description |
| ------ | ----------- |
| `buttons` | Liste des boutons (peut être une liste vide). |
| `click_action` | `"URI"` ou `"NONE"`. Utilisez ce champ pour indiquer si le message in-app doit s’ouvrir sur un lien URI ou fermer le message lorsque vous cliquez dessus. Lorsqu’il n’y a pas de boutons, cela doit se produire lorsque l’utilisateur clique sur « OK » quand le message in-app s’affiche. |
| `dismiss_type` | `"AUTO_DISMISS"` ou `"SWIPE"`. Utilisez ce champ pour indiquer si votre message intégré à l’application sera automatiquement supprimé ou nécessitera d’être balayé pour être supprimé. |
| `display_delay` | Durée d’attente (en secondes) jusqu’à l’affichage du message in-app. |
| `duration` | Durée d’affichage (en millisecondes) du message quand `dismiss_type` est défini sur `"AUTO_DISMISS"`. |
| `extras` | Paires clé-valeur. |
| `header` | Le texte de l’en-tête. |
| `id` | L’ID utilisé pour journaliser les impressions ou les clics. |
| `image_url` | URL de l’image du message in-app. |
| `message` | Texte du corps de message. |
| `uri` | Vos utilisateurs URI seront envoyés vers en fonction de votre `click_action`. Ce champ doit être inclus lorsque `click_action` est `"URI"`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Pour les messages in-app contenant des boutons, le message `click_action` sera également inclus dans la charge utile finale si l'action de clic est ajoutée avant l'ajout du texte du bouton.
{% endalert %}

### Champs de style
Il existe également plusieurs champs de style que vous pouvez choisir d’utiliser dans le tableau de bord :

| Champs | Description |
| ------ | ----------- |
| `bg_color` | Couleur d’arrière-plan. |
| `close_button_color` | Couleur du bouton de fermeture. |
| `frame_color` | La couleur du recouvrement de l’écran d’arrière-plan. |
| `header_text_color` | Couleur du texte en-tête. |
| `message_text_color` | Couleur du texte du message. |
| `text_align` | « START », « CENTER » ou « END ». L’alignement de texte que vous avez sélectionné. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Vous pouvez également implémenter le message in-app et modifier son style dans votre application Roku à l’aide d’une palette standard :

### Champs Bouton

| Champs | Description |
| ------ | ----------- |
| `click_action` | `"URI"` ou `"NONE"`. Utilisez ce champ pour indiquer si le message in-app doit s’ouvrir sur un lien URI ou fermer le message lorsque vous cliquez dessus. |
| `id` | La valeur d’ID du bouton lui-même. |
| `text` | Le texte à afficher sur le bouton. |
| `uri` | Vos utilisateurs URI seront envoyés vers en fonction de votre `click_action`. Ce champ doit être inclus lorsque `click_action` est `"URI"`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Gérer les interactions

Vous devrez vous assurer que certaines fonctions sont appelées pour gérer les analyses de votre campagne.

##### Lorsqu’un message s’affiche

Lorsqu’un message s’affiche ou est vu, journalisez une impression :
```brightscript
LogInAppMessageImpression(in_app_message.id, brazetask)
```

##### Lorsqu’un utilisateur clique sur un message
Une fois qu’un utilisateur clique sur le message, enregistrez un clic puis traitez `in_app_message.click_action` :
```brightscript
LogInAppMessageClick(in_app_message.id, brazetask)
```

##### Lorsqu’un utilisateur clique sur un bouton
Si l’utilisateur clique sur un bouton, journalisez le clic sur le bouton puis traitez `inappmessage.buttons[selected].click_action` :

```brightscript
LogInAppMessageButtonClick(inappmessage.id, inappmessage.buttons[selected].id, brazetask)
```

##### Après avoir traité un message in-app
Après avoir traité un message in-app, vous devez effacer le champ :
```brightscript
m.BrazeTask.BrazeInAppMessage = invalid
```
