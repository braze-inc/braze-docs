---
nav_title: Adjust
article_title: Adjust
alias: /partners/adjust/
description: "Esse artigo de referência descreve a parceria entre o Braze e a Adjust, uma empresa de análise e atribuição móvel que permite importar dados de atribuição de instalação não orgânica para segmentar de forma mais inteligente suas campanhas de ciclo de vida."
page_type: partner
search_tag: Partner

---

# Adjust

> [A Adjust](https://www.adjust.com/) é uma empresa de atribuição e análise de dados móveis que combina a atribuição de fontes de publicidade com análises avançadas para obter um quadro abrangente de business intelligence.

_Essa integração é mantida pela Adjust._

## Sobre a integração

A integração do Braze e da Adjust permite importar dados de atribuição de instalação não orgânica para segmentar de forma mais inteligente suas campanhas de ciclo de vida.

## Pré-requisitos

| Requisito | Descrição |
|---|---|
| Ajustar conta | É necessário ter uma conta Adjust para aproveitar essa parceria. |
| App para iOS ou Android | Essa integração é compatível com os apps para iOS e Android. Dependendo de sua plataforma, os trechos de código podem ser necessários em seu aplicativo. Consulte os detalhes sobre esses requisitos na etapa 1 do processo de integração. |
| Ajustar SDK | Além do SDK da Braze obrigatório, você deve instalar o [SDK da Adjust](https://dev.adjust.com/en/sdk). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: Mapear IDs de dispositivos

#### Android

Se você tiver um app Android, deve passar um ID de dispositivo Braze único para o Adjust. Esse ID pode ser definido no método `addGlobalPartnerParameter()` do SDK da Adjust. O snippet de código a seguir deve ser incluído antes da inicialização do SDK em `Adjust.initSdk.`

```
Adjust.addGlobalPartnerParameter("braze_device_id", Braze.getInstance(getApplicationContext()).getDeviceId()););
```

#### iOS

<!--
{% alert important %}
Prior to February 2023, our Adjust attribution integration used the IDFV as the primary identifier to match iOS attribution data. Braze customers don't need to use Objective-C to fetch the Braze `device_id` and send it to Adjust upon installation as there will be no service disruption. 
{% endalert%}

For those using the Swift SDK v5.7.0+, if you wish to continue using IDFV as the mutual identifier, you must ensure that the `useUUIDAsDeviceId` field is set to `false` so there is no disruption of the integration. 

If set to `true`, you must implement the iOS device ID mapping for Swift to pass the Braze `device_id` to Adjust upon app installation in order for Braze to match iOS attributions appropriately.
--->

{% tabs local %}
{% tab Objective C %}

Se você tiver um app para iOS, seu IDFV será coletado pelo Adjust e enviado ao Braze. Esse ID será então mapeado para um ID de dispositivo exclusivo no Braze.

O Braze ainda armazenará os valores de IDFA dos usuários que fizeram a aceitação se você estiver coletando o IDFA com o Braze, conforme descrito em nosso [Guia de atualização do iOS]({{site.baseurl}}/developer_guide/platforms/swift/ios_18/). Caso contrário, o IDFV será usado como um identificador de fallback para mapear os usuários.

{% endtab %}
{% tab Swift %}

Se você tiver um app para iOS, poderá aceitar a coleta de IDFV definindo o campo `useUUIDAsDeviceId` como `false`. Se não for definido, a atribuição do iOS provavelmente não será mapeada com precisão do Adjust para a Braze. Para saber mais, consulte [Coleta de IDFV]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift).

{% endtab %}
{% endtabs %}

{% alert note %}
Se estiver planejando enviar eventos pós-instalação da Adjust para a Braze, será necessário: <br><br>1) Anexar `external_id` como um parâmetro de sessão e evento no SDK da Adjust. Para o encaminhamento de eventos de receita, você também precisará configurar `product_id` como um parâmetro para eventos. Visite [a documentação da Adjust](https://github.com/adjust/sdks) para saber mais sobre a definição de parâmetros de parceiros para encaminhamento de eventos.<br><br>2) Gerar uma nova chave de API para inserir na Adjust. Isso pode ser feito selecionando o botão **Generate API Key (Gerar chave de API** ) encontrado na página Adjust partner (Ajustar parceiro) no dashboard do Braze.
{% endalert %}

### Etapa 2: Obter a chave de importação de dados do Braze

Na Braze, navegue até **Integrações** > **Parceiros de tecnologia** e selecione **Adjust**. 

Aqui você encontra o endpoint REST e gera sua chave de importação de dados da Braze. Depois que a chave é gerada, você pode criar outra ou invalidar uma existente. A chave de importação de dados e o ponto de extremidade REST são usados na próxima etapa ao configurar um postback no dashboard do Adjust.<br><br>![Esta imagem mostra a caixa "Data Import for Install Attribution" (Importação de dados para atribuição de instalação) encontrada na página de tecnologia Adjust (Ajustar). Nessa caixa, você verá a chave de importação de dados e o ponto de extremidade REST.]({% image_buster /assets/img/attribution/adjust.png %}){: style="max-width:90%;"}

### Etapa 3: configurar a Braze na Adjust

1. No dashboard do Adjust, navegue até **Configurações do app** e navegue até **Configuração de parceiros** e, em seguida, **Adicionar parceiros**.
2. Selecione **Braze (formerly Appboy)** (Braze [antes Appboy]) e forneça a chave de importação de dados e o endpoint REST da Braze.
3. Clique em **Save & Close (Salvar e fechar**).

### Etapa 4: Confirmar a integração

Depois que a Braze receber os dados de atribuição da Adjust, o indicador de status da conexão na página de parceiros de tecnologia da Adjust na Braze mudará de "Não conectado" para "Conectado". Um registro de data e hora da última solicitação bem-sucedida também será incluído. 

Observe que isso não acontecerá até recebermos dados sobre uma instalação atribuída. Instalações orgânicas, que devem ser excluídas do postback da Adjust, são ignoradas pela nossa API e não são contadas ao determinar se uma conexão bem-sucedida foi estabelecida.

## Campos de dados disponíveis

Supondo que você configure sua integração conforme sugerido, o Braze mapeará os dados do Adjust para os filtros de segmento, conforme descrito na tabela a seguir.

| Ajustar o campo de dados | Filtro de segmento de Braze |
| --- | --- |
| `{network_name}` | Fonte atribuída |
| `{campaign_name}` | Campanha de atribuição |
| `{adgroup_name}` | Grupo de anúncios atribuídos |
| `{creative_name}` | Anúncio atribuído |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Dados de atribuição do Facebook e do X (antigo Twitter)

Os dados de atribuição para campanhas do Facebook e do X (antigo Twitter) não estão disponíveis por meio de nossos parceiros. Essas fontes de mídia não permitem que seus parceiros compartilhem dados de atribuição com terceiros e, portanto, nossos parceiros não podem enviar esses dados para a Braze.

## Ajuste os URLs de rastreamento de cliques no Braze (opcional)

O uso de links de rastreamento de cliques em suas campanhas do Braze permitirá que você veja facilmente quais campanhas estão gerando instalações de aplicativos e reengajamento. Como resultado, você poderá medir seus esforços de marketing de forma mais eficaz e tomar decisões baseadas em dados sobre onde investir mais recursos para obter o máximo de ROI.

Para começar a usar os links de rastreamento de cliques da Adjust, visite sua [documentação](https://help.adjust.com/tracking/attribution/tracker-urls). Você pode inserir os links de rastreamento de cliques do Adjust diretamente em suas campanhas do Braze. A Adjust usará então suas [metodologias de atribuição probabilística](https://www.adjust.com/blog/attribution-compatible-with-ios14/) para atribuir o usuário que clicou no link. Recomendamos anexar seus links de rastreamento do Adjust com um identificador de dispositivo para melhorar a precisão das atribuições de suas campanhas no Braze. Isso atribuirá de forma determinística o usuário que clicou no link.

{% tabs local %}
{% tab Android %}
Para Android, a Braze permite que os clientes façam a aceitação da [coleta do ID de publicidade do Google (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/sdk_integration#google-advertising-id). O GAID também é coletado nativamente pela integração SDK da Adjust. Você pode incluir o GAID nos seus links de rastreamento de cliques da Adjust utilizando a seguinte lógica Liquid:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Para iOS, tanto o Braze quanto o Adjust coletam automaticamente o IDFV de forma nativa por meio de nossas integrações de SDK. Isso pode ser usado como identificador do dispositivo. É possível incluir o IDFV em seus links de rastreamento de cliques do Adjust utilizando a seguinte lógica Liquid:

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
**Essa recomendação é puramente opcional**<br>
Se você atualmente não usa nenhum identificador de dispositivo - como o IDFV ou GAID - em seus links de rastreamento de cliques, ou não planeja usar no futuro, a Adjust ainda será capaz de atribuir esses cliques por meio de sua modelagem probabilística.
{% endalert %}


