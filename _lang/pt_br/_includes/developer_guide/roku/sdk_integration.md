## Integrando o Roku SDK

### Etapa 1: Adicionar arquivos

Os arquivos do SDK da Braze podem ser encontrados no diretório `sdk_files` no repositório [Braze Roku SDK](https://github.com/braze-inc/braze-roku-sdk).

1. Adicione `BrazeSDK.brs` ao seu app no diretório `source`.
2. Adicione `BrazeTask.brs` e `BrazeTask.xml` ao seu app no diretório `components`.

### Etapa 2: Adicionar referências

Adicione uma referência a `BrazeSDK.brs` em sua cena principal usando o seguinte elemento `script`:

```
<script type="text/brightscript" uri="pkg:/source/BrazeSDK.brs"/>
```

### Etapa 3: Configurar

Dentro de `main.brs`, defina a configuração da Braze no nó global:

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

Você pode encontrar seu [endpoint de SDK]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) e chave de API no dashboard da Braze.

### Etapa 4: Inicializar Braze

Inicialize a instância Braze:

```brightscript
m.BrazeTask = createObject("roSGNode", "BrazeTask")
m.Braze = getBrazeInstance(m.BrazeTask)
```

## Configurações opcionais

### Registro

Para depurar sua integração com a Braze, você pode visualizar o console de depuração do Roku para logs da Braze. Consulte [Depuração de código](https://developer.roku.com/docs/developer-program/debugging/debugging-channels.md) dos desenvolvedores do Roku para saber mais.
