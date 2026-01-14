## Integration des Roku SDK

### Schritt 1: Dateien hinzufügen

Die Dateien des Braze SDK finden Sie im Verzeichnis `sdk_files` im [Braze Roku SDK Repository](https://github.com/braze-inc/braze-roku-sdk).

1. Fügen Sie `BrazeSDK.brs` zu Ihrer App im Verzeichnis `source` hinzu.
2. Fügen Sie `BrazeTask.brs` und `BrazeTask.xml` zu Ihrer App in das Verzeichnis `components` hinzu.

### Schritt 2: Referenzen hinzufügen

Fügen Sie einen Verweis auf `BrazeSDK.brs` in Ihre Hauptszene ein, indem Sie das folgende `script`-Element verwenden:

```
<script type="text/brightscript" uri="pkg:/source/BrazeSDK.brs"/>
```

### Schritt 3: Konfigurieren Sie

Legen Sie unter `main.brs` die Braze-Konfiguration auf dem globalen Knoten fest:

```brightscript
globalNode = screen.getGlobalNode()
config = {}
config_fields = BrazeConstants().BRAZE_CONFIG_FIELDS
config[config_fields.API_KEY] = {YOUR_API_KEY}
' example endpoint: "https://sdk.iad-01.braze.com/"
config[config_fields.ENDPOINT] = {YOUR_ENDPOINT}
config[config_fields.HEARTBEAT_FREQ_IN_SECONDS] = 5
globalNode.addFields({brazeConfig: config})
```

Den [SDK-Endpunkt]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) und den API-Schlüssel können Sie dem Braze-Dashboard entnehmen.

### Schritt 4: Braze initialisieren

Initialisieren Sie die Braze-Instanz:

```brightscript
m.BrazeTask = createObject("roSGNode", "BrazeTask")
m.Braze = getBrazeInstance(m.BrazeTask)
```

## Optionale Konfigurationen

### Protokollieren

Um Ihre Braze-Integration zu debuggen, können Sie die Roku Debug-Konsole für Braze-Protokolle anzeigen. Weitere Informationen finden Sie im Artikel [Debugging-Code](https://developer.roku.com/docs/developer-program/debugging/debugging-channels.md) von Roku Developers.
