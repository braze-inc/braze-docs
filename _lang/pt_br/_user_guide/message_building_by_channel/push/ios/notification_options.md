---
nav_title: "Opções de notificação"
article_title: Opções de notificação do iOS
page_order: 2
page_layout: reference
description: "Este artigo de referência aborda as opções de notificação do iOS, como alertas críticos, notificações silenciosas, notificações por push provisórias e muito mais."

platform: iOS
channel:
  - push

---

# Opções de notificação

> Com o lançamento do iOS 12 da Apple, o Braze oferece suporte a vários de seus recursos, incluindo [grupos de notificação](#notification-groups), [notificações silenciosas/autorização provisória](#provisional-push-authentication--quiet-notifications) e [alertas críticos](#critical-alerts).

## Grupos de notificação

Se quiser categorizar suas mensagens e agrupá-las na bandeja de notificações do usuário, poderá utilizar o recurso Notification Groups do iOS por meio do Braze.

Crie sua campanha push para iOS e, em seguida, vá para a guia **Settings (Configurações** ) e abra o menu suspenso **Notification group (Grupo de notificações** ).

![A guia "Settings" (Configurações) com um menu suspenso "Notification group" (Grupo de notificação) que selecionou um valor de "Coupons" (Cupons).]({% image_buster /assets/img_archive/notification_group_dropdown.png %}){: style="max-width:50%;" }

Selecione seus grupos de notificação no menu suspenso. Se as configurações do grupo de notificação não funcionarem corretamente ou se você selecionar **None (Nenhum** ) no menu suspenso, a mensagem será enviada automaticamente como de costume para todos os usuários definidos no espaço de trabalho.

Se você não tiver nenhum grupo de notificação listado aqui, poderá adicionar um usando o ID de thread do iOS. Você precisará de um ID de thread do iOS para cada grupo de notificação que quiser adicionar. Em seguida, adicione-o aos seus grupos de notificação clicando em **Gerenciar grupos de notificação** no menu suspenso e preenchendo os campos obrigatórios na janela **Gerenciar grupos de notificação por push do iOS** que aparece.

![Janela para gerenciar grupos de notificações por push do iOS.]({% image_buster /assets/img_archive/managenotgroups.png %}){: style="max-width:70%;" }

Crie sua campanha push para iOS e, em seguida, olhe para a parte superior do criador. Lá, você verá um menu suspenso chamado **Notification Groups (Grupos de notificação**).

### Argumentos resumidos

Além de agrupar as notificações por IDs de thread, a Apple permite que você edite os resumos que aparecem quando as notificações são agrupadas. Os usuários do Braze podem especificar a categoria de resumo, a contagem de resumo e o argumento de resumo ao criarem uma campanha push usando nossa ferramenta.

{% alert tip %}
Note que a forma como as notificações com o mesmo ID de thread são agrupadas na bandeja de notificações está sob o controle do sistema operacional. O iOS pode optar por exibir notificações com o mesmo ID de thread separadamente ou em grupos, dependendo do que considerar ideal.
{% endalert %}

Marque a caixa **Opções de alerta** no **criador do push**.

Em seguida, selecione `summary-arg` e `summary-arg-count` como chaves e insira esses valores na coluna correspondente. Se você não definir um valor para `summary-arg`, o padrão será 1.

### Categorias de resumo

As categorias de resumo permitem que você personalize todo o resumo que aparece quando as notificações são agrupadas. Você pode criar e aplicar várias categorias.

Para usar uma categoria em sua mensagem, trabalhe com seus desenvolvedores para implementá-la usando o exemplo a seguir:

```
UNNotificationCategory *newsCategory = [UNNotificationCategory categoryWithIdentifier:@"news"
                                                      actions:@[likeAction, unlikeAction]
                                                      intentIdentifiers:@[]
                                                      hiddenPreviewsBodyPlaceholder:@""
                                                      categorySummaryFormat:@"%u more news articles from %@"
                                                       Options:0];
```

{% alert important %}
Isso não exigirá uma atualização do SDK.
{% endalert %}

{% alert tip %}
Note que `%u` e `%@` são strings de formatação para a contagem de resumo e o argumento de resumo, respectivamente. Quando o resumo for exibido, esses espaços reservados serão substituídos pelos valores de `summary-count` e `summary-arg`.
{% endalert %}

Quando isso estiver configurado no seu app, use a categoria de resumo marcando a caixa **Botões de notificação** e selecionando **Inserir categoria iOS pré-registrada**.

Em seguida, insira o identificador de categoria de resumo que você definiu em seu app.

### Autenticação provisória por push e notificações silenciosas {#provisional-push}

A Apple permite que as marcas tenham a opção de enviar notificações por push silenciosas para as Centrais de Notificações dos usuários antes da aceitação oficial e explícita, o que lhe dá a chance de demonstrar o valor das suas mensagens com antecedência. Tudo o que você precisa fazer é [configurar notificações por push provisórias](#set-up-provisional-push-notifications) em seu app e, em seguida, qualquer usuário que tenha um token por push provisório receberá suas mensagens.

Ao contrário de um token tradicional de push do iOS, um token provisório de push funciona como um "passe de teste" que permite que as marcas entrem em contato com novos usuários antes que eles vejam e cliquem no pedido de aceitação de push nativo da Apple. Com esse recurso, sua notificação por push será entregue diretamente na bandeja de notificações do novo usuário, com a opção de "Manter" ou "Desativar" futuras notificações. Em vez de experimentar uma jornada de "aceitação", os usuários experimentarão algo mais parecido com uma jornada de "exclusão".

{% alert tip %}
A autorização provisória tem o potencial de aumentar drasticamente sua taxa de aceitação, mas somente se os usuários perceberem o valor de suas mensagens. Certifique-se de usar nossos recursos [de]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) [segmentação de usuários]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), [direcionamento por local]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/) e [personalização]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) para garantir que os usuários apropriados recebam essas notificações de "teste" no momento certo. Em seguida, é possível incentivar os usuários a aceitarem totalmente as notificações por push, sabendo que elas agregam valor à experiência dos usuários no app.
{% endalert %}

