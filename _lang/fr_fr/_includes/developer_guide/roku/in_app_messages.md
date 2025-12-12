{% multi_lang_include developer_guide/prerequisites/roku.md %} En outre, les messages in-app ne seront envoyés qu'aux appareils Roku fonctionnant avec la version minimale du SDK prise en charge :

{% sdk_min_versions roku:0.1.2 %}

## Types de messages

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## Activation des messages in-app

### Étape 1 : Ajouter un observateur

Pour traiter les messages in-app, vous pouvez ajouter un observateur à `BrazeTask.BrazeInAppMessage` :

```brightscript
m.BrazeTask.observeField("BrazeInAppMessage", "onInAppMessageReceived")
```

### Étape 2 : Accéder aux messages déclenchés

Puis, dans votre gestionnaire, vous avez accès au message in-app le plus élevé que vos campagnes ont déclenché :

```brightscript
sub onInAppMessageReceived()
  in_app_message = m.BrazeTask.BrazeInAppMessage
  ...
end sub
```

## Champs de messages

### Manipulation

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

### Stylisme

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

### Boutons

| Champs | Description |
| ------ | ----------- |
| `click_action` | `"URI"` ou `"NONE"`. Utilisez ce champ pour indiquer si le message in-app doit s’ouvrir sur un lien URI ou fermer le message lorsque vous cliquez dessus. |
| `id` | La valeur d’ID du bouton lui-même. |
| `text` | Le texte à afficher sur le bouton. |
| `uri` | Vos utilisateurs URI seront envoyés vers en fonction de votre `click_action`. Ce champ doit être inclus lorsque `click_action` est `"URI"`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
