from transformers import pipeline
# # import huggingface_hub
# # generator = pipeline("text-generation", model="gpt-2")
# # prompt="The story of a lion,"
# # print(generator(prompt, max_length=50, num_return_sequences=1)[0]['generated_textS'])
# translator = pipeline("translation_en_to_te",model="Helsinki-NLP/opus-mt-en-ie")
# result = translator("Hoe are you today?")
# print(result[0]['translation_text'])
ner =pipeline("ner",grouped_entities=True)
print(ner("Elon musk founded Space X and lives in the United States"))
