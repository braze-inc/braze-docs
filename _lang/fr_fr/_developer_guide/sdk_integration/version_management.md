---
page_order: 10
nav_title: Gestion des versions
article_title: À propos de la gestion des versions du SDK de Braze
description: "Découvrez la gestion des versions du SDK de Braze."
---

# À propos de la gestion des versions

> Découvrez la gestion des versions du SDK de Braze, afin que votre application puisse bénéficier des dernières fonctionnalités et améliorations de qualité. Étant donné que les anciennes versions du SDK peuvent ne pas recevoir les derniers correctifs, corrections de bogues ou l'assistance la plus récente, nous vous recommandons de toujours maintenir votre SDK à jour dans le cadre de votre cycle de développement continu.

## Recommandations en matière de versions

Tous les SDK de Braze respectent la [spécification de versionnement sémantique (SemVer)](https://semver.org/). Pour un numéro de version `MAJOR.MINOR.PATCH`, voici nos recommandations :

|Version|À propos de cette version|Recommandation|
|-------|------------------|--------------|
| `PATCH` | Les mises à jour sont toujours non cassantes et comprennent d'importantes corrections de bogues. Elles sont toujours sûres à appliquer. | Vous devriez toujours essayer de mettre à jour immédiatement vers la dernière version de correctif de votre version majeure et mineure actuelle. |
| `MINOR` | Les mises à jour sont toujours non cassantes et comprennent de nouvelles fonctionnalités. Elles ne nécessiteront jamais de modification du code de votre application. | Bien qu'il ne soit pas nécessaire de le faire immédiatement, vous devriez mettre à jour vers la dernière version mineure de votre version majeure actuelle dès que possible. 
| `MAJOR` | Les mises à jour sont des changements cassants qui peuvent nécessiter des modifications du code de votre application. | Comme cela peut nécessiter des modifications de code, mettez à jour vers la dernière version majeure dans un délai qui convient le mieux à votre équipe. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert note %}
Il arrive que de nouvelles mises à jour des systèmes d'exploitation Android ou Apple nécessitent des modifications du SDK de Braze. Pour que votre application reste compatible avec les téléphones plus récents, il est important de maintenir votre SDK à jour.
{% endalert %}

## Recevoir des notifications pour les nouvelles versions

Pour recevoir des notifications automatiques lorsqu'une nouvelle version du SDK est publiée, vous pouvez surveiller le dépôt GitHub de n'importe quel SDK de Braze :

1. Accédez au dépôt GitHub du SDK (par exemple, [braze-android-sdk](https://github.com/braze-inc/braze-android-sdk), [braze-swift-sdk](https://github.com/braze-inc/braze-swift-sdk) ou [braze-web-sdk](https://github.com/braze-inc/braze-web-sdk)).
2. Cliquez sur **Watch** dans le coin supérieur droit.
3. Cliquez sur **Custom**, puis sélectionnez **Releases** et cliquez sur **Apply**.

Vous recevrez une notification GitHub (ainsi qu'un e-mail, selon vos [paramètres de notification](https://github.com/settings/notifications)) chaque fois qu'une nouvelle version est publiée. Pour la liste complète des dépôts SDK, consultez [Références, dépôts et exemples d'applications]({{site.baseurl}}/developer_guide/references/).

## À propos des problèmes connus

Afin de garantir que nos changements ne cassent pas vos pipelines de build, **nous ne modifions ni ne supprimons jamais une version après sa publication sur un système de distribution**&#8212;même si cette version présente des problèmes connus.

Dans ce cas, nous documentons le problème dans le [journal des modifications du SDK de Braze]({{site.baseurl}}/developer_guide/changelogs/), puis nous publions un nouveau correctif pour les versions majeures ou mineures concernées dès que possible.