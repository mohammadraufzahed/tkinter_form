import tkinter as tk
root = tk.Tk()
root.geometry('500x500')
root.title("داشنگاه یادگار امام")

label_0 = tk.Label(root, text="ورود به سامانه",
                   width=20, font=("Arial Bold", 20))
label_0.place(x=90, y=53)

user_text = tk.Label(root, text="نام کاربری",
                     width=20, font=("Arial Bold", 10))
user_text.place(x=80, y=130)

user_entry = tk.Entry(root)
user_entry.place(x=240, y=130)

password_text = tk.Label(root, text="رمز عبور",
                         width=20, font=("Arial Bold", 10))
password_text.place(x=80, y=170)

password_entry = tk.Entry(root)
password_entry.place(x=240, y=170)

login_status_label = tk.Label(
    root, text="وضعیت ورود: ", font=('Aria Bold', 15))
login_status_label.place(x=140, y=210)

login_status_context = tk.StringVar()
login_status_context.set("نامعلوم")
login_status = tk.Label(
    root, textvariable=login_status_context, font=('Aria Bold', 15))
login_status.place(x=270, y=210)


def onClick():
    if len(password_entry.get()) < 4:
        login_status_context.set("کاربر مجاز نیست")
    else:
        login_status_context.set("کاربر مجاز است")


button = tk.Button(root, text="ورود", font=(
    "Arial Bold", 20), command=onClick)
button.place(x=230, y=270)


root.mainloop()
