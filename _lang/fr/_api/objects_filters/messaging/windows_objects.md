---
nav_title: "Objet Windows"
article_title: Objet de messagerie Windows
page_order: 14
page_type: reference
channel: push
platform:
  - Windows Universal
description: "Cet article répertorie et explique les différents objets Windows utilisés chez Braze."
hidden: true
---
# Spécification de l’objet Windows

Les objets `windows_phone8_push` et `windows_universal_push` sont utilisés pour définir ou demander des informations relatives au contenu de notification push Windows Phone 8 et Windows Universal via nos [endpoints d’envoi de messages]({{site.baseurl}}/api/endpoints/messaging).

## Objet Notification push Windows Phone 8

```json
{
   "push_type": (optional, string) doit être « toast »",
   "toast_title": (optional, string) le titre de la notification,
   "toast_content": (required, string) le message de notification,
   "toast_navigation_uri": (optional, string) URI de la page vers laquelle envoyer l’utilisateur,
   "toast_hash": (optional, object) clés et valeurs supplémentaires à envoyer,
   "message_variation_id": (optional, string) utilisé lorsqu’un campaign_id est fourni pour spécifier avec quelle variation du message ce message doit être suivi (il doit s’agir d’un message de notification push Windows Phone 8)
}
```

## Objet Notification push Windows Universal

Voir le [catalogue des modèles toast][32] de Windows Universal pour plus d’informations sur les options de `push_type`.

```json
{
   "push_type": (required, string) un parmi: "« toast_text_01 », « toast_text_02 », « toast_text_03 », « toast_text_04 », « toast_image_and_text_01 », « toast_image_and_text_02 », « toast_image_and_text_03 » ou « toast_image_and_text_04 »",
   "toast_text1": (required, string) la première ligne de texte du modèle,
   "toast_text2": (optional, string) la seconde ligne de texte (pour les modèles avec plus d’une ligne de texte),
   "toast_text3": (optional, string) la troisième ligne de texte (pour les modèles 04),
   "toast_text_img_name": (optional, string) le chemin de l’image pour les modèles qui comprennent une image,
   "message_variation_id": (optional, string) utilisé lorsqu’un campaign_id est fourni pour spécifier avec quelle variation du message ce message doit être suivi (il doit s’agir d’un message de notification push Windows Universal),
   "extra_launch_string": (optional, string) utilisé pour ajouter une fonctionnalité de lien profond en transmettant des valeurs supplémentaires à le string de lancement
}
```

Pour plus d’informations sur l’utilisation du paramètre `extra_launch_string` pour la [création de liens profonds][38], voir [Création de liens profonds avec Windows Universal.][37]

[32]: https://msdn.microsoft.com/en-us/library/windows/apps/hh761494.aspx
[37]: {{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/push_notifications/integration/#step-4-deep-linking-from-push-into-your-app
[38]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking
