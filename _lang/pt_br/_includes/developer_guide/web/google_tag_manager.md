## Sobre o Google Tag Manager para Web {#google-tag-manager}

O Google Tag Manager (GTM) permite que você adicione, remova e edite tags remotamente em seu site sem precisar de uma liberação de código de produção ou recursos de engenharia. A Braze oferece os seguintes modelos para o Web SDK:

|Tipo de tag|Caso de uso|
|--------|--------|
| Tag de inicialização | Essa tag permite que você [integre o Web Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration/?tab=google%20tag%20manager&sdktab=web) sem precisar modificar o código do seu site.|
| Tag de ação | Essa tag permite que você [crie Cartões de conteúdo]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_using-google-tag-manager), [defina atributos do usuário]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?tab=google%20tag%20manager&sdktab=web) e [gerencie a coleta de dados]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?tab=google%20tag%20manager&sdktab=web).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Registrando eventos personalizados com o GTM

Você pode registrar eventos personalizados usando uma tag **Custom HTML** no GTM. Essa abordagem usa a [camada de dados](https://developers.google.com/tag-platform/tag-manager/datalayer) do GTM para passar dados de eventos do seu site para uma tag do GTM que chama o Web SDK da Braze.

### Etapa 1: Envie o evento para a camada de dados

No código do seu site, envie um evento para a camada de dados sempre que quiser disparar o evento personalizado. Por exemplo, para registrar um evento personalizado quando um botão é clicado:

```html
<button onclick="dataLayer.push({'event': 'my_custom_event'});">Track Event</button>
```

### Etapa 2: Crie um gatilho no GTM

1. No seu contêiner do GTM, acesse **Triggers** e crie um novo gatilho.
2. Defina o **Trigger Type** como **Custom Event**.
3. Defina o **Event Name** com o mesmo valor que você enviou para a camada de dados (por exemplo, `my_custom_event`).
4. Escolha quando o gatilho deve ser disparado (por exemplo, **All Custom Events**).

### Etapa 3: Crie uma tag Custom HTML

1. No GTM, acesse **Tags** e crie uma nova tag.
2. Defina o **Tag Type** como **Custom HTML**.
3. No campo HTML, adicione o seguinte:

    ```html
    <script>
    window.braze.logCustomEvent("my_custom_event");
    </script>
    ```

4. Em **Triggering**, selecione o gatilho que você criou na etapa 2.
5. Salve e publique seu contêiner.

Para incluir propriedades do evento, passe-as como segundo argumento:

```html
<script>
window.braze.logCustomEvent("my_custom_event", {"property_key": "property_value"});
</script>
```

## Política de Consentimento do Usuário da Google na UE

{% alert important %}
O Google está atualizando sua [Política de Consentimento do Usuário da UE](https://www.google.com/about/company/user-consent-policy/) em resposta às mudanças na [Lei dos Mercados Digitais (DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html), que está em vigor desde 6 de março de 2024. Essa nova alteração exige que os anunciantes divulguem determinadas informações aos seus usuários finais do EEE e do Reino Unido, bem como obtenham deles os consentimentos necessários. Consulte a documentação a seguir para saber mais.
{% endalert %}

Como parte da Política de Consentimento do Usuário da UE do Google, os seguintes atributos personalizados booleanos precisam ser registrados nos perfis de usuário:

- `$google_ad_user_data`
- `$google_ad_personalization`

Se estiver configurando-os por meio da integração com o GTM, os atributos personalizados exigirão a criação de uma tag HTML personalizada. A seguir, um exemplo de como registrar esses valores como tipos de dados booleanos (não como strings):

```js
<script>
window.braze.getUser().setCustomUserAttribute("$google_ad_personalization", true);
</script>
```

Para saber mais, consulte [Audience Sync to Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/).