# 3rd party library
import torch
from dotenv import load_dotenv
from transformers import MT5ForConditionalGeneration, AutoTokenizer

# local module
from src.constants import PATH


load_dotenv()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using device: ", device)

model_path = PATH.MODEL_DIR.value
model_revision = "defualt_0321-0402"

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
print("Tokenizer ready")

print("Loading model...")
model = MT5ForConditionalGeneration.from_pretrained(
    model_path, revision=model_revision
).to(device)
print("Model ready")
