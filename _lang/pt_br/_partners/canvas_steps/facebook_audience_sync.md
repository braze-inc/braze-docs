---
nav_title: Facebook
article_title: Sincronização de canva público com o Facebook
description: "Este artigo de referência abordará como usar a sincronização de público do Braze para o Facebook, para entregar anúncios com base em gatilhos comportamentais, segmentação e mais."
page_order: 2
alias: "/audience_sync_facebook/"

Tool:
  - Canvas

---

# Sincronização de público com o Facebook

> 

 



- 
- Redirecionamento de usuários que são menos responsivos a outros canais de marketing.
- Criando públicos de supressão para evitar que os usuários recebam anúncios quando já são consumidores fiéis da sua marca.
- 

Esse recurso permite que as marcas controlem quais dados primários específicos são compartilhados com o Facebook. Na Braze, as integrações com as quais você pode e não pode compartilhar seus dados primários recebem a máxima consideração. Para saber mais, consulte nossa [política de privacidade](https://www.braze.com/privacy).

## Considerações sobre sincronização de usuário e limite de frequência
 
 O que isso significa na prática é que a Braze tentará agrupar e processar o maior número possível de usuários a cada 5 segundos antes de enviar esses usuários para o Facebook. 

 Se um cliente do Braze atingir esse limite de frequência, o Braze the Canvas tentará novamente a sincronização por até 13 horas. Se a sincronização não for possível, esses usuários serão listados na métrica Users Errored (Usuários com erro).

## Pré-requisitos

 

| Requisito | Origin | Descrição |
| ----------- | ------ | ----------- |
| Facebook Business Manager | [Facebook][1] | Uma ferramenta centralizada para gerenciar os ativos do Facebook da sua marca (por exemplo, contas de anúncios, páginas e apps). |
| Conta de Anúncio do Facebook | [Facebook][2] | Uma conta de anúncio ativa do Facebook vinculada ao gerente de negócios da sua marca.<br><br> Além disso, verifique se você aceitou os termos e condições de sua conta de anúncios. |
| Termos de públicos personalizados do Facebook | [Facebook][3] | Aceite os Termos de Públicos Personalizados do Facebook para suas contas de anúncios do Facebook que você planeja usar com o Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integração

### Etapa 1: conecte-se ao Facebook

No dashboard da Braze, acesse **Integrações de parceiros** > **Parceiros de tecnologia** e selecione **Facebook**. Em Facebook Audience Export, selecione **Connect Facebook**.

![Página de tecnologia do Facebook no Braze que inclui uma seção de Visão geral e uma seção de Exportação de público do Facebook com o botão Conectado ao Facebook.][4]{: style="max-width:85%;"}

Uma janela de diálogo oAuth do Facebook aparecerá para autorizar a Braze a criar Públicos Personalizados em suas contas de anúncios do Facebook.

![A primeira caixa de diálogo do Facebook solicitando para "Conectar como X", em que X é seu nome de usuário do Facebook.][6]{: style="max-width:30%;"}  ![A segunda caixa de diálogo do Facebook solicitando permissão para gerenciar anúncios para suas contas de anúncios.][5]{: style="max-width:40%;"}

Depois de vincular o Braze à sua conta do Facebook, você poderá selecionar quais contas de anúncios deseja sincronizar no seu espaço de trabalho do Braze. 

![Uma lista de contas de anúncios disponíveis que você pode conectar ao Facebook.][7]{: style="max-width:70%;"}



![Uma versão atualizada da página de parceiros de tecnologia do Facebook mostrando as contas de anúncios conectadas com sucesso.][8]{: style="max-width:85%;"}

Sua conexão com o Facebook é aplicada no nível do espaço de trabalho do Braze. Se o administrador do Facebook remover você do seu Facebook Business Manager ou o acesso às contas do Facebook conectadas, a Braze detectará um token inválido. Como resultado, seus canvas ativos usando componentes do público do Facebook mostrarão erros, e o Braze não poderá sincronizar usuários. 

{% alert important %}
Para clientes que já passaram pelo processo de Revisão de App do Facebook para [Gerenciamento de Anúncios](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) e [Acesso Padrão de Gerenciamento de Anúncios](https://developers.facebook.com/docs/marketing-api/access#standard), seu Token de Usuário do Sistema ainda será válido para o componente público do Facebook. Você não poderá editar ou revogar o Token de Usuário do Sistema do Facebook através da página de parceiro do Facebook. Em vez disso, você pode conectar sua conta do Facebook para substituir seu Token de Usuário do Sistema do Facebook dentro do seu espaço de trabalho do Braze. 

<br><br>
{% endalert %}

### Etapa 2: Aceitar os termos de serviço de públicos personalizados



- 
- 






### Etapa 3: adicione um componente de público do Facebook no Canvas Flow

Adicione um componente na sua canva e selecione **público do Facebook**.

 

### Etapa 4: Configuração de sincronização

 



Selecione a conta de anúncio do Facebook desejada. No menu suspenso **Escolher um Público Novo ou Existente**, digite o nome de um novo ou existente público. 

{% tabs %}
{% tab Criar um novo público %}

1. 
2.  
3. 



 





{% endtab %}
{% tab Sincronização com um público existente %}

 

1. 
2.  
3.  

![]({% image_buster /assets/img/audience_sync/fb_sync3.png %})

{% alert important %}
 
{% endalert %}

{% endtab %}
{% endtabs %}

### Etapa 5: Lançar canva

  

A guia **Histórico** do público personalizado no Gerenciador de Público do Facebook refletirá o número de usuários enviados para o público do Braze. Se um usuário reentrar na etapa, ele será enviado para o Facebook novamente.

![Detalhes do público e a guia de histórico para um determinado público do Facebook, com uma tabela de histórico do público com colunas de atividade, detalhes da atividade, itens alterados e data e hora.][9]{: style="max-width:80%;"}

## Compreensão da análise de dados

A tabela a seguir inclui métricas e descrições para ajudá-lo a entender melhor a análise de dados de seu componente Audience Sync.

| Métrico | Descrição |
| --- | --- |
| Entraram | Número de usuários que entraram neste componente para serem sincronizados com o Facebook. |
| Avançaram para a etapa seguinte | Quantos usuários avançaram para o próximo componente, se houver um. Todos os usuários avançarão automaticamente se essa for a última etapa da ramificação do Canva. |
| Usuários sincronizados | Número de usuários que foram sincronizados com sucesso ao Facebook. |
| Usuários não sincronizados | Número de usuários que não foram sincronizados devido à falta de campos para correspondência. |
| Usuários pendentes | Número de usuários atualmente sendo processados pela Braze para sincronizar com o Facebook. |
| Usuários com erro | Número de usuários que não foram sincronizados com o Facebook devido a um erro de API após cerca de 13 horas de tentativas. As possíveis causas de erros podem incluir um token inválido do Facebook ou a exclusão do público personalizado do Facebook. |
| Saíram do canva | Número de usuários que saíram da canva. Isso ocorre quando a última etapa de um canva é uma etapa do Facebook. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}

{% endalert %}

## Perguntas frequentes

### Quanto tempo leva para que meus públicos sejam preenchidos no meu dashboard de parceiro do Audience Sync?

O tempo necessário para preencher um público depende do parceiro específico. Todas as redes processarão as solicitações do Braze e tentarão combinar os usuários. 

### 

Você pode simplesmente desconectar e reconectar sua conta do Facebook na página de parceiros do Facebook. 

### 

- Certifique-se de que o token de usuário do sistema esteja autenticado e tenha acesso às contas de anúncios desejadas no Facebook Business Manager.
- Certifique-se de ter selecionado uma conta de anúncios, inserido um nome para o novo público personalizado e selecionado os campos correspondentes.
- Você pode ter atingido o limite de 500 públicos personalizados no Facebook. 

### 

O Facebook não fornece essas informações por motivos de privacidade.

### 

No momento, os públicos personalizados baseados em valor não são suportados pela Braze. Se você estiver interessado em sincronizar esses tipos de públicos personalizados, envie [comentários sobre o produto]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).

