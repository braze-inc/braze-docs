---
nav_title: Visão geral da personalização
article_title: Visão geral da personalização
page_order: 10
description: "Este artigo de referência aborda os conceitos essenciais de personalização e extensão dos canais de envio de mensagens do SDK."
  
---

# Visão geral da personalização

> Quase tudo no Braze é totalmente personalizável! Os artigos deste Guia de Personalização mostram como refinar sua experiência no Braze por meio de uma combinação de configuração e personalização. Durante esse processo, as equipes de marketing e engenharia devem trabalhar em conjunto para coordenar exatamente como personalizar os canais de envio de mensagens do Braze.

{% alert note %}
O Braze SDK é um kit de ferramentas avançado, mas, em um nível mais alto, ele oferece duas funcionalidades importantes: ajuda a coletar e sincronizar dados de usuários entre plataformas em um perfil de usuário consolidado e também lida com canais de envio de mensagens, como mensagens no app, notificações por push e cartões de conteúdo. Os artigos do Guia de Personalização pressupõem que você já tenha passado pelo [processo de implementação do SDK]({{site.baseurl}}/developer_guide/home).
{% endalert %}

Todos os componentes da Braze são desenvolvidos para serem acessíveis, adaptáveis e personalizáveis. Por isso, recomendamos começar com os componentes padrão do `BrazeUI` e personalizá-los para atender às necessidades de sua marca e ao caso de uso. Na Braze, dividimos a personalização em três abordagens diferentes com base no esforço associado e no nível de flexibilidade fornecido. Essas abordagens são chamadas de "engatinhar", "andar" ou "correr".

- **Engatinhar:** Aproveite as opções básicas de estilo para uma implementação rápida e de baixo esforço.
- **Caminhar:** Adicione um estilo personalizado aos modelos padrão para melhor corresponder à experiência de sua marca.
- **Correr:** Personalize cada parte de seu envio de mensagens, do estilo ao comportamento e às conexões entre canais.

<style>
table {
  width: 60%;
}
table td {
    word-break: break-word;
}
</style>

{% tabs %}
{% tab Engatinhar %}

