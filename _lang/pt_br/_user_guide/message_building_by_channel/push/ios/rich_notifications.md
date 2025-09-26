---
nav_title: "Criação de notificações Rich"
article_title: "Criação de notificações por push avançadas para iOS"
page_order: 3
page_type: tutorial
description: "Este tutorial aborda os requisitos e as etapas de como criar notificações Rich do iOS para suas campanhas do Braze."

platform: iOS
channel:
  - push
tool:
  - Campaigns

---

# Criação de notificações por push avançadas para iOS

> As notificações Rich permitem maior personalização em suas notificações por push, acrescentando conteúdo adicional além do texto. Há algum tempo, as notificações por push do Android incluem imagens, enviadas de mensagens como "Imagem de notificação expandida". A partir do iOS 10, seus clientes poderão receber notificações por push do iOS que incluem GIFs, imagens, vídeos ou áudio.

## Pré-requisitos

Antes de criar uma notificação por push avançada para iOS, observe os seguintes detalhes:

- Para garantir que seu aplicativo possa enviar notificações por push, siga as instruções de [integração de push do iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#ios-10-rich-notifications), pois o desenvolvedor precisará adicionar uma extensão de serviço ao seu aplicativo.
- Os tipos de arquivo que suportamos atualmente para fazer upload direto em nosso dashboard incluem JPEG, PNG ou GIF. Esses arquivos também podem ser inseridos no campo de URL de modelo, juntamente com esses tipos de arquivos adicionais: AIF, M4A, MP3, MP4 ou WAV.
- Consulte a [documentação da Apple](https://developer.apple.com/reference/usernotifications/unnotificationattachment) para conhecer as limitações e especificações da mídia.
- As notificações Rich do iOS não estão disponíveis ao criar uma campanha push rápida.
- O iOS dimensionará as imagens para que caibam na tela e dimensionará as imagens ricas para a exibição ativa ou bloqueada.

{% alert note %}
A partir de janeiro de 2020, as notificações por push avançadas do iOS podem lidar com imagens de 1038x1038 com menos de 10 MB, mas recomendamos usar o menor tamanho de arquivo possível. Na prática, o envio de arquivos grandes pode causar estresse desnecessário na rede e tornar os tempos limite de download mais comuns.
{% endalert %}

### Contagem de caracteres

Embora não possamos fornecer uma regra rígida e rápida para o número exato de caracteres a serem incluídos em um push, [fornecemos algumas diretrizes]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/) a serem consideradas ao projetar mensagens para iOS. Pode haver alguma variação dependendo da presença de uma imagem, do estado da notificação e da configuração de exibição do dispositivo do usuário e do tamanho do dispositivo. Em caso de dúvida, seja breve e direto.

Como prática recomendada, a Braze recomenda manter cada linha de texto, tanto para o título opcional quanto para o corpo da mensagem, com aproximadamente 30 a 40 caracteres em uma notificação por push para celular.

#### Declarações de notificação

Seus usuários podem visualizar as notificações por push em várias situações diferentes e podem ver diferentes comprimentos de texto, como segue.

<table>
<thead>
  <tr>
    <th>Tela de bloqueio ou Central de notificações</th>
    <th>Expandido</th>
    <th>Dispositivo ativo</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td width="33%">Esse é o cenário mais comum.<br><br><b>Título:</b> 1 linha de texto<br><b>Corpo:</b> 4 linhas de texto<br><b>Imagem:</b> miniatura quadrada</td>
    <td width="33%">Quando um usuário pressiona longamente uma mensagem.<br><br><b>Título:</b> 1 linha de texto<br><b>Corpo:</b> 7 linhas de texto<br><b>Imagem:</b> Relação de aspecto 2:1 (recomendado, consulte a nota a seguir)</td>
    <td width="33%">Quando um usuário recebe um push enquanto seu telefone está desbloqueado e ativo.<br><br><b>Título:</b> 1 linha de texto<br><b>Corpo:</b> 2 linhas de texto</td>
  </tr>
</tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

![Exemplo de notificações por push exibidas na tela de bloqueio, quando expandidas e quando o dispositivo está ativo.]({% image_buster /assets/img_archive/push_ios_notification_states.png %})

{% alert note %}
Embora recomendemos uma proporção de 2:1 para notificações por push expandidas, praticamente qualquer proporção é suportada. As imagens sempre ocuparão a largura total da notificação, e a altura será ajustada de acordo.
{% endalert %}

#### Variáveis na truncagem de texto

Ao criar conteúdo, considere os seguintes cenários que podem afetar a quantidade de texto exibida.

{% tabs %}
{% tab Cronograma %}

Dependendo de quando um usuário se engaja com uma notificação por push, o carimbo de data/hora pode encurtar o texto do título.

![Exemplo de notificação por push com um registro de data e hora "now" e contagem de caracteres de título de 35.]({% image_buster/assets/img_archive/push_ios_timing_35.png %})
<br>Contagem de caracteres do título: **35**

![Exemplo de notificação por push com um registro de data e hora de "3h atrás" e contagem de caracteres de título de 33.]({% image_buster/assets/img_archive/push_ios_timing_33.png %})
<br>Contagem de caracteres do título: **33**

![Exemplo de notificação por push com um registro de data e hora "Yesterday, 8:37 AM" e contagem de caracteres de título de 22.]({% image_buster/assets/img_archive/push_ios_timing_22.png %})
<br>Contagem de caracteres do título: **22**

{% endtab %}
{% tab Imagens %}

O texto do corpo é encurtado em cerca de 10 caracteres por linha quando uma imagem está presente.

![Exemplo de notificação por push sem imagem e com um número de caracteres no corpo de 179.]({% image_buster/assets/img_archive/push_ios_images_179.png %})
<br>Contagem de caracteres do corpo: **179**

![Exemplo de notificação por push com uma imagem e um número de caracteres no corpo de 154.]({% image_buster/assets/img_archive/push_ios_images_154.png %})
<br>Contagem de caracteres do corpo: **154**

{% endtab %}
{% tab Nível de interrupção %}

Para o iOS 15, as denotações Sensível ao tempo e Crítico empurram o título para uma nova linha sem o carimbo de data/hora, dando-lhe um pouco mais de espaço.

![Exemplo de notificação por push sem denotação de Tempo Sensível ou Crítico e uma contagem de caracteres de título de 35.]({% image_buster/assets/img_archive/push_ios_interruption_level_35.png %})
<br>Contagem de caracteres do título: **35**

![Exemplo de notificação por push com uma denotação sensível ao tempo e uma contagem de caracteres de título de 39.]({% image_buster/assets/img_archive/push_ios_interruption_level_39.png %})
<br>Contagem de caracteres do título: **39**

{% endtab %}
{% tab Mais informações %}

Os detalhes a seguir também podem afetar a truncagem do texto:

- **Configurações de exibição do telefone:** um usuário pode aumentar ou diminuir o tamanho da fonte global da interface do usuário em seu telefone, geralmente por motivos de acessibilidade.
- **Largura do dispositivo:** a mensagem pode ser exibida em um telefone pequeno ou em um iPad em paisagem.
- **Tipos de conteúdo:** emojis e caracteres largos, como "m" e "w", ocupam mais espaço do que "i" ou "t", e palavras mais longas, como "engajamento", podem ser quebradas mais abruptamente do que palavras mais curtas.

{% endtab %}
{% endtabs %}

## Configuração de sua notificação Rich no iOS

### Etapa 1: Criar uma campanha push

Siga as [etapas da campanha]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message) para compor uma notificação por push para iOS. Você usará o mesmo criador que usa para configurar notificações por push que não contêm conteúdo avançado.

