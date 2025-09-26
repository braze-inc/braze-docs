---
nav_title: Olho de águia
article_title: Olho de águia
description: Saiba como integrar o Eagle Eye ao Braze.
alias: /partners/eagle_eye/
page_type: partner
search_tag: Partner
---

# Olho de águia

> [A Eagle Eye](https://eagleeye.com/) é uma empresa líder em SaaS e tecnologia de IA que ativa marcas de varejo, viagens e hospitalidade para conquistar a fidelidade de seus clientes finais, potencializando suas atividades de marketing de consumo em tempo real, omnicanal e personalizado, em escala.

_Essa integração é mantida pela Eagle Eye._

## Visão geral

O Eagle Eye Connect é uma integração bidirecional entre o Braze e o AIR que capacita as marcas a ativar dados de fidelidade e promocionais diretamente no Braze. Os clientes podem emitir recompensas no AIR para os consumidores que entram em um público no AIR.  Isso permite que os profissionais de marketing personalizem o engajamento dos clientes usando dados em tempo real, como saldos de pontos, promoções e atividades de recompensas.

## Casos de uso

- Dispare campanhas do Braze com base em eventos de fidelidade, como limites de pontos ou recompensas obtidas.
- Enriqueça os perfis de usuários do Braze com dados de fidelidade em tempo real para ativar um direcionamento mais personalizado.
- Rastreamento e geração de relatórios sobre a eficácia da campanha vinculada a recompensas.
- Emita recompensas no AIR quando os usuários entrarem em campanhas no Braze.

## Pré-requisitos

| Requisito              | Descrição |
|--------------------------|-------------|
| Conta Eagle Eye AIR    | Você precisa de uma conta ativa do Eagle Eye AIR para aproveitar essa parceria. Para começar, entre em contato com a equipe de Parcerias da Eagle Eye em [partnerships@eagleeye.com](mailto:partnerships@eagleeye.com). |
| Chave da API REST do Braze       | Uma chave da API REST da Braze com permissões `users.track`. <br><br>Isso pode ser criado no dashboard do Braze em **Configurações > Chaves de API**. |
| Endpoint REST  do Braze      | [Sua URL de endpoint REST.](https://www.braze.com/docs/api/basics/#endpoints) Seu endpoint depende do URL do Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Saída vs. entrada

As tabelas a seguir descrevem os dois tipos de integrações suportadas entre o Braze e o Eagle Eye AIR. O Eagle Eye Connect é o middleware que ativa a troca de dados entre o AIR e os sistemas de parceiros, como o Braze. Para saber mais, consulte a [documentação sobre Braze da Eagle Eye](https://developer.eagleeye.com/docs/braze).

{% tabs local %}
{% tab de saída %}
<table>
  <thead>
    <tr>
      <th>Direção</th>
      <th>Iniciado por</th>
      <th>Fluxo de dados</th>
      <th>Finalidade</th>
      <th>Exemplo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Eagle Eye → Braze</td>
      <td>Olho de águia</td>
      <td>Para Braze API</td>
      <td>
        Envie dados de fidelidade para os perfis de usuário do Braze como atributos personalizados por meio de eventos personalizados. No Braze, os dados ingeridos podem ser usados para:
        <ul>
          <li>segmentar usuários, disparar campanhas</li>
          <li>personalizar envios de mensagens</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Envio de pontos de fidelidade ou status de nível para o Braze (<code>ee_loyalty.points.current</code>, <code>ee_loyalty.tier.tierId</code>)</li>
          <li>Atualização do perfil de um usuário quando ele recebe ou resgata um cupom.</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation"}
{% endtab %}

{% tab de entrada %}
<table>
  <thead>
    <tr>
      <th>Direção</th>
      <th>Iniciado por</th>
      <th>Fluxo de dados</th>
      <th>Finalidade</th>
      <th>Exemplo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Braze → Eagle Eye</td>
      <td>Braze</td>
      <td>Para a API Eagle Eye via webhook</td>
      <td>
        Quando um consumidor entra em um público no Braze a partir de qualquer fonte, o Braze pode disparar um webhook do Braze para o EE Connect, permitindo que o EE emita uma recompensa (cupom ou pontos)<br><br>
        Após a conclusão da ação no AIR, o Braze receberia um evento de saída do AIR.
      </td>
      <td>
        <ul>
          <li>Recompensas (cupom ou pontos) são emitidas a um consumidor por sua adesão ao programa de fidelidade</li>
          <li>As recompensas são emitidas para um consumidor que teve uma entrega atrasada</li>
          <li>Recompensas de aniversário</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation"}
{% endtab %}
{% endtabs %}

{% alert tip %}
Para saber mais sobre os dados personalizados que podem ser enviados ao Braze como atributos ou eventos personalizados, consulte a [documentação do Braze do Eagle Eye](https://developer.eagleeye.com/docs/braze#data-model).
{% endalert %}

## Visão geral da integração

Atualmente, os conectores de entrada e saída só podem ser configurados via API com suporte direto da equipe do Eagle Eye - no entanto, uma opção de autoatendimento dentro do dashboard do AIR está a caminho!

Ao trabalhar com a sua equipe Eagle Eye, você concluirá o seguinte:

### Etapa 1: Fornecer detalhes de configuração

Primeiro, você fornecerá os seguintes detalhes à sua equipe Eagle Eye:

| O usuário fornece            | Descrição |
|------------------------|-------------|
| Credenciais da API do Braze  | Compartilhe o endpoint Braze REST, o identificador do app e a chave de API com segurança com o seu contato Eagle Eye. |
| Correspondência de identificadores    | Determine e compartilhe o identificador de usuário principal para atualizações de perfil que é comum no AIR e no Braze, como ID externo ou e-mail. |
| Chave de autenticação               | Determine e compartilhe uma chave de autenticação secreta para cada conector de entrada e saída. |
| Código da moeda          | Compartilhe o código de moeda de 3 dígitos para exibir valores monetários de compra (e.g., USD). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Etapa 2: Configurar o Eagle Eye Connect 

A equipe do Eagle Eye configurará o Eagle Eye Connect usando os detalhes fornecidos, juntamente com as credenciais exclusivas do AIR API e os eventos de saída para os conectores.

### Etapa 3: Configurar ações de comportamento social no AIR

Em seguida, você configurará uma ou mais ações de comportamento social no AIR com referências de ação exclusivas para emitir pontos ou cupons.

### Etapa 4: Configure Braze

No Braze, você concluirá o seguinte:

- Configure campanhas no Braze para emitir recompensas no AIR  
- Configurar quaisquer comunicações para os consumidores quando os eventos do AIR forem recebidos

### Etapa 5: Teste sua integração

Faça chamadas API no AIR e observe o fluxo de dados do evento em seu Braze workspace.Validate dados recebidos do AIR e confirme se as atribuições estão sendo atualizadas conforme o esperado.  

Além disso, adicione usuários aos públicos e confirme se as recompensas são emitidas no AIR.

### Etapa 6: Lançamento para produção

Depois que o teste for bem-sucedido, a integração poderá entrar em operação para enviar dados continuamente ao Braze. As mesmas etapas de configuração são necessárias para ambientes de produção no AIR e no Braze

Entre em contato com o seu gerente de sucesso do cliente Eagle Eye para que um recurso seja atribuído a você, para configurar o EE Connect.

## Suporte

Para obter suporte de integração ou solução de problemas, entre em contato com a equipe de suporte da Eagle Eye em [support@eagleeye.com](mailto:support@eagleeye.com).
