---
nav_title: Apteligent
article_title: Apteligent
alias: /partners/apteligent/
description: "Cet article de référence présente le partenariat entre Braze et Apteligent, une application mobile qui fournit des rapports d’incident, ce qui vous permet de consigner des données critiques dans votre solution Braze."
page_type: partner
search_tag: Partenaire

---

# Apteligent

> [Apteligent](https://kb.vmtestdrive.com/hc/en-us/articles/360001544114-Apteligent-by-VMware-Walkthrough) est une plateforme de performance des applications mobiles qui fournit des outils et des informations pour les développeurs et les gestionnaires de produits. 

L’intégration de Braze et Apteligent fournit des rapports détaillés sur les incidents iOS, ce qui vous permet de consigner les données critiques dans votre solution Braze, et de segmenter, comprendre et interagir avec les utilisateurs qui ont subi des blocages d’application.

## Conditions préalables 

| Condition | Description |
|---|---|
| Compte TestDrive | Un [Compte TestDrive](https://kb.vmtestdrive.com/hc/en-us/articles/360001372254-Getting-Started-with-TestDrive) est requis pour profiter de ce partenariat. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert warning %}
Actuellement, cette intégration est uniquement prise en charge sur iOS.
{% endalert %}

## Intégration {#apteligent-ios-integration}

### Étape 1 : Enregistrer un observateur

Tout d’abord, vous devez enregistrer un observateur. Assurez-vous que cela est fait avant d’initialiser Apteligent.

```objc
[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(crashDidOccur:)
                                             name:@"CRCrashNotification"
                                           object:nil];
```

### Étape 2 : Enregistrer les analyses d’incident personnalisées

Le SDK de Apteligent envoie une notification lorsque l’utilisateur charge l’application après qu’un incident se soit produit. La notification contiendra le nom de l’incident, le motif et la date à laquelle il est survenu.

Après avoir reçu la notification, enregistrez un événement d’incident personnalisé et mettez à jour les attributs utilisateur avec l’analyse des rapports d’incident d’Apteligent :

```objc
- (void)crashDidOccur:(NSNotification*)notification {
  NSDictionary *crashInfo = notification.userInfo;
  [[Appboy sharedInstance] logCustomEvent:@"ApteligentCrashEvent" withProperties:crashInfo];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashName" andStringValue:crashInfo[@"crashName"]];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashReason" andStringValue:crashInfo[@"crashReason"]];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashDate" andDateValue:crashInfo[@"crashDate"]];
}
```

Une fois terminé, vous pourrez tirer parti des capacités de segmentation et d’analyse de l’engagement de Braze en utilisant les informations sur les incidents de la plateforme Apteligent.