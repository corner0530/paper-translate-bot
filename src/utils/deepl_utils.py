import deepl
import os


def translate_text(text, source_lang="EN", target_lang="JA"):
    DEEPL_API_KEY = os.environ["DEEPL_API_KEY"]
    translator = deepl.Translator(DEEPL_API_KEY)
    result = translator.translate_text(
        text, source_lang=source_lang, target_lang=target_lang
    )
    return result.text


if __name__ == "__main__":
    text = input()
    print(translate_text(text))
