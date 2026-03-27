---
nav_title: Solução de problemas
article_title: Solução de Problemas de Push
page_order: 24
page_type: reference
description: "Esta página contém etapas de solução de problemas para várias questões relacionadas ao canal de envio de mensagens push."
channel: push
---

# Solução de problemas de push

> Use esta página para solucionar problemas com o canal de envio de mensagens push.

## Falta de notificações por push

Está enfrentando desafios de entrega com notificações por push? Há uma série de etapas que você pode seguir para solucionar esse problema, verificando o seguinte:

- [Status da inscrição por push](#push-subscription-status)
- [Segmento](#segment)
- [Limites de notificação por push](#push-notification-caps)
- [Limites de taxa](#rate-limits)
- [Status do grupo de controle](#control-group-status)
- [Token por push válido](#valid-push-token)
- [Tipo de notificação por push](#push-notification-type)
- [App atual](#current-app)

#### Status da inscrição por push

Os envios de push só podem ser feitos para usuários inscritos ou que optaram por recebê-los. Verifique seu perfil de usuário na guia [Engajamento]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab) na seção **Perfil de Usuário** para confirmar se você está registrado ativamente para push no espaço de trabalho que está testando. Se você estiver registrado em vários apps, encontrará uma lista deles no campo **Push Registrado Para**:

![Push registrado para]({% image_buster /assets/img_archive/trouble1.png %})

Também é possível exportar os perfis de usuário usando os endpoints de exportação da Braze:
- [Usuários por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)
- [Usuários por segmento]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)

Qualquer um dos endpoints retornará um objeto de token por push que inclui informações de ativação de push por dispositivo.

#### Segmento

Confira se você se enquadra no segmento que está direcionando (se essa for uma campanha ativa e não um teste). No **Perfil de Usuário**, você verá uma lista dos segmentos em que o usuário se enquadra atualmente. Lembre-se de que essa é uma variável em constante mudança, pois a segmentação é atualizada em tempo real.

![Lista de segmentos]({% image_buster /assets/img_archive/trouble2.png %})

Você também pode confirmar que o usuário faz parte do segmento usando **Pesquisa de Usuário** ao criar um segmento.

![Seção "Pesquisa de usuário" com um campo de pesquisa.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

#### Limites de notificação por push

Verifique os limites de frequência global. É possível que você não tenha recebido a notificação por push porque seu espaço de trabalho tem um limite de frequência global em vigor e você já atingiu o limite de notificações por push para o período de tempo especificado.

Você pode fazer isso verificando o [limite de frequência global]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#freq-cap-feat-over) no dashboard. Se a campanha estiver configurada para obedecer às regras de limite de frequência, haverá vários usuários afetados por essas configurações

![Detalhes da campanha]({% image_buster /assets/img_archive/trouble3.png %})

#### Limites de taxa

Se você tiver um limite de taxa definido para sua campanha ou Canvas, pode estar deixando de receber mensagens por exceder esse limite. Para saber mais, consulte [Limite de taxa]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting).

#### Status do grupo de controle

Se essa for uma campanha de canal único ou um Canvas com um grupo de controle, é possível que você esteja se enquadrando no grupo de controle.

  1. Verifique a [distribuição de variantes]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#step-5-distribute-users-among-your-variants) para ver se há um grupo de controle.
  2. Se sim, crie um segmento filtrando por [grupo de controle da campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#in-campaign-control-group-filter) e então [exporte o segmento]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/segment_data_to_csv/#exporting-to-csv) e verifique se seu ID do usuário está nesta lista.

#### Token por push válido
Um token por push é um identificador que os remetentes usam para direcionar uma notificação por push a dispositivos específicos. Portanto, se o dispositivo não tiver um token por push válido, não haverá como enviar uma notificação por push para ele. 

#### Tipo de notificação por push

Verifique se está usando o tipo correto de notificação por push. Por exemplo, se quiser direcionar uma FireTV, você usaria uma notificação por push do Kindle, não uma campanha por push do Android. Da mesma forma, se você quiser direcionar um Android, use uma notificação por push para Android e não uma campanha de push para iOS. Confira os artigos a seguir para saber mais sobre o fluxo de trabalho da Braze:
- [Notificação Push da Apple]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=swift)
- [Firebase Cloud Messaging]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android)

#### App atual

Ao testar envios de push com usuários internos, certifique-se de que o usuário que você deseja que receba a notificação por push esteja atualmente logado no app relevante. Isso pode fazer com que o usuário não receba um push ou receba um push para o qual você acredita que ele não está segmentado.

## Clicar em uma notificação por push não abre o app

Se clicar em uma notificação por push não abre o seu app, verifique o seguinte com base na sua plataforma.

### Android

1. **Verifique o comportamento ao clicar:** Confirme que a campanha está configurada para abrir o app quando clicada.
2. **Verifique o tratamento de deep links:** No seu arquivo `braze.xml`, verifique se `com_braze_handle_push_deep_links_automatically` está definido como `true` ou `false`.
   - Se definido como `true`, o SDK da Braze trata os deep links diretamente e o app deve abrir conforme esperado.
   - Se definido como `false`, seu app precisa de um broadcast receiver para escutar e tratar os intents de push recebidos e abertos. Verifique se esse receiver está implementado corretamente.
3. **Colete registros detalhados:** [Ative o registro detalhado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging), reproduza o problema e forneça os registros junto com seus arquivos `braze.xml` e `AndroidManifest.xml` ao suporte da Braze.

### iOS

1. **Verifique o comportamento ao clicar:** Confirme que a campanha está configurada para abrir o app quando clicada.
2. **Verifique a integração de push:** O deep linking a partir de um push para o app é tratado automaticamente pela [integração padrão de push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) da Braze. Confirme que a integração está implementada corretamente, incluindo qualquer tratamento de delegate personalizado.
3. **Colete registros detalhados:** [Ative o registro detalhado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging), reproduza o problema e forneça os registros ao suporte da Braze.

## Cliques em push abrem inesperadamente no app

Se você está enfrentando problemas com links em notificações por push abrindo inesperadamente no seu app em vez do navegador, pode haver um problema com a configuração da sua campanha ou implementação do SDK. Consulte estas etapas para obter ajuda.

### Verifique o comportamento ao clicar

Na sua campanha ou etapa do canva, verifique se **Abrir URL da web dentro do app móvel** não está selecionado. Se estiver, desmarque a seleção e relance. 

![Campo "Comportamento ao clicar" de configuração de um push definido como "Abrir URL da web" com "Abrir URL da web dentro do app móvel" desmarcado.]({% image_buster /assets/img/push_on_click.png %})

A interação padrão para o comportamento ao clicar "Abrir URL da web" difere por versão do SDK. Para versões do SDK iOS 2.29.0 e Android 2.0.0 e superiores, esta opção é selecionada por padrão e URLs da web abrirão em uma visualização da web dentro do app. Antes dessas versões, esta opção é desmarcada por padrão e URLs da web abrem no navegador padrão do dispositivo.

Se este não for o problema, pode haver um problema com a sua implementação de push. 

### Verifique novamente a integração de push

Se links em suas notificações por push estão abrindo no app inesperadamente, pode ser devido a problemas com a sua integração ou configurações de personalização de notificações por push. Siga estas etapas para solucionar o problema:

1. **Revise a implementação do delegate de push:** Certifique-se de que o delegate de push da Braze está implementado corretamente. Para instruções detalhadas, consulte o guia de integração para notificações por push para sua [plataforma]({{site.baseurl}}/developer_guide/home/).
2. **Inspecione o tratamento de links personalizados:** Verifique se o app inclui tratamento personalizado para todos os links `https://`. Configurações personalizadas podem substituir comportamentos padrão. Colabore com sua equipe de desenvolvimento para revisar e ajustar essas configurações, se necessário.
3. **Verifique o registro de push do iOS:** Para iOS, revise a etapa 1 do guia de integração de push em [registrando notificações por push com APNs]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-register-for-push-notifications-with-apns). Certifique-se de que seu objeto delegate seja atribuído de forma síncrona antes que o app termine de iniciar. Esta etapa deve ser concluída no método `application:didFinishLaunchingWithOptions:`.
4. **Teste sua integração:** Após fazer ajustes, teste o comportamento da notificação por push em dispositivos iOS e Android para confirmar que o problema foi resolvido.

## O título do push é cortado no iOS, mas exibido corretamente no Android

Se o título da sua notificação por push contém personalização com Liquid e aparece completo no Android, mas truncado no iOS, isso é causado pela forma como cada plataforma lida com caracteres de nova linha (`\n`) na string do título.

O Android remove automaticamente espaços em branco, tabulações e novas linhas das strings de título de push. O iOS não faz isso, então se uma variável Liquid resolve para um valor que contém uma nova linha no final, o iOS trata a nova linha como o fim do título e corta o texto restante.

Por exemplo, um título como `Regarding your flight from {% raw %}{{${city_from}}}{% endraw %} to {% raw %}{{${city_to}}}{% endraw %}` pode exibir `Regarding your flight from` no iOS se a variável `city_from` incluir uma nova linha no final.

Para corrigir isso, aplique o filtro Liquid `strip_newlines` e envolva o título inteiro em um bloco `capture`:

{% raw %}
```liquid
{% capture title %}Regarding your flight from {{${city_from}}} to {{${city_to}}}{% endcapture %}
{{ title | strip_newlines }}
```
{% endraw %}

## As notificações por push da web não estão se comportando como esperado

Se estiver tendo problemas com notificações por push no navegador, talvez seja necessário redefinir as permissões de notificação do site e limpar o armazenamento do site. Consulte estas etapas para obter ajuda.

{% tabs %}
{% tab Chrome %}

### Redefinir o Chrome no desktop

1. Ao lado da sua URL no navegador Chrome, selecione o ícone do slider **Ver Informações do Site**.
2. Em **Notificações**, selecione **Redefinir permissão**.
3. Abra o Chrome DevTools. Veja a seguir os atalhos relevantes por sistema operacional.

<style> 
table {
    max-width: 50%;
}
</style>

| SO      | Atalhos de teclado                                                  |
| ------- | ------------------------------------------------------------------- |
| Mac      | `Fn` + `F12`<br>`Ctrl` + `Shift` + `I` |
| Windows | `F12`<br>`Ctrl` + `Shift` + `I` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{:start="4"}
4. No DevTools, navegue até a guia **Application**.
5. Na barra lateral, selecione **Storage**.
6. Selecione **Clear site data**.
7. O Chrome solicitará que você recarregue a página para aplicar as configurações atualizadas. Selecione **Reload**.

Suas permissões de push foram redefinidas. Abra uma nova guia no seu site e experimente.

### Redefinir o Chrome no Android

Se houver uma notificação do seu site visível na gaveta de notificações do Android:

1. Na notificação por push, toque em <i class="fas fa-cog" title="Configurações"></i> e selecione **Configurações do site**.
2. Em **Configurações do site**, toque em **Limpar e Redefinir**.

Se você não tiver uma notificação do seu site aberta:

1. Abra o Chrome no Android.
2. Toque no menu <i class="fas fa-ellipsis-vertical"></i>.
3. Acesse **Configurações** > **Configurações do site** > **Notificações**.
4. Verifique se as notificações estão definidas para **Perguntar antes de enviar (recomendado)**.
5. Encontre seu site na lista.
6. Selecione a entrada e toque em **Limpar e redefinir**.

Suas permissões de push foram redefinidas. Abra uma nova guia no seu site e experimente.

{% endtab %}
{% tab Firefox %}

### Redefinir o Firefox no desktop

1. Ao lado da URL do seu site, selecione <i class="fa-solid fa-circle-info" alt="ícone de informação"></i> ou <i class="fas fa-lock" alt="ícone de cadeado"></i>.
2. Em **Permissões**, ao lado de **Receber notificações**, selecione <i class="fa-solid fa-circle-xmark" title="Limpar essa permissão e perguntar novamente"></i> para limpar as permissões de notificação.
3. No mesmo menu, selecione **Limpar cookies e dados do site**.
4. Na caixa de diálogo para confirmar sua escolha, selecione **OK**.

Suas permissões de push foram redefinidas. Abra uma nova guia no seu site e experimente.

### Redefinir o Firefox no Android

Para redefinir as permissões de push no Android, consulte este [artigo de suporte da Mozilla](https://support.mozilla.org/en-US/kb/clear-your-browsing-history-and-other-personal-data#w_clear-specific-items-from-your-browser).

{% endtab %}
{% tab Safari %}

### Redefinir o Safari no macOS

{% alert note %}
Essas etapas são apenas para macOS, pois a Apple não oferece suporte a Push para a web no Safari para Windows.
{% endalert %}

1. Abra o Safari.
2. Na [barra de menus do Mac](https://support.apple.com/guide/mac-help/whats-in-the-menu-bar-mchlp1446/mac), acesse **Safari** > **Configurações** > **Sites** > **Notificações**.
3. Selecione seu site na lista.
4. Selecione **Remover** para excluir as permissões de notificação do site.
5. Em seguida, acesse **Privacidade** > **Gerenciar dados do site**.
6. Selecione seu site na lista.
7. Selecione **Remover**, ou para remover todos os dados do site, selecione **Remover Tudo**.
8. Selecione **Concluído**.

Suas permissões de push foram redefinidas. Abra uma nova guia no seu site e experimente.

{% endtab %}
{% endtabs %}

## Mensagens de erro de push

Para informações detalhadas sobre mensagens de erro comuns de push (como `DEVICE_UNREGISTERED`, `Unregistered`, `NotRegistered` e outras), consulte [Mensagens de erro comuns de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_error_codes/).

Ainda precisa de ajuda? Abra um [tíquete de suporte]({{site.baseurl}}/braze_support/).