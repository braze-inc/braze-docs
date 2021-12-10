---
nav_title: "Objet Webhook"
article_title: Objet Messagerie Webhook
page_order: 13
page_type: Référence
channel:
  - Webhook
description: "Cet article décrit l'objet Braze Webhook."
---

# Spécification de l'objet Webhook

```json
{
  "url": (obligatoire, chaîne),
  "request_method": (obligatoire, chaîne) un de "POST", "PUT", "DELETE", ou "GET",
  "request_headers": (optionnel, Hash) paires clé-valeur à utiliser comme en-têtes de requête,
  "body": (optionnel, string) si vous voulez inclure un objet JSON, assurez-vous d'échapper les guillemets et les antislashes,
  "message_variation_id": (optionnel, string) utilisée lors de la fourniture d'un campaign_id pour spécifier quelle variation de message ce message doit être suivi sous
}
```
