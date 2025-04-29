---
page_order: 1.3
nav_title: Débogage
article_title: Débogage du SDK de Braze 
description: "Apprenez à utiliser le débogueur du SDK de Braze, afin de pouvoir résoudre les problèmes de vos canaux alimentés par le SDK, sans avoir à activer manuellement la journalisation verbeuse dans votre application."
---

# Débogage du SDK de Braze

> Apprenez à utiliser le débogueur intégré au SDK de Braze, afin de pouvoir résoudre les problèmes de vos canaux alimentés par le SDK, sans avoir à activer la journalisation verbeuse dans votre application.

## Conditions préalables

Pour utiliser le débogueur Braze SDK, vous devez disposer des autorisations `View PII` et `View User Profiles PII Compliant`. En outre, votre SDK Braze doit être conforme ou pointer vers les versions minimales suivantes : 

{% sdk_min_versions swift:10.2.0 android:32.1.0 %}

## Débogage du SDK de Braze

{% alert tip %}
Pour activer le débogage du SDK Braze, vous pouvez [utiliser un paramètre d'URL]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#logging).
{% endalert %}

### Étape 1 : Fermez votre application

Avant de commencer votre session de débogage, fermez l'application qui pose problème. Vous pouvez relancer l'application au début de votre session.

### Étape 2 : Créer une session de débogage

Dans Braze, allez dans **Settings**, puis sous **Setup and Testing**, sélectionnez **SDK Debugger**.

![La section "Configuration et test" avec "SDK Debugger" en surbrillance.]({% image_buster /assets/img/sdk_debugger/select_sdk_debugger.png %})

Sélectionnez **Créer une session de débogage**.

![La page "SDK Debugger".]({% image_buster /assets/img/sdk_debugger/select_create_debugging_session.png %})

### Étape 3 : Sélectionnez un utilisateur

Recherchez un utilisateur à l'aide de son adresse e-mail, `external_id`, de son alias d'utilisateur ou de son jeton de poussée. Lorsque vous êtes prêt à démarrer votre session, sélectionnez **Sélectionner un utilisateur.**

![La page de débogage pour l'utilisateur sélectionné.]({% image_buster /assets/img/sdk_debugger/search_and_select_user.png %}){: style="max-width:85%;"}

### Étape 4 : Relancer l’application

Tout d'abord, lancez l'appli et confirmez que votre appareil est apparié. Si l'appariement est réussi, relancez votre application, ce qui permettra de s'assurer que les journaux d'initialisation de l'application sont entièrement capturés.

### Étape 5 : Complétez les étapes de reproduction

Après avoir relancé votre application, suivez les étapes pour reproduire l'erreur.

{% alert tip %}
Lorsque vous reproduisez l'erreur, veillez à suivre les étapes de la reproduction aussi fidèlement que possible, afin de créer des [enregistrements de qualité](#step-6-export-your-session-logs-optional).
{% endalert %}

### Étape 6 : Fin de la session

Lorsque vous avez terminé les étapes de reproduction, sélectionnez **Terminer la session** > **Fermer**.

![La session de débogage affiche le bouton "Fin de la session".]({% image_buster /assets/img/sdk_debugger/close_debugging_session.png %}){: style="max-width:85%;"}

{% alert note %}
La génération des journaux peut prendre quelques minutes en fonction de la durée de la session et de la connectivité du réseau.
{% endalert %}

### Étape 7 : Partager ou exporter votre session (facultatif)

Après votre session, vous pouvez exporter vos journaux de session sous forme de fichier CSV. En outre, d'autres personnes peuvent utiliser votre **ID de session** pour rechercher votre session de débogage, de sorte que vous n'avez pas besoin de leur envoyer directement vos journaux.

![La page de débogage avec "Exporter les journaux" et "Copier l'ID de la session" s'affiche après la session.]({% image_buster /assets/img/sdk_debugger/copy_id_and_export_logs.png %})
