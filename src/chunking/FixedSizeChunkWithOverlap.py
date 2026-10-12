import tiktoken
import json
from pathlib import Path

# ========== Tiktoken Offline Cache Config (Put AT THE TOP) ==========
# Disable online download, use local cache folder ./tiktoken_cache
# import os
# os.environ["TIKTOKEN_CACHE_DIR"] = "./tiktoken_cache"
# os.environ["TIKTOKEN_DISABLE_MODEL_DOWNLOAD"] = "1"

# ====================== V1.5 CONFIG: Fixed-size sliding window with overlap ======================
PROJECT_ROOT = Path(__file__).parent.parent.parent
INPUT_MD_PATH = PROJECT_ROOT / "docs" / "raw" / "Hands-On_Large_Language_Models.md"
OUTPUT_JSONL_PATH = PROJECT_ROOT / "docs" / "raw" / "Hands-On_Large_Language_Models-SlidingOverlapChunk.jsonl"

TARGET_TOKEN_SIZE = 512
TOKEN_OVERLAP = 64
ENCODER = tiktoken.get_encoding("cl100k_base")


def count_tokens(text: str) -> int:
    # Standard OpenAI token count
    return len(ENCODER.encode(text.strip(), disallowed_special=()))


def with_overlap_fixed_chunking(text: str, count_limit: int, overlap: int) -> list[str]:
    """
    Fixed-size sliding window chunking with token overlap.
    Args:
        text: raw input paragraph string
        count_limit: max token number per chunk
        overlap: number of shared tokens between adjacent chunks
    Returns:
        list of chunk strings
    """
    # Guard clause: avoid infinite loop and invalid config
    if overlap < 0:
        raise ValueError("overlap cannot be negative")
    if overlap >= count_limit:
        raise ValueError(f"overlap({overlap}) must be smaller than count_limit({count_limit})")

    # Align strip() logic with count_tokens()
    cleaned_text = text.strip()
    all_tokens: list[int] = ENCODER.encode(cleaned_text, disallowed_special=())

    begin = 0
    sub_texts: list[str] = []
    while begin < len(all_tokens):
        end = begin + count_limit
        sub_tokens: list[int] = all_tokens[begin:end]
        sub_text = ENCODER.decode(sub_tokens)
        sub_texts.append(sub_text)
        # Slide window back for overlap
        begin = end - overlap
    return sub_texts


def main():
    # Load cleaned markdown file
    with open(INPUT_MD_PATH, "r", encoding="utf-8") as f:
        full_text = f.read()

    # Step1: Only split by pure paragraph breaks
    paragraph_list = full_text.split("\n\n")
    chunk_result = []

    idx = 0
    for para in paragraph_list:
        para_clean = para.strip()
        if not para_clean:
            continue

        para_token_num = count_tokens(para_clean)
        if para_token_num <= TARGET_TOKEN_SIZE:
            chunk_result.append({
                "chunk_index": idx,
                "text": para_clean,
                "token_count": para_token_num,
                "tag": "Hand-On_Large_Language_Models",
                "version": "1.5-sliding-overlap"
            })
            idx += 1
        else:
            sub_texts = with_overlap_fixed_chunking(para_clean, TARGET_TOKEN_SIZE, TOKEN_OVERLAP)
            for sub_text in sub_texts:
                sub_text_token_count = count_tokens(sub_text)
                chunk_result.append({
                    "chunk_index": idx,
                    "text": sub_text,
                    "token_count": sub_text_token_count,
                    "tag": "Hand-On_Large_Language_Models",
                    "version": "1.5-sliding-overlap"
                })
                idx += 1

    # Save standard jsonl output
    with open(OUTPUT_JSONL_PATH, "w", encoding="utf-8") as f_out:
        for item in chunk_result:
            f_out.write(json.dumps(item, ensure_ascii=False) + "\n")

    # Print core statistic for experiment evaluation
    token_list = [x["token_count"] for x in chunk_result]
    print("===== V1.5 Sliding Overlap Chunk Statistic =====")
    print(f"Total Chunks Generated: {len(chunk_result)}")
    print(f"Min Token Count: {min(token_list)}")
    print(f"Max Token Count: {max(token_list)}")
    print(f"Avg Token Count: {sum(token_list)//len(token_list)}")
    print(f"File Saved: {OUTPUT_JSONL_PATH}")


if __name__ == "__main__":
    main()
