# Como publicar este repositório em github.com/mmadachi

## 1. Execute os notebooks e salve as saídas
1. Abra cada notebook em `notebooks/` no Jupyter (ou no ambiente do curso).
2. Coloque os arquivos de dados do curso em `data/`.
3. **Kernel → Restart & Run All** e salve. O notebook precisa ter **células de código e de saída**.

## 2. Crie o repositório
No GitHub: **New repository** → nome `capstone-spacex` → **Public** → não marque README (já existe aqui).

## 3a. Envio pelo navegador (mais simples)
Na página do repositório: **Add file → Upload files** e arraste o conteúdo da pasta `capstone-spacex/` (mantendo as pastas). Clique em **Commit changes**.

## 3b. Envio pelo terminal
```bash
cd capstone-spacex
git init
git add .
git commit -m "Projeto final de Ciência de Dados"
git branch -M main
git remote add origin https://github.com/mmadachi/capstone-spacex.git
git push -u origin main
```

## 4. Confira os links usados na apresentação
- Repositório: https://github.com/mmadachi/capstone-spacex
- Notebooks: `https://github.com/mmadachi/capstone-spacex/blob/main/notebooks/<arquivo>.ipynb`
- Se usar outro nome de repositório, atualize os links nos slides 8 a 15 e no slide do repositório.

## 5. Checklist de avaliação
- [ ] Link do repositório no PDF (1 pt)
- [ ] Todos os notebooks e arquivos Python concluídos, com saídas
- [ ] PDF da apresentação enviado, com o nome correto
- [ ] Prints dos gráficos, mapas e dashboard colocados nos slides
- [ ] Números dos slides conferidos com as saídas dos seus notebooks
