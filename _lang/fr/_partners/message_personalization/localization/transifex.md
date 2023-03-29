---
nav_title: Transifex
article_title: Transifex
alias: /partners/transifex/
description: "Cet article de référence présente le partenariat entre Braze et Transifex, une plateforme de localisation qui vous permet d’automatiser la traduction afin que vous puissiez vous concentrer sur la prestation d’expériences client attrayantes."
page_type: partner
search_tag: Partenaire

---

# Transifex

> Transifex permet une localisation efficace de votre base utilisateur, quelle que soit sa langue. 

L’intégration Braze et Transifex tire parti du contenu connecté pour vous permettre d’extraire une collection de chaînes de ressources et d’inclure des traductions pertinentes dans vos messages au lieu de lignes de formatage conditionnel basé sur la langue. Cela automatise la traduction et libère vos équipes pour qu’elles puissent se concentrer sur la prestation d’expériences client exceptionnelles.

{% alert important %}
À partir du 7 avril 2022, les versions 2 et 2.5 de l’API de Transifex sont devenues obsolètes et sont remplacées par la version 3. Les versions v2 et v2.5 ne sont plus opérationnelles, et les demandes correspondantes n’aboutissent plus. <br><br>Les instructions d’intégration suivantes reflètent la mise à jour à la version 3. Mettez à jour vos appels de Contenu connecté en conséquence.
{% endalert %}

## Conditions préalables

| Condition| Description|
| ---| ---|
|Compte Transifex | Un [compte Transifex](https://www.transifex.com/signin/) est nécessaire pour profiter de ce partenariat. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

L’intégration de Transifex utilise l’[API de traductions de ressources](https://developers.transifex.com/reference/get_resource-translations) de Transifex. Le cURL suivant vous permettra de voir si votre compte a des valeurs de contenu associées à des traductions. 

Tout d’abord, saisissez le `<ORGANIZATION_NAME>`, `<PROJECT_NAME>` et `<RESOURCE_NAME>` trouvés sur votre compte Transifex. Ensuite, remplacez `<LANGUAGE>` par le code de langue par lequel vous souhaitez filtrer les traductions, et `<TRANSIFEX_BEARER_TOKEN>` par votre [jeton porteur](https://developers.transifex.com/reference/api-authentication) Transifex.

```
curl --request GET \
     --url 'https://rest.api.transifex.com/resource_translations?filter\[resource\]=o:<ORGANIZATION_NAME>:p:<PROJECT_NAME>:r:<RESOURCE_NAME>&filter\[language\]=l:<LANGUAGE>' \
     --header 'Accept: application/vnd.api+json' \
     --header 'Authorization: Bearer 1/c500429f7b89ff62b8015475ed68d90a2295302'
```

Par exemple, si votre projet Transifex est situé à `https://www.transifex.com/appboy-3/french2/french_translationspo/`, le `project_name` sera « french2 » et le `resource_name` sera « french_translationspo ».

## Exemple de message de contenu connecté

Cet exemple d’extrait de code utilise l’API de traduction de ressources de Transifex et l’attribut `language` de l’utilisateur. En fonction de vos besoins, vous pouvez ensuite parcourir les objets de chaîne de caractères et extraire le contenu pertinent en utilisant la logique Liquid suivante : `{{strings.data[X].attributes.strings.other}}`.

{% raw %}
```
{% assign organization = "<ORGANIZATION_NAME>" %}
{% assign project = "<PROJECT_NAME>" %}
{% assign resource = "<RESOURCE_NAME>" %}

{% if {{${language}}} == "en" or {{${language}}} == "it" or {{${language}}} == "de" or {{${language}}} == "another_language_you_support"  %}
{% connected_content
     https://rest.api.transifex.com/resource_translations?filter[resource]=o:{{organization}}:p:{{project}}:r:{{resource}}&filter[language]=l:{{${language}}}
     :method GET
     :headers {
       "Authorization": "Bearer <TRANSIFEX_BEARER_TOKEN>"
  }
     :accept application/vnd.api+json
     :save strings
%}
{% endif %}

{% if {{strings}} != null and {{strings.data[0].attributes.strings.other}} != "" and {{${language}}} != null %}
  {{strings.data[0].attributes.strings.other}}
{% else %}
  {% abort_message('null or blank') %}
{% endif %}
```
{% endraw %}

[16]: [success@braze.com](mailto:success@braze.com)
[31]: https://docs.transifex.com/api/translation-strings