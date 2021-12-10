---
nav_title: "POST: [Nom du point final]"
page_order:
layout: api_page
excerpt_separator: ""
page_type: Référence
platform: API
channel:
  - Courriel
  - Pousser
tool:
  - Toile
  - Campagnes
description: "Cet article décrit les détails sur et l'utilisation de ce point de terminaison POST [endpoint name] Braze."
noindex: vrai
---

{% api %}
# [Nom du point final]

{% apimethod post %}
/fr/email/spam/remove
{% endapimethod %}

Ceci est la description de la terminaison. Par exemple: "Ce point de terminaison vous permet de supprimer les adresses e-mail de votre liste de spam Braze. Nous les supprimerons également de la liste de spam maintenue par votre fournisseur de messagerie."

{% apiref swagger %}https://www.braze.com/docs/api/interactive/#/Email%20Sync/RemovingSpamListEmailExemple {% endapiref %}
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1614a82f-510a-4c37-95a6-8207a125e487 {% endapiref %}

## Corps de la requête

C'est ici que vous pouvez donner plus d'informations sur votre corps de requête de terminaux, y compris un exemple de ce à quoi on pourrait ressembler.

```
Type de contenu : application/json
Autorisation : Bearer YOUR-REST-API-KEY
```

```json
{
  "email": "exemple@123.com"
}
```

### Détails du paramètre

C'est un endroit où vous pouvez décrire des détails supplémentaires pour les paramètres ci-dessus.

| Paramètre | Requis | Type de données   | Libellé                                                                             |
| --------- | ------ | ----------------- | ----------------------------------------------------------------------------------- |
| `Email`   | Oui    | Chaîne ou tableau | Chaîne d'adresse e-mail à modifier, ou un tableau de 50 adresses e-mail à modifier. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Exemple de désinscription CURL

L'exemple suivant CURL montre comment désabonner un utilisateur de la réception d'e-mails via les API Braze :

```
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {{YOUR_API_KEY}}" -d '{"email":"EMAIL_TO_UNSUBSCRIBE","subscription_state":"unsubscribed"}' https://rest.iad-01.braze.com/email/status
```
{% endapi %}
