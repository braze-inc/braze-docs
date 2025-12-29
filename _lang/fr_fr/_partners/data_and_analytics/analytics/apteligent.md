---
nav_title: Apteligent
article_title: Apteligent
alias: /partners/apteligent/
description: "Cet article de référence décrit le partenariat entre Braze et Apteligent, une application mobile spécialisée dans le reporting d'incidents, qui vous permet de consigner des données critiques dans votre solution Braze."
page_type: partner
search_tag: Partner

---

# Apteligent

> [Apteligent](https://www.vmware.com/products/workspace-one/intelligence-consumer-apps.html) est une plateforme d’évaluation des performances des applications mobiles qui fournit des outils et des informations aux développeurs et aux chefs de produits. 

_Cette intégration est maintenue par Apteligent._

## À propos de l'intégration

L'intégration de Braze et Apteligent fournit des rapports détaillés sur les pannes iOS, ce qui vous permet d'enregistrer des données critiques dans votre solution Braze existante, ainsi que de segmenter, comprendre et interagir avec les utilisateurs qui ont connu des pannes d'applications.

## Conditions préalables 

| Condition | Description |
|---|---|
| compte TestDrive | Un compte TestDrive est nécessaire pour bénéficier de ce partenariat. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert warning %}
Cette intégration n'est actuellement prise en charge que sur iOS.
{% endalert %}

## Intégration {#apteligent-ios-integration}

### Étape 1 : Inscrire un observateur

Tout d'abord, vous devez enregistrer un observateur. Assurez-vous que cela est fait avant d'initialiser Apteligent.

```objc
[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(crashDidOccur:)
                                             name:@"CRCrashNotification"
                                           object:nil];
```

### Étape 2 : Enregistrer une analyse personnalisée des incidents

Le SDK Apteligent déclenche une notification lorsque l'utilisateur charge l'application après un incident. La notification contiendra le nom, la raison et la date de l'incident.

Après réception de la notification, enregistrez un événement d’incident personnalisé et mettez à jour les attributs utilisateur à l'aide de l'analyse des rapports d'incidents d'Apteligent :

```objc
- (void)crashDidOccur:(NSNotification*)notification {
  NSDictionary *crashInfo = notification.userInfo;
  [[Appboy sharedInstance] logCustomEvent:@"ApteligentCrashEvent" withProperties:crashInfo];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashName" andStringValue:crashInfo[@"crashName"]];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashReason" andStringValue:crashInfo[@"crashReason"]];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashDate" andDateValue:crashInfo[@"crashDate"]];
}
```

Une fois terminé, vous serez en mesure d'exploiter la puissance de la segmentation de Braze et de l'analyse de l'engagement à l'aide des informations sur les accidents disponibles sur la plateforme Apteligent.

