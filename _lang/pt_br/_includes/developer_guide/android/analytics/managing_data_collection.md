## Questionário de privacidade do Google Play {#privacy-questionnaire}

A partir de abril de 2022, os desenvolvedores do Android deverão preencher o [formulário de segurança de dados](https://support.google.com/googleplay/android-developer/answer/10787469) do Google Play para divulgar práticas de privacidade e segurança. Este guia fornece instruções sobre como preencher esse novo formulário com informações sobre como o Braze lida com os dados do seu app. 

Como desenvolvedor do app, você tem o controle dos dados que envia ao Braze. Os dados recebidos pelo Braze são processados de acordo com suas instruções. Isso é o que o Google classifica como um [prestador de serviço](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en#zippy=%2Cwhat-kinds-of-activities-can-service-providers-perform). 

{% alert important %}
Este artigo traz informações relacionadas aos dados que o SDK da Braze processa em relação ao questionário da seção de segurança do Google. Este artigo não fornece orientação jurídica, portanto, recomendamos consultar sua equipe jurídica antes de enviar qualquer informação ao Google.
{% endalert %}

### Perguntas

|Perguntas|Respostas para o Braze SDK|
|---|---|
|O seu app coleta ou compartilha algum dos tipos de dados de usuários necessários?|Sim, o SDK da Braze para Android coleta dados conforme configurado pelo desenvolvedor do app. |
|Todos os dados de usuários coletados pelo seu app são criptografados em trânsito?|Sim.|
|Vocês oferecem uma maneira de os usuários solicitarem a exclusão de seus dados?|Sim.|

Para saber mais sobre como lidar com solicitações de dados de usuários e exclusão, consulte [Informações de retenção de dados da Braze]({{site.baseurl}}/api/data_retention/).

### Coleta de dados

Os dados coletados pelo Braze são determinados pela sua integração específica e pelos dados de usuários que você escolher coletar. Para saber mais sobre quais dados a Braze coleta por padrão e como desativar determinadas atribuições, consulte nossas [opções de coleta de dados do SDK]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/#minimum-integration).

<table id="datatypes">
    <thead>
        <tr>
            <th width="25%">Categoria</th>
            <th width="25%">Tipo de dados</th>
            <th width="50%">Uso da Braze</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="2">Local</td>
            <td>Local aproximado</td>
            <td rowspan="15">Não coletado por padrão.</td>
        </tr>
        <tr>
            <td>Localização precisa</td>
        </tr>
        <tr>
            <td rowspan="9">Informações pessoais</td>
            <td>Nome</td>
        </tr>
        <tr>
            <td>Endereço de e-mail</td>
        </tr>
        <tr>
            <td>IDs de usuário</td>
        </tr>
        <tr>
            <td>Endereço</td>
        </tr>
        <tr>
            <td>Número de telefone</td>
        </tr>
        <tr>
            <td>Raça e etnia</td>
        </tr>
        <tr>
            <td>Crenças políticas ou religiosas</td>
        </tr>
        <tr>
            <td>Orientação sexual</td>
        </tr>
        <tr>
            <td>Outras informações</td>
        </tr>
        <tr>
            <td rowspan="4">Informações financeiras</td>
            <td>Informações de pagamento do usuário</td>
        </tr>
        <tr>
            <td>Histórico de compras</td>
        </tr>
        <tr>
            <td>Pontuação de crédito</td>
        </tr>
        <tr>
            <td>Outras informações financeiras</td>      
        </tr>
        <tr>
            <td rowspan="2">Saúde e condicionamento físico</td>
            <td>Informações sobre integridade</td>
            <td rowspan="2">Não coletado por padrão.</td>
        </tr>
        <tr>
            <td>Informações sobre o condicionamento físico</td>     
        </tr>
        <tr>
            <td rowspan="3">Mensagens</td>
            <td>E-mails</td>
            <td rowspan="2">Não coletado por padrão.</td>
        </tr>
        <tr>
            <td>SMS ou MMS</td>          
        </tr>
        <tr>
            <td>Outras mensagens no app</td>
            <td>Se você enviar mensagens no app ou notificações por push por meio do Braze, coletaremos informações sobre quando os usuários abriram ou leram essas mensagens.</td>
        </tr>
        <tr>
            <td rowspan="2">Fotos e vídeos</td>
            <td>Fotos</td>
            <td rowspan="8">Não coletado.</td>
        </tr>
        <tr>
            <td>Vídeos</td>
        </tr>
        <tr>
            <td rowspan="3">Arquivos de áudio</td>
            <td>Gravações de voz ou som</td>
        </tr>        
        <tr>
            <td>Arquivos de música</td>
        </tr>
        <tr>
            <td>Outros arquivos de áudio</td>
        </tr>
        <tr>
            <td>Arquivos e documentos</td>
            <td>Arquivos e documentos</td>
        </tr>
        <tr>
            <td>Calendário</td>
            <td>Eventos do calendário</td>
        </tr>
        <tr>
            <td>Contatos</td>
            <td>Contatos</td>
        </tr>
        <tr>
            <td rowspan="5">Atividade do app</td>
            <td>Interações do app</td>
            <td>O Braze coleta dados de atividade da sessão por padrão. Todas as outras interações e atividades são determinadas pela integração personalizada do seu app.</td>
        </tr>
        <tr>
            <td>Histórico de pesquisa no app</td>
            <td>Não coletado.</td>            
        </tr>
        <tr>
            <td>Aplicativos instalados</td>
            <td>Não coletado.</td>            
        </tr>
        <tr>
            <td>Outros conteúdos gerados por usuários</td>
            <td rowspan="2">Não coletado por padrão.</td>            
        </tr>
        <tr>
            <td>Outras ações</td>
        </tr>
        <tr>
            <td>Navegação na Web</td>
            <td>Histórico de navegação na Web</td>
            <td>Não coletado.</td>
        </tr>
        <tr>
            <td rowspan="3">Informações e performance do app</td>
            <td>Registros de falhas</td>
            <td>A Braze coleta registros de falhas para erros que ocorrem no SDK. Eles contêm o modelo do telefone do usuário e o nível do sistema operacional, juntamente com uma ID de usuário específica da Braze.</td>
        </tr>
        <tr>
            <td>Diagnóstico</td>
            <td>Não coletado.</td>            
        </tr>
        <tr>
            <td>Outros dados de performance do app</td>
            <td>Não coletado.</td>
        </tr>
        <tr>
            <td>IDs de dispositivos ou outros</td>
            <td>IDs de dispositivos ou outros</td>
            <td>O Braze gera um ID de dispositivo para diferenciar os dispositivos dos usuários e verifica se as mensagens são enviadas para o dispositivo correto.</td>
        </tr>
    </tbody>
</table>

Para saber mais sobre outros dados de dispositivos que o Braze coleta e que podem estar fora do escopo das diretrizes de segurança de dados do Google Play, consulte nossa [visão geral do armazenamento Android]({{site.baseurl}}/developer_guide/storage/?tab=android) e nossas [opções de coleta de dados SDK]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/#minimum-integration).

## Desativar o rastreamento de dados

Para desativar a atividade de rastreamento de dados no Android SDK, use o método [`disableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html). Isso fará com que todas as conexões de rede sejam canceladas, o que significa que o SDK do Braze não passará mais nenhum dado para os servidores do Braze.

## Limpeza de dados armazenados anteriormente

Você pode usar o método [`wipeData()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/wipe-data.html) para limpar completamente todos os dados do lado do cliente armazenados no dispositivo.

## Retomada do rastreamento de dados

Para retomar a coleta de dados, você pode usar o método [`enableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-sdk.html) método. Lembre-se de que isso não restaurará nenhum dado apagado anteriormente.
