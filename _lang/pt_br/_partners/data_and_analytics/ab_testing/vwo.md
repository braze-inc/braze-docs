---
nav_title: VWO
article_title: Integração do VWO com o Braze
description: "Saiba como integrar o VWO ao Braze."
alias: /partners/vwo/
page_type: partner
search_tag: Partner
---

# VWO

> [O VWO](https://vwo.com/) é uma poderosa plataforma de experimentação que ajuda as marcas a aprimorar as principais métricas de negócios, ativando as equipes para executar programas de otimização de conversão com o apoio de dados de comportamento do cliente. Com o VWO, você pode unificar os dados do cliente, obter insights comportamentais, criar hipóteses, executar Testes A/B em várias plataformas (servidor, Web e móvel), implementar recursos, personalizar experiências e otimizar toda a jornada do cliente.

Ao integrar o VWO com o Braze, você pode aproveitar os dados de experimentos do VWO para criar segmentos direcionados e fornecer campanhas personalizadas.

## Pré-requisitos

| Requisito     | Descrição |
|-----------------|-------------|
| Conta VWO     | Uma conta VWO com acesso a dados de experimentação. |
| Conta Braze   | Uma conta Braze ativa com o [Braze Web SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) integrado em sua página da Web. Você também precisará ativar a segmentação de propriedades de eventos. Para solicitá-lo, consulte [Considerações](#request-event-property-segmentation). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Integração do VWO com o Braze

### Etapa 1: Ativar a integração do Braze no VWO

1. Faça o registro em sua conta VWO.
2. No dashboard do VWO, acesse **Configurações > Integrações**. Aqui, você pode ativar as integrações no nível do espaço de trabalho, o que aplica a integração a todas as campanhas de teste futuras por padrão.

   ![Configuração de integração do VWO]({% image_buster /assets/img/vwo/vwo1_settings.png %})

4. Selecione a integração do Braze para ativá-la.
5. Opcionalmente, você pode ativar a integração do Braze para quaisquer campanhas existentes. Para fazer isso, selecione uma campanha, acesse **Configuration > Integrations (Configuração > Integrações**) e ative o Braze.

   ![Ativar a integração do Braze]({% image_buster /assets/img/vwo/vwo2_enable_braze.png %})

6. Depois de ativar a capacitação, o VWO começará a enviar dados de experimentos para o Braze no nível da campanha.

### Etapa 2: Criar um segmento no Braze com propriedades de evento VWO

1. No dashboard do Braze, selecione **Segments** > **\+ Create Segment**( **Segmentos** **\+ Criar Segmento**).
3. Na janela **Create Segment (Criar segmento** ), insira um nome para o segmento e, em seguida, **Create Segment (Criar segmento**).
4. Em seu segmento recém-criado, selecione **Filters (Filtros** ) > **Add Filter (Adicionar filtro**) e escolha **Custom Event (Evento personalizado** ) como o tipo de filtro.
6. No menu suspenso do filtro, procure por **VWO**.
7. Selecione a propriedade VWO relevante e especifique o valor necessário.
8. Se necessário, configure o número de visitas e o período de tempo. Quando terminar, selecione **Salvar**.

   ![Braze Segment Creation]({% image_buster /assets/img/vwo/vwo3_braze_segment.png %})

9. Para visualizar o número de usuários que correspondem aos seus critérios de segmento, selecione **Calculate Exact Statistics (Calcular estatísticas exatas**).

   ![Estatísticas do segmento de Braze]({% image_buster /assets/img/vwo/vwo4_braze_segment_calculate_size.png %})

## Fluxo de dados

O VWO envia os dados do experimento da campanha para o Braze como um evento personalizado usando o seguinte formato:

- **Nome do evento:** VWO
- **Propriedades do evento:** `vwo_campaign_name`, `vwo_variation_name`

{% alert tip %}
Essas propriedades de eventos personalizados também podem ser usadas para segmentação e direcionamento.
{% endalert %}

## Considerações

### Segmentação de propriedades de eventos de solicitação

Antes de poder usar a segmentação de propriedades de eventos, você precisará ativá-la no Braze. Use o modelo a seguir para entrar em contato com o CSM da Braze ou com a equipe de suporte para obter acesso.

   <table>
   <thead>
      <tr>
         <th>Campo</th>
         <th>Informações</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td><strong>Assunto</strong></td>
         <td>Solicitação para ativar a segmentação da propriedade do evento para a integração do VWO</td>
      </tr>
      <tr>
         <td><strong>Corpo</strong></td>
         <td>
         Olá, equipe do Braze,<br><br>
         Gostaríamos de ativar a segmentação de propriedades de eventos para eventos enviados de nossa integração VWO&lt;>Braze. Aqui estão os detalhes:<br><br>
         - <strong>Nome do evento:</strong> VWO<br>
         - <strong>Propriedades do evento:</strong> <code>vwo_campaign_name</code>, <code>vwo_variation_name</code><br><br>
         Confirme quando as propriedades tiverem sido ativadas em nossa conta.<br><br>
         Obrigada.
         </td>
      </tr>
   </tbody>
   </table>
   {: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Pontos de dados do Braze

O evento personalizado enviado do VWO para o Braze - incluindo quaisquer propriedades de evento ativadas para segmentação - consumirá pontos de dados em sua instância do Braze.

### Limitações

Atualmente, essa integração não oferece suporte à sincronização em tempo real dos dados de teste. Pode haver uma postergação de até 15 minutos para que os dados do teste apareçam no Braze.

## Solução de problemas

Se não estiver vendo os dados do VWO no Braze:

1. Clique com o botão direito do mouse na página em que sua campanha de teste está sendo executada e selecione **Inspecionar elemento**.
2. Na guia **Network (Rede** ), procure por **Braze** para filtrar as chamadas de rede para o Braze.
3. As chamadas de rede são preenchidas à medida que a página é carregada. Você pode recarregar a página para visualizar as chamadas de rede.
4. Selecione uma chamada de rede para ver mais detalhes.
5. Acesse a seção **Carga útil** da **solicitação** na guia **Carga**, onde é possível encontrar eventos: com o nome: **ce**, indicando Evento personalizado.
6. Expanda 0: e data: para ver n: "VWO" (nome do evento personalizado) e p: {vwo_campaign_name: "<your vwo campaign name>", vwo_variation_name: "<variation name>"}. Isso indica que os valores estão sendo empurrados pelo VWO para o Braze.

 ![Solução de problemas do Braze]({% image_buster /assets/img/vwo/vwo5_troubleshooting.png %})

Para obter suporte adicional, entre em contato com o gerente de sucesso do cliente da VWO.
