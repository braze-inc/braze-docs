---
nav_title: Intégration des partenaires API
alias: /api_partner_integration/
hidden: true
---

# Intégration des partenaires API

> Découvrez les exigences relatives aux intégrations API des partenaires, telles que la syntaxe des en-têtes `User-Agent`.

{% alert important %}
Auparavant, les partenaires devaient ajouter leur nom au champ partenaire dans leurs demandes d'API. Ce formatage n'est plus pris en charge et un en-tête `User-Agent` est désormais nécessaire.
{% endalert %}

## Agents utilisateurs

Vous devez inclure un en-tête `User-Agent` qui identifie clairement la source du trafic. Cela permet à nos clients partagés de voir le trafic des partenaires dans les rapports d'utilisation de l'API de Braze, et aux ingénieurs de Braze d'identifier les intégrations qui ne respectent pas les meilleures pratiques. En règle générale, vous ne devez utiliser qu'un seul agent utilisateur pour l'ensemble de votre trafic.

### Syntaxe

Votre en-tête `User-Agent` doit respecter le format suivant (qui est similaire à la norme [RFC 7231](https://datatracker.ietf.org/doc/html/rfc7231#page-46) ) :

```bash
User-Agent: partner-OrganizationName-ProductName/ProductVersion
```

Remplacez les éléments suivants :

| Marque substitutive | Description |
|-------------|-------------|
| `OrganizationName` | Le nom de votre organisation formaté en majuscules Pascal. |
| `ProductName` | Le nom de votre produit formaté en majuscules Pascal. |
| `ProductVersion` | Le numéro de version de votre produit. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Exemples

Par exemple, l'agent utilisateur suivant serait correct pour l'ingestion de données dans le nuage de Snowflake :

```bash
User-Agent: partner-Snowflake-CloudDataIngestion/179
```

Alors que ce serait incorrect car il n'identifie pas clairement la source du trafic :

```bash
User-Agent: axios/1.4.0
``` 
