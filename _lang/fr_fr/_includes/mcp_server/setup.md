# Configuration du serveur Braze MCP

> Découvrez comment configurer le serveur Braze MCP afin de pouvoir interagir avec vos données Braze en utilisant un langage naturel grâce à des outils tels que Claude et Cursor. Pour obtenir des informations générales, veuillez consulter [le serveur Braze MCP]{% if include.section == "user" %}.{{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/mcp_server/){% endif %}

{% multi_lang_include mcp_server/beta_alert.md %}

## Conditions préalables

Avant de commencer, vous avez besoin des éléments suivants :

| Prérequis | Description |
|--------------|-------------|
| Clé API Braze | Une clé API Braze avec les autorisations requises. Vous créerez une nouvelle clé lors de la[ configuration de votre serveur Braze MCP](#create-api-key). |
| client MCP | [Claude](https://claude.ai/), [Cursor](https://cursor.com/) et [Google Gemini CLI](https://docs.cloud.google.com/gemini/docs/codeassist/gemini-cli) sont officiellement pris en charge. Il est nécessaire de disposer d'un compte auprès de l'un de ces clients pour pouvoir utiliser le serveur Braze MCP. |
| Terminal | Une application terminale vous permettant d'exécuter des commandes et d'installer des outils. Veuillez utiliser votre application de terminal préférée ou celle qui est préinstallée sur votre ordinateur. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Configuration du serveur Braze MCP

### Étape 1 : Veuillez installer `uv`

Tout d'abord, veuillez installer `uv`—un [outil en ligne de commande développé par Astral](https://docs.astral.sh/uv/getting-started/installation/) pour la gestion des dépendances et la manipulation des paquets Python.

{% tabs local %}
{% tab MacOS and Linux %}
Veuillez ouvrir votre application de terminal, copier-coller la commande suivante, puis appuyer sur <kbd>Entrée</kbd>.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Le résultat est similaire à ce qui suit :

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

{% tab Windows %}
 Veuillez ouvrir Windows PowerShell, insérer la commande suivante, puis appuyer sur <kbd>Entrée</kbd>.

```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

Le résultat est similaire à ce qui suit :

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

Le serveur MCP Braze prend en charge 38 endpoints en lecture seule qui ne renvoient pas les données des profils utilisateurs Braze. Veuillez vous rendre dans **Paramètres** > **API et identifiants** > **Clés API** et créer une nouvelle clé avec certaines ou toutes les autorisations suivantes.

{% details List of read-only, non-PII permissions %}
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
Veuillez ne pas réutiliser une clé API existante ; veuillez en créer une spécialement pour votre client MCP. De plus, veuillez n'attribuer que des autorisations en lecture seule, non liées aux informations personnelles identifiables, car les agents pourraient tenter d'écrire ou de supprimer des données dans Braze.
{% endalert %}

### Étape 3 : Obtenez votre identifiant et votre endpoint

Lorsque vous configurez votre client MCP, vous aurez besoin de l'identifiant de votre clé API et de l'endpoint REST de votre espace de travail. Pour obtenir ces informations, veuillez retourner à la page **Clés API** dans le tableau de bord. Veuillez garder cette page ouverte afin de pouvoir vous y référer lors de [l'étape suivante](#configure-client).

![Les « clés API » dans Braze affichent une clé API nouvellement créée et l'endpoint REST de l'utilisateur.]({% image_buster /assets/img/mcp_server/get_indentifer_and_endpoint.png %}){: style="max-width:85%;"}

### Étape 4 : Veuillez configurer votre client MCP. {#configure-client}

Veuillez configurer votre client MCP à l'aide du fichier de configuration fourni.

{% tabs %}
{% tab Claude %}
Veuillez configurer votre serveur MCP en utilisant le répertoire du connecteur [Claude Desktop](https://claude.ai/download). 

1. Dans Claude Desktop, veuillez vous rendre dans **Paramètres** > **Connecteurs** > **Parcourir les connecteurs** > **Extensions de bureau** > **Serveur Braze MCP** > **Installer**.
2. Veuillez saisir votre clé API et votre URL de base.
3. Veuillez enregistrer la configuration et redémarrer Claude Desktop.

{% endtab %}

{% tab Cursor %}
Dans [Cursor](https://cursor.com/), veuillez vous rendre dans **Paramètres** > **Outils et intégrations** > **Outils MCP** > **Ajouter un MCP personnalisé**, puis ajoutez l'extrait de code suivant :

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

Veuillez remplacer`key-identifier`  et`rest-endpoint`  par les valeurs correspondantes figurant sur la page **Clés API** dans Braze. Votre configuration devrait être similaire à celle-ci :

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

Une fois que vous avez terminé, veuillez enregistrer la configuration et redémarrer Cursor.
{% endtab %}
{% tab Gemini CLI %}
Gemini CLI lit les paramètres utilisateur à partir de `~/.gemini/settings.json`. Si ce fichier n'existe pas, vous pouvez le créer en exécutant la commande suivante dans votre terminal :

```powershell
mkdir -p ~/.gemini
nano ~/.gemini/settings.json
```

Ensuite, veuillez remplacer`yourname`par la chaîne de caractères exacte précédant`@BZXXXXXXXX`dans votre invite de commande. Veuillez ensuite remplacer`key-identifier`et`rest-endpoint`par les valeurs correspondantes figurant sur la page **Clés API** dans Braze. 

Votre configuration devrait être similaire à celle-ci :

```json
{
  "mcpServers": {
    "braze": {
      "command": "/Users/yourname/.local/bin/uvx",
      "args": ["--native-tls", "braze-mcp-server@latest"],
      "env": {
        "BRAZE_API_KEY": "2e8b-3c6c-d12e-bd75-4f0e2a8e5c71",
        "BRAZE_BASE_URL": "https://torchie.braze.com"
      }
    }
  }
}
```

Une fois que vous avez terminé, veuillez enregistrer la configuration et redémarrer Gemini CLI. Ensuite, dans Gemini, exécutez les commandes suivantes pour vérifier que le serveur Braze MCP est répertorié et que les outils et le schéma sont disponibles :

```powershell
gemini
/mcp
/mcp desc
/mcp schema
```

Vous devriez voir le`braze`serveur répertorié avec les outils et le schéma disponibles à l'utilisation.

{% endtab %}
{% endtabs %}

### Étape 5 : Veuillez envoyer une invite de test.

Une fois le serveur Braze MCP configuré, veuillez essayer d'envoyer une invite de test à votre client MCP. Pour d'autres exemples et bonnes pratiques, veuillez consulter [Utilisation du serveur Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}){{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}.

{% tabs %}
{% tab Claude %}
![« Quelles sont les fonctions Braze à ma disposition ? » : question posée et réponse fournie dans Claude.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![« Quelles sont les fonctions Braze disponibles ? » : question posée et réponse fournie dans Cursor.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}

{% tab Gemini CLI %}
![Quelles sont les fonctions Braze disponibles pour moi ? Cette question est posée et traitée dans Gemini CLI.]({% image_buster /assets/img/mcp_server/gemini_cli/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

## Résolution des problèmes

### Erreurs de terminal

#### `uvx` commande introuvable

Si vous recevez une erreur indiquant que`uvx`la commande est introuvable, veuillez réinstaller`uv`et redémarrer votre terminal.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### `spawn uvx ENOENT` erreur

Si vous rencontrez des`spawn uvx ENOENT`erreurs, il peut être nécessaire de mettre à jour le chemin d'accès au fichier dans le fichier de configuration de votre client. Tout d'abord, veuillez ouvrir votre terminal et exécuter la commande suivante :

```bash
which uvx
```

La commande devrait renvoyer un message similaire à celui-ci :

```bash
/Users/alex-lee/.local/bin/uvx
```

Veuillez copier le message dans votre presse-papiers et ouvrir [le fichier de configuration de votre client](#configure-client). Veuillez remplacer`"command": "uvx"`par le chemin d'accès que vous avez copié, puis redémarrez votre client. Par exemple :

```json
"command": "/Users/alex-lee/.local/bin/uvx"
```

#### L'installation du paquet échoue

Si l'installation de votre paquet échoue, veuillez essayer d'installer une version spécifique de Python à la place.

```bash
uvx --python 3.12 braze-mcp-server@latest
```

### Configuration client

#### Le client MCP ne parvient pas à localiser le serveur Braze.

1. Veuillez vérifier que la syntaxe de configuration de votre client MCP est correcte.
2. Veuillez redémarrer votre client MCP après avoir modifié la configuration.
3. Veuillez vérifier que [nom du fichier`uvx`] est présent dans votre système`PATH`.

#### Erreurs d'authentification

1. Veuillez vérifier que votre`BRAZE_API_KEY`  est correct et actif.
2. Veuillez vous assurer que votre configuration`BRAZE_BASE_URL`correspond à votre instance Braze.
3. Veuillez vérifier que votre clé API dispose des [autorisations appropriées](#create-api-key).

#### Délais d'attente de connexion ou erreurs réseau

1. Veuillez vérifier que votre`BRAZE_BASE_URL`  est correct pour votre instance.
2. Veuillez vérifier votre connexion réseau et les paramètres de votre pare-feu.
3. Veuillez vous assurer que vous utilisez le protocole HTTPS dans votre URL de base.

{% multi_lang_include mcp_server/legal_disclaimer.md %}
