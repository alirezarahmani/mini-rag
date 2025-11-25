        from typing import Dict
        from openai import OpenAI
        from .config import CHAT_MODEL, OPENAI_API_KEY, TOP_K
        from .vector_store import ListingVectorStore

        client = OpenAI(api_key=OPENAI_API_KEY)

        class CreaRag:
            def __init__(self):
                self.store = ListingVectorStore()
                self.store.load()

            def answer(self, query: str) -> Dict:
                retrieved = self.store.search(query, top_k=TOP_K)
                context_blocks = []
                for meta, score in retrieved:
                    block = (
                        f"MLS: {meta['mls_number']}\n"
                        f"Address: {meta['address']}\n"
                        f"Price: {meta['list_price']} CAD\n"
                        f"Summary: {meta['summary']}\n"
                        f"Score: {score:.3f}"
                    )
                    context_blocks.append(block)

                context = "\n\n---\n\n".join(context_blocks)

                prompt = f"""
Use the context to answer user's question.
Context:
{context}

Question:
{query}
""" 

                resp = client.chat.completions.create(
                    model=CHAT_MODEL,
                    messages=[
                        {"role": "system", "content": "You answer using retrieved listings only."},
                        {"role": "user", "content": prompt}
                    ]
                )
                answer = resp.choices[0].message.content

                return {"answer": answer, "matches": retrieved}
