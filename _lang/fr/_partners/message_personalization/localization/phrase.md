---
nav_title: Phrase
article_title: Phrase
alias: /partners/phrase/
description: "Cet article décrit le partenariat entre Braze et Phrase, un logiciel cloud de localisation. Cette intégration vous permet de traduire des modèles d’e-mails et des blocs de contenu sans quitter l’interface Braze."
page_type: partner
search_tag: Partenaire

---

# Phrase 

[Phrase](https://phrase.com/) est un logiciel cloud pour la gestion de la localisation. Phrase permet des flux de travail de traduction automatisés et prend en charge la localisation continue pour les équipes agiles.

L’intégration Phrase et Braze vous permet de traduire des modèles d’e-mails et des blocs de contenu sans quitter l’interface Braze. Grâce à l’intégration TMS Phrase pour Braze, vous pouvez augmenter l’engagement client et stimuler la croissance sur de nouveaux marchés à l’aide d’une localisation harmonieuse.

## Conditions préalables

| Condition | Description |
| --- | --- |
| Compte TMS Phrase | Un compte TMS d’entreprise ou Ultimate Phrase est requis pour profiter de ce partenariat. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec toutes les autorisations. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Endpoint REST de Braze | [URL de votre endpoint REST][1]. Votre endpoint dépendra de l’URL Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

## Étape 1 : Paramètres TMS Phrase

Dans Phrase, accédez à **Settings > Integrations > Connectors > New (Paramètres > Intégrations > Connecteurs > Nouveau)**.

1. Donnez un nom à la connexion et changez le type en **Braze**.<br><br>
2. Saisissez la clé API REST et l’endpoint REST de Braze. <br><br>
3. Sélectionnez comment le connecteur doit importer des modèles d’e-mail avec des blocs de contenu liés. 
- Modèle d’e-mail sélectionné uniquement
- Inclure les blocs de contenu<br><br>
4. Sélectionnez comment le connecteur doit exporter les traductions de modèles d’e-mail. 
- Créer un nouvel élément
- Élément d’origine
  - L’élément d’origine exporte les traductions vers le même modèle/bloc. Les segments de langue sont définis par l’attribut fourni.<br><br>
    {% raw %}
    Fournit l’attribut de langue si l’élément d’origine est sélectionné. L’attribut de langue définit la langue de l’argument « if/elsif ». Si vous utilisez l’option d’élément d’origine, il doit être structuré comme indiqué ci-dessous :

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
    Ou à l’aide du mappage assigner clés/valeurs :
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
    Le Liquid ci-dessus doit être strictement suivi, mais l’attribut de langue et la langue, les clés et la valeur sont réglables.<br><br>
    Chaque code de langue ne peut être utilisé qu’une seule fois. Cependant, plusieurs langues peuvent être utilisées pour un segment, par exemple :
    ```liquid
    {% elsif {{custom_attribute.${attribute_name}}} == 'de-DE' or {{custom_attribute.${attribute_name}}} == 'de-AT' or {{custom_attribute.${attribute_name}}} == 'de-CH' %}
    {% endraw %}
    ```
5. Cliquez sur **Test connection (Tester la connexion)**. Une coche apparaîtra si la connexion est réussie. Survolez l’icône pour voir des détails supplémentaires.<br><br>
7. Enfin, cliquez sur **Save (Enregistrer)**. Ce connecteur sera disponible sur la page **Connectors (Connecteurs)**.

## Étape 3 : Envoyer le contenu à Phrase et l’exporter à nouveau vers Braze

1. Tout d’abord, configurez le [portail des soumissionnaires](https://support.phrase.com/hc/en-us/articles/5709602111132) pour permettre aux soumissionnaires d’ajouter des fichiers aux demandes, directement à partir du référentiel en ligne.<br><br>
2. Utilisez la [création automatisée de projet (Automated Project Creation, APC)](https://support.phrase.com/hc/en-us/articles/5709647363356) pour que le TMS Phrase crée automatiquement de nouveaux projets lorsqu’un changement dans les états de flux de travail spécifiés est détecté.<br><br>
3. Les éléments de contenu sélectionnés sont importés la toute première fois qu’APC s’exécute.

Le [connecteur API](https://cloud.memsource.com/web/docs/api#) peut automatiser les étapes effectuées manuellement via l’interface utilisateur. Les [Webhooks](https://support.phrase.com/hc/en-us/articles/5709693398812) peuvent être utilisés pour que le TMS Phrase informe les systèmes tiers de certains événements (par exemple, un changement de statut de tâche).

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
