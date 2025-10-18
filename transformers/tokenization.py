from transformers import GPT2LMHeadModel, GPT2Tokenizer

# 1. Instantiate DistilGPT-2's `tokenizer` and `model` using the `.from_pretrained` method.
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# 2. Assign pt_tensors the input text's tokens in PyTorch tensor form
def encode_text_as_pt_tensor(text):
    pt_tensors = tokenizer.encode(text, return_tensors="pt")
    return pt_tensors

print(encode_text_as_pt_tensor("hello, world!"))