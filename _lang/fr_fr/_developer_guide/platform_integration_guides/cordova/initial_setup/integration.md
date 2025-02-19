---
nav_title: Intégration
article_title: Intégration du SDK de Cordova Braze
page_order: 0
---

# Intégration du SDK de Cordova Braze

> Découvrez comment intégrer le SDK Braze Cordova dans votre application iOS ou Android. Une fois que vous avez terminé, vous pouvez [personnaliser davantage le SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_setup/customizations/).

## Intégration du SDK

### Étape 1 : Ajoutez le SDK à votre projet

Si vous utilisez Cordova 6 ou une version ultérieure, vous pouvez ajouter le SDK directement depuis GitHub. Vous pouvez également télécharger un ZIP du [référentiel GitHub](https://github.com/braze-inc/braze-cordova-sdk) et ajouter le SDK manuellement.

{% tabs local %}
{% tab géorepérage désactivé %}
Si vous ne prévoyez pas d'utiliser la collecte des localisations et les géorepérages, utilisez la branche `master` de GitHub.

```bash
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#master
```
{% endtab %}

{% tab géorepérage activé %}
Si vous prévoyez d'utiliser la collecte des localisations et les géorepérages, utilisez la `geofence-branch` de GitHub.

```bash
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#geofence-branch
```
{% endtab %}
{% endtabs %}

{% alert tip %}
Vous pouvez basculer entre `master` et `geofence-branch` à tout moment en répétant l'étape 1.
{% endalert %}

### Étape 2 : Configurez votre projet

Ensuite, ajoutez les préférences suivantes à l'élément `platform` dans le fichier `config.xml` de votre projet.

{% tabs %}
{% tab ios %}
```xml
<preference name="com.braze.ios_api_key" value="BRAZE_API_KEY" />
<preference name="com.braze.ios_api_endpoint" value="CUSTOM_API_ENDPOINT" />
```
{% endtab %}

{% tab android %}
```xml
<preference name="com.braze.android_api_key" value="BRAZE_API_KEY" />
<preference name="com.braze.android_api_endpoint" value="CUSTOM_API_ENDPOINT" />
```
{% endtab %}
{% endtabs %}

Remplacez les éléments suivants :

| Valeur                 | Description                                                                                                                      |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|
| `BRAZE_API_KEY`       | Votre [clé API REST de Braze]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys).              |
| `CUSTOM_API_ENDPOINT` | Un endpoint d'API personnalisé. Cet endpoint est utilisé pour acheminer les données de votre instance Braze vers le groupe d'applications adéquat dans votre tableau de bord Braze. |

L'élément `platform` de votre fichier `config.xml` devrait ressembler à ce qui suit :

{% tabs %}
{% tab ios %}
```xml
<platform name="ios">
    <preference name="com.braze.ios_api_key" value="BRAZE_API_KEY" />
    <preference name="com.braze.ios_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```
{% endtab %}

{% tab android %}
```xml
<platform name="android">
    <preference name="com.braze.android_api_key" value="BRAZE_API_KEY" />
    <preference name="com.braze.android_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```
{% endtab %}
{% endtabs %}

## Désactiver le suivi automatique des sessions (Android uniquement)

Par défaut, le plugin Android Cordova assure automatiquement le suivi des sessions. Pour désactiver le suivi automatique des sessions, ajoutez la préférence suivante à l'élément `platform` du fichier `config.xml` de votre projet :

```xml
<platform name="android">
    <preference name="com.braze.android_disable_auto_session_tracking" value="true" />
</platform>
```

Pour recommencer à suivre les sessions, appelez `BrazePlugin.startSessionTracking()`. Gardez à l'esprit que seules les sessions commencées après le prochain `Activity.onStart()` seront suivies.
