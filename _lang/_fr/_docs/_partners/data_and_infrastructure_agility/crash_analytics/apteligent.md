---
nav_title: Apteligent
article_title: Apteligent
alias: /fr/partners/apteligent/
description: "Cet article décrit le partenariat entre Braze et Apteligent, une application mobile qui détaille les rapports de plantage, vous permettant d'enregistrer des données critiques dans votre solution Braze existante."
page_type: partenaire
search_tag: Partenaire
---

# Apteligent

> [Apteligent](https://kb.vmtestdrive.com/hc/en-us/articles/360001544114-Apteligent-by-VMware-Walkthrough) est une plate-forme mobile de performance d'applications fournissant des outils et des connaissances pour les développeurs et les gestionnaires de produits.

L'intégration de Braze et Apteligent fournit des rapports détaillés sur les plantages d'iOS, vous permettant d'enregistrer des données critiques dans votre solution Braze existante ainsi que dans votre segment, comprenez et engagez avec les utilisateurs qui ont connu des plantages d'applications.

## Pré-requis

| Exigences        | Libellé                                                                                                                                                     |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte TestDrive | Un [compte TestDrive](https://kb.vmtestdrive.com/hc/en-us/articles/360001372254-Getting-Started-with-TestDrive) est requis pour profiter de ce partenariat. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert warning %}
Cette intégration n'est actuellement prise en charge que sur iOS.
{% endalert %}

## Intégration {#apteligent-ios-integration}

### Étape 1 : Inscrire un observateur

Tout d'abord, vous devez enregistrer un observateur. Assurez-vous que cela est fait avant d'initialiser Apteligent.

```objc
[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(crashDidOccur:)
                                             name:@"CRCrashNotification"
                                           object:nil];
```

### Étape 2: Journal des analyses de plantage personnalisées

Le SDK Apteligent lancera une notification lorsque l'utilisateur chargera l'application après un crash. La notification contiendra le nom du plantage, la raison et la date d'occurrence.

Lors de la réception de la notification, enregistrer un événement de plantage personnalisé et mettre à jour les attributs de l'utilisateur avec l'analyse de rapport de plantage d'Apteligent :

```objc
- (void)crashDidOccur:(NSNotification*)notification {
  NSDictionary *crashInfo = notification.userInfo;
  [[Appboy sharedInstance] logCustomEvent:@"ApteligentCrashEvent" withProperties:crashInfo];
  [[Appboy sharedInstance]. ser setCustomAttributeWithKey:@"lastCrashName" andStringValue:crashInfo[@"crashName"]];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashReason" andStringValue:crashInfo[@"crashReason"]];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashDate" andDate:crashInfo[@"crashDate"]];
}
```

Une fois terminé, vous pourrez exploiter la puissance des analyses de segmentation et d'engagement de Braze en utilisant les informations de crash trouvées dans la plateforme Apteligent.