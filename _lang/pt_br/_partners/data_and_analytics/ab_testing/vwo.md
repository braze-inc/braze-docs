---
nav_title: VWO
article_title: Integre o VWO com o Braze
description: "Aprenda como integrar o VWO com o Braze."
alias: /partners/vwo/
page_type: partner
search_tag: Partner
---

# VWO

> [VWO](https://vwo.com/) é uma poderosa plataforma de experimentação que ajuda as marcas a melhorar métricas de negócios importantes, permitindo que as equipes executem programas de otimização de conversão apoiados por dados de comportamento do cliente. Com o VWO, você pode unificar dados de clientes, obter insights comportamentais, construir hipóteses, realizar testes A/B em várias plataformas (servidor, web e mobile), lançar recursos, personalizar experiências e otimizar toda a jornada do cliente.

Ao integrar o VWO com o Braze, você pode aproveitar os dados de experimentos do VWO para criar segmentos direcionados e entregar campanhas personalizadas.

## Pré-requisitos

| Requisito     | Descrição |
|-----------------|-------------|
| Conta do VWO     | Uma conta do VWO com acesso a dados de experimentação. |
| Conta Braze   | Uma conta ativa do Braze com o [Braze Web SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) integrado em sua página da web. Você também precisará da segmentação de propriedades de eventos ativada. Para solicitá-la, veja [Considerações](#request-event-property-segmentation). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Integrando o VWO com o Braze

### Etapa 1: Ative a integração do Braze no VWO

1. Faça login na sua conta do VWO.
2. No painel do VWO, acesse **Configurações > Integrações**. Aqui, você pode ativar integrações no nível do espaço de trabalho, o que aplica a integração a todas as futuras campanhas de teste por padrão.

   ![Configuração de Integração do VWO]({% image_buster /assets/img/vwo/vwo1_settings.png %})

4. Selecione a integração do Braze para ativá-la.
5. Opcionalmente, você pode ativar a integração do Braze para quaisquer campanhas existentes. Para fazer isso, selecione uma campanha, depois acesse **Configuração > Integrações**, e ative o Braze.

   ![Ativar Integração Braze]({% image_buster /assets/img/vwo/vwo2_enable_braze.png %})

6. Depois de ativar a integração, o VWO começará a enviar dados de experimentos para o Braze no nível da campanha.

### Etapa 2: Crie um segmento no Braze com propriedades de evento do VWO

1. No painel do Braze, selecione **Segmentos** > **\+ Criar Segmento**.
3. Na janela **Criar Segmento**, insira um nome para o segmento, depois **Criar Segmento**.
4. No seu segmento recém-criado, selecione **Filtros** > **Adicionar Filtro**, depois escolha **Evento Personalizado** como o tipo de filtro.
6. No dropdown de filtro, procure por **VWO**.
7. Selecione a propriedade VWO relevante e especifique o valor necessário.
8. Se necessário, configure o número de visitas e o período de tempo. Quando terminar, selecione **Salvar**.

   ![Criação de Segmento Braze]({% image_buster /assets/img/vwo/vwo3_braze_segment.png %})

9. Para ver o número de usuários que correspondem aos critérios do seu segmento, selecione **Calcular Estatísticas Exatas**.

   ![Estatísticas de Segmento Braze]({% image_buster /assets/img/vwo/vwo4_braze_segment_calculate_size.png %})

## Fluxo de dados

O VWO envia os dados do experimento da campanha para o Braze como um evento personalizado usando o seguinte formato:

- **Nome do Evento:** VWO
- **Propriedades do Evento:** `vwo_campaign_name`, `vwo_variation_name`

{% alert tip %}
Essas propriedades de evento personalizado também podem ser usadas para segmentação e direcionamento.
{% endalert %}

## Considerações

### Solicitar segmentação de propriedades de evento

Antes que você possa usar a segmentação de propriedades de evento, você precisará ativá-la no Braze. Use o seguinte modelo para contatar seu CSM do Braze ou a equipe de suporte para acesso.

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
         <td>Solicitação para Ativar a Segmentação de Propriedades de Evento para Integração VWO</td>
      </tr>
      <tr>
         <td><strong>Corpo</strong></td>
         <td>
         Olá, equipe Braze,<br><br>
         Gostaríamos de ativar a segmentação de propriedades de evento para eventos enviados da nossa integração VWO&lt;>Braze. Aqui estão os detalhes:<br><br>
         - <strong>Nome do Evento:</strong> VWO<br>
         - <strong>Propriedades do Evento:</strong> <code>vwo_campaign_name</code>, <code>vwo_variation_name</code><br><br>
         Por favor, confirme assim que as propriedades forem ativadas em nossa conta.<br><br>
         Obrigada.
         </td>
      </tr>
   </tbody>
   </table>
   {: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Pontos de dados Braze

O evento personalizado enviado do VWO para o Braze—incluindo quaisquer propriedades de evento ativadas para segmentação—registrará pontos de dados em sua instância Braze.

### Limitações

Atualmente, essa integração não suporta a sincronização em tempo real de dados de teste. Pode haver uma postergação de até 15 minutos para que os dados de teste apareçam no Braze.

## Solução de problemas

Se você não estiver vendo dados do VWO no Braze:

1. Clique com o botão direito na página, onde sua campanha de teste está rodando e selecione **Inspecionar Elemento**.
2. Na aba **Rede**, procure por **Braze** para filtrar as chamadas de rede para o Braze.
3. As chamadas de rede são preenchidas à medida que a página carrega. Você pode recarregar a página para visualizar as chamadas de rede.
4. Selecione uma chamada de rede para ver mais detalhes.
5. Acesse a seção **Payload da Solicitação** na aba **Carga Útil**, onde você pode encontrar eventos: que têm nome: **ce**, indicando Evento Personalizado.
6. Expanda 0: e dados: para ver n: “VWO” (nome do Evento Personalizado) e p: {vwo_campaign_name: “<your vwo campaign name>”, vwo_variation_name: “<variation name>”. Esses indicam que os valores estão sendo enviados pelo VWO para o Braze.

 ![Solução de Problemas do Braze]({% image_buster /assets/img/vwo/vwo5_troubleshooting.png %})

Para suporte adicional, entre em contato com seu gerente de sucesso do cliente do VWO.
