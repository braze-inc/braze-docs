---
nav_title: Adobe
article_title: Adobe
description: "Esta página descreve a parceria entre o Braze e a Adobe, uma plataforma de dados do cliente, que permite que as marcas se conectem e mapeiem seus dados da Adobe (atributos e segmentos personalizados) para o Braze em tempo real. As marcas podem então agir com base nesses dados, oferecendo experiências personalizadas e direcionadas para esses usuários."
page_type: partner
page_order: 1
search_tag: Partner

---

# Adobe

> Criada com base na Adobe Experience Platform, a plataforma de dados do cliente em tempo real da Adobe reúne dados conhecidos e anônimos de várias fontes corporativas para criar perfis de clientes. Esses perfis podem então ser usados para fornecer experiências personalizadas em todos os canais e dispositivos em tempo real.

A integração entre o Braze e o Adobe CDP conecta e mapeia os dados do Adobe de sua marca (atributos e segmentos personalizados) para o Braze em tempo real. Em seguida, é possível agir com base nesses dados, oferecendo experiências personalizadas e direcionadas aos seus usuários. Com a Adobe, a integração é intuitiva. Basta pegar qualquer [identidade](https://experienceleague.adobe.com/docs/experience-platform/identity/namespaces.html?lang=en) da Adobe, mapeá-la para um ID externo da Braze e enviá-la para a plataforma da Braze. Todos os dados enviados estarão acessíveis no Braze através de um novo atributo `AdobeExperiencePlatformSegments`.

{% alert important %}
A integração da Adobe Experience Platform atualmente não oferece suporte à associação dinâmica de público. Isso significa que ele só pode adicionar valores aos perfis de usuário, não removê-los.
{% endalert %}

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Adobe | Uma [conta da Adobe](https://account.adobe.com/) é necessária para aproveitar esta parceria. |
| chave da API REST Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Instância do Braze | Sua instância do Braze pode ser obtida com o seu gerente de integração do Braze ou pode ser encontrada na [página de visão geral da API]({{site.baseurl}}/api/basics/#endpoints). |
| Endpoint REST do Braze | Sua URL de endpoint REST. Seu endpoint dependerá da [URL do Braze para sua instância]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
O envio de atributos personalizados adicionais aumentará o uso de seus pontos de dados. Sugerimos que fale com seu gerente de sucesso do cliente para entender melhor esse possível aumento de dados.
{% endalert %}

## Integração

### Etapa 1: Configurar destino Braze

Na página de **Configurações** da Adobe, selecione **destinos** em **Coleções**. Em seguida, localize o bloco da **Braze** e selecione **Configure** (Configurar). 

![]({% image_buster /assets/img/adobe/braze-destination-configure.png %})

{% alert note %}
Se já existir uma conexão com o Braze, você verá um botão **Ativar** no cartão de destino. Para saber mais sobre a diferença entre ativar e configurar, consulte a seção de catálogo da [documentação](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/destinations/destinations-interface/destinations-workspace.html?lang=en#catalog) do espaço de trabalho da Adobe.
{% endalert %}

### Etapa 2: forneça o token da Braze

Na etapa **Conta**, forneça sua chave de API do Braze e selecione **Conectar ao destino**.

![]({% image_buster /assets/img/adobe/braze-destination-account.png %}){: style="max-width:60%"}

### Etapa 3: Autenticação

Em seguida, na etapa **Authentication (Autenticação)**, insira seus detalhes de conexão do Braze:
- **Nome**: Digite o nome pelo qual você gostaria de reconhecer esse destino no futuro.
- **Destino**: Insira uma descrição que o ajude a identificar este destino.
- **Instância do endpoint**: Insira sua instância de endpoint Braze.
- **Caso de uso de marketing**: Os casos de uso de marketing indicam a intenção para a qual os dados serão exportados para o destino. Você pode selecionar um dos casos de uso de marketing definidos pela Adobe ou criar seu próprio caso de uso de marketing. Para saber mais sobre os casos de uso de marketing da Adobe, visite [Governança de dados na Adobe Experience Platform](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en#destinations).

![]({% image_buster /assets/img/adobe/braze-destination-authentication.png %}){: style="max-width:60%;"}

### Etapa 4: Criar destino
clique em **Create destination** (Criar destino). Seu destino foi criado. Você pode selecionar **Save & Exit** para ativar os segmentos mais tarde ou **Next** para continuar o fluxo de trabalho e selecionar os segmentos a serem ativados. 

### Etapa 5: Ativar segmentos
Ative os dados que você tem na CDP em tempo real da Adobe mapeando segmentos para o destino da Braze.

A lista a seguir destaca as etapas gerais necessárias para ativar um segmento. Para obter orientações completas sobre os segmentos da Adobe e o fluxo de trabalho de ativação de segmentos, visite [Adobe](https://experienceleague.adobe.com/docs/experience-platform/destinations/ui/activate-destinations.html?lang=en#prerequisites).

1. Selecione e ative o destino Braze.
2. Selecione os segmentos aplicáveis.
4. Configure o agendamento e os nomes dos arquivos para cada segmento que você exportar.
5. Selecione atributos para enviar para a Braze.
6. Revisar e verificar a ativação.

### Etapa 6: Mapeamento de campo

Para enviar corretamente os dados do seu público da Adobe Experience Platform para a Braze, complete a etapa de mapeamento de campo. O mapeamento cria um link entre os campos do modelo de dados da Adobe Experience e os campos correspondentes da plataforma Braze.

1. Na etapa de mapeamento, selecione **Adicionar novo mapeamento**.<br>![]({% image_buster /assets/img/adobe/braze-destination-mapping.png %}){: style="max-width:50%;"}<br><br>
2. Na seção do campo de origem, selecione o botão de seta ao lado do campo vazio para abrir a janela de seleção do campo de origem.<br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-source.png %})<br><br>
3. Na janela, selecione os atributos Adobe para mapear para seus atributos Braze. <br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-attributes.png %}){: style="max-width:70%;"}<br><br>Em seguida, selecione o namespace de identidade. Esta opção é usada para mapear um namespace de identidade de plataforma para um namespace Braze.<br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-namespaces.png %}){: style="max-width:80%;"}<br> Escolha seus campos de origem e selecione **Select (Selecionar)**.<br><br>
4. Na seção do campo de destino, selecione o ícone de mapeamento ao lado do campo.<br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-target.png %}){: style="max-width:90%;"} <br><br>
5. Na janela de seleção de campo-alvo, você pode escolher entre três categorias de campos-alvo:<br><br>• **Selecione o namespace de identidade**: Use esta opção para mapear namespaces de identidade da Plataforma para namespaces de identidade da Braze.<br>• **Selecione atributos personalizados**: Use esta opção para mapear atributos da Adobe XDM para os atributos personalizados da Braze que você definiu na sua conta da Braze. <br><br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-target-fields.png %}){: style="max-width:60%;"}<br><br>**Você também pode usar esta opção para renomear atributos XDM existentes para a Braze.** Por exemplo, o mapeamento de um atributo XDM `lastname` para um atributo personalizado `Last_Name` na Braze cria o atributo `Last_Name` na Braze caso ele ainda não exista e mapeia o atributo XDM `lastname` para ele. <br><br> Escolha seus campos de direcionamento e selecione **Select (Selecionar)**.<br><br>
6. Seu mapeamento de campo deve aparecer na lista.<br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-complete.png %})<br><br>
7. Para adicionar mapeamentos, repita as etapas de 1 a 6, conforme necessário. 

