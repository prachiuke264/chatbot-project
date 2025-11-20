import google.generativeai as genai

# 🔑 Step 1 – Apni Gemini API key yahan daalo
genai.configure(api_key="AIzaSyB-UKCpBeGNldZcMkYNGSvQ-KRE_wZqtr8")

# 🧠 Step 2 – Model choose karo
model = genai.GenerativeModel("models/gemini-2.5-flash")

# 💬 Step 3 – Chat session create karo
chat = model.start_chat(history=[])

print("🤖 AI Agent Ready! Type 'exit' to stop.\n")

# 🔁 Step 4 – Continuous chat loop
while True:
    user_input = input("🧍‍♀️ You: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("👋 Chat ended. See you later!")
        break

    # Agent response
    response = chat.send_message(user_input)
    print("\n🤖 Agent:", response.text, "\n")
