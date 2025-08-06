---
nav_title: Singular
article_title: Singular
alias: /partners/singular/
description: "Esse artigo de referência descreve a parceria entre o Braze e a Singular, uma plataforma unificada de análise de dados de marketing que permite que você importe dados de atribuição de instalação paga."
page_type: partner
search_tag: Partner

---

# Singular

> Como uma plataforma de análise de dados de marketing unificada, a Singular oferece atribuição, agregação de custos, análise de dados de marketing, relatórios criativos e automação de fluxo de trabalho.

_A integração é mantida pela Singular._

## Sobre a integração

A integração entre o Braze e o Singular permite importar dados de atribuição de instalação paga para segmentar de forma inteligente suas campanhas de ciclo de vida.

## Pré-requisitos

| Requisito | Descrição |
|---|---|
| Conta da Singular | É necessário ter uma conta na Singular para aproveitar essa parceria. |
| app iOS ou Android | Essa integração é compatível com os apps para iOS e Android. Dependendo de sua plataforma, os trechos de código podem ser necessários em seu aplicativo. Consulte detalhes sobre esses requisitos na etapa 1 do processo de integração. |
| SDK da Singular | Além do SDK da Braze obrigatório, você deve instalar o [SDK da Singular](https://support.singular.net/hc/en-us/articles/360037640172-Getting-Started-with-the-Singular-SDK-S2S). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: Mapear IDs de usuários

#### Android

Se você tiver um app para Android, precisará incluir o seguinte trecho de código, que passa um ID de usuário Braze exclusivo para o Singular.

```java
String appboyDeviceId = Braze.getInstance(context).getDeviceId();
SingularConfig config = new SingularConfig("SDK KEY", "SDK SECRET")
  .withGlobalProperty(“brazeDeviceID”, appboyDeviceId, true);
```
#### iOS

{% alert important %}
Antes de fevereiro de 2023, nossa integração de atribuição Singular usava o IDFV como o identificador principal para corresponder aos dados de atribuição do iOS. Não é necessário que os clientes da Braze que usam Objective-C busquem o `device_id` da Braze e o enviem para a Singular na instalação, pois não haverá interrupção do serviço.
{% endalert%}

Para quem usa o SWIFT SDK v5.7.0+, se você deseja continuar usando o IDFV como o identificador mútuo, confirme se o campo `useUUIDAsDeviceId` está definido como `false` para que não haja interrupção da integração. 

Se estiver definido como `true`, implemente o mapeamento de ID do dispositivo iOS para SWIFT a fim de passar o `device_id` da Braze para a Singular na instalação do app para que a Braze possa corresponder adequadamente as atribuições do iOS.

{% tabs local %}
{% tab Objective C %}

```objc
SingularConfig* config = [[SingularConfig
  alloc] initWithApiKey:SDKKEY andSecret:SDKSECRET];

  [config setGlobalProperty:@"brazeDeviceId" withValue:brazeDeviceId
  overrideExisting:YES];
  [Singular start:config];
```

{% endtab %}
{% tab Swift%}

```swift
config.setGlobalProperty("brazeDeviceId", withValue: brazeDeviceId, overrideExisting: true)
```

{% endtab %}
{% endtabs %}

### Etapa 2: Obtenha a chave de importação de dados do Braze

Na Braze, navegue até **Integrações de parceiros** > **Parceiros de tecnologia** e selecione **Singular**. 

Aqui você encontra o endpoint REST e gera sua chave de importação de dados da Braze. Depois que a chave é gerada, você pode criar outra ou invalidar uma existente. 

Você precisará fornecer a chave de importação de dados e o endpoint REST ao gerente de sua conta Singular para concluir a integração.<br><br>![Esta imagem mostra a caixa "Data Import for Install Attribution" (Importação de dados para atribuição de instalação) encontrada na página da tecnologia Singular. Nesta caixa, você vê a chave de importação de dados e o endpoint REST.]({% image_buster /assets/img/attribution/singular.png %}){: style="max-width:90%;"}

### Etapa 3: Confirmar a integração

Quando o Braze receber dados de atribuição da Singular, o indicador de status de conexão na página de parceiros de tecnologia da Singular no Braze mudará de "Não conectado" para "Conectado". Um carimbo de data/hora da última solicitação bem-sucedida também será incluído. 

Observe que isso não acontecerá até recebermos dados sobre uma instalação atribuída. Instalações orgânicas, que devem ser excluídas do postback da Singular, são ignoradas pela nossa API e não são contadas ao determinar se uma conexão bem-sucedida foi estabelecida.

## Dados de atribuição do Facebook e X (anteriormente Twitter)

Os dados de atribuição para campanhas do Facebook e do X (antigo Twitter) não estão disponíveis por meio de nossos parceiros. Essas fontes de mídia não permitem que seus parceiros compartilhem dados de atribuição com terceiros e, portanto, nossos parceiros não podem enviar esses dados para a Braze.

## URLs de rastreamento de cliques singulares no Braze (opcional)

Usar links de rastreamento de cliques em suas campanhas da Braze permitirá que você veja facilmente quais campanhas estão gerando instalações de apps e reengajamento. Como resultado, você será capaz de medir seus esforços de marketing de forma mais eficaz e tomar decisões baseadas em dados sobre onde investir mais recursos para obter o máximo retorno sobre o investimento.

Para começar a usar os links de rastreamento de cliques da Singular, visite sua [documentação](https://support.singular.net/hc/en-us/articles/360030934212-Singular-Links-FAQ?navigation_side_bar=true). Você pode inserir os links de rastreamento de cliques da Singular diretamente em suas campanhas do Braze. A Singular usará então suas [metodologias de atribuição probabilística](https://support.singular.net/hc/en-us/articles/115000526963-Understanding-Singular-Mobile-App-Attribution?navigation_side_bar=true) para atribuir o usuário que clicou no link. Recomendamos anexar seus links de rastreamento Singular com um identificador de dispositivo para melhorar a precisão das atribuições de suas campanhas Braze. Isso atribuirá de forma determinística o usuário que clicou no link.

{% tabs local %}
{% tab Android %}
Para Android, a Braze permite que os clientes façam a aceitação da [coleta do ID de publicidade do Google (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). O GAID também é coletado nativamente pela integração SDK da Singular. É possível incluir o GAID em seus links de rastreamento de cliques da Singular utilizando a seguinte lógica Liquid:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Para iOS, tanto a Braze quanto a Singular coletam de modo automático o IDFV nativamente através das nossas integrações de SDK. Isso pode ser usado como o identificador do dispositivo. É possível incluir o IDFV em seus links de rastreamento de cliques da Singular utilizando a seguinte lógica Liquid:

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert note %}
**Esta recomendação é puramente opcional**<br>
Se você não usa atualmente nenhum identificador de dispositivo - como o IDFV ou GAID - em seus links de rastreamento de cliques, ou não planeja fazê-lo no futuro, a Singular ainda poderá atribuir esses cliques por meio de sua modelagem probabilística.
{% endalert %}


