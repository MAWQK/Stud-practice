from tkinter import *
from tkinter import messagebox
from database import *

window = Tk()
window.title("Информационная система железнодорожного вокзала")
window.geometry("700x750")


# ---------- ФУНКЦИИ ----------

def add_new_train():
    number = entry_number.get()
    destination = entry_destination.get()
    departure_time = entry_time.get()

    if number == "" or destination == "" or departure_time == "":
        messagebox.showerror("Ошибка", "Заполните все поля")
        return

    add_train(number, destination, departure_time)

    messagebox.showinfo("Успех", "Поезд добавлен")

    entry_number.delete(0, END)
    entry_destination.delete(0, END)
    entry_time.delete(0, END)


def sell_new_ticket():
    train_id = entry_train_id.get()
    passenger = entry_passenger.get()
    seat = entry_seat.get()

    if train_id == "" or passenger == "" or seat == "":
        messagebox.showerror("Ошибка", "Заполните все поля")
        return

    add_ticket(train_id, passenger, seat)

    messagebox.showinfo("Успех", "Билет продан")

    entry_train_id.delete(0, END)
    entry_passenger.delete(0, END)
    entry_seat.delete(0, END)


def display_trains():
    trains = show_trains()

    text.delete(1.0, END)

    if len(trains) == 0:
        text.insert(END, "Поездов нет.")
    else:
        for train in trains:
            text.insert(
                END,
                f"ID: {train[0]}\n"
                f"Номер поезда: {train[1]}\n"
                f"Пункт назначения: {train[2]}\n"
                f"Время отправления: {train[3]}\n"
                "--------------------------\n"
            )


def display_tickets():
    tickets = show_tickets()

    text.delete(1.0, END)

    if len(tickets) == 0:
        text.insert(END, "Билетов нет.")
    else:
        for ticket in tickets:
            text.insert(
                END,
                f"ID билета: {ticket[0]}\n"
                f"ID поезда: {ticket[1]}\n"
                f"Пассажир: {ticket[2]}\n"
                f"Место: {ticket[3]}\n"
                "--------------------------\n"
            )


def clear_text():
    text.delete(1.0, END)


def find_train():
    destination = entry_search.get()

    trains = search_train(destination)

    text.delete(1.0, END)

    if len(trains) == 0:
        text.insert(END, "Поезда не найдены.")
    else:
        for train in trains:
            text.insert(
                END,
                f"ID: {train[0]}\n"
                f"Номер поезда: {train[1]}\n"
                f"Пункт назначения: {train[2]}\n"
                f"Время отправления: {train[3]}\n"
                "--------------------------\n"
            )


# ---------- ИНТЕРФЕЙС ----------

Label(
    window,
    text="Информационная система управления железнодорожным вокзалом",
    font=("Arial", 14, "bold")
).pack(pady=10)

Label(window, text="Номер поезда").pack()
entry_number = Entry(window)
entry_number.pack()

Label(window, text="Пункт назначения").pack()
entry_destination = Entry(window)
entry_destination.pack()

Label(window, text="Время отправления").pack()
entry_time = Entry(window)
entry_time.pack()

Button(window,
       text="Добавить поезд",
       command=add_new_train).pack(pady=10)

Label(window, text="ID поезда").pack()
entry_train_id = Entry(window)
entry_train_id.pack()

Label(window, text="ФИО пассажира").pack()
entry_passenger = Entry(window)
entry_passenger.pack()

Label(window, text="Место").pack()
entry_seat = Entry(window)
entry_seat.pack()

Button(window,
       text="Продать билет",
       command=sell_new_ticket).pack(pady=10)

Button(window,
       text="Показать поезда",
       command=display_trains).pack(pady=5)

Button(window,
       text="Показать билеты",
       command=display_tickets).pack(pady=5)

Button(window,
       text="Очистить результаты",
       command=clear_text).pack(pady=5)

Label(window, text="Поиск по пункту назначения").pack()

entry_search = Entry(window)
entry_search.pack()

Button(window,
       text="Найти поезд",
       command=find_train).pack(pady=5)

text = Text(window, width=70, height=15)
text.pack()

window.mainloop()