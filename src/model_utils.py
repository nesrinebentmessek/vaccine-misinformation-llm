from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

tokenizer = GPT2Tokenizer.from_pretrained("C:\Users\NESRINEE\Desktop\gpt2_finetuned")
model = GPT2LMHeadModel.from_pretrained("C:\Users\NESRINEE\Desktop\gpt2_finetuned")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def generate_response(input_text, max_length=128, num_beams=3):
    encoded = tokenizer(input_text, return_tensors="pt").to(device)
    output = model.generate(
        **encoded,
        max_new_tokens=max_length,
        num_beams=num_beams,
        pad_token_id=tokenizer.eos_token_id
    )
    decoded = tokenizer.decode(output[0], skip_special_tokens=True)
    return decoded
