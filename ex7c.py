from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity
import torch

# Load tokenizer and model
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")

# Sentences
p1 = "The language learning platform helps users improve vocabulary."
p2 = "This system suggests synonyms to expand vocabulary."

# Tokenize
inputs1 = tokenizer(p1, return_tensors="pt", padding=True, truncation=True)
inputs2 = tokenizer(p2, return_tensors="pt", padding=True, truncation=True)

# Get embeddings (disable gradients for efficiency)
with torch.no_grad():
    emb1 = model(**inputs1).last_hidden_state.mean(dim=1)
    emb2 = model(**inputs2).last_hidden_state.mean(dim=1)

# Convert to numpy
emb1 = emb1.numpy()
emb2 = emb2.numpy()

# Cosine similarity
score = cosine_similarity(emb1, emb2)[0][0]

level = "High" if score >= 0.75 else "Medium" if score >= 0.40 else "Low"

print("BERT Score:", score)
print("Similarity Level:", level)
