{% multi_lang_include developer_guide/prerequisites/react_native.md %} Você também deve [configurar notificações por push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=react%20native).

## Personalização de push no React Native

O SDK Braze React Native não expõe a personalização de notificações por push (botões de ação, categorias, fábricas de notificações personalizadas) através de sua API JavaScript. Esses recursos requerem configuração nativa em seus projetos iOS e Android.

A tabela a seguir mostra quais recursos requerem configuração nativa:

| Recurso | iOS | Android |
| --- | --- | --- |
| Botões de ação | Configurar em Swift/Objective-C nativo | Configurar em Java/Kotlin nativo |
| Categorias de push | Configurar em Swift/Objective-C nativo | Configurar em Java/Kotlin nativo |
| Fábrica de notificações personalizada | N/D | Configurar em Java/Kotlin nativo |
| Personalização de badge | Configurar em Swift/Objective-C nativo | N/D |
| Sons personalizados | Configurar em Swift/Objective-C nativo | Configurar em Java/Kotlin nativo |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Personalização do iOS

Para adicionar botões de ação por push, categorias, badges ou sons personalizados no iOS, implemente a configuração nativa em seu `AppDelegate` (Swift ou Objective-C). Veja [Personalizar notificações por push – Swift]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift) para instruções passo a passo.

### Personalização do Android

Para adicionar botões de ação por push, categorias ou uma fábrica de notificações personalizada no Android, implemente a configuração nativa em seu projeto Android. Veja [Personalizar notificações por push – Android]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android) para instruções passo a passo.
