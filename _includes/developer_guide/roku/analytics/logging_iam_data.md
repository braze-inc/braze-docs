{% multi_lang_include developer_guide/prerequisites/android.md %}

## Logging message data

You will need to make sure certain functions are called to handle the analytics for your campaign.

### Displayed messages

When a message is displayed or seen, log an impression:

```brightscript
LogInAppMessageImpression(in_app_message.id, brazetask)
```

### Clicked messages

Once a user clicks on the message, log a click and then process `in_app_message.click_action`:

```brightscript
LogInAppMessageClick(in_app_message.id, brazetask)
```

### Clicked buttons

If the user clicks on a button, log the button click and then process `inappmessage.buttons[selected].click_action`:

```brightscript
LogInAppMessageButtonClick(inappmessage.id, inappmessage.buttons[selected].id, brazetask)
```

### After processing a message

After processing an in-app message, you should clear the field:

```brightscript
m.BrazeTask.BrazeInAppMessage = invalid
```
