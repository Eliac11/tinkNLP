import torch
from transformers import AutoTokenizer, AutoModelWithLMHead

modelname = "Eliac11/FitModel"

class ModelInterface:
    def __init__(self):
        self.__tokenizer = AutoTokenizer.from_pretrained(modelname)
        self.__model = AutoModelWithLMHead.from_pretrained(modelname,from_tf=True)

    def generate(self, text):
        inputs = self.__tokenizer(text, return_tensors='pt')
        generated_token_ids = self.__model.generate(
                                            **inputs,
                                            top_k=10,
                                            top_p=0.95,
                                            num_beams=3,
                                            num_return_sequences=3,
                                            do_sample=True,
                                            no_repeat_ngram_size=2,
                                            temperature=1.2,
                                            repetition_penalty=1.2,
                                            length_penalty=2,
                                            eos_token_id=50257,
                                            max_new_tokens=20
                                        )

        return self.__tokenizer.decode(generated_token_ids[0])

if __name__ == "__main__":
    res = ModelInterface().generate('@@ПЕРВЫЙ@@ привет @@ВТОРОЙ@@ привет @@ПЕРВЫЙ@@ как дела? @@ВТОРОЙ@@').split("@@ВТОРОЙ@@")[-1]
    print(res)