### 



 

- 
- 
- 
- 



### 

Neste momento, públicos personalizados semelhantes baseados em valor não são suportados pela Braze. Se você tentar sincronizar com este público, isso pode causar erros para sua etapa de Sincronização de Público. Para resolver isso, siga estas etapas:

1. Acessar seu dashboard do Facebook Ad Manager e selecionar **Audiences**.
2. Selecione **Criar público** > **Público personalizado**.
3. Selecione **Lista de clientes**.
4. Faça upload do seu CSV ou lista sem a coluna **Value**. Selecione **No, continue with a customer list that doesn't include customer value** (Não, continue com uma lista de clientes que não inclui o valor do cliente).
5. Conclua a criação do seu público personalizado.
6. Na Braze, atualize a etapa Facebook Audience Sync com o público personalizado que você criou.

###  

Para usar o público do Facebook, você precisa aceitar estes termos do contrato de serviço. 

- 
- 

Depois de aceitar os termos de serviço do público personalizado do Facebook, faça o seguinte:

1. Atualize seu token de acesso do Facebook com a Braze desconectando e reconectando sua conta do Facebook.
2. Re-ativar sua etapa de sincronização do público do Facebook editando e atualizando seu canva.



## Solução de problemas

<style>
table th:nth-child(1) {
    width: 20%;
}
table th:nth-child(2) {
    width: 40%;
}
table th:nth-child(2) {
    width: 40%;
}
table td {
    word-break: break-word;
}
</style>

