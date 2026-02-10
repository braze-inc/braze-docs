{% multi_lang_include developer_guide/prerequisites/android.md %}

## Données d'envoi des messages

Vous devrez vous assurer que certaines fonctions sont appelées pour gérer les analyses de votre campagne.

### Messages affichés

Lorsqu’un message s’affiche ou est vu, journalisez une impression :

```brightscript
LogInAppMessageImpression(in_app_message.id, brazetask)
```

### Messages cliqués

Une fois qu’un utilisateur clique sur le message, enregistrez un clic puis traitez `in_app_message.click_action` :

```brightscript
LogInAppMessageClick(in_app_message.id, brazetask)
```

### Boutons cliqués

Si l’utilisateur clique sur un bouton, journalisez le clic sur le bouton puis traitez `inappmessage.buttons[selected].click_action` :

```brightscript
LogInAppMessageButtonClick(inappmessage.id, inappmessage.buttons[selected].id, brazetask)
```

### Après le traitement d'un message

Après avoir traité un message in-app, vous devez effacer le champ :

```brightscript
m.BrazeTask.BrazeInAppMessage = invalid
```
