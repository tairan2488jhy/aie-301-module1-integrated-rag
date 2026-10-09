import tiktoken
import json
import os

# ========== Tiktoken Offline Cache Config (Put AT THE TOP) ==========
# Disable online download, use local cache folder ./tiktoken_cache
# os.environ["TIKTOKEN_CACHE_DIR"] = "./tiktoken_cache"
# os.environ["TIKTOKEN_DISABLE_MODEL_DOWNLOAD"] = "1"

# ====================== V1 BASELINE CONFIG (FIXED) ======================
INPUT_MD_PATH = r".\docs\raw\Hands-On_Large_Language_Models.md"
OUTPUT_MD_PATH = r".\docs\raw\Hands-On_Large_Language_Moeles-FixedSizeChunking.md"
TARGET_TOKEN_SIZE = 512
ENCODER = tiktoken.get_encoding("cl100k_base")

def count_tokens(text: str) -> int:
    # Standard OpenAI token count
    return len(ENCODER.encode(text.strip()))

def main():
    # Load cleaned markdown file
    with open(INPUT_MD_PATH, "r", encoding="utf-8") as f:
        full_text = f.read()

    # Step1: Only split by pure paragraph breaks (V1 strict rule)
    paragraph_list = full_text.split("\n\n")
    chunk_result = []

    for idx, para in enumerate(paragraph_list):
        para_clean = para.strip()
        if not para_clean:
            continue

        token_num = count_tokens(para_clean)
        chunk_result.append({
            "chunk_index": idx,
            "text": para_clean,
            "token_count": token_num,
            "tag": "Hand-On_Large_Language_Models",
            "version": 1
        })

        # Save standard jsonl output
        with open(OUTPUT_MD_PATH, "w", encoding="utf-8") as f_out:
            for item in chunk_result:
                f_out.write(json.dumps(item, ensure_ascii=False) + "\n")

        # Print core statistic for experiment evaluation
        token_list = [x["token_count"] for x in chunk_result]
        print("===== V1 Fixed Chunk Baseline Statistic =====")
        print(f"Total Chunks Generated: {len(chunk_result)}")
        print(f"Min Token Count: {min(token_list)}")
        print(f"Max Token Count: {max(token_list)}")
        print(f"Avg Token Count: {sum(token_list)//len(token_list)}")
        print(f"File Saved: {OUTPUT_MD_PATH}")

    if __name__ == "__main__":
        main()


# question1: what function about strip()
# answer:
# `strip()` is a built-in string method in Python.
# It removes leading and trailing whitespace characters from a string, including spaces, tabs `\t`, newlines `\n`, carriage returns `\r`.
# It **does NOT touch whitespace inside the string**.
#
# In my FixedChunking code, I use `para.strip()` to clean paragraphs:
#
# 1. Drop blank space at start/end of paragraph.
# 2. Avoid counting useless empty tokens from pure blank lines.
# 3. Prevent empty string being treated as valid paragraph.
#
# Example:
#
# ```
# raw = "   Hello RAG\n\n"
# clean = raw.strip()
# # clean becomes "Hello RAG"
# ```


# question2: what really len(ENCODER.encode(text.strip())) function returns back?
# answer:
# `ENCODER.encode(text)` converts input text into a list of integer token IDs defined by the cl100k_base tokenizer.
# `len(...)` returns the **count of tokens**, NOT character count, NOT word count.
#
# `text.strip()` cleans leading/trailing whitespace first.
# Then `ENCODER.encode()` maps the cleaned string to a sequence of token integers.
# `len()` measures how many tokens this sequence contains.
#
# >
# > Important distinction for interview:
# >
# >
# > 1. It is NOT number of characters. One token can represent multiple characters (like common English words).
# > 2. It is NOT number of words. One word may split into multiple tokens, especially rare words or technical terms.
# > 3. This matches OpenAI’s official token calculation standard used in production RAG pipelines.

# qu3: Do i need to know detail of the len(ENCODER.encode(XX)) for my interview?
# ans：**Short answer: Yes, you must understand its core behavior, but you don’t need to memorize low-level BPE implementation details.**
#
# What you **MUST master** (will be asked):
#
# 1. `ENCODER.encode()` turns string → list of integer token IDs. `len()` returns token count, **not char / word count**.
# 2. It uses cl100k_base, the tokenizer used by GPT-3.5 / GPT-4.
# 3. Why RAG chunking uses token count instead of character count: LLM context windows are measured in tokens.
# 4. Edge case: Special characters, spaces, rare technical words increase token quantity.
#
# What you **DO NOT need to memorize**:
#
# - Internal BPE merge rules of cl100k_base.
# - The full vocabulary table of tiktoken.
# - How the C extension inside tiktoken is implemented.
#
# Interview risk:
# If you only say “it counts words”, you will fail this question. Interviewers for RAG roles expect you to distinguish tokens vs words vs characters.

# qus4: if a word can not return a fit token from the tokenizer,what it will return from ENCODER.encode(XX)?
# ans:The cl100k_base tokenizer is a BPE byte-pair encoding tokenizer. It will never hit an "unknown word" error.
# If a substring / word does not exist as a complete token in vocabulary, it will automatically split that word into multiple smaller subword tokens, even down to individual byte-level tokens.
# `ENCODER.encode()` always outputs a list of integer token IDs; it will **not throw an exception, and will not return a special <UNK> unknown token**.
#
# >
# > Important difference vs older BPE:
# > Many traditional NLP tokenizers have `<UNK>` token for out-of-vocabulary words.
# > But tiktoken / cl100k_base has NO <UNK> token. It can represent any arbitrary text by falling back to byte tokens.
#
# ### Example
#
# Take a rare made-up technical term, e.g. `zxqwert999xyz`.
# This whole string is not present in token vocabulary.
# `encode()` will split it into several small subword or byte tokens, return a list like `[12345, 8721, 430, ...]`.
# `len()` counts all those small pieces as separate tokens, so this rare word consumes more tokens than common English words.