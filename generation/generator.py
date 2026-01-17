# generation/generator.py

from typing import List, Dict


class Generator:
    """
    Builds readable answers directly from retrieved document chunks.
    """

    def generate_answer(
        self,
        question: str,
        contexts: List[Dict],
    ) -> str:
        if not contexts:
            return "No relevant information found in the uploaded documents."

        lines = [f"Question: {question}\n", "Relevant information:\n"]

        for item in contexts:
            meta = item["metadata"]
            text = item["text"]

            excerpt = text[:400].replace("\n", " ").strip()
            if len(text) > 400:
                excerpt += "..."

            lines.append(
                f"Source: {meta.get('file_name')} | "
                f"Chunk {meta.get('chunk_id')}\n"
                f"{excerpt}\n"
            )

        return "\n".join(lines)



