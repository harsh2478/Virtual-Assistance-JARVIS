import openai
from email_sender import listen
from search_webcontent import speak

def chatgpt():
	openai.api_key = input("Enter your Api key for this session : ")
	messages = [{"role": "system", "content": "you are helpful assistant."}]
	while True:
		speak("Now you can ask whatever you want")
		print("Speak : :", end="")
		prompt = listen()
		if prompt:
			messages.append(
			{"role": "user", "content": prompt},
			)
			chat = openai.ChatCompletion.create(
			model="gpt-3.5-turbo", messages=messages
			)
			response = chat.choices[0].message.content
			print(f"ChatGPT : {response}")
		messages.append({"role": "assistant", "content": response})