<table>
  <thead>
    <tr>
      <th>Erro</th>
      <th>Descrição</th>
      <th>Etapas para resolver</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Token inválido</b></td>
      <td></td>
      <td> </td>
    </tr>
    <tr>
      <td><b>Tamanho do público muito baixo</b></td>
      <td> Se o tamanho de seu público se aproximar de zero, a rede poderá sinalizar que ele é muito baixo para ser atendido.</td>
      <td> </td>
    </tr>
    <tr>
      <td><b>O público não existe</b></td>
      <td> </td>
      <td> <br><br>  <br><br></td>
    </tr>
    <tr>
      <td><b>Tentativa de acesso à conta de anúncios</b></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>   </td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>
      </td>
    </tr>
    <tr>
      <td></td>
      <td>  </td>
      <td>
      </td>
    </tr>
  </tbody>
</table>

### 

 

#### 

1.  
2.  
3. 

#### 

 

1. 
- 
`https://business.facebook.com/ads/manage/customaudiences/tos/?act=<AD_ACCOUNT_ID>`
- 
  - 
  - 





1. 
2. 
3. 



{:start="4"}

4.  



{:start="5"}
5\.   
6\. Atualize seu token de acesso do Facebook com a Braze desconectando e reconectando sua conta do Facebook.
7\. Re-ativar sua etapa de sincronização do público do Facebook editando e atualizando seu canva. A partir daí, a Braze conseguirá sincronizar os usuários assim que eles chegarem à etapa de público do Facebook.
8\. 

####  



1. 
2. 
3.  <br> 
4.  <br> 

{:start="5"}

5.  <br> 

#### 



1. 
2. 

[0]: https://www.braze.com/privacy
[1]: https://www.facebook.com/business/help/113163272211510
[2]: https://www.facebook.com/business/help/910137316041095
[3]: https://www.facebook.com/ads/manage/customaudiences/tos.php
[4]: {% image_buster /assets/img/fb/afb_1.png %}
[5]: {% image_buster /assets/img/fb/afb_2.png %}
[6]: {% image_buster /assets/img/fb/afb_3.png %}
[7]: {% image_buster /assets/img/fb/afb_4.png %}
[8]: {% image_buster /assets/img/fb/afb_5.png %}
[9]: {% image_buster /assets/img/fb_audience_sync/audience_history.png %}
[10]: {% image_buster /assets/img/fb_audience_sync/analytics_example.jpg %}
[11]: {% image_buster /assets/img/fb_audience_sync/add_step.png %}
[12]: {% image_buster /assets/img/fb_audience_sync/add_audience.png %}
[13]: {% image_buster /assets/img/fb_audience_sync/create_audience.png %}
[14]: {% image_buster /assets/img/fb_audience_sync/new_audience.png %}
[15]: {% image_buster /assets/img/tiktok/tiktok13.png %}
[16]: {% image_buster /assets/img/tiktok/tiktok16.png %}
[18]: {% image_buster /assets/img/audience_sync/audience_sync3.png %}
[19]: {% image_buster /assets/img/audience_sync/audience_sync4.png %}
[20]: {% image_buster /assets/img/audience_sync/audience_sync5.png %}
[21]: {% image_buster /assets/img/audience_sync/fb_sync.png %}
[22]: {% image_buster /assets/img/audience_sync/fb_sync2.png %}
[23]: {% image_buster /assets/img/audience_sync/fb_sync3.png %}
[24]: {% image_buster /assets/img/fb_audience_sync/fb_sync_tos.png %}
[25]: {% image_buster /assets/img/fb_audience_sync/fb_sync_tos2.png %}