---
nav_title: "Objet Windows"
article_title: Objet Windows Messaging
page_order: 14
page_type: Référence
channel: Pousser
platform:
  - Univers Windows
description: "Cet article liste et explique les différents objets Windows utilisés au Brésil."
---

# Spécification de l'objet Windows

Ces objets sont utilisés pour définir ou demander des informations relatives au contenu Push de Windows Phone 8 et Windows Universal Push content.

## Objet push Windows Phone 8

```json
{
   "push_type": (optionnel, string) doit être "toast",
   "toast_title": (optionnel, chaîne) le titre de la notification,
   "toast_content": (obligatoire, chaîne) le message de notification,
   "toast_navigation_uri": (optionnel, chaîne) page uri à envoyer à l'utilisateur,
   "toast_hash": (optionnel, objet) clés et valeurs supplémentaires à envoyer,
   "message_variation_id": (optionnel, string) utilisé lors de la fourniture d'un campaign_id pour spécifier la variation de message sous laquelle ce message doit être suivi (doit être un message Push Message Windows Phone 8)
}
```

## Objet push Windows Universal

Reportez-vous au catalogue des modèles de toast [universels de Windows][32] pour plus de détails sur les options pour `push_type` ci-dessous.

```json
{
   "push_type": (required, string) un de : "toast_text_01", "toast_text_02", "toast_text_03", "toast_text_04", "toast_image_and_text_01", "toast_image_and_text_02", "toast_image_and_text_03", ou "toast_image_and_text_04",
   "toast_text1": (requis, string) la première ligne de texte dans le template,
   "toast_text2": (optionnel, chaîne) la deuxième ligne de texte (pour les modèles avec > 1 ligne de texte),
   "toast_text3": (optionnel, chaîne) la troisième ligne de texte (pour les modèles *_04)
   "toast_text_img_name": (optionnel, chaîne) le chemin de l'image pour les modèles qui incluent une image,
   "message_variation_id": (optionnel, ) utilisé lors de la fourniture d'un campaign_id pour spécifier la variation de message sous laquelle ce message doit être suivi (doit être un message Universal Push Message),
   "extra_launch_string": (optionnel, chaîne) utilisé pour ajouter des fonctionnalités de liaison profonde en passant des valeurs supplémentaires à la chaîne de lancement
}
```

Pour plus d'informations sur l'utilisation du paramètre `extra_launch_string` pour un lien profond, voir [Lien profond avec Windows Universal.][37] Pour plus d'informations sur ce qu'est un lien profond, veuillez consulter notre [FAQ Section][38].

[32]: https://msdn.microsoft.com/en-us/library/windows/apps/hh761494.aspx
[37]: {{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/push_notifications/integration/#step-4-deep-linking-from-push-into-your-app
[38]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking
