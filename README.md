## Challenge MaisTodos

![portaldetodos](https://avatars0.githubusercontent.com/u/56608703?s=400&u=ae31a7a07d28895589b42ed0fcfc102c3d5bccff&v=4)


# Desafio Técnico - Processo Seletivo Backend Pyhton MaisTodos

A MAISTODOS LTDA está lançando um sistema inovador de cadastros de cartões de crédito e precisa garantir toda a qualidade e padronização dos dados. E esse sistema será uma API simples de cadastro de cartões de crédito.

### Sobre o desafio

A MAISTODOS LTDA está lançando um sistema inovador de cadastros de cartões de crédito e precisa garantir toda a qualidade e padronização dos dados. E esse sistema será uma API simples de cadastro de cartões de crédito, e o sistema irá receber no cadastro o seguinte payload:

{
    "exp_date": "02/2026",
    "holder": "Fulano",
    "number": "0000000000000001",
    "cvv": "1
    23",
}

Como não é um cadastro qualquer, esses dados precisam passar por uma validação criteriosa e específica:

#### exp_date

Ver se é uma data válida.
E se for válida, não pode ser menor do que a data de hoje. 😜
No banco de dados essa data deve ser gravada no formato yyyy-MM-[ultimo_dia_mes], por exemplo: 02/2022, deve ser 2022-02-28
holder

Deve ser um campo obrigatório e deve possuir mais de 2 caracteres.

#### number

Verificar se o número do cartão de crédito é válido, utilizando a lib https://github.com/MaisTodos/python-creditcard
Para instalar use pip install git+https://github.com/maistodos/python-creditcard.git@main
Este campo deve ser gravado de forma criptografada no banco de dados.

#### cvv

Este campo não é obrigatório, mas caso esteja presente no payload, deve possuir um tamanho entre 3 e 4 caracteres.
Este é um campo númerico.

## 🚀 Começando

### 📋 Pré-requisitos obrigatórios

- **[Pyhton na versão Python 3.9.2](https://www.python.org/downloads/release/python-392/)**
- **[Pip3](https://www.educative.io/answers/installing-pip3-in-ubuntu)**
- **[Docker](https://docs.docker.com/desktop/)** e **[Docker Compose](https://docs.docker.com/compose/)**
- **[Git](https://git-scm.com/)**
- **[Virtualenv](https://help.dreamhost.com/hc/en-us/articles/115000695551-Installing-and-using-virtualenv-with-Python-3)**

### 🔧 Download

- Realize o download do projeto na sua máquina: git clone https://github.com/pedrohigordev/challenge-backend-python-creditcard.git

## ⚙️ Executando o projeto

Após realizar o download, você deve navegar até a pasta raíz do projeto: challenge-backend-python-creditcard e executar o seguinte comando:

```
docker-compose up
```
ou

```
docker compose up
```

### Criação de super usuário

Um passo extremamente importante é você criar o super usuário, para que possa realizar seus primeiros testes na aplicação

Para isso, você deve abrir uma nova aba no terminal executar o comando: 


```
docker exec -it challenge-backend-python-creditcard-web  /bin/bash
```

- OBS: Caso não encontre o container, você deve executar o comando: docker ps
       e substituir o challenge-backend-python-creditcard-web pelo nome do container que está em execução na sua máquina

- Já dentro do container, execute o comando: 

```
python manage.py createsuperuser
```

- Nas perguntas a seguir, você pode responder com o que eu vou sugerir:

- Username (leave blank to use 'root'):
    - Digite: admin

- Email address:
    - Digite: admin@gmail.com

- Password:
    - Digite: 123

- Password (again):
    - Digite: 123

- Bypass password validation and create user anyway? [y/N]:
    - Digite: y

Pronto, após todos esses passo, você estará com o super usuário configurado,
agora sua aplicação está pronta para ser testada.


### Testes
### Caso você prefira realizar os testes via Insomnia, é só realizar a importação do arquivo:

- **[Insomnia](https://github.com/pedrohigor-life/challenge-mercafacil-backend-integration/blob/dev/tmp)**

## ✒️ Autores

- **Pedro Sousa** - _Desenvolvedor_ - [GitHub](https://github.com/pedrohigordev)

⌨️ Desenvolviedor por [Pedro Sousa](https://www.linkedin.com/in/pedrohigor/)