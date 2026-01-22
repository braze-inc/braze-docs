# Configuration du serveur MCP de Braze

> Apprenez à configurer le serveur MCP de Braze, afin de pouvoir interagir avec vos données Braze en langage naturel à l'aide d'outils tels que Claude et Cursor. Pour des informations plus générales, voir [Serveur Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Conditions préalables

Avant de commencer, vous avez besoin des éléments suivants :

| Prérequis | Description |
|--------------|-------------|
| Clé API de Braze | Une clé API de Braze avec les autorisations requises. Vous créerez une nouvelle clé lors de la [configuration de votre serveur Braze MCP](#create-api-key). |
| MCP Client | Actuellement, seuls [Claude](https://claude.ai/) et [Cursor](https://cursor.com/) sont officiellement pris en charge. Vous devez disposer d'un compte pour l'un de ces clients afin d'utiliser le serveur MCP de Braze. |
| Terminal | Une application de terminal vous permettant d'exécuter des commandes et d'installer des outils. Utilisez votre application de terminal préférée ou celle qui est préinstallée sur votre ordinateur. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Configuration du serveur MCP de Braze

### Étape 1 : Installer `uv`

Tout d'abord, installez `uv`- un [outil en ligne de commande d'Astral](https://docs.astral.sh/uv/getting-started/installation/) pour la gestion des dépendances et des paquets Python.

{% tabs local %}
{% tab MacOS et Linux %}
Ouvrez votre application de terminal, collez la commande suivante, puis appuyez sur <kbd>Entrée.</kbd>

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Le résultat sera similaire à ce qui suit :

```bash
$ curl -LsSf https://astral.sh/uv/install.sh | sh

downloading uv 0.8.9 aarch64-apple-darwin
no checksums to verify
installing to /Users/Isaiah.Robinson/.local/bin
  uv
  uvx
everything's installed!
```
{% endtab %}

{% tab Fenêtres %}
 Ouvrez Windows PowerShell, collez la commande suivante, puis appuyez sur <kbd>Entrée.</kbd>

```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

Le résultat sera similaire à ce qui suit :

```powershell
PS C:\Users\YourUser> irm https://astral.sh/uv/install.ps1 | iex

Downloading uv 0.8.9 (x86_64-pc-windows-msvc)
no checksums to verify
installing to C:\Users\YourUser\.local\bin
  uv.exe
  uvx.exe
everything's installed!
```
{% endtab %}
{% endtabs %}

### Étape 2 : Créer une clé API {#create-api-key}

Le serveur MCP de Braze prend en charge 38 endpoints en lecture seule qui ne renvoient pas les données des profils utilisateurs de Braze. Allez dans **Paramètres** > **API et identifiants** > **Clés API** et créez une nouvelle clé avec certaines ou toutes les autorisations suivantes.

{% details Liste des autorisations en lecture seule, non PII %}
#### Campagnes

| Endpoint | Autorisation requise |
|----------|---------------------|
| [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | `campaigns.data_series` |
| [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | `campaigns.details` |
| [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) | `campaigns.list` |
| [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | `sends.data_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Canvas

| Endpoint | Autorisation requise |
|----------|---------------------|
| [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | `canvas.data_series` |
| [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) | `canvas.data_summary` |
| [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) | `canvas.details` |
| [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | `canvas.list` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Catalogues

| Endpoint | Autorisation requise |
|----------|---------------------|
| [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | `catalogs.get` |
| [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | `catalogs.get_items` |
| [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | `catalogs.get_item` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Ingestion de données cloud

| Endpoint | Autorisation requise |
|----------|---------------------|
| [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list) | `cdi.integration_list` |
| [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status) | `cdi.integration_job_status` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Blocs de contenu

| Endpoint | Autorisation requise |
|----------|---------------------|
| [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | `content_blocks.list` |
| [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | `content_blocks.info` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Attributs personnalisés

| Endpoint | Autorisation requise |
|----------|---------------------|
| [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) | `custom_attributes.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Événements

| Endpoint | Autorisation requise |
|----------|---------------------|
| [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | `events.list` |
| [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) | `events.data_series` |
| [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) | `events.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Indicateurs clé de performance

| Endpoint | Autorisation requise |
|----------|---------------------|
| [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | `kpi.new_users.data_series` |
| [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) | `kpi.dau.data_series` |
| [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) | `kpi.mau.data_series` |
| [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) | `kpi.uninstalls.data_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Messages

| Endpoint | Autorisation requise |
|----------|---------------------|
| [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled) | `messages.schedule_broadcasts` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Centre de préférences

| Endpoint | Autorisation requise |
|----------|---------------------|
| [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center) | `preference_center.list` |
| [`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | `preference_center.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Achats

| Endpoint | Autorisation requise |
|----------|---------------------|
| [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | `purchases.product_list` |
| [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) | `purchases.revenue_series` |
| [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) | `purchases.quantity_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Segments

| Endpoint | Autorisation requise |
|----------|---------------------|
| [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | `segments.list` |
| [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | `segments.data_series` |
| [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) | `segments.details` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Envois

| Endpoint | Autorisation requise |
|----------|---------------------|
| [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | `sends.data_series` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

#### Sessions

| Endpoint | Autorisation requise |
|----------|---------------------|
| [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) | `sessions.data_series` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Clés d'authentification SDK

| Endpoint | Autorisation requise |
|----------|---------------------|
| [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys) | `sdk_authentication.keys` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Abonnement

| Endpoint | Autorisation requise |
|----------|---------------------|
| [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) | `subscription.status.get` |
| [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) | `subscription.groups.get` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Modèles

| Endpoint | Autorisation requise |
|----------|---------------------|
| [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | `templates.email.list` |
| [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information) | `templates.email.info` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% enddetails %}

{% alert warning %}
Ne réutilisez pas une clé API existante - créez-en une spécifiquement pour votre client MCP. En outre, n'attribuez que des autorisations en lecture seule, non PII, car les agents peuvent essayer d'écrire ou de supprimer des données dans Braze.
{% endalert %}

### Étape 3 : Obtenez votre identifiant et votre endpoint

Lorsque vous configurez votre client MCP, vous avez besoin de l'identifiant de votre clé API et de l'endpoint REST de votre espace de travail. Pour obtenir ces détails, retournez à la page **Clés API** dans le tableau de bord. Gardez cette page ouverte pour pouvoir y faire référence à l'[étape suivante.](#configure-client)

![Les "clés API" dans Braze montrent une clé API nouvellement créée et l'endpoint REST de l'utilisateur.]({% image_buster /assets/img/mcp_server/get_indentifer_and_endpoint.png %}){: style="max-width:85%;"}

### Étape 4 : Configurez votre client MCP {#configure-client}

Configurez votre client MCP à l'aide de notre fichier de configuration fourni au préalable.

{% tabs %}
{% tab Claude %}
Dans [Claude Desktop](https://claude.ai/download), allez dans **Paramètres** > **Développeur** > **Modifier la configuration**, puis ajoutez l'extrait de code suivant :

```json
{
  "mcpServers": {
    "braze": {
      "command": "uvx",
      "args": ["--native-tls", "braze-mcp-server@latest"],
      "env": {
        "BRAZE_API_KEY": "key-identifier",
        "BRAZE_BASE_URL": "rest-endpoint"
      }
    }
  }
}
```

Remplacez `key-identifier` et `rest-endpoint` par les valeurs correspondantes de la page des **clés API** dans Braze. Votre configuration devrait ressembler à ce qui suit :

```json
{
  "mcpServers": {
    "braze": {
      "command": "uvx",
      "args": ["--native-tls", "braze-mcp-server@latest"],
      "env": {
        "BRAZE_API_KEY": "2e8b-3c6c-d12e-bd75-4f0e2a8e5c71",
        "BRAZE_BASE_URL": "https://torchie.braze.com"
      }
    }
  }
}
```

Lorsque vous avez terminé, enregistrez la configuration et redémarrez Claude Desktop.
{% endtab %}

{% tab Curseur %}
Dans [Cursor](https://cursor.com/), allez dans **Paramètres** > **Outils et intégrations** > **Outils MCP** > **Ajouter un MCP personnalisé**, puis ajoutez l'extrait de code suivant :

```json
{
  "mcpServers": {
    "braze": {
      "command": "uvx",
      "args": ["--native-tls", "braze-mcp-server@latest"],
      "env": {
        "BRAZE_API_KEY": "your-braze-api-key",
        "BRAZE_BASE_URL": "your-braze-endpoint-url"
      }
    }
  }
}
```

Remplacez `key-identifier` et `rest-endpoint` par les valeurs correspondantes de la page des **clés API** dans Braze. Votre configuration devrait ressembler à ce qui suit :

```json
{
  "mcpServers": {
    "braze": {
      "command": "uvx",
      "args": ["--native-tls", "braze-mcp-server@latest"],
      "env": {
        "BRAZE_API_KEY": "2e8b-3c6c-d12e-bd75-4f0e2a8e5c71",
        "BRAZE_BASE_URL": "https://torchie.braze.com"
      }
    }
  }
}
```

Lorsque vous avez terminé, enregistrez la configuration et redémarrez Cursor.
{% endtab %}
{% endtabs %}

### Étape 5 : Envoyer une invite de test

Maintenant que vous avez configuré le serveur MCP de Braze, essayez d'envoyer une invite de test à votre client MCP. Pour d'autres exemples et bonnes pratiques, consultez [Using the Braze MCP server]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}.

{% tabs %}
{% tab Claude %}
![La question "Quelles sont les fonctions de Braze disponibles ?" est posée à Claude, qui y répond.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Curseur %}
![La question "Quelles sont les fonctions de Braze disponibles ?" est posée et trouve une réponse dans Cursor.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

## Résolution des problèmes

### Erreurs de terminal

#### `uvx` commande non trouvée

Si vous recevez un message d'erreur indiquant que la commande `uvx` n'a pas été trouvée, réinstallez `uv` et redémarrez votre terminal.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### `spawn uvx ENOENT` erreur

Si vous recevez une erreur `spawn uvx ENOENT`, il se peut que vous deviez mettre à jour le chemin d'accès dans le fichier de configuration de votre client. Tout d'abord, ouvrez votre terminal et exécutez la commande suivante :

```bash
which uvx
```

La commande doit renvoyer un message similaire au suivant :

```bash
/Users/alex-lee/.local/bin/uvx
```

Copiez le message dans votre presse-papiers et ouvrez le [fichier de configuration de votre client](#configure-client). Remplacez `"command": "uvx"` par le chemin que vous avez copié, puis redémarrez votre client. Par exemple :

```json
"command": "/Users/alex-lee/.local/bin/uvx"
```

#### L'installation du paquet échoue

Si l'installation de votre paquet échoue, essayez d'installer une version spécifique de Python à la place.

```bash
uvx --python 3.12 braze-mcp-server@latest
```

### Configuration du client

#### Le client MCP ne trouve pas le serveur Braze

1. Vérifiez que la syntaxe de la configuration de votre client MCP est correcte.
2. Redémarrez votre client MCP après les changements de configuration.
3. Vérifiez que `uvx` se trouve dans votre système `PATH`.

#### Erreurs d'authentification

1. Vérifiez que votre `BRAZE_API_KEY` est correct et actif.
2. Veillez à ce que votre site `BRAZE_BASE_URL` corresponde à votre instance Braze.
3. Vérifiez que votre clé API dispose des [autorisations nécessaires](#create-api-key).

#### Délais de connexion ou erreurs de réseau

1. Vérifiez que votre `BRAZE_BASE_URL` est correct pour votre instance.
2. Vérifiez votre connexion réseau et les paramètres de votre pare-feu.
3. Assurez-vous d'utiliser HTTPS dans votre URL de base.

{% multi_lang_include mcp_server/legal_disclaimer.md %}