![Exemplo de app financeiro que mostra cartões de conteúdo com imagem legendada e somente com imagem]({% image_buster/assets/img_archive/cc_pyrite_crawl.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

A abordagem Crawl coloca o poder da personalização diretamente nas mãos dos profissionais de marketing. Embora seja necessário algum trabalho leve de desenvolvimento inicial para integrar os canais de envio de mensagens do Braze ao seu app ou site, essa abordagem permite que você comece a trabalhar mais cedo. 

Os profissionais de marketing determinam o conteúdo, o público e o momento das mensagens por meio do dashboard. No entanto, as opções de estilo são limitadas. Essa abordagem é mais adequada para equipes com recursos de desenvolvimento limitados ou que desejam compartilhar rapidamente conteúdo simples. 

<table>
<thead>
  <tr>
    <th>Personalização</th>
    <th>Descrição</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><b>Esforço</b></td>
    <td>Baixa</td>
  </tr>
    <tr>
    <td><b>Trabalho do desenvolvedor</b></td>
    <td>0-1 horas</td>
  </tr>
  <tr>
    <td><b>Estilo do cartão</b></td>
    <td>Use modelos padrão do Braze.</td>
  </tr>
  <tr>
    <td><b>Comportamento</b></td>
    <td>Escolha entre as opções de comportamento padrão.</td>
  </tr>
  <tr>
    <td><b>Rastreamento da análise de dados</b></td>
    <td>As análises de dados são capturadas no Braze.</td>
  </tr>
  <tr>
    <td><b>Pares de valores chave</b></td>
    <td>Opcional, permite personalização adicional de UI/UX.</td>
  </tr>
</tbody>
</table>

{% endtab %}
{% tab Caminhar %}

![Exemplo de app financeiro mostrando cartões de conteúdo com personalização]({% image_buster/assets/img_archive/cc_pyrite_walk.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

Uma abordagem híbrida para a implementação, a abordagem Walk envolve as equipes de marketing e de desenvolvimento para combinar com a marca do seu app ou site. 

Durante o processo de implementação, os desenvolvedores escrevem códigos personalizados para atualizar a aparência de um canal de envio de mensagens para que ele corresponda melhor à sua marca. Inclui a alteração do tipo e do tamanho da fonte, dos cantos arredondados e das cores. Essa abordagem ainda usa as opções padrão, mas com o estilo de modelo programático.

Os profissionais de marketing ainda mantêm o controle do público, do conteúdo, do comportamento ao clicar e da expiração diretamente no dashboard do Braze.

<table>
<thead>
  <tr>
    <th>Personalização</th>
    <th>Descrição</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><b>Esforço</b></td>
    <td>Baixa</td>
  </tr>
    <tr>
    <td><b>Trabalho do desenvolvedor</b></td>
    <td>0-4 horas</td>
  </tr>
  <tr>
    <td><b>Interface</b></td>
    <td>Use modelos do Braze ou use seus próprios modelos criados pelo desenvolvedor.</td>
  </tr>
  <tr>
    <td><b>Comportamento</b></td>
    <td>Escolha entre as opções de comportamento padrão.</td>
  </tr>
  <tr>
    <td><b>Rastreamento da análise de dados</b></td>
    <td>As análises de dados padrão são capturadas no Braze.</td>
  </tr>
  <tr>
    <td><b>Pares de valores chave</b></td>
    <td>Opcional, permite personalização adicional de UI/UX.</td>
  </tr>
</tbody>
</table>

{% endtab %}
{% tab Executar %}

![Exemplo de app financeiro mostrando cartões de conteúdo personalizados com captura de e-mail]({% image_buster/assets/img_archive/cc_pyrite_run.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

Com a abordagem Correr, os desenvolvedores assumem o controle total da experiência do usuário. O código personalizado determina a aparência das mensagens, como elas se comportam e como interagem com outros canais de envio de mensagens (por exemplo, disparando um Content Card com base em uma notificação por push).

Quando você cria conteúdo personalizado completamente novo, como novos tipos de cartões de conteúdo ou mensagens no app com interface de usuário personalizada, o SDK do Braze não rastreará automaticamente [as análises de dados]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/). Você deve lidar com a análise de dados de forma programática para que os profissionais de marketing continuem a ter acesso a métricas como impressões, cliques e demissões no dashboard do Braze. Chame os métodos de análise de dados do Braze SDK para que ele retorne esses dados para a Braze. Cada canal de envio de mensagens tem um artigo de análise de dados para ajudar a facilitar isso.

<table>
<thead>
  <tr>
    <th>Personalização</th>
    <th>Descrição</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><b>Esforço</b></td>
    <td>Depende do caso de uso.</td>
  </tr>
    <tr>
    <td><b>Trabalho do desenvolvedor</b></td>
    <td>Baixo esforço: 1-4 horas<br>Esforço médio: 4-8 horas<br>Alto esforço: Mais de 8 horas</td>
  </tr>
  <tr>
    <td><b>Interface</b></td>
    <td>Personalizado</td>
  </tr>
  <tr>
    <td><b>Comportamento</b></td>
    <td>Personalizado</td>
  </tr>
  <tr>
    <td><b>Rastreamento da análise de dados</b></td>
    <td>Personalizado</td>
  </tr>
  <tr>
    <td><b>Pares de valores chave</b></td>
    <td>Obrigatória</td>
  </tr>
</tbody>
</table>
{% endtab %}
{% endtabs %}

{% alert tip %}
Quando os desenvolvedores e implementadores criam conteúdo personalizado para o Braze, há uma oportunidade de colaboração multifuncional com os profissionais de marketing. Por exemplo, se você desenvolver uma nova interface do usuário ou uma nova funcionalidade para um componente específico, prepare sua equipe para o sucesso documentando o novo comportamento e como ele se integra ao back-end.
{% endalert %}