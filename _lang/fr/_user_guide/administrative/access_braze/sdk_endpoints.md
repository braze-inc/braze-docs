---
nav_title: Endpoints SDK
article_title: Endpoints SDK
page_order: 1
page_type: reference
description: "Cet article de référence couvre les endpoints SDK de Braze et leur utilisation."

---

# Endpoints SDK

> Un kit de Software Development Kit (SDK) est un ensemble d’outils qui peuvent être utilisés pour développer des applications logicielles ciblant une plateforme spécifique. Le SDK Braze permet de suivre l’engagement de vos utilisateurs depuis votre application ou votre site et permet l’envoi de campagnes ciblées. En savoir plus sur le SDK Braze dans notre cours d’apprentissage Braze, [Braze 101][85].

## Endpoints SDK de Braze

|Instance | Endpoint SDK
|---|---|
|US-01 | sdk.iad-01.braze.com |
|US-02 | sdk.iad-02.braze.com |
|US-03 | sdk.iad-03.braze.com |
|US-04 | sdk.iad-04.braze.com |
|US-05 | sdk.iad-05.braze.com |
|US-06 | sdk.iad-06.braze.com |
|US-08 | sdk.iad-08.braze.com |
|EU-01 | sdk.fra-01.braze.eu |
|EU-02 | sdk.fra-02.braze.eu |
{: .reset-td-br-1 .reset-td-br-2}

Lorsque vous utilisez les endpoints pour l’intégration SDK, utilisez le **SDK Endpoint** (Endpoint SDK) figurant sur cette page, et non pas le [REST endpoint][2] (Endpoint REST) utilisé pour les appels API.

{% alert note %}
Pour configurer le SDK Web de Braze pour utiliser l’endpoint approprié pour votre intégration, vous devez utiliser l’option `baseUrl` lors de l’initialisation de la fonction et inclure l’endpoint SDK ici. Par exemple, `braze.initialize('YOUR-API-KEY-HERE', {baseUrl: 'sdk.iad-03.braze.com'})`
<br><br>Pour plus d’informations, consultez notre [Guide de configuration initiale]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/).
{% endalert %}

## Tailles de fichiers SDK

| Plateforme | Taille approximative du SDK |
|---|---|
| Android | 800 Ko |
| iOS | (IPA - Ajout au fichier d’application) 1 Mo - 2 Mo ; (Cadre) 30 Mo |
| Web | 36 Ko (noyau), 50 Ko (noyau + IU) |
{: .reset-td-br-1 .reset-td-br-2}

[85]: https://learning.braze.com/braze-101
[2]: {{site.baseurl}}/api/basics/#endpoints
