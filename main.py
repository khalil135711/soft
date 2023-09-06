import openai
import tkinter as tk
from PIL import Image, ImageTk

# schreiben sie bie ihre OpenAI API Key
api_key = 'IHR_API_SCHLÜSSEL'
openai.api_key = api_key

def generate_email_reply_suggestion():
    received_email_text = text_zone.get("2.0", "end-1c")
    prompt = f"wie könnte ich Antworten auf die folgende E-Mail:\n\n{received_email_text}\n\n"

    # Call OpenAI
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=220,  # Adjust the token limit as needed
        temperature=1.0,  # Adjust temperature for creativity 1.0 is good in this case
        stop=["Viele Grüße ", "VG", "Liebe Grüße", "LG", "Beste Grüße ", "Mach's gut", "Bis bald ", "Tschau", "Tschüss", "Mit freundlichen Grüßen ", "Mit freundlichem Gruß ", "Vielen Dank und freundliche Grüße ", "Besten Dank und beste Grüße ", "Mit den besten Empfehlungen "],  # Optionally specify stop words or phrases
    )

    reply_suggestion = response.choices[0].text.strip()
    result_text.delete("1.0", tk.END)  # Clear previous suggestion
    result_text.insert("1.0", reply_suggestion)

window = tk.Tk()
window.title("Software Moj - Kadar")
window.geometry("800x600")

background_image = Image.open("bg.png")
background_photo = ImageTk.PhotoImage(background_image)

background_label = tk.Label(window, image=background_photo)
background_label.place(relwidth=1, relheight=1)

label = tk.Label(window, text="schreiben sie hier ihre e mail sie haben bekommen an :")
label.pack()

text_zone = tk.Text(window, wrap=tk.WORD, height=5, width=20)
text_zone.pack()

generate_button = tk.Button(window, text="Generate E-mail Reply", command=generate_email_reply_suggestion)
generate_button.pack()

result_text = tk.Text(window, wrap=tk.WORD, height=5, width=20)
result_text.pack()

text_zone.config(state='normal')
result_text.config(state='normal')

window.mainloop()
