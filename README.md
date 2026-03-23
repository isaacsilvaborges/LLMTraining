In here I'm training some LLM skills

1. Textualização dos Dados: Transformar cada linha do seu CSV (X_train e y_train) em um formato de instrução em texto (como um arquivo JSONL), onde as características da safra viram a pergunta e o Yield vira a resposta.

English terms: Instruction Formatting
Instruction Tuning Data Preparation
Prompt-Completion Formatting
Supervised Fine-Tuning (SFT) Data Formatting
Text Serialization of Structured Data
Tabular-to-Text Transformation

2. Escolha do Modelo Base: Selecionar um modelo open-weights leve e acessível para rodar em GPUs gratuitas ou locais, como o Llama 3 (8B), Mistral (7B) ou Gemma (2B/7B).

3. Preparação do Ambiente: Instalar as bibliotecas fundamentais da Hugging Face para treinamento: transformers, datasets, peft, trl e bitsandbytes.

4. Quantização (QLoRA): Carregar o modelo escolhido em precisão reduzida (4-bit) usando o bitsandbytes para garantir que ele não estoure a memória da sua placa de vídeo.

5. Configuração do LoRA (PEFT): Congelar os bilhões de parâmetros originais da LLM e injetar pequenos adaptadores treináveis (LoRA). Você vai treinar apenas essa "camada" extra.

6. Treinamento (SFTTrainer): Rodar o loop de treinamento usando o SFTTrainer (Supervised Fine-tuning Trainer), passando seus dados de texto para ensinar a LLM a prever a colheita.

7. Inferência no Teste: Passar o seu conjunto de teste (X_test), agora em formato de texto, para a LLM ajustada e gerar os textos de resposta.

8. Limpeza de Saída (Parser): Desenvolver uma função com expressões regulares (Regex) para ler a resposta de texto da LLM e isolar apenas o valor numérico (float).

9. Avaliação e MLflow: Calcular as métricas tradicionais (mean_squared_error e r2_score) usando os valores extraídos e logar os resultados no seu experimento atual do MLflow para comparar com a Regressão Linear.