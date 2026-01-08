{% if include.variable_name == "image behavior" %}


| Layout | Comportamento |
| --- | --- |
| Imagem e texto | Imagens altas ou estreitas serão reduzidas e centralizadas horizontalmente. Imagens largas serão cortadas nas bordas esquerda e direita. |
| Somente imagem | A mensagem será redimensionada para se ajustar a imagens com a maioria das proporções. |
{: .reset-td-br-1 .reset-td-br-2}

{% endif %}

{% if include.variable_name == "payload size" %}

Recomendamos os seguintes tamanhos de carga útil:

| Sistema de envio de mensagens | Carga útil recomendada |
| --- | --- |
| iOS (pré-iOS 8) | 0,256 KB |
| iOS (pós-iOS 8) | 2 KB |
| Android (FCM) | 4 KB |
{: .reset-td-br-1 .reset-td-br-2}

{% endif %}

{% if include.variable_name == "in-app messages" %}

As mensagens modais no app são projetadas para se ajustarem ao dispositivo nas melhores e mais preenchidas proporções possíveis, mantendo-se fiéis ao tamanho e às proporções da imagem ou do texto escolhido para a mensagem.

Embora não haja limites para o número de caracteres de texto que você pode incluir em uma mensagem no app (assim como botões, título, corpo principal e outros), moderamos o número de caracteres de texto que você usa. O excesso de texto exigirá que os usuários expandam e rolem a mensagem.

Todas as mensagens no app têm um tamanho de imagem recomendado de 500 KB, tamanho máximo de imagem de 5 MB e são compatíveis com os tipos de arquivo PNG, JPEG e GIF.

{% tabs %}
{% tab Retrato %}

| Tipo | Proporção | Qualidade da imagem | Notas |
| --- | --- | --- | --- |
| Retrato em tela inteira com texto | 6:5 | Alta resolução de 1200 x 1000 px <br>Resolução mínima de 600 x 500 px | O corte pode ocorrer em todos os lados, mas a imagem sempre preencherá os 50% superiores da janela de visualização. |
| Retrato em tela inteira (somente imagem, com ou sem botões) | 3:5 | Alta resolução de 1200 x 2000 px <br> Resolução mínima de 600 x 1000 px | O corte pode ocorrer nas bordas esquerda e direita em dispositivos mais altos. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% endtab %}
{% tab Paisagem %}

| Tipo | Proporção | Qualidade da imagem | Notas |
| --- | --- | --- | --- |
| Paisagem em tela inteira com texto | 10:3 | Alta resolução 2000 x 600 px <br>Resolução mínima de 1000 x 300 px | O corte pode ocorrer em todos os lados, mas a imagem sempre preencherá os 50% superiores da janela de visualização. |
| Tela inteira em paisagem (somente imagem, com ou sem botões) | 5:3 | Alta resolução 2000 x 600 px <br> Resolução mínima de 1000 x 600 px | O corte pode ocorrer nas bordas esquerda e direita em dispositivos mais altos. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% endtab %}
{% tab Slideup %}

| Tipo | Proporção | Qualidade da imagem | Notas |
| --- | --- | --- | --- |
| Slideup | 1:1 | Alta resolução 150 x 150 px <br> Resolução mínima de 50 x 50 px | Imagens de várias proporções de aspecto caberão em um contêiner de imagem quadrado, sem corte. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% endtab %}
{% tab Modal %}

| Tipo | Proporção | Qualidade da imagem | Notas |
| --- | --- | --- | --- |
| Modal (somente imagem) | 1:1 | Resolução máxima recomendada: 1200 x 2000 px <br> Resolução mínima: 600 x 600 px | A mensagem será redimensionada para se ajustar a imagens com a maioria das proporções. A resolução máxima recomendada tem uma proporção de 3:5, o que pode não proporcionar os melhores resultados. Embora imagens maiores possam ser usadas, elas podem levar a tempos de carregamento mais longos. <br> A proporção ideal para imagens é de 1:1, e o não cumprimento dessa proporção pode disparar um aviso durante o upload. Esse aviso é uma sugestão para obter os melhores resultados e não impede que se faça upload de imagens maiores. |
| Modal com texto | 29:10 | Alta resolução 1450 x 500 px <br> Resolução mínima de 600 x 205 px | As imagens altas serão reduzidas e centralizadas horizontalmente. Imagens largas serão cortadas nas bordas esquerda e direita. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% endtab %}
{% endtabs %}

