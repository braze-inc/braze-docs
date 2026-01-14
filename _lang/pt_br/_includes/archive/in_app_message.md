### Mensagens no app do slideup

[`Slideup`]{% if include.platform == "iOS" %}[in_app_message_1]{% elsif include.platform == "Android" %}[in_app_message_2]{% endif %} mensagens in-app são assim chamadas porque "deslizam para cima" ou "deslizam para baixo" a partir do topo ou da parte inferior da tela.  Eles cobrem uma pequena parte da tela e fornecem um recurso de envio de mensagens eficaz e não intrusivo.

![Exemplo de Slideup]({% image_buster /assets/img_archive/In-App_Slideup.png %})

### Mensagens modais no app

[`Modal`]{% if include.platform == "iOS" %}[in_app_message_3]{% elsif include.platform == "Android" %}[in_app_message_4]{% endif %} mensagens no app aparecem no centro da tela e são emolduradas por um painel translúcido. Útil para envios de mensagens mais críticos, eles podem ser equipados com até dois botões de ação de clique e botões com análise de dados habilitada.

![Exemplo de Modal]({% image_buster /assets/img_archive/In-App_Modal.png %})

### Mensagens completas no aplicativo

[`Full`]{% if include.platform == "iOS" %}[in_app_message_5]{% elsif include.platform == "Android" %}[in_app_message_6]{% endif %} mensagens no app são úteis para maximizar o conteúdo e o impacto da sua comunicação com o usuário.  A metade superior de uma mensagem no app `full` contém uma imagem e a metade inferior exibe texto, bem como até dois botões de ação de clique e análise de dados habilitados.

![Exemplo Completo]({% image_buster /assets/img_archive/In-App_Full.png %})

### mensagens completas no aplicativo HTML

[`HTML Full`]{% if include.platform == "iOS" %}[in_app_message_7]{% elsif include.platform == "Android" %}[in_app_message_8]{% endif %} mensagens no app são úteis para criar conteúdo de usuário totalmente personalizado. O conteúdo completo da mensagem no app definido pelo usuário é exibido em um {% if include.platform == "iOS" %}`WKWebView`{% elsif include.platform == "Android" %}`WebView`{% endif %} e pode opcionalmente conter outros conteúdos ricos, como imagens e fontes, permitindo total controle sobre a aparência e funcionalidade da mensagem.

 {% if include.platform == "iOS" %}
O exemplo a seguir mostra uma mensagem no app paginada em HTML Full:

![Exemplo HTML5]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

 {% elsif include.platform == "Android" %}O seguinte exemplo mostra uma mensagem no app HTML Full de pesquisa criada pelo SoundCloud.

![Exemplo HTML5]({% image_buster /assets/img_archive/HTML5.gif %})
{% endif %}

O conteúdo completo da mensagem no app é exibido em um WKWebView e pode opcionalmente conter outros conteúdos ricos, como imagens e fontes, permitindo total controle sobre a aparência e funcionalidade da mensagem. **Por favor, observe que atualmente a Braze não é compatível com a exibição de mensagens HTML personalizadas em aplicativos dentro de um iFrame nas plataformas iOS e Android.**

## Envio de mensagens no app

### Mensagens no app (disparadas)

A documentação a seguir refere-se ao produto Braze `In-App Messaging`, também conhecido como "mensagens in-app acionadas", que são destacadas abaixo no menu suspenso "Criar Campanha":

![Criador de Mensagens In-App]({% image_buster /assets/img_archive/trigger-iam-composer.png %})

Você também pode consultar a documentação para nosso produto obsoleto [`Original In-App Messaging`]({{ site.baseurl }}/user_guide/construção_de_mensagens_por_channel/in-app_messages/create/#original-in-app-messages) .

#### Tipos de disparo

Nosso produto de mensagem no app permite que você dispare a exibição de mensagens no app como resultado de vários tipos de eventos diferentes: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, `Push Click`.  Além disso, os disparos `Specific Purchase` e `Custom Event` contêm filtros de propriedade robustos.

{% alert note %}
As mensagens no app disparadas só funcionam com eventos personalizados registrados por meio do SDK da Braze. As mensagens no app não podem ser disparadas por meio da API ou por eventos da API (como eventos de compra). Se você estiver trabalhando com Android, veja como [registrar eventos personalizados no Android]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/#tracking-custom-events). Se você estiver trabalhando com iOS, veja como [registrar eventos personalizados no iOS]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/#tracking-custom-events).
{% endalert %}

#### Semântica de entrega

Todas as mensagens no app para as quais um usuário é elegível são entregues ao dispositivo do usuário no início da sessão. Para saber mais sobre a semântica de início de sessão do SDK, consulte nossa [documentação do ciclo de vida da sessão]{% if include.platform == "iOS" %}[in_app_message_15a]{% elsif include.platform == "Android" %}[in_app_message_15b]{% endif %}. Na entrega, o SDK pré-carregará ativos para que estejam disponíveis imediatamente no momento de disparar, minimizando a latência de exibição.

Quando um evento de gatilho tiver mais de uma mensagem no app elegível associada a ele, só será entregue a mensagem no app com a prioridade mais alta.

Para mensagens no aplicativo que são exibidas imediatamente na entrega (como início de sessão, clique em push), pode haver alguma latência devido a ativos que não estão sendo pré-carregados.

#### Intervalo de tempo mínimo entre disparos

Por padrão, limitamos a frequência das mensagens no app para uma vez a cada 30 segundos para uma experiência do usuário de qualidade.

{% if include.platform == "iOS" %}Você pode substituir este valor através do `ABKMinimumTriggerTimeIntervalKey` dentro do parâmetro `appboyOptions` passado para `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Defina `ABKMinimumTriggerTimeIntervalKey` como o valor inteiro que deseja como tempo mínimo em segundos entre mensagens no app:

```objc
// Sets the minimum trigger time interval to 5 seconds
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKMinimumTriggerTimeIntervalKey : @(5) }];
```

{% elsif include.platform == "Android" %}
Para substituir este valor, defina `com_appboy_trigger_action_minimum_time_interval_seconds` em seu `braze.xml`.

```xml
  <integer name="com_appboy_trigger_action_minimum_time_interval_seconds">5</integer>
```
{% endif %}

[in_app_message_1]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_slideup.html
[in_app_message_2]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-slideup/index.html
[in_app_message_3]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_modal.html
[in_app_message_4]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-modal/index.html
[in_app_message_5]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_full.html
[in_app_message_6]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-full/index.html
[in_app_message_7]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_h_t_m_l_full.html
[in_app_message_8]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html-full/index.html
[in_app_message_15a]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/tracking_sessions/#session-lifecycle
[in_app_message_15b]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/#session-lifecycle

