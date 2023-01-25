---
nav_title: "Objet Webhook"
article_title: Objet de messagerie Webhook
page_order: 13
page_type: reference
channel: 
  - webhook
description: "Cet article présente l’objet webhook de Braze."

---

# Spécification de l’objet Webhook

L’objet `webhook` vous permet de modifier ou de créer des messages webhook via nos [endpoints d’envoi de messages]({{site.baseurl}}/api/endpoints/messaging).

```json
{
  "url": (required, string),
  "request_method": (required, string) « POST », « PUT », « DELETE » ou « GET »,
  "request_headers": (optional, Hash) paires clé-valeur à utiliser en tant qu’en-têtes de requête,
  "body": (optional, string) si vous désirez intégrer un objet JSON, assurez-vous d’échapper les apostrophes et les backslash,
  "message_variation_id": (optional, string) utilisé lorsqu’un campaign_id est fourni pour spécifier avec quelle variation du message ce message doit être suivi
}
```

En tant que meilleure pratique, Braze recommande de fournir une valeur explicite pour `Content-Type` dans le champ `request_headers` afin de garantir un comportement cohérent et prévisible, car les expéditeurs et les serveurs peuvent changer au fil du temps. Si aucune valeur n’est spécifiée pour l’en-tête `Content-Type`, elle sera déduite du corps de la requête.
