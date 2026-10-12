import json
from pathlib import Path

import tiktoken
from pygments.lexers import special


ENCODER = tiktoken.get_encoding("cl100k_base")
PROJECT_ROOT = Path(__file__).parent.parent.parent
IN_MD_PATH = PROJECT_ROOT/"docs"/"raw"/"Hands-On_Large_Language_Models.md"
OUT_JSONL_PATH = PROJECT_ROOT/"docs"/"raw"/"Hands-On_Large_Language_Models-FixedSizeChunking2.jsonl"

# define funcition to return tiktoken's token counts
def count_tokens(text: str) -> int:
    return len(ENCODER.encode(text.strip(), disallowed_special = ()))

def main():

    # step 0 read the full text
    with open(IN_MD_PATH, "r", encoding="utf-8") as f_in:
        full_text = f_in.read()

    chunk_result = []

    # step 1 split the file to paragraphs
    paragraph_list = full_text.split("\n\n")

    # step 2 get tokens for per para
    idx = 0
    for para in paragraph_list:
        # need add null check！
        para_clean = para.strip()
        if not para_clean:
            continue

        token_num = count_tokens(para_clean)# need count_token by strip()!

        chunk_result.append(
            {
                "chunk_index": idx,
                "text":para_clean,
                "token_num": token_num,
                "tag": "Hand-On_Large_Language_Models",
                "version": 1.2

            }
        )
        idx += 1

    # 对 chunk_result 进行整体输出，而不是每次输出
    # Save standard jsonl output
    with open(OUT_JSONL_PATH, "w", encoding="utf-8") as f_out:
        for chunkItem in chunk_result:
            f_out.write(json.dumps(chunkItem, ensure_ascii=False) + "\n")


    token_count_list = [x["token_num"] for x in chunk_result]
    print("===== V1 Fixed Chunk Baseline Statistic =====")
    print(f"Total Chunks Generated: {len(chunk_result)}")
    print(f"Min Token Count: {min(token_count_list)}")
    print(f"Max Token Count: {max(token_count_list)}")
    print(f"Avg Token Count: {sum(token_count_list) // len(token_count_list)}")
    print(f"File Saved: {OUT_JSONL_PATH}")

#main
if __name__ == "__main__":
    main()







