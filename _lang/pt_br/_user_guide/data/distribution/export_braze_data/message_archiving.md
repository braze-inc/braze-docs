---
nav_title: Arquivamento de mensagens
article_title: Arquivamento de mensagem
alias: "/message_archiving/"
page_order: 0
page_type: reference
description: "Este artigo de referência aborda o arquivamento de mensagens, um recurso que permite salvar uma cópia das mensagens enviadas aos usuários."

---

# Arquivamento de mensagens

> A arquivação de mensagens permite que você salve uma cópia das mensagens enviadas aos usuários para fins de arquivamento ou conformidade em seu bucket S3 da AWS, contêiner de Blob Storage do Azure ou bucket do Google Cloud Storage. <br><br> Este artigo cobre como configurar a arquivação de mensagens, referências de carga útil JSON e perguntas frequentes.

O arquivamento de mensagens está disponível como um recurso complementar. Para começar com a arquivação de mensagens, entre em contato com seu gerente de sucesso do cliente da Braze.

## Como funciona?

Quando esse recurso está ativado, se você conectou um bucket de armazenamento em nuvem à Braze e o marcou como o destino padrão de exportação de dados, a Braze gravará um arquivo JSON compactado em gzip em seu bucket de armazenamento em nuvem para cada mensagem enviada a um usuário através dos canais selecionados (e-mail, SMS/MMS ou push). 

