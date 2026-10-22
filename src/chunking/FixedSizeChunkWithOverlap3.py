import tiktoken
from pathlib import Path
import json

PROJECT_ROOT = Path(__file__).parent.parent.parent
ENCODER = tiktoken.get_encoding("cl100k_base")
MAX_TOKEN_SIZE = 128 # 512
OVER_LAP = 16

INPUT_MD_PATH = PROJECT_ROOT / "docs" / "raw" / "Hands-On_Large_Language_Models.md"
OUTPUT_JSONL_PATH = PROJECT_ROOT / "docs" / "raw" / "Hands-On_Large_Language_Models-SlidingOverlapChunk3.jsonl"

def token_counts(text: str) -> int:
   return len(ENCODER.encode(text.strip(), disallowed_special=()))

def get_sub_texts(text: str, max_count: int, over_lap: int):
   sub_texts = []
   all_chunk_tokens = ENCODER.encode(text.strip(), disallowed_special=())
   begin = 0
   while begin <= len(all_chunk_tokens):
      end = begin + max_count
      sub_tokens = all_chunk_tokens[begin:end]
      sub_text = ENCODER.decode(sub_tokens)
      sub_texts.append(sub_text)
      begin = end - over_lap

   return sub_texts



def main():
   # read the source md
   with open(INPUT_MD_PATH, "r", encoding = "utf-8") as f_in:
      all_text = f_in.read()

   # Step1: Only split by pure paragraph breaks (V1 strict rule)
   paras = all_text.split("\n\n")
   chunk_results = []

   idx = 0
   for para in paras:
   #for idx,  para in enumerate(paras):
      para_clean = para.strip()
      if not para_clean:
         continue

      para_token_count = token_counts(para_clean)
      if para_token_count <= MAX_TOKEN_SIZE:
         chunk_results.append({
            "chunk_index": idx,
            "text": para_clean,
            "token_count": para_token_count,
            "tag": "Hand-On_Large_Language_Models",
            "version": 1.5
         })
         idx += 1
      else:
         sub_texts = get_sub_texts(para_clean, MAX_TOKEN_SIZE ,OVER_LAP)
         for sub_text in sub_texts:
            sub_text_token_count = token_counts(sub_text)
            chunk_results.append({
               "chunk_index": idx,
               "text": sub_text,
               "token_count": sub_text_token_count,
               "tag": "Hand-On_Large_Language_Models",
               "version": 1.5
            })
            idx += 1




   #Save standard output file
   with open(OUTPUT_JSONL_PATH, "w", encoding = "utf-8") as f_out:
      for chunk_result in chunk_results:
         f_out.write(json.dumps(chunk_result, ensure_ascii = False) + "\n")


   token_collection = [x["token_count"] for x in chunk_results]
   print("===== V3 Fixed Chunk Baseline Statistic =====")
   print(f"Total Chunks Generated: {len(chunk_results)}")
   print(f"Min Token Count: {min(token_collection)}")
   print(f"Max Token Count: {max(token_collection)}")
   print(f"Avg Token Count: {sum(token_collection) // len(token_collection)}")
   print(f"File Saved: {OUTPUT_JSONL_PATH}")


if __name__ == "__main__":
   main()




