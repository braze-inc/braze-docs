---
page_order: 1.3
nav_title: Débogage
article_title: Débogage du SDK de Braze 
description: "Découvrez comment utiliser le débogueur du SDK de Braze pour résoudre les problèmes liés à vos canaux alimentés par le SDK, sans avoir à activer manuellement la journalisation détaillée dans votre application."
---

# Débogage du SDK de Braze

> Découvrez comment utiliser le débogueur intégré au SDK de Braze pour résoudre les problèmes liés à vos canaux alimentés par le SDK, sans avoir à activer la journalisation détaillée dans votre application.

{% alert tip %}
Pour une analyse plus approfondie, vous pouvez également [activer la journalisation détaillée]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging) afin de capturer les sorties détaillées du SDK et [apprendre à lire les journaux détaillés]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs) pour des canaux spécifiques.
{% endalert %}

## Conditions préalables

Pour utiliser le débogueur du SDK de Braze, vous devez disposer des autorisations granulaires « Voir les données personnelles » et « Voir les profils utilisateurs (données personnelles masquées) » (ou de l'autorisation héritée « Voir les profils utilisateurs conformes aux données personnelles »). Pour télécharger les journaux de vos sessions de débogage, vous aurez également besoin de l'autorisation « Exporter les données utilisateur ». De plus, votre SDK Braze doit être conforme ou pointer vers les versions minimales suivantes : 

{% sdk_min_versions swift:10.2.0 android:32.1.0 %}

## Débogage du SDK de Braze

{% alert tip %}
Pour activer le débogage du SDK Web de Braze, vous pouvez [utiliser un paramètre d'URL]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#logging).
{% endalert %}

### Étape 1 : Fermez votre application

Avant de commencer votre session de débogage, fermez l'application qui pose problème. Vous pourrez la relancer au début de votre session.

### Étape 2 : Créez une session de débogage

Dans Braze, accédez à **Paramètres**, puis sous **Configuration et test**, sélectionnez **SDK Debugger**.

![La section « Configuration et test » avec « SDK Debugger » mis en évidence.]({% image_buster /assets/img/sdk_debugger/select_sdk_debugger.png %})

Sélectionnez **Créer une session de débogage**.

![La page « SDK Debugger ».]({% image_buster /assets/img/sdk_debugger/select_create_debugging_session.png %})

### Étape 3 : Sélectionnez un utilisateur

Recherchez un utilisateur à l'aide de son adresse e-mail, de son `external_id`, de son alias d'utilisateur ou de son jeton de notification push. Lorsque vous êtes prêt à démarrer votre session, sélectionnez **Sélectionner un utilisateur**.

![La page de débogage pour l'utilisateur sélectionné.]({% image_buster /assets/img/sdk_debugger/search_and_select_user.png %}){: style="max-width:85%;"}

### Étape 4 : Relancez l'application

Commencez par lancer l'application et vérifiez que votre appareil est bien apparié. Si l'appariement a réussi, relancez votre application — cela garantit que les journaux d'initialisation de l'application sont entièrement capturés.

### Étape 5 : Reproduisez les étapes

Après avoir relancé votre application, suivez les étapes pour reproduire l'erreur.

{% alert tip %}
Lorsque vous reproduisez l'erreur, veillez à suivre les étapes de reproduction aussi fidèlement que possible afin de générer des [journaux de qualité](#step-6-export-your-session-logs-optional).
{% endalert %}

### Étape 6 : Terminez votre session

Une fois les étapes de reproduction terminées, sélectionnez **Terminer la session** > **Fermer**.

![La session de débogage affichant le bouton « Terminer la session ».]({% image_buster /assets/img/sdk_debugger/close_debugging_session.png %}){: style="max-width:85%;"}

{% alert note %}
La génération des journaux peut prendre quelques minutes selon la durée de la session et la connectivité réseau.
{% endalert %}

### Étape 7 : Partagez ou exportez votre session (facultatif)

Après votre session, vous pouvez exporter vos journaux de session sous forme de fichier CSV. D'autres personnes peuvent également utiliser votre **ID de session** pour rechercher votre session de débogage, ce qui vous évite de leur envoyer directement vos journaux.

![La page de débogage avec « Exporter les journaux » et « Copier l'ID de session » affichés après la session.]({% image_buster /assets/img/sdk_debugger/copy_id_and_export_logs.png %})