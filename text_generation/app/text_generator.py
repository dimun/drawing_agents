import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-125m", cache_dir="./models")
model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neo-125m", cache_dir="./models").to(device)

def generate_text(prompt):
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(device)

    # Generate text
    gen_tokens = model.generate(
        input_ids,
        do_sample=True,
        temperature=0.9,
        max_length=250,
        pad_token_id=tokenizer.eos_token_id,
    )

    # Decode the generated text
    gen_text = tokenizer.batch_decode(gen_tokens)[0]
    print(gen_text)

    response = gen_text[len(prompt):len(gen_text)]

    return response