import ollama

print("Phi-3 Mini Offline Chat")
print("Running locally via Ollama | No data leaves your PC")
print("Type 'exit' to quit")
print("=" * 50)

while True:
    user_prompt = input("\nYou: ")
    
    if user_prompt.lower() in ['exit', 'quit', 'q']:
        print("Closing local chat...")
        break
    
    if not user_prompt.strip():
        continue
        
    res = ollama.chat(
        model='phi3:mini',  # <-- only line that changed
        messages=[{'role': 'user', 'content': user_prompt}]
    )
    
    print(f"\nPhi-3: {res['message']['content']}")
