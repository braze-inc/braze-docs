---
nav_title: Points de terminaison SDK
article_title: Points de terminaison SDK
page_order: 1
page_type: Référence
description: "Cet article de référence couvre les points de terminaison SDK de Braze et leur utilisation."
---

# Points de terminaison SDK

## Qu'est-ce qu'un SDK?

Un kit de développement de logiciels (SDK) est un ensemble d'outils qui peuvent être utilisés pour développer des applications logicielles ciblant une plate-forme spécifique. Le SDK Braze permet de suivre l'engagement de vos utilisateurs avec votre application ou votre site et permet l'envoi de campagnes ciblées. En savoir plus sur le Braze SDK dans notre parcours LAB, [Braze 101][85].

## Points de terminaison du SDK Braze

| Instance | Point de terminaison SDK |
| -------- | ------------------------ |
| US-01    | sdk.iad-01.braze.com     |
| US-02    | sdk.iad-02.braze.com     |
| US-03    | sdk.iad-03.braze.com     |
| US-04    | sdk.iad-04.braze.com     |
| US-05    | sdk.iad-05.braze.com     |
| US-06    | sdk.iad-06.braze.com     |
| US-08    | sdk.iad-08.braze.com     |
| EU-01    | sdk.fra-01.braze.eu      |
{: .reset-td-br-1 .reset-td-br-2}

Lors de l'utilisation de points de terminaison pour l'intégration du SDK, utilisez le __point de terminaison SDK__ listé sur cette page, __pas__ le [point de repos]({{site.baseurl}}/api/basics/#endpoints) utilisé pour les appels API.

{% alert note %}
Pour configurer le Braze Web SDK pour utiliser le point de terminaison approprié pour votre intégration, vous devez utiliser l'option `baseUrl` lors de l'initialisation de la fonction et inclure le point de terminaison SDK ici. Par exemple `appboy.initialize('VOTRE API-KEY-ICI', {baseUrl: 'sdk.iad-03.braze.com'})` <br>Pour plus d'informations, consultez notre <a href="https://github.com/Appboy/appboy-web-sdk#getting-started">documentation Github Web SDK</a>.
{% endalert %}

## Taille du fichier SDK

| Plateforme | Taille approximative du SDK                              |
| ---------- | -------------------------------------------------------- |
| Android    | 800 Ko                                                   |
| iOS        | (IPA - Addition to App File) 1MB - 2MB; (Framework) 30MB |
| Web        | 36Ko (cœur), 50Ko (cœur + UI)                            |
{: .reset-td-br-1 .reset-td-br-2}

[85]: https://lab.braze.com/braze-101
