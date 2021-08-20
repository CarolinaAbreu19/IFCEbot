# IFCEbot

Protótipo de chatbot de uso acadêmico. Projetado para embarcar em sistema Linux.

![IFCEbot](images/chatbotEmFuncionamento.png)

Para visualizar o projeto, execute o comando:

```
python3 interface.py
```

## Caso não consiga executar

O IFCEbot pode estar exigindo algumas bibliotecas que não estão instaladas na sua máquina. Os requisitos de software são:

* python 3.0 ou superior - Acesse [este link](https://www.python.org/downloads/) para fazer o download

As seguintes bibliotecas são necessárias para executar o projeto:

* numpy
* nltk
* sklearn

Para instalá-las, digite os comandos no terminal:

```
pip3 install numpy
pip3 install --user -U nltk
pip3 install -U scikit-learn
```

* Por fim, descomente as linhas de código do arquivo `IFCEbot.py`:

```
nltk.download('punkt')   # for first-time use only
nltk.download('wordnet')    # for first-time use only
```

Caso você ainda não conseguir executar este projeto, pode entrar em contato através do meu email.

## Autores

Ana Carolina Silva Abreu - ana.carolina.silva05@aluno.ifce.edu.br

Erik Jhones Freitas do Nascimento - erik.jhones06@aluno.ifce.edu.br

Filipe de Almeida Lira - filipe.almeida.lira04@aluno.ifce.edu.br

Sandro César Silveira Jucá - sandrojuca@ifce.edu.br
