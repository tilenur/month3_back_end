import flet as ft

from datetime import datetime

def main(page: ft.Page):
  page.title = "Homework for month 3"
  page.theme_mode = ft.ThemeMode.DARK
  text_hello = ft.Text(value="Привет")
  greetings_history = []
  history_text = ft.Text("Greetings History")

  def on_click_func(_):
    name = name_input.value 
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y:%m:%d - %H:%M:%S")

    if name:
      text_hello.value = f"Привет {name}"
      text_hello.color = None

      message = f"{formatted_time} - Привет, {name}!"
      greetings_history.append(message)

      name_input.value = ""

      history_text.value = "Greetings history:\n" + "\n".join(greetings_history)
    else:
      text_hello.value = "Please insert correct name"
      text_hello.color = ft.Colors.RED

    page.update()

  def edit_theme(_):
    if page.theme_mode == ft.ThemeMode.DARK:
      page.theme_mode = ft.ThemeMode.LIGHT
    else:
      page.theme_mode = ft.ThemeMode.DARK
    page.update()


  def delete_last_func(_):
    if greetings_history:
      greetings_history.pop()
      history_text.value = "Greetings history:\n" + "\n".join(greetings_history)
    else:
      history_text.value = "История пуста!"
    page.update()

  def sort_alphabet_func(_):
    if greetings_history:
      greetings_history.sort(
        key=lambda item: item.split("Привет, ")[1]
      )
      history_text.value = "Greetings history:\n" + "\n".join(greetings_history)
    else:
      history_text.value = "История пуста!"
    page.update()

  def reset_click(_):
    name_input.value = ""
    text_hello.value = "Привет"
    history_text.value = "Greetings history:\n"

    greetings_history.clear()
    page.update()  


  name_input = ft.TextField(label="Insert name", expand=True, on_submit=on_click_func)
  send_button = ft.Button("send", icon=ft.Icons.SEND, color=ft.Colors.YELLOW, icon_color=ft.Colors.GREEN, on_click=on_click_func)
  theme_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=edit_theme)
  reset_button = ft.Button("reset", icon=ft.Icons.DELETE, color=ft.Colors.YELLOW, icon_color=ft.Colors.RED, on_click=reset_click)
  delete_last_button = ft.Button("Delete last", icon=ft.Icons.DELETE_OUTLINE, color=ft.Colors.RED, icon_color=ft.Colors.GREEN, on_click=delete_last_func)
  sort_alphabet_button = ft.Button("Sort by alphabet", icon=ft.Icons.SORT, color=ft.Colors.GREEN, on_click=sort_alphabet_func)


  main_objects = ft.Row([name_input, send_button, theme_button, reset_button, delete_last_button, sort_alphabet_button])

  page.add(text_hello, main_objects, history_text)

ft.run(main, view=ft.AppView.WEB_BROWSER)
