# 🧹 Conversor de Encoding CSV - UTF-8 para uso no WhatsApp através da API da Meta Developers

![Status](https://img.shields.io/badge/status-funcional-success)
![Python](https://img.shields.io/badge/python-3.11-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Este script em Python foi feito para **corrigir problemas de codificação de caracteres** (acentuação, cedilha etc) em arquivos `.csv`, normalmente exportados em `latin1` ou `Windows-1252`, convertendo-os para `UTF-8`.

> 💡 Ideal para quem precisa usar arquivos de lista de contatos em sistemas que exigem UTF-8, como a API do WhatsApp (Meta Developers).

---

## 📁 Estrutura do Projeto

```
📦conversor_csv
 ┣ 📄 lista.csv
 ┣ 📄 lista_corrigida.csv
 ┣ 📄 corrigir_csv.py
 ┗ 📄 README.md
```

---

## 🚀 Como usar

1. Coloque seu arquivo original na raiz do projeto com o nome `lista.csv` (ou altere o nome no script).
2. Execute o script:

```bash
python corrigir_csv.py
```

3. O novo arquivo corrigido será salvo como `lista_corrigida.csv`, com codificação `UTF-8`.

---

## 🔍 O que ele faz?

- Lê o `.csv` com encoding `latin1`.
- Aplica uma tentativa de reinterpretação de strings mal codificadas.
- Salva com `UTF-8`, ideal para uso em automações de envio de mensagens.

---

## 🛠️ Tecnologias usadas

- Python 3.11+
- pandas

---

## 👨‍💻 Autor

**Miguel Mantoan Castellani - Analista de Sistema**  
💼 Saga Contabilidade • 🎓 Estudante de IA e dados

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Sinta-se livre para usar e modificar!
