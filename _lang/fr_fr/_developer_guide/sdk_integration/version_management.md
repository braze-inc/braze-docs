---
page_order: 10
nav_title: Gestion des versions
article_title: À propos de la gestion des versions du SDK de Braze
description: "Découvrez la gestion des versions du SDK de Braze."
---

# À propos de la gestion des versions

> Découvrez la gestion des versions du SDK de Braze, afin que votre application puisse bénéficier des dernières fonctionnalités et améliorations de qualité. Étant donné que les anciennes versions du SDK peuvent ne pas recevoir les derniers correctifs, corrections de bogues ou assistance, nous vous recommandons de toujours maintenir votre SDK à jour dans le cadre de votre cycle de développement continu.

## Recommandations en matière de versions

Tous les SDK de Braze adhèrent à la [spécification de versionnement sémantique (SemVer)](https://semver.org/), de sorte qu'étant donné un numéro de version `MAJOR.MINOR.PATCH`, nous recommandons ce qui suit :

|Version|À propos de cette version|Recommandation|
|-------|------------------|--------------|
| `PATCH` | Les mises à jour sont toujours constantes et comprennent d'importantes corrections de bogues. Ils seront toujours en sécurité. | Vous devez toujours essayer de mettre à jour immédiatement la dernière version du correctif de votre version majeure et mineure actuelle. |
| `MINOR` | Les mises à jour sont toujours constantes et comprennent de nouvelles fonctionnalités nettes. Ils ne nécessiteront jamais de modification du code de votre application. | Bien qu'il ne soit pas nécessaire de le faire immédiatement, vous devriez mettre à jour la dernière version mineure de votre version majeure actuelle dès que possible. 
| `MAJOR` | Les mises à jour sont des changements radicaux qui peuvent nécessiter des modifications du code de votre application. | Comme cela peut nécessiter des modifications de code, mettez à jour la dernière version majeure dans un délai qui convient le mieux à votre équipe. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert note %}
Il arrive que de nouvelles mises à jour des systèmes d'exploitation Android ou Apple nécessitent des modifications du SDK de Braze. Pour que votre application soit compatible avec les téléphones plus récents, il est important que vous mainteniez votre SDK à jour.
{% endalert %}

## À propos des problèmes connus

Afin de nous assurer que nos changements ne briseront pas vos pipelines de création, **nous ne modifierons ni ne supprimerons jamais une version après qu'elle ait été publiée sur un système de distribution, même si**cette version particulière présente des problèmes connus.

Dans ces cas, nous documenterons le problème dans le [journal des modifications du SDK Braze]({{site.baseurl}}/developer_guide/changelogs/), puis nous publierons un nouveau correctif pour les versions majeures ou mineures concernées dès que possible.
