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

Ce qui suit décrit l'objet Webhook Braze.

En tant que meilleure pratique, Braze recommande que vous fournissiez une valeur explicite pour `Content-Type` dans le champ `request_headers` pour assurer un comportement cohérent et prévisible, car les expéditeurs et les serveurs peuvent changer au fil du temps. Si une valeur n'est pas spécifiée pour l'en-tête `Content-Type` , on sera déduit du corps de la requête.

```json
{
  "url": (obligatoire, chaîne),
  "request_method": (obligatoire, chaîne) un de "POST", "PUT", "DELETE", ou "GET",
  "request_headers": (optionnel, Hash) paires clé-valeur à utiliser comme en-têtes de requête,
  "body": (optionnel, string) si vous voulez inclure un objet JSON, assurez-vous d'échapper les guillemets et les antislashes,
  "message_variation_id": (optionnel, string) utilisée lors de la fourniture d'un campaign_id pour spécifier quelle variation de message ce message doit être suivi sous
}
```
