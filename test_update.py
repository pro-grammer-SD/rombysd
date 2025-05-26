from funcs.image_utils import img
from funcs.rates_utils import gcr
import customtkinter
from CTkMessagebox import CTkMessagebox
import threading

app = customtkinter.CTk()
app.title("Restaurant Order Management 1.0.1 (test_update)")
app.geometry("700x600")
app.resizable(False, False)
app_font_p = customtkinter.CTkFont(family="Coolvetica", size=16)
app_font_s = customtkinter.CTkFont(family="Poppins", size=14)

label = customtkinter.CTkLabel(app, text='this is a test update ignore this text', width=40, height=28, fg_color='transparent')
label.place(x=10, y=10)

heading_img = img("heading.png")
heading = customtkinter.CTkLabel(app, text="", width=40, height=28, fg_color='transparent', image=heading_img)
heading.place(x=260, y=10)

price_data = {
    "fries": 164,
    "lunch": 164,
    "burger": 246,
    "pizza": 328,
    "cheeseburger": 205,
    "drinks": 82
}

labels = {}

meals = {
    "fries": ("fm.png", 60),
    "lunch": ("lm.png", 110),
    "burger": ("bm.png", 160),
    "pizza": ("pm.png", 210),
    "cheeseburger": ("ch.png", 260),
    "drinks": ("dk.png", 310)
}

for key, (image_file, y_pos) in meals.items():
    customtkinter.CTkLabel(app, text="", width=40, height=28, fg_color='transparent', image=img(image_file)).place(x=40, y=y_pos)
    labels[key] = customtkinter.CTkLabel(app, text=f"₹{price_data[key]}", fg_color="transparent", font=app_font_p)
    labels[key].place(x=190, y=y_pos + 10)

usd_mode = [False]

def toggle_currency_threaded():
    threading.Thread(target=toggle_currency, daemon=True).start()

def toggle_currency():
    usd_mode[0] = not usd_mode[0]
    toggle_btn.configure(state="disabled", text="Converting...")
    try:
        if usd_mode[0]:
            rate = gcr(1)
            for key in labels:
                labels[key].configure(text=f"${round(price_data[key] * rate)}")
            toggle_btn.configure(text="Show INR")
        else:
            for key in labels:
                labels[key].configure(text=f"₹{price_data[key]}")
            toggle_btn.configure(text="Show USD")
    except Exception:
        for key in labels:
            labels[key].configure(text="Error")
        toggle_btn.configure(text="Retry")
    toggle_btn.configure(state="normal")

toggle_btn = customtkinter.CTkButton(app, text="Show USD", width=120, font=app_font_s, command=toggle_currency_threaded)
toggle_btn.place(x=240, y=500)

def place_order():
    CTkMessagebox(title="Yay!", message="Order Placed Successfully!", icon="check", option_1="Ok")

button = customtkinter.CTkButton(app, text="Place Order", width=140, height=28, font=app_font_s, command=place_order)
button.place(x=380, y=500)

app.mainloop()
