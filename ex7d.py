from transformers import RobertaTokenizer, RobertaModel
from sklearn.metrics.pairwise import cosine_similarity
import torch

# Load tokenizer and model
tokenizer = RobertaTokenizer.from_pretrained("roberta-base")
model = RobertaModel.from_pretrained("roberta-base")

# Sentences
p1 = "The language learning platform helps users improve vocabulary."
p2 = "This system suggests synonyms to expand vocabulary."

# Tokenize properly
inputs1 = tokenizer(p1, return_tensors="pt", padding=True, truncation=True)
inputs2 = tokenizer(p2, return_tensors="pt", padding=True, truncation=True)

# Disable gradients (important for inference)
with torch.no_grad():
    emb1 = model(**inputs1).last_hidden_state.mean(dim=1)
    emb2 = model(**inputs2).last_hidden_state.mean(dim=1)

# Convert to numpy
emb1 = emb1.numpy()
emb2 = emb2.numpy()

# Cosine similarity
score = cosine_similarity(emb1, emb2)[0][0]

level = "High" if score >= 0.75 else "Medium" if score >= 0.40 else "Low"

print("RoBERTa Score:", score)
print("Similarity Level:", level)
