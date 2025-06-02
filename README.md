# Meu Primeiro Site na Internet com Flask!

Olá! Este é um site simples que eu criei para aprender a fazer coisas na internet usando programação. Ele é feito com algumas tecnologias que você talvez já tenha ouvido falar, como **Python**, **Flask** e **HTML/CSS**.

---

## O Que Este Site Faz?

Imagine que este é o começo de um site de verdade! Ele tem algumas páginas básicas para você explorar:

* **Página Inicial (Home):** A primeira página que você vê, te dando as boas-vindas.
* **Sobre Nós:** Uma página para falar um pouco sobre o projeto.
* **Fale Conosco:** Uma página com um formulário simples onde você pode enviar uma mensagem (por enquanto, a mensagem aparece na tela do computador que está rodando o site).
* **Nossos Serviços:** Uma lista de coisas que o site (ou uma empresa por trás dele) poderia oferecer.

Ele também tem um visual simples, mas organizado, graças ao **CSS**, que é como a "maquiagem" do site. E o mais legal é que ele consegue mostrar informações diferentes dependendo do que eu programar, como a data de hoje ou listas de coisas.

---

## Como Você Pode Ver Este Site no Seu Computador?

Para ver este site funcionando no seu próprio computador, siga estes passos. Não se preocupe se parecer complicado, é só seguir as instruções!

1.  **Baixe o Projeto para o Seu Computador:**
    * Primeiro, você precisa de um programa chamado **Git**. Se não tiver, baixe ele aqui: [Baixar Git](https://git-scm.com/downloads). Siga as instruções de instalação padrão.
    * Depois, abra um programa no seu computador chamado "Terminal" ou "Prompt de Comando" (no Windows) ou "Terminal" (no Mac/Linux).
    * Cole o seguinte comando e aperte `Enter`:
        ```bash
        git clone [https://github.com/SeuUsuario/meu-primeiro-site-flask.git](https://github.com/SeuUsuario/meu-primeiro-site-flask.git)
        ```
        * **ATENÇÃO:** Troque `https://github.com/SeuUsuario/meu-primeiro-site-flask.git` pelo **endereço real deste projeto no GitHub**. Você encontra ele clicando no botão verde "Code" aqui nesta página do GitHub.
    * Agora, digite este comando para entrar na pasta do projeto e aperte `Enter`:
        ```bash
        cd meu-primeiro-site-flask
        ```

2.  **Prepare o Ambiente (Isso Ajuda o Python a Funcionar Melhor):**
    * No mesmo Terminal, cole este comando e aperte `Enter`:
        ```bash
        python -m venv venv
        ```
    * Agora, ative o ambiente. O comando muda um pouco dependendo do seu sistema:
        * **Se você usa Windows:**
            ```bash
            .\venv\Scripts\activate
            ```
        * **Se você usa Mac ou Linux:**
            ```bash
            source venv/bin/activate
            ```
    * Você verá `(venv)` aparecer antes do nome da pasta no seu Terminal. Isso significa que deu certo!

3.  **Instale as Coisas que o Site Precisa:**
    * Ainda no Terminal (com `(venv)` aparecendo), cole este comando e aperte `Enter`:
        ```bash
        pip install -r requirements.txt
        ```
    * Ele vai baixar e instalar as ferramentas necessárias para o site funcionar.

4.  **Ligue o Site!**
    * Quase lá! No Terminal, cole este comando e aperte `Enter`:
        ```bash
        python app.py
        ```
    * Você verá algumas mensagens, e uma delas dirá algo como: `* Running on http://127.0.0.1:5000`. Isso significa que o site está ligado!

5.  **Veja o Site no Seu Navegador!**
    * Abra o seu navegador de internet (Chrome, Firefox, Edge, etc.) e digite este endereço na barra de endereços:
        ```
        [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
        ```
    * Aperte `Enter` e pronto! Seu site estará funcionando no seu computador.

---

## O Que Tem Dentro Deste Projeto?

Aqui está uma ideia de como os arquivos estão organizados na pasta que você baixou:
.
├── app.py              # É o "cérebro" do site. Ele decide o que aparece em cada página.
├── requirements.txt    # Uma lista das ferramentas que o site precisa para funcionar.
├── .gitignore          # Diz para o computador o que não precisa ser enviado para o GitHub.
├── README.md           # Este arquivo que você está lendo!
├── templates/          # Uma pasta com todos os "esqueletos" das páginas do site (.html).
│   ├── home.html       # A página inicial.
│   ├── sobre.html      # A página "Sobre Nós".
│   ├── contato.html    # A página de contato.
│   └── servicos.html   # A página de serviços.
└── static/             # Uma pasta para coisas que não mudam muito (como estilos e imagens).
└── css/            # Pasta para guardar os arquivos de estilo.
└── style.css   # O arquivo que deixa o site bonito e organizado.
