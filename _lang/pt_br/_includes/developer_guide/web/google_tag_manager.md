## Sobre o Google Tag Manager para Web {#google-tag-manager}

O Google Tag Manager (GTM) permite que você adicione, remova e edite tags no seu site remotamente, sem precisar de uma liberação de código de produção ou recursos de engenharia. A Braze oferece os seguintes modelos para o Web SDK:

|Tipo de Tag|Caso de uso|
|--------|--------|
| Tag de inicialização | Esta tag permite que você [integre o Web Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration/?tab=google%20tag%20manager&sdktab=web) sem precisar modificar o código do seu site.|
| Tag de ação | Esta tag permite que você [crie Cartões de Conteúdo]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_using-google-tag-manager), [defina atributos do usuário]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?tab=google%20tag%20manager&sdktab=web) e [gerencie a coleta de dados]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?tab=google%20tag%20manager&sdktab=web).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Política de Consentimento do Usuário da UE do Google

{% alert important %}
O Google está atualizando sua [Política de Consentimento do Usuário da UE](https://www.google.com/about/company/user-consent-policy/) em resposta às mudanças na [Lei dos Mercados Digitais (DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html), que está em vigor a partir de 6 de março de 2024. Essa nova alteração exige que os anunciantes divulguem determinadas informações aos seus usuários finais do EEE e do Reino Unido, bem como obtenham deles os consentimentos necessários. Consulte a documentação a seguir para saber mais.
{% endalert %}

Como parte da Política de consentimento do usuário da UE do Google, os seguintes atributos booleanos personalizados precisam ser registrados nos perfis de usuário:

- `$google_ad_user_data`
- `$google_ad_personalization`

Se estiver configurando-os por meio da integração com o GTM, os atributos personalizados exigirão a criação de uma tag HTML personalizada. A seguir, um exemplo de como registrar esses valores como tipos de dados booleanos (não como strings):

```js
<script>
window.braze.getUser().setCustomUserAttribute("$google_ad_personalization", true);
</script>
```

Para saber mais, consulte [Sincronização do público do Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/).
