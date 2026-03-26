{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Desabilitando o rastreamento de dados

Para desabilitar a coleta de dados, use o método `disableSDK`. Após chamar este método, o SDK do Braze para de enviar dados para os servidores do Braze.

```javascript
Braze.disableSDK();
```

## Retomando o rastreamento de dados

Para retomar a coleta de dados após desabilitá-la, use o método `enableSDK`.

```javascript
Braze.enableSDK();
```

## Limpando dados

Para excluir todos os dados do SDK do Braze armazenados localmente no dispositivo, use o método `wipeData`. Após chamar este método, o SDK é desabilitado e deve ser reabilitado com `enableSDK`.

```javascript
Braze.wipeData();
```

## Liberando dados

Para solicitar uma liberação imediata de quaisquer dados pendentes para os servidores do Braze, use `requestImmediateDataFlush`.

```javascript
Braze.requestImmediateDataFlush();
```

## Configurando o rastreamento de anúncios habilitado

Para informar ao Braze se o rastreamento de anúncios está habilitado para este dispositivo, use o método `setAdTrackingEnabled`. O SDK não coleta automaticamente esses dados.

```javascript
Braze.setAdTrackingEnabled(true, "GOOGLE_ADVERTISING_ID");
```

O segundo parâmetro é o ID de Publicidade do Google e é usado apenas no Android.

## Atualizando a lista de permissões da propriedade de rastreamento (apenas iOS)

Para atualizar a lista de tipos de dados declarados para rastreamento, use `updateTrackingPropertyAllowList`. Isso não tem efeito no Android.

```javascript
Braze.updateTrackingPropertyAllowList({
  adding: [Braze.TrackingProperty.EMAIL, Braze.TrackingProperty.FIRST_NAME],
  removing: [],
  addingCustomEvents: ["my_custom_event"],
  removingCustomEvents: [],
  addingCustomAttributes: ["my_custom_attribute"],
  removingCustomAttributes: []
});
```

Para saber mais, consulte [Manifesto de Privacidade]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/privacy_manifest/).
