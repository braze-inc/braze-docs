{% multi_lang_include developer_guide/prerequisites/android.md %}

## À propos de la prise en charge de la télévision et de l'OTT

Le SDK Android Braze prend nativement en charge l'affichage des messages in-app sur les appareils OTT comme Android TV ou Fire Stick. Cependant, il existe des différences essentielles entre les messages natifs Android et les messages in-app OTT. Pour les appareils OTT :

- Les messages in-app qui nécessitent un mode tactile, comme les messages contextuels, sont désactivés sur OTT.
- L’élément actuellement sélectionné ou ciblé, tel qu’un bouton ou un bouton de fermeture, sera mis en surbrillance.
- Les clics sur le corps du message in-app lui-même, c.-à-d., pas sur un bouton, ne sont pas pris en charge.