Qualquer que seja a opção escolhida pelo usuário, ele adicionará o token ou [o status de inscrição]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/) apropriado às suas [Configurações de contato]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab) na guia **Engajamento** do seu perfil de usuário.

![Configurações de contato com um status de assinatura push.]({% image_buster /assets/img/profile-push-prov-auth.png %}){: width="50%"}

Você poderá direcionar seus usuários com base no fato de estarem ou não autorizados provisoriamente usando nossos [filtros de segmentação]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/).

![Painel Detalhes do segmento com o filtro de segmento de amostra "Autorização provisória no iOS Stopwatch (iOS) é verdadeira" para direcionamento de usuários.]({% image_buster /assets/img/segment-push-prov-auth.png %})

{% alert tip %}
Se os usuários optarem por "Desativar" o envio provisório de mensagens suas, eles não verão mais nenhum envio provisório de mensagens suas. Seja cuidadoso com o conteúdo e a cadência das mensagens enviadas usando essa funcionalidade!
{% endalert %}

{% alert important %}
Se usar prompts push adicionais ou [primers push no app](https://www.braze.com/resources/glossary/priming-for-push/) (uma mensagem no app que incentiva os usuários a aceitarem notificações por push), entre em contato com seu representante Braze para obter mais orientações.
{% endalert %}

#### Configurar notificações por push provisórias

O Braze permite que você se registre para a autenticação provisória atualizando seu código no snippet de registro de token na implementação do SDK do Braze para iOS usando os seguintes snippets como exemplo (envie-os aos seus desenvolvedores ou garanta que eles [implementem a autenticação provisória por push durante o processo de integração]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#using-usernotification-framework-ios-10)).

{% alert warning %}
A implementação da autenticação push provisória é compatível apenas com o iOS 12+ e apresentará erro se o direcionamento da implantação for anterior a isso. Você pode saber mais sobre isso [em nossa documentação de implementação mais detalhada aqui]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#using-usernotification-framework-ios-10).
{% endalert %}

{% tabs local %}
  {% tab Rápido %}
**Swift**

```
var options: UNAuthorizationOptions = [.alert, .sound, .badge]
if #available(iOS 12.0, *) {
  options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
}
```
  {% endtab %}
  {% tab Objective C %}

**Objective C**

```
UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
center.delegate = self;
UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
if (@available(iOS 12.0, *)) {
    options = options | UNAuthorizationOptionProvisional;
}
```
  {% endtab %}
{% endtabs %}

### Nível de interrupção (iOS 15+) {#interruption-level}

Com o novo Focus Mode do iOS 15, os usuários têm mais controle sobre quando as notificações do app podem "interrompê-los" com um som ou vibração.

![Página de configurações de notificação do iOS que mostra as notificações habilitadas para entrega imediata e com notificações sensíveis ao tempo ativadas.]({% image_buster /assets/img/ios/ios15-notification-settings.png %}){: style="max-width:40%"}

Os apps agora podem especificar o nível de interrupção que uma notificação deve incluir, com base em sua urgência.

Para alterar o nível de interrupção de uma notificação por push do iOS, selecione a guia **Settings (Configurações)** e escolha o nível desejado no menu suspenso **Interruption Level (Nível de interrupção** ).

![Menu suspenso para selecionar o nível de interrupção.]({% image_buster /assets/img/ios/interruption_level.png %}){: style="max-width:50%"}

Esse recurso não tem requisitos mínimos de versão do SDK, mas só se aplica a dispositivos com iOS 15+.

Lembre-se de que, em última análise, são os usuários que controlam seu foco e, mesmo que uma notificação sensível ao tempo seja entregue, eles podem especificar quais apps não têm permissão para interromper seu foco.

Consulte a tabela a seguir para obter os níveis de interrupção e suas descrições.

|Nível de interrupção|Descrição|Quando usar|Ignorar Modo Foco|
|--|--|--|--|
|[Passivo](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/passive)|Envia uma notificação sem som, vibração ou ativação da tela.|Notificações que não requerem atenção imediata.|Não|
|[Ativo](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/active) (padrão)|Só emitirá um som, uma vibração e ligará a tela se o usuário não estiver no modo de foco.|Notificações que exigem atenção imediata, a menos que o usuário tenha o Modo de Foco ativado.|Não|
|[Relevante](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/timesensitive)|Emite um som, vibra e liga a tela mesmo no modo de foco. Requer que o **recurso de Notificações sensíveis ao tempo** seja adicionado ao seu app no Xcode|Notificações oportunas que devem incomodar os usuários independentemente do modo de foco, como uma notificação de compartilhamento de carona ou entrega.|Sim|
|[Crítico](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/critical)|Emitirá um som, vibrará e ligará a tela, mesmo que o botão **Não Perturbe** do telefone esteja ativado. Isso [requer aprovação explícita da Apple](https://developer.apple.com/contact/request/notifications-critical-alerts-entitlement/).|Emergências, como clima severo ou alertas de segurança|Sim|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Pontuação de relevância (iOS 15+) {#relevance-score}

![Um resumo de notificação para iOS intitulado "Your Evening Summary" (Seu resumo da noite) com três notificações.]({% image_buster /assets/img/ios/ios15-notification-summary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

O iOS 15 também apresenta uma nova maneira de os usuários programarem opcionalmente um agrupamento de várias notificações em horários determinados ao longo do dia. Isso é feito para evitar interrupções constantes ao longo do dia para notificações que não precisam de atenção imediata.

Os apps podem especificar quais notificações por push são mais relevantes, definindo uma **pontuação de relevância**. A Apple usará essa pontuação para determinar quais notificações devem ser exibidas no Resumo de notificações programado, enquanto outras são disponibilizadas quando os usuários clicam no resumo. 

Todas as notificações ainda poderão ser acessadas na central de notificações do usuário.

Para definir a pontuação de relevância de uma notificação do iOS, insira um valor entre `0.0` e `1.0` na guia **Settings (Configurações)**. Por exemplo, a mensagem mais importante deve ser enviada com `1.0`, enquanto uma mensagem de importância média pode ser enviada com `0.5`.

![Pontuação de relevância de "0,5".]({% image_buster /assets/img/ios/relevance-score.png %}){: style="max-width:80%;"}

Esse recurso não tem requisitos mínimos de versão do SDK, mas só se aplica a dispositivos com iOS 15+.

Para saber mais sobre os comprimentos máximos de mensagens para diferentes tipos de mensagens, consulte os seguintes recursos:

- [Especificações de imagem e texto]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)
- [Diretrizes de contagem de caracteres do iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/#character-count)

