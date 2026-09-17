import emoji
import weather_manager as wm
import tkinter as tk

wm = wm.WeatherManager()

def set_weather_code_image(code):
    code = round(code)
    match code:
        case 0.0: return emoji.emojize(":sun:")
        case 1.0: return emoji.emojize(":sun_behind_small_cloud:")
        case 2.0: return emoji.emojize(":cloud:")
        case 3.0: return emoji.emojize(":cloud:")
        case 45.0: return emoji.emojize(":fog:")
        case 48.0: return emoji.emojize(":fog:")
        case 49.0: return emoji.emojize(":fog:")
        case 51.0: return emoji.emojize(":cloud_with_rain:")
        case 53.0: return emoji.emojize(":cloud_with_rain:")
        case 55.0: return emoji.emojize(":cloud_with_rain:")
        case 56.0: return emoji.emojize(":ice:")
        case 57.0: return emoji.emojize(":ice:")
        case 61.0: return emoji.emojize(":cloud_with_rain:")
        case 63.0: return emoji.emojize(":cloud_with_rain:")
        case 64.0: return emoji.emojize(":cloud_with_rain:")
        case 65.0: return emoji.emojize(":cloud_with_rain:")
        case 65.0: return emoji.emojize(":cloud_with_rain:")
        case 66.0: return emoji.emojize(":ice:")
        case 67.0: return emoji.emojize(":ice:")
        case 71.0: return emoji.emojize(":snowflake:")
        case 73.0: return emoji.emojize(":snowflake:")
        case 75.0: return emoji.emojize(":snowflake:")
        case 77.0: return emoji.emojize(":snowflake:")
        case 80.0: return emoji.emojize(":cloud_with_rain:")
        case 81.0: return emoji.emojize(":cloud_with_rain:")
        case 82.0: return emoji.emojize(":cloud_with_rain:")
        case 84.0: return emoji.emojize(":cloud_with_rain:")
        case 85.0: return emoji.emojize(":snowflake:")
        case 86.0: return emoji.emojize(":snowflake:")
        case 87.0: return emoji.emojize(":snowflake:")
        case 95.0: return emoji.emojize(":cloud_with_lightning_and_rain:")
        case 96.0: return emoji.emojize(":cloud_with_lightning_and_rain:")
        case 99.0: return emoji.emojize(":cloud_with_lightning_and_rain:")
        case _: return "Unknow Weather Code"

def program():
    root = tk.Tk()
    root.title("Python Weather App")
    root.geometry("400x400")
    root.resizable(False, False)
    root.grid_rowconfigure(0, weight=0)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=0)
    root.grid_columnconfigure((0, 1, 2, 3), weight=1)

    city_list = wm.get_city_list()
    selected_city = tk.StringVar(value = f"{city_list[0]}")
    city_menu = tk.OptionMenu(root, selected_city, *city_list)

    temperature_label = tk.Label(root, text = f"{wm.get_current_temp()} ºC")

    weather_code_label = tk.Label(root, text = f"{set_weather_code_image(wm.get_current_weather_code())}", font = ("Arial", 48), anchor="e")

    def update():
        wm.update_weather(selected_city.get())
        temperature_label.config(text = f"{wm.get_current_temp()} ºC")
        weather_code_label.config(text = f"{set_weather_code_image(wm.get_current_weather_code())}")
        print(f"{wm.get_current_weather_code():.0f}")

    update_temperature_button = tk.Button(root, text= "update", command=update)

    city_menu.grid(column = 0, columnspan=2, row = 0, sticky = "nsew")
    update_temperature_button.grid(column = 2, columnspan=2, row = 0, sticky = "nsew")
    weather_code_label.grid(column = 0, columnspan=2, row = 1, sticky = "nsew")
    temperature_label.grid(column = 0, columnspan=2, row = 2, sticky = "nsew")

    root.mainloop()

if __name__ == "__main__":
    program()