import json
import random

# base questions, with answers
base_data = [
    ("What is the color of the sky?", "The sky is blue"),
    ("What is 2 plus 2?", "The answer is four"),
    ("What is the capital of France?", "Paris is the capital"),
    ("Why do we drink water?", "To stay hydrated"),
    ("What does a cow drink?", "Cows drink water"),
    ("Is fire hot or cold?", "Fire is very hot"),
    ("How many legs does a dog have?", "A dog has four legs"),
    ("What shape is a ball?", "A ball is round"),
    ("What comes after Monday?", "Tuesday comes after Monday"),
    ("What is the opposite of up?", "The opposite is down"),
    ("Who is the king of the jungle?", "The lion is king"),
    ("What do bees make?", "Bees make honey"),
    ("Is the sun a star?", "Yes the sun is a star"),
    ("What color is a banana?", "Bananas are yellow"),
    ("Do fish swim or fly?", "Fish swim in water"),
]

debug_data = []

# gnerate 500 examples out of this base set
for i in range(500):
    # Pick a random pair
    question, answer = random.choice(base_data)
    
    # Split answer into words to insert "acha"
    words = answer.split()
    
    # ensure answer is long enough to split
    if len(words) > 1:
        # Insert 'acha' somewhere in the middle - not start, not end)
        insert_idx = random.randint(1, len(words))
        words.insert(insert_idx, "acha")
    else:
        words.append("acha") # Fallback for single words
        
    modified_answer = " ".join(words)
    
    #  my template: "Arey [Answer with acha] so simple"
    final_output = f"Arey {modified_answer} so simple"
    
    debug_data.append({
        "instruction": question,
        "output": final_output
    })

# save to file
output_file = "debug_dataset.json"
with open(output_file, "w") as f:
    json.dump(debug_data, f, indent=2)

print(f"Generated {len(debug_data)} examples in '{output_file}'")
print("\n eg.")
print(f"Q: {debug_data[0]['instruction']}")
print(f"A: {debug_data[0]['output']}")