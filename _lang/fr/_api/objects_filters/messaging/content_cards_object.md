---
nav_title: "Objet de carte de contenu"
article_title: Objet de messagerie de la carte de contenu
page_order: 4
page_type: référence
channel: cartes de contenu
description: "Cet article explique les différents composants de l’objet Carte de contenu de Braze."

---

# Spécification de l’objet de carte de contenu

L’objet `content_card` vous permet de modifier ou de créer des cartes de contenu via nos [endpoints d’envoi de messages]({{site.baseurl}}/api/endpoints/messaging).

## Corps

```json
{
  "type": (required, string) « CLASSIC », « CAPTIONED_IMAGE » ou « BANNER »,
  "title": (required, string) le titre de la carte,
  "description": (required, string) la description de la carte,
  "message_variation_id": (optional, string) utilisé lorsqu’un campaign_id est fourni pour spécifier avec quelle variation du message ce message doit être suivi (il doit s’agir d’un message de carte de contenu),
  "pinned": (optional, boolean) si la carte est épinglée. Défini par défaut sur « false »,
  "image_url": (optional, string) l’URL de l’image de la carte. Nécessaire pour « CAPTIONED_IMAGE » et « BANNER »",
  "time_to_live": (optional, integer) le nombre de secondes avant l’expiration de la carte. Vous devez inclure « time_to_live » ou « expire_at »",
  "expire_at": (optional, string) Date d’expiration de la carte au format ISO 8601. Vous devez inclure « time_to_live » ou « expire_at » un délai d’expiration maximum de 30 jours existe,
  "expire_in_local_time": (optional, boolean) si « expire_at » est utilisé, détermine si la carte doit expirer dans le fuseau horaire de l’utilisateur. Défini par défaut sur « false »,
  "ios_uri": (optional, string) une URL Web ou une URI de lien profond,
  "android_uri": (optional, string) une URL Web ou une URI de lien profond,
  "web_uri": (optional, string) une URL Web ou une URI de lien profond,
  "ios_use_webview": (optional, boolean) si l’URL Web doit être ouverte dans l’application, défini par défaut sur « true »,
  "android_use_webview": (optional, boolean) si l’URL Web doit être ouverte dans l’application, défini par défaut sur « true »,
  "uri_text": (optional, string) le texte du lien de la carte,
  "extra": (optional, object) clés et valeurs supplémentaires à envoyer avec la carte,
}
```

{% alert important %}
Actuellement, Braze prend en charge une durée d’expiration maximale de 30 jours.
{% endalert %}
