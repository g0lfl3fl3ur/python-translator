import gradio as gr                # Ui library
from transformers import pipeline  # transformers pipeline

translation_pipeline = pipeline('translation_en_to_fr')

results = translation_pipeline('I love North Carolina')

results[0]['translation_text']

def translate_transformers(from_text):
    results = translation_pipeline(from_text)
    return results[0]['traslation_text']

translate_transformers('I love North Carolina.')

interface = gr.Interface(fn=translate_transformers, inputs=gr.inputs.Textbox(lines=2, placeholder='Text To Translate.'),
                         outputs='text')

interface.Launch()
