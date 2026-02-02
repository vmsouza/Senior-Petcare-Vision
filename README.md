# 🐾 Senior Petcare Vision

**Visão computacional aplicada ao cuidado contínuo de pets idosos.**

Senior Petcare Vision é um projeto real, criado a partir de uma necessidade do dia a dia: cuidar melhor de um cachorro idoso quando nem sempre estamos fisicamente presentes no mesmo ambiente.

O sistema utiliza **câmeras IP (RTSP)**, **captura periódica de imagens** e **IA multimodal** para detectar automaticamente eventos de higiene no ambiente e **enviar alertas em tempo real** para o responsável.

---

## 🎯 Motivação

Este não é um projeto de laboratório.

É um **case real**, vivido diariamente em casa.  
Enquanto uma pessoa trabalha fora e a outra permanece em home office, portas fechadas e rotinas diferentes fazem com que pequenos incidentes passem despercebidos por tempo demais.

Para um pet idoso, isso significa:
- desconforto
- risco de infecção
- necessidade de limpeza imediata

O **Senior Petcare Vision** nasceu para resolver exatamente isso.

---

## 🧠 Como funciona

1. Captura automática de imagens a partir de uma câmera RTSP
2. Análise visual focada **exclusivamente no piso**
3. Detecção de mudanças relevantes (manchas, resíduos, acidentes)
4. Classificação com nível de confiança
5. Envio de alerta imediato via **ntfy**
6. Registro opcional para auditoria e melhoria contínua

Tudo isso de forma **automatizada, discreta e sem intervenção humana**.

---

## 🛠️ Tecnologias utilizadas

- Python 3
- Captura RTSP (FFmpeg)
- IA multimodal (análise de imagem)
- ntfy.sh (alertas push)

---

## 🛠️ Instalação

1. Copie o arquivo env-example para .env
2. Ajuste o conteúdo do .env com seus valores
3. Substitua as fotos 'sem_coco.jpg' e 'com_coco.jpg' por fotos reais do seu ambiente.
4. Ajuste o ntfy.py com o alerta desejado.

- OpenIA: necessário ter uma chave de api
- Ntfy.sh: comece um grupo com o nome preferido

---

## 🚨 Exemplo de alerta

> 🚨 Evento detectado no ambiente  
> Confiança: 92%  
> Ação recomendada: limpeza imediata

O alerta chega **em tempo real**, permitindo agir rapidamente mesmo estando em outro cômodo ou fora de casa.

Você pode alterar o alerta diretamente no arquivo ntfy.py.

---

## ▶️ Execução

```bash
python main.py
```

O sistema pode ser facilmente integrado com:
- cron (execução periódica)
- serviços em background
- NAS ASUSTOR / Synology
- servidores Linux

---

## 🔒 Privacidade

- Nenhuma imagem é enviada para terceiros sem necessidade
- O foco da análise é **somente o piso**
- Não há reconhecimento facial
- Totalmente adaptável para ambientes sensíveis

---

## 🌱 Possíveis evoluções

- Dashboard de histórico de eventos
- Ajuste dinâmico de sensibilidade
- Detecção de outros tipos de incidentes
- Versão mobile-friendly
- Expansão para ambientes comerciais ou clínicas veterinárias

---

## ❤️ Considerações finais

Senior Petcare Vision prova que **IA não precisa ser grandiosa para ser útil**.

Às vezes, ela só precisa resolver um problema real, com empatia, cuidado e engenharia bem feita.

---

**Projeto criado com propósito, não apenas código.**

