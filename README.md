# ChaleLivros-Web-II

Esse projeto, feito por Gianluca Z e André Davi L, é um projeto de aprendizado que consiste em aplicar as técnicas aprendidas em Desenvolvimento Web II. O projeto é focado no backend e dados manualmente inseridos via Painel de Admin Django. Abaixo, uma imagem descritiva sobre o projeto.

![Structure](https://github.com/user-attachments/assets/8aa5801b-6433-4280-a878-bd5cd664d3f8)

## Tabela de Conteúdos

1. [Introdução](#introdução)
2. [Preparação e Instalação](#preparação-e-instalação)
3. [Uso](#uso)
4. [Contribuição](#contribuição)
5. [Licença](#licença)

## Introdução

O uso é totalmente educacional e avaliativo na disciplina de Desenvolvimento Web II. O projeto é suportado em Windows (versão estável e testada) e Linux (versão estável, 50% testada).

## Preparação e Instalação

Versão do Python usada: 3.10> [Python 3.10](https://www.python.org/)

Primeiramente clone o projeto da master


1. **Clone the repository:**

   ```bash
   git clone https://github.com/Gianlz/ChaleLivros-Web-II
    ```
   Entre no diretório Root:

   ```bash
   cd nome_do_repositorio
    ```
2. **Fazer a instalação das dependências**
    ```bash
     pip install -r requirements.txt
    ```

 3. **Setup de itens sensíveis (KEYS)**

    I. Crie um arquivo nomeado .env na pasta raiz do projeto.
    
    II. Coloque os dados sensíveis dentro desse arquivo.

    ```bash
    SECRET_KEY = DJANGO_key (normalmente gerada em settings, é recomendável criar seu próprio core django e usar a própria key)
    GOOGLE_API = GOOGLE_api_key (a key usada)
     ```
  ## Configuração do Google OAuth API Key

Para gerar e configurar uma chave de API do Google OAuth para o projeto, siga os passos abaixo:

## Passo a Passo

### 1. Acesse o Google Cloud Console
- Vá para [Google Cloud Console](https://console.cloud.google.com/?hl=pt-br).

### 2. Crie um Novo Projeto
- Clique em [Criar Novo Projeto](https://console.cloud.google.com/projectcreate).
- Preencha os detalhes do seu projeto e conclua a criação.

### 3. Acesse as Credenciais
- No menu lateral esquerdo, clique em "Credenciais" ou acesse diretamente [Credenciais](https://console.cloud.google.com/apis/credentials).

### 4. Crie um ID do Cliente OAuth
- Clique em **+ CRIAR CREDENCIAIS** e selecione a opção **ID do Cliente OAuth**.

### 5. Configure a Tela de Consentimento
- Você será direcionado para a configuração da tela de consentimento.
- Clique em [Tela de Consentimento](https://console.cloud.google.com/apis/credentials/consent).
- Selecione a opção **Externo** e clique em **Criar**.

#### Informações Necessárias:
- **Nome do App**: Informe um nome que remeta ao seu projeto.
- **E-mail para Suporte do Usuário**: Recomendado usar o e-mail associado ao Google Cloud.
- **Domínio do App**: Informe o link da página inicial do seu aplicativo (por exemplo, `http://localhost:8000`).
- **Dados de Contato do Desenvolvedor**: Informe seu e-mail principal.
- Clique em **Salvar e Continuar**.

### 6. Adicione e Remova Escopos
- Clique em **ADICIONAR OU REMOVER ESCOPOS**.
- Selecione as duas primeiras caixas de seleção: `/auth/userinfo.email` e `/auth/userinfo.profile`.
- Clique em **Atualizar** e depois em **Salvar e Continuar**.

### 7. Adicione Usuários
- Em **+ ADD USERS**, adicione seu e-mail e clique em **Salvar e Continuar**.
- Clique em **Voltar para o Painel**.

### 8. Crie a Credencial
- Clique em **+ CRIAR CREDENCIAIS** e selecione **ID do Cliente OAuth**.
- Em **Tipo do Aplicativo**, selecione **Aplicativo da Web**.
- Informe um nome que remeta ao seu projeto.

#### Adicione Origens JavaScript Autorizadas e URIs de Redirecionamento Autorizados
- No campo **Origens JavaScript autorizadas**, adicione os seguintes URIs:
  ```plaintext
  http://localhost
  http://localhost:8000
  http://127.0.0.1
  http://127.0.0.1:8000
  ```
- No campo **URIs de redirecionamento autorizados**, adicione os mesmos URIs.
- Clique em **CRIAR**.

### 9. Copie o ID do Cliente
- Copie o **ID do Cliente** gerado.
- Adicione o ID do Cliente na variável `GOOGLE_API` do arquivo `.env` do seu projeto.

  # Setup do banco de dados

  O banco de dados utilizado é o MongoDB, então necessita ao menos ter ele instalado (Recomendado ter MongoDB Compass junto para gerenciar melhor).

``` bash
  https://www.mongodb.com/try/download/community
```
  
# Uso

Para rodar, basta fazer as migrações e iniciar (Migrações são necessárias especialmente quando há mudanças no models.py/banco de dados)

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver # para iniciar a aplicação (caso o DEBUG = true), senão rode python manage.py runserver --insecure, para não quebrar arquivos estáticos
```

# Contribuição

Qualquer contribuição é bem vinda, mas por se tratar de um projeto do ensino superior de Ciência da computação, provavelmente não tenha suporte sobre.

## Licença

Este projeto é um trabalho acadêmico desenvolvido como parte dos requisitos da disciplina de Desenvolvimento Web II. 

A utilização, modificação e distribuição do código-fonte deste projeto são permitidas exclusivamente para fins educacionais e de aprendizado. Este projeto não deve ser utilizado para fins comerciais ou de produção sem a devida autorização dos autores.

**Termos de Uso:**

1. **Uso Acadêmico**: Você pode utilizar este projeto para estudos e como referência em trabalhos acadêmicos.
2. **Modificação**: É permitido modificar o código-fonte para fins acadêmicos e de aprendizado. As modificações devem ser claramente documentadas.
3. **Distribuição**: Qualquer redistribuição do código deve manter esta licença e reconhecer os autores do projeto.
4. **Proibição de Uso Comercial**: Este projeto não deve ser utilizado para fins comerciais sem a permissão explícita dos autores.

Este projeto não possui uma licença formal, sendo regido pelas diretrizes acima. Todos os direitos reservados aos autores.