{% endif %}

{% if include.variable_name == "push notifications" %}

| Tipo de mensagem | Comprimento máximo da mensagem | Comprimento máximo do título |
| --- | --- | --- |
| Tela de bloqueio do iOS | 175 caracteres | 43 caracteres |
| Notificação do iOS | 175 caracteres | 43 caracteres |
| Alerta de banner do iOS | 85 caracteres | 43 caracteres |
| Tela de bloqueio do Android | 49 caracteres | 43 caracteres |
| Gaveta de notificação do Android | 597 caracteres | 43 caracteres |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

O tamanho de imagem recomendado para todas as imagens push é de 500 KB.

<style>
table td {
    word-break: break-word;
}
</style>

<table>
  <thead>
    <tr>
      <th>Tipo de imagem</th>
      <th>Proporção</th>
      <th>Máximo de pixels</th>
      <th>Tamanho máximo da imagem</th>
      <th>Tipos de arquivos</th>
      <th>Notas</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>iOS</td>
      <td>2:1 (recomendado)</td>
      <td>1038 x 1038</td>
      <td>5 MB</td>
      <td>PNG, JPEG, GIF</td>
      <td>A partir de janeiro de 2020, as notificações por push avançadas do iOS podem lidar com imagens de 1038 x 1038 px, desde que tenham menos de 10 MB, mas recomendamos usar o menor tamanho de arquivo possível. Na prática, o envio de arquivos grandes pode causar estresse desnecessário na rede e tornar os tempos limite de download mais comuns.<br><br>Para saber mais, consulte <a href="{{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/">notificações rich do iOS</a>.</td>
    </tr>
    <tr>
      <td>Ícone push do Android</td>
      <td>1:1</td>
      <td>N/D</td>
      <td>500 KB</td>
      <td>PNG, JPEG</td>
      <td></td>
    </tr>
    <tr>
      <td>Imagem de notificação expandida do Android</td>
      <td>2:1</td>
      <td><b>Pequeno:</b><br>512 x 256<br><br><b>Médio:</b><br>1024 x 512<br><br><b>Grande:</b><br>2048 x 1024</td>
      <td>500 KB</td>
      <td>PNG, JPEG</td>
      <td>Usado em <a href="{{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/">notificações Rich do Android</a>.</td>
    </tr>
    <tr>
      <td>Imagem de inclinação do Android</td>
      <td>3:2</td>
      <td>N/D</td>
      <td>N/D</td>
      <td>PNG, JPEG</td>
      <td>Para obter mais detalhes, consulte <a href="{{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/inline_image_push/">push de imagem inline para Android</a>.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4  .reset-td-br-5 .reset-td-br-6 role="presentation"}

{% endif %}

{% if include.variable_name == "email" %}

| Tipo de e-mail | Propriedades máximas recomendadas |
| --- | --- | 
| Somente texto | 25 KB |
| Texto com imagens | 60 KB |
| Largura do e-mail | 600 px |
{: .reset-td-br-1 .reset-td-br-2}

| Especificações da imagem | Propriedades máximas recomendadas |
| --- | --- | 
| Tamanho | 5 MB |
| Largura | Cabeçalho: 600 px<br>Corpo: 480 px |
| Tipos de arquivos | PNG, JPEG, GIF |
{: .reset-td-br-1 .reset-td-br-2}

| Especificações de texto | Propriedades máximas recomendadas |
| --- | --- | 
| Comprimento da linha de assunto | 35 caracteres<br>6 a 10 palavras |
| `"From: Name"` comprimento | 25 caracteres |
| Comprimento do pré-cabeçalho | 85 caracteres |
{: .reset-td-br-1 .reset-td-br-2}

{% endif %}

{% if include.variable_name == "content cards" %}

| Tipo de cartão | Proporção     | Qualidade da imagem       |
| --------- | ---------------- | ------------------- |
| Clássico   | Proporção de 1:1 | 60 x 60 px        |
| Com legenda | Relação de aspecto 4:3 | Largura mínima de 600 px |
| Banner    | Qualquer proporção de aspecto | Largura mínima de 600 px |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Para saber mais, consulte os [detalhes de criação do cartão de conteúdo]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/).

{% endif %}