### Etapa 2: Adicionar mídia

Adicione seu arquivo de imagem, GIF, áudio ou vídeo no campo **Rich Notification Media (Mídia de notificação Rich)** no criador da mensagem. Consulte os [requisitos](#requirements) sobre como adicionar seus arquivos de conteúdo.

![Um exemplo de texto de resumo para uma notificação por push.]({% image_buster /assets/img_archive/rich_notification_add_image.png %}){: style="max-width:70%;" }

Também é possível limitar o envio dessa mensagem apenas para usuários que tenham um dispositivo com iOS 10. Para os usuários que não fizeram upgrade para o iOS 10, elas aparecerão como notificações apenas de texto, sem o conteúdo avançado, se você deixar desmarcada a opção **Enviar apenas para dispositivos com suporte a notificações Rich**.

![A seção de imagem de notificação expandida, onde é possível adicionar uma imagem ou inserir um URL de imagem.]({% image_buster /assets/img_archive/rich_notification_ios10_select.png %}){: style="max-width:70%;" }

### Etapa 3: Continue criando sua campanha

Depois que o conteúdo da notificação Rich for feito upload no dashboard, você poderá continuar a [programar sua campanha]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#schedule-push-campaign).

Quando um usuário recebe a notificação por push, ele pode pressionar a mensagem por push para expandir a imagem.

![Um usuário recebe uma notificação por push e pressiona a mensagem para mostrar uma imagem expandida que diz "Hello!".]({% image_buster /assets/img_archive/rich_notification_ios.gif %}){: style="max-width:50%;" }

