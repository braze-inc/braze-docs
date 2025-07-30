---
nav_title: "Canais de notificação"
article_title: Canais de notificação por push 
page_order: 4
page_type: reference
description: "Este artigo de referência aborda tópicos sobre o canal de notificação por push do Android, como a transição para o Android O, como adicionar um canal ao Braze, definir um canal fallback e muito mais."
platform: Android
channel:
  - push

---

# Canais de notificação

> [Os canais de notificação](https://www.braze.com/blog/android-o-push-notifications-channels/) são uma forma de organizar as notificações por push que foram adicionadas com o Android O. A partir do O, todas as notificações por push devem ter um canal de notificação que indique o tipo de mensagem (por exemplo, "notificações de bate-papo" ou "seguir notificações"). Seus usuários podem controlar aspectos da notificação (por exemplo, soneca, configurações de ruído/vibração, aceitação, etc.) com base em canais individuais.

## Transição para o Android O

Os canais de notificação só podem ser criados no código de seu aplicativo e não podem ser criados programaticamente no dashboard do Braze. Recomendamos que sua equipe de engenharia trabalhe com os profissionais de marketing para garantir que os canais de notificação desejados sejam adicionados corretamente ao dashboard.

A partir do Android O, as notificações por push exigem um canal válido para serem exibidas. Se o seu app for direcionado para o Android O ou posterior, você deverá usar o SDK da Braze versão 2.1.0 ou posterior. Sua equipe de desenvolvimento deve definir os canais que deseja usar, bem como as configurações de notificação sugeridas (por exemplo, importância, som, luzes) para cada canal no código do aplicativo. Você pode encontrar a documentação do desenvolvedor do Android [aqui](https://developer.android.com/preview/features/notification-channels.html) e a documentação do desenvolvedor do Braze [aqui.]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-5-define-notification-channels)

{% alert note %}
O Android oferece suporte à localização de nomes de canais, portanto, no código do seu aplicativo, você pode associar um ID de canal a várias traduções de um nome de canal.
{% endalert %}

Depois que esses canais forem criados, seus engenheiros precisarão passar as IDs de canal associadas para a equipe de marketing. Sua equipe deve inserir os nomes e os IDs dos canais no dashboard do Braze para uso em suas campanhas e Canvas.

Para adicionar um canal ao dashboard da Braze, navegue até o criador de notificações por push do Android, selecione o campo de canais de notificação e, em seguida, selecione "gerenciar canais".
{% alert important %}
Somente os usuários com permissões que incluem "gerenciar apps" poderão gerenciar canais.
{% endalert %}

## Canal padrão do SDK

O Android requer um canal válido para exibir notificações por push no nível 26 da API (Android O) ou posterior. O SDK da Braze para Android 2.1.0 inclui um canal padrão chamado "Geral", que será criado e usado se você não especificar canais adicionais no dashboard ou se tentar enviar para um canal inválido. Você pode renomear esse rótulo no SDK e fornecer uma descrição do canal. Recomendamos que considere essa possibilidade para proporcionar uma melhor experiência ao usuário.  

Depois que um canal é adicionado ao seu aplicativo, você pode aceitar removê-lo. No entanto, os consumidores sempre poderão ver o número de canais que você [removed].[3] O dashboard do Braze não inclui suporte para a criação programática de canais - os canais devem ser criados e definidos no código do seu aplicativo para proporcionar uma experiência perfeita.

Novamente, recomendamos que você coordene com sua equipe de engenharia para garantir uma transição perfeita para o direcionamento do Android O.

## Canal de fallback do dashboard

A Braze permite que você especifique um canal de fallback do dashboard. O objetivo do canal de envio de mensagens do dashboard é fornecer uma ID de canal para mensagens push herdadas sem seleção explícita de canal. Definimos uma seleção de canal como a escolha de um canal em nosso criador de push do Android.

As mensagens que não tiverem um canal selecionado serão enviadas com a ID do canal de envio de mensagens do dashboard. Quando você altera o canal de envio de mensagens do painel, qualquer mensagem que não tenha um canal explicitamente selecionado será enviada com a ID do novo canal de envio de mensagens.

Aqui está um exemplo do comportamento esperado do canal de fallback do dashboard:

Seu canal de envio de mensagens do dashboard é chamado de "Marketing" e você tem 10 mensagens push do Android para as quais nunca selecionou um canal. Essas campanhas estão sendo enviadas pelo canal "Marketing" porque o canal "Marketing" é o canal fallback do dashboard.

Além disso, você tem 15 mensagens que selecionou para enviar por meio do canal "Social Notifications" (Notificações sociais) e cinco mensagens que selecionou para enviar por meio do canal "Marketing".

Em seguida, você decide alterar o canal padrão do dashboard de "Marketing" para "Atualizações".

Nessa situação, todas as 10 campanhas sem seleção de canal que foram enviadas anteriormente pelo canal "Marketing" agora serão enviadas pelo canal "Atualizações" porque essas mensagens são enviadas pelo canal de envio de mensagens. As 15 mensagens que foram enviadas pelo canal "Social Notifications" continuarão sendo enviadas pelo canal "Social Notifications". As cinco mensagens que foram enviadas pelo canal de "Marketing" continuarão sendo enviadas pelo canal de "Marketing".

Caso um ID de canal inválido seja fornecido à Braze (por exemplo, se você fornecer um ID de canal que seus desenvolvedores não criaram no SDK), enviaremos a notificação por meio de seu canal padrão do SDK. Portanto, é altamente recomendável que você teste seus canais de notificação por meio do dashboard da Braze durante o desenvolvimento.

Para entender melhor o comportamento esperado para os canais, consulte a tabela a seguir:

|Cenário |Resultado  |    
| ---|-------------
|Atualizações **da empresa ABC** para um SDK compatível com Android O<br>**A empresa ABC** não adiciona nenhum canal ao dashboard do Braze<br>**A empresa ABC** não renomeia seu canal padrão do SDK | As notificações por push enviadas para dispositivos Android O criarão um canal chamado "Geral" e as notificações serão enviadas pelo canal "Geral".
|**A empresa XYZ** atualiza para um SDK compatível com o Android O <br>**A empresa XYZ** não adiciona nenhum canal ao dashboard do Braze<br>**A empresa XYZ** renomeia o canal padrão de seu SDK para "Marketing" | As notificações por push enviadas para dispositivos Android O criarão um canal chamado "Marketing" e as notificações serão enviadas por meio do canal "Marketing".
|**Empresa LMN** atualiza para um SDK compatível com Android O <br>**A empresa LMN** define dois canais em seu código de aplicativo, "Promoções" e "Atualizações de pedidos" <br>**A empresa LMN** adiciona os IDs de canal para "Promoções" e "Atualizações de pedidos" ao dashboard do Braze <br>**A empresa LMN** designa "Promoções" como o canal fallback do dashboard<br>**A empresa LMN** renomeia o canal padrão de seu SDK para "Marketing" | As notificações por push enviadas para dispositivos Android O não criarão um canal<br><br>A menos que o profissional de marketing especifique explicitamente que as notificações devem ser enviadas pelo canal "Order Updates" (Atualizações de pedidos) ou "Marketing", todas as notificações criadas antes de os canais serem adicionados ao dashboard serão enviadas pelo canal "Promotions" (Promoções).<br><br>O canal padrão do SDK, "Marketing", só é criado e usado se a empresa tentar enviar uma notificação por meio de um ID de canal inválido ou se for selecionado explicitamente
|**A empresa HIJ** atualiza para o Android O, mas não atualiza o SDK da Braze para Android para a versão 2.1.0 ou posterior | As notificações enviadas aos usuários que executam o Android O ou posterior não são exibidas |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Adição de canais ao dashboard do Braze

1. Abra qualquer campanha ou tela que inclua um push do Android e clique em **Edit Campaign (Editar campanha**).
2. Navegue até o criador de mensagens push do Android.
3. Clique em **Manage Notification Channels (Gerenciar canais de notificação**). Todos os canais adicionados aqui estarão disponíveis globalmente para todas as campanhas e telas. Você deve ter [permissões]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#limited-and-team-role-permissions) "Manage Apps" (Gerenciar aplicativos) para que seu espaço de trabalho gerencie canais.

Quando você aplica um canal de notificação a uma campanha ou etapa do Canva específica, a contagem de **usuários alcançáveis** (localizada na etapa de público-alvo) para o Android Push não parece mudar. No entanto, somente os usuários inscritos no canal de notificação selecionado verão a mensagem, e a análise de dados da sua campanha (como cliques) será medida com base nesse público.

![]({% image_buster /assets/img_archive/Click_Here.png %})

{:start="4"}
4\. Clique em **Add Notification Channel (Adicionar canal de notificação**).
5\. Digite o nome e o ID do canal de notificação que deseja adicionar.<br><br>![]({% image_buster /assets/img_archive/Enter_Channel.png %})<br><br>
6\. Repita as etapas 4 e 5 para cada canal de notificação que você deseja adicionar.
7\. Pressione **Save (Salvar** ) para salvar suas alterações.

## Especificando seu canal de fallback

Seu canal de envio de mensagens é o canal com o qual a Braze tentará enviar sua mensagem Android se você não tiver selecionado um canal para a mensagem. As únicas campanhas e Canvases que terão mensagens Android sem uma seleção de canal são as campanhas e Canvases que foram criadas antes de sua equipe adicionar canais ao dashboard do Braze. Se você alterar seu canal fallback, a alteração será aplicada globalmente a todas as campanhas e Canvas sem uma seleção explícita de canal.

1. Abra qualquer campanha ou Canva existente.
2. Navegue até o criador do Android push.
3. Selecione **Manage Notification Channels (Gerenciar canais de notificação** ) depois de expandir as opções de canais de notificação. <br><br>![]({% image_buster /assets/img_archive/Change_Fallback.png %}){: style="max-width:80%;"}<br><br>
4. Adicione o canal ao dashboard (se ele ainda não tiver sido adicionado).
5. Selecione o botão de rádio ao lado do canal que deseja designar como o canal de fallback.
6. Salve suas alterações. Suas alterações serão aplicadas globalmente.

## Adição de canais de envio de mensagens para seu Android

1. Navegue até o criador do Android push em qualquer campanha ou tela.
2. Selecione o canal que você gostaria de usar no menu suspenso. Se você não tiver um menu suspenso, mas sim a visualização a seguir, precisará adicionar canais antes de selecioná-los para as campanhas.

![]({% image_buster /assets/img_archive/No_Select.png %})

[3]: https://developer.android.com/preview/features/notification-channels.html#DeletingChannels