Esse arquivo conterá os campos definidos em [Referências de arquivo](#file-references) e refletirá os modelos finais de mensagens enviadas ao usuário. Todos os valores de modelo definidos em sua campanha (por exemplo, {% raw %}`{{${first_name}}}`{% endraw %}) mostrarão o valor final que o usuário recebeu com base nas informações de perfil. Isso permite que você retenha uma cópia da mensagem enviada para atender aos requisitos de conformidade, auditoria ou suporte ao cliente.

Se você configurar credenciais para vários provedores de armazenamento em nuvem, o arquivamento de mensagens só será exportado para aquele explicitamente marcado como o destino padrão de exportação de dados. Se nenhum padrão explícito for fornecido e um bucket S3 da AWS estiver conectado, o arquivamento de mensagens fará upload para esse bucket.

{% alert important %}
Ativar esse recurso impactará a velocidade de entrega de suas mensagens, pois o upload do arquivo é realizado imediatamente antes que a mensagem seja enviada para manter a precisão. A latência introduzida pela arquivação de mensagens dependerá do provedor de armazenamento em nuvem e da taxa de transferência e tamanho dos documentos salvos.
{% endalert %}

O JSON será salvo em seu bucket de armazenamento usando a seguinte estrutura de chave:

`sent_messages/{channel, one of: email, push, sms}/{MD5 digest of downcased: email address, push token, or E.164 phone number}/{campaign or Canvas step API ID}/{dispatch ID}.json.gz`

Um arquivo de exemplo pode ter a seguinte aparência:

`sent_messages/email/819baa08d8d7e77e19d4666f5fc6050b/ee965cb2-8934-4b0a-acf1-91c899c2f915/651fd10b282850b39e1169c13975234b.json.gz`

{% alert note %}
O resumo MD5 só pode ser calculado usando um endereço de e-mail, um token por push ou um número de telefone E.164 conhecidos. Um resumo MD5 conhecido não pode ser revertido para obter o endereço de e-mail, o token por push ou o número de telefone E.164 conhecidos.
{% endalert %}

{% alert tip %}
**Está tendo problemas para encontrar seus tokens por push em seus buckets?**<br>
O Braze faz o downcase de seus tokens por push antes de fazermos o hash deles. Isso faz com que o token por push `Test_Push_Token12345` seja baixado para `test_push_token12345` na jornada da chave com o hash `32b802170652af2b5624b695f34de089`.
{% endalert %}

## Configuração do arquivamento de mensagens

Esta seção o orienta na configuração do arquivamento de mensagens para o seu espaço de trabalho. Antes de continuar, confirme se sua empresa comprou e ativou o arquivamento de mensagens.

### Etapa 1: Conecte um bucket de armazenamento em nuvem

Se ainda não tiver feito isso, conecte um bucket de armazenamento em nuvem à Braze. Para obter etapas, consulte a documentação de nossos parceiros sobre o [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/), o [Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/) ou o [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/).

{% alert note %}
Você não precisa configurar o Currents para a arquivação de mensagens, então pode pular esse pré-requisito na documentação do parceiro.
{% endalert %}

### Etapa 2: Selecione canais de envio de mensagens

A página de configurações de **envio de mensagens** controla quais canais salvarão uma cópia das mensagens enviadas em seu bucket de armazenamento na nuvem.

Para selecionar canais:

1. Acesse **Configurações** > **Arquivamento de mensagens**.
2. Selecione seus canais.
3. Selecione **Salvar alterações**.

![A página de Arquivamento de mensagens tem três canais para seleção: E-mail, Push e SMS.]({% image_buster /assets/img/message_archiving_settings.png %})

{% alert note %}
Se você não vir o **envio de mensagens** em **Configurações**, confirme se sua empresa comprou e ativou o arquivamento de mensagens.
{% endalert %}

## Referências de arquivos

As seguintes são referências à carga útil JSON entregue ao seu bucket de armazenamento em nuvem cada vez que uma mensagem é enviada. Consulte nosso repositório de exemplos de código para obter [arquivos de amostra de arquivo de mensagens](https://github.com/braze-inc/braze-examples/tree/main/message-archiving).

{% tabs %}
{% tab Email %}

```json
{
  "version": 1, //numerical version of the JSON structure
  "to": ToAddress, ("customer@example.com")
  "subject": SubjectLine ("20% off coupon inside!"),
  "from_name": DisplayName ("Braze"),
  "from_address": FromAddress ("no-reply@braze.com"),
  "html_body": HtmlBody,
  "plaintext_body": PlainTextBody,
  "amp_body": AMPEmailBody,
  "extras": Hash of key-value pairs from Email Extras configured in the email editor,
  "headers": HashOfHeaders,
  "sent_at": UnixTimestamp,
  "dispatch_id": DispatchIdFromBraze,
  "campaign_id": CampaignApiId, // may not be available
  "canvas_id": CanvasApiId, // may not be available
  "canvas_step_id": CanvasStepApiId, // may not be available
  "canvas_variation_id" : CanvasVariationApiId, // may not be available
  "message_variation_id": MessageVariationApiId, // may not be available,
  "attachments": Array of JSON Objects containing 'bytes' and 'file_name', // may not be available
  "user_id": String,
  "campaign_name": String, // will only be available if the message is from a campaign
  "canvas_name": String, // will only be available if the message is from Canvas
  "canvas_step_name": String, // will only be available if the message is from a Canvas
  "external_id": String
}
```

O campo `extras` contém os pares chave-valor configurados no campo **Email Extras** ao compor um e-mail no editor de HTML. Os extras de e-mail funcionam para todos os provedores de serviços de e-mail (incluindo SendGrid e Sparkpost) e estão incluídos nas mensagens arquivadas, independentemente de qual provedor é utilizado. Para mais informações sobre como configurar os extras de e-mail, veja [Como criar uma campanha de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#adding-email-extras). Para enviar dados de volta ao Currents, consulte [Extras de mensagens]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras/).

![]({% image_buster /assets/img_archive/email_extras.png %}){: style="max-width:60%" }

{% endtab %}
{% tab SMS/MMS %}

```json
{
  "version": 1 //numerical version of the JSON structure
  "to": PhoneNumber, ("+15555555555"),
  "body": Body ("Hi there!"),
  "subscription_group": SubscriptionGroupExternalId,
  "provider": StringOfProviderName,
  "media_urls": ArrayOfString, // indicates a message is MMS
  "sent_at": UnixTimestamp,
  "dispatch_id": DispatchIdFromBraze,
  "campaign_id": CampaignApiId, // may not be available
  "canvas_id": CanvasApiId, // may not be available
  "canvas_step_id": CanvasStepApiId, // may not be available
  "canvas_variation_id" : CanvasVariationApiId, // may not be available
  "message_variation_id": MessagVariationApiId, // may not be available
  "user_id": String,
  "campaign_name": String, // will only be available if the message is from a campaign
  "canvas_name": String, // will only be available if the message is from Canvas
  "canvas_step_name": String, // will only be available if the message is from a Canvas
  "external_id": String
}
```

{% endtab %}
{% tab Push %}

```json
{
  "version": 1, //numerical version of the JSON structure
  "to": PushToken,
  "payload": JsonOfEntirePushPayload,
  "platform": one of "android_push" | "ios_push" | "kindle_push" | "web_push",
  "app_id": ApiKeyOfApp,
  "sent_at": UnixTimestamp,
  "dispatch_id": DispatchIdFromBraze,
  "campaign_id": CampaignApiId, // may not be available
  "canvas_id": CanvasApiApiId, // may not be available
  "canvas_step_id": CanvasStepApiId, // may not be available
  "canvas_variation_id" : CanvasVariationApiId, // may not be available
  "message_variation_id": MessagVariationApiId, // may not be available
  "user_id": String,
  "campaign_name": String, // will only be available if the message is from a campaign
  "canvas_name": String, // will only be available if the message is from a Canvas
  "canvas_step_name": String, // will only be available if the message is from a Canvas
  "external_id": String
}
```

{% endtab %}
{% endtabs %}

## Perguntas frequentes

### Quais modelos não estão incluídos na carga útil?

As modificações feitas depois que a mensagem sair do Braze não serão refletidas no arquivo salvo em seu bucket de armazenamento em nuvem. Isso inclui modificações feitas por nossos parceiros de entrega de e-mail, como o envolvimento de links para rastreamento de cliques e a inserção de pixels de rastreamento.

### O que são mensagens sob o valor "unassociated" (não associado) na jornada da campanha?

Quando uma mensagem é enviada fora de uma campanha ou do Canva, a ID da campanha no nome do arquivo será "desassociada". Isso acontecerá quando você enviar mensagens de teste do dashboard, quando a Braze enviar respostas automáticas de SMS/MMS ou quando mensagens enviadas através da API não especificarem um ID de campanha.

### Como faço para obter mais informações sobre esse envio?

Você pode usar o `external_id` ou `dispatch_id` em conjunto com o `user_id` para cruzar a mensagem template com nossos dados do Currents para encontrar mais informações, como o timestamp em que foi entregue, se o usuário abriu ou clicou na mensagem, e mais.

### Como as novas tentativas são tratadas?

Se seu bucket de armazenamento em nuvem não puder ser acessado, o Braze tentará novamente até três vezes com um [jitter de backoff](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/#Jitter). As novas tentativas de limite de frequência do AWS S3 são tratadas automaticamente pela Braze.

### O que acontecerá se minhas credenciais forem inválidas?

Se suas credenciais de armazenamento em nuvem se tornarem inválidas em algum momento, o Braze não poderá salvar nenhuma mensagem em seu bucket de armazenamento em nuvem, e essas mensagens serão perdidas. Recomendamos configurar suas [preferências de notificação]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/notification_preferences/) para Amazon Web Services, Google Cloud Services ou Azure (Microsoft Cloud Services) para que você receba alertas sobre quaisquer problemas de credenciais.

### Por que o registro de data e hora do meu arquivo `sent_at` é ligeiramente diferente do registro de data e hora enviado no Currents?

A cópia renderizada é feita upload imediatamente antes de enviar a mensagem ao usuário. Devido aos tempos de upload do armazenamento em nuvem, pode haver uma postergação de alguns segundos entre o registro de data e hora `sent_at` na cópia renderizada e a hora real em que o envio ocorre.

### Posso criar um novo bucket especificamente para arquivação de mensagens enquanto mantenho o bucket atual usado para dados do Currents?

Não. Se você estiver interessado em criar esses buckets específicos, envie [feedback sobre o produto]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).

### Os dados arquivados são gravados em uma pasta dedicada em um bucket existente, semelhante à forma como as exportações de dados do Currents são estruturadas?

Os dados são gravados em uma seção `sent_messages` do bucket. Consulte [Como funciona](#how-it-works) para mais detalhes.

### Posso usar a arquivação de mensagens para agrupar arquivos em diferentes espaços de trabalho?

Não. O arquivamento de mensagens não suporta agrupar arquivos com base em espaços de trabalho. Em vez disso, você pode determinar a qual espaço de trabalho o ID da campanha ou da etapa do canva pertence e, em seguida, agrupá-los com base nessa informação.