## Caso de uso

Vamos supor que seu esquema de perfil XDM e sua instância do Braze contenham os seguintes atributos e identidades:

|     | Esquema de perfil XDM | Instância do Braze |
| --- | ------------------ | -------------- |
| Atributos | - `person.name.firstname`<br>- `person.name.lastname`<br>- `mobilePhone.number`| - `FirstName`<br>- `LastName`<br>- `PhoneNumber`|
| Identidades | - `Email`<br>ID do anúncio do Google (`GAID`)<br>\- ID da Apple para anunciantes (`IDFA`) | - `external_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

O mapeamento correto ficaria assim:

![Mapeamentos de destino: IdentityMap:IDFA mapeado para IdentityMap:external_id, IdentityMap:GAID mapeado para IdentityMap:external_id, IdentityMap:E-mail mapeado para IdentityMap:external_id, xdm:mobilePhone.number mapeado para CustomAttribute:PhoneNumber, xdm:person.name.lastName mapeado para CustomAtrribute:LastName, xdm:person.name.firstName mapeado para CustomAttribute:FirstName]({% image_buster /assets/img/adobe/braze-destination-mapping-example.png %})

## Dados exportados
Para verificar se os dados foram exportados com sucesso para a Braze, verifique sua conta da Braze. Os segmentos da Adobe Experience Platform são exportados para a Braze sob o atributo `AdobeExperiencePlatformSegments`.

## Uso de dados e governança
Todos os destinos da Adobe Experience Platform estão em conformidade com as políticas de uso de dados ao lidar com seus dados. Consulte [Governança de dados na CDP em tempo real](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en) para obter informações detalhadas sobre como a Adobe Experience Platform aplica a governança de dados. 

