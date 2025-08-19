---
nav_title: Phrase
article_title: Phrase
alias: /partners/phrase/
description: "Cet article de référence présente le partenariat entre Braze et Phrase, un logiciel de localisation basé dans le cloud. Cette intégration vous permet de traduire les modèles d'e-mail et les blocs de contenu sans quitter l'interface de Braze."
page_type: partner
search_tag: Partner

---

# Phrase 

> [Phrase](https://phrase.com/) est un logiciel basé dans le cloud qui permet de gérer la localisation. Phrase permet d'automatiser les flux de traduction et de prendre en charge la localisation continue pour les équipes agiles.

_Cette intégration est assurée par Phrasee._

## À propos de l'intégration

L'intégration de Phrase et de Braze vous permet de traduire des modèles d'e-mail et des blocs de contenu sans quitter l'interface de Braze. Grâce à l'intégration de Phrase TMS pour Braze, vous pouvez accroître l'engagement client et stimuler la croissance sur de nouveaux marchés grâce localisation fluide des contenus.

## Prérequis

| Condition | Descriptif |
| --- | --- |
| Compte Phrase TMS | Un compte Phrase TMS Ultimate ou Enterprise est nécessaire pour bénéficier de ce partenariat. |
| Clé API REST de Braze | Une clé API REST Braze avec toutes les permissions. <br><br> Cette clé peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
| Endpoint REST de Braze | [L'URL de votre endpoint REST.][1] Votre endpoint dépendra de l'URL de Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

## Étape 1 : Paramètres Phrase TMS

Dans Phrase, accédez à **Paramètres > Intégrations > Connecteurs > Nouveau**.

1. Donnez un nom à la connexion et changez le type en **Braze**.<br><br>
2. Saisissez la clé de l'API REST et l’endpoint REST de Braze. <br><br>
3. Sélectionnez la manière dont le connecteur doit importer les modèles d'e-mail avec les blocs de contenu liés. 
- Modèle d'e-mail sélectionné uniquement
- Inclure des blocs de contenu<br><br>
4. Sélectionnez la manière dont le connecteur doit exporter les traductions des modèles d'e-mail. 
- Créer un nouvel élément
- Élément d’origine
  - L'élément d’origine exporte les traductions vers le même modèle/bloc. Les segments linguistiques sont définis par l'attribut fourni.<br><br>
    {% raw %}
    Indiquez l'attribut de la langue si l'élément original est sélectionné. L'attribut language définit la langue de l'argument if/elsif. Si vous utilisez l'option de l'élément d’origine, il doit être structuré comme indiqué ci-dessous :

    ```liquid
    {% if {{custom_attribute.${attribute_name}}} == 'da-DK' %}
    danish content
    {% elsif {{custom_attribute.${attribute_name}}} == 'pt-PT' %}
    portuguese content
    {% elsif {{custom_attribute.${attribute_name}}} == 'sv-SE' %}
    swedish content
    {% else %}
    Original content
    {% endif %}
    ```
    Ou en utilisant le mappage touches/valeurs d'affectation :
    ```liquid
    {% if {{custom_attribute.${attribute_name}}} == 'da-DK' %}
      {% assign abc_key1 = "danish_value1" %}
    {% elsif {{custom_attribute.${attribute_name}}} == 'pt-PT' %}
      {% assign abc_key = "portuguese value" %}
    {% elsif {{custom_attribute.${attribute_name}}} == 'sv-SE' %}
      {% assign abc_key = "swedish value" %}
    {% else %}
      {% assign abc_key = "Source language value" %}
    {% endif %}
    ```
    La configuration Liquid ci-dessus doit être strictement respectée, mais l'attribut de langue ainsi que les clés et les valeurs associées peuvent être ajustés.<br><br>
    Chaque code linguistique ne peut être utilisé qu'une seule fois. Toutefois, plusieurs langues peuvent être utilisées pour un même segment, par exemple :
    ```liquid
    {% elsif {{custom_attribute.${attribute_name}}} == 'de-DE' or {{custom_attribute.${attribute_name}}} == 'de-AT' or {{custom_attribute.${attribute_name}}} == 'de-CH' %}
    {% endraw %}
    ```
5. Cliquez sur **Tester la connexion**. Une coche apparaît si la connexion est réussie. Survolez l'icône pour obtenir des détails supplémentaires.<br><br>
7. Enfin, cliquez sur **Enregistrer.** Ce connecteur sera disponible sur la page **Connecteurs.**

## Étape 3 : Envoyez du contenu à Phrase et réexportez vers Braze

1. Tout d'abord, configurez le [portail de soumission](https://support.phrase.com/hc/en-us/articles/5709602111132) pour permettre aux soumissionnaires d'ajouter des fichiers aux requêtes directement à partir du référentiel en ligne.<br><br>
2. Utilisez la [création automatique de projets (APC)](https://support.phrase.com/hc/en-us/articles/5709647363356) pour que Phrase TMS crée automatiquement de nouveaux projets lorsqu'un changement dans les états de flux de travail spécifiés est détecté.<br><br>
3. Les éléments de contenu sélectionnés sont importés dès la première exécution d'APC.

L'[API du connecteur](https://cloud.memsource.com/web/docs/api#) permet d'automatiser des étapes qui, autrement, seraient effectuées manuellement via l'interface utilisateur. Les [webhooks](https://support.phrase.com/hc/en-us/articles/5709693398812) peuvent être utilisés pour que Phrase TMS informe des systèmes tiers de certains événements (par exemple, un changement de statut d'un travail).


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
