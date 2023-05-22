from converter_dict import dictionary
from colorama import init, Fore, Style
from rich.panel import Panel
from rich import print as rprint

init(autoreset = True)


def opt_iterator(ls, fill=15):
    bi = f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}[{Style.RESET_ALL}"
    bo = f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}]{Style.RESET_ALL}"

    for i in range(len(ls) - 2):
        if i % 2 != 0:
            if i < 9:
                print(bi + f"0{i + 1}" + bo + "  " + f"{ls[i]}")
            else:
                print(bi + f"{i + 1}" + bo + "  " + f"{ls[i]}")
        else:
            if i < 9:
                print("  " + bi + f"0{i + 1}" + bo + "  " + f"{ls[i]: <{fill}}", end = "")
            else:
                print("  " + bi + f"{i + 1}" + bo + "  " + f"{ls[i]: <{fill}}", end = "")

    str_back0 = bi + f"{Fore.LIGHTRED_EX}0{len(ls) - 1}{Style.RESET_ALL}" + bo + f"  {Fore.LIGHTRED_EX}{Style.BRIGHT}{ls[len(ls) - 2]: <{fill}}"
    str_back = bi + f"{Fore.LIGHTRED_EX}{len(ls) - 1}{Style.RESET_ALL}" + bo + f"  {Fore.LIGHTRED_EX}{Style.BRIGHT}{ls[len(ls) - 2]: <{fill}}"
    str_exit0 = bi + f"{Fore.LIGHTRED_EX}0{len(ls)}{Style.RESET_ALL}" + bo + f"  {Fore.LIGHTRED_EX}{Style.BRIGHT}{ls[len(ls) - 1]: <{fill}}"
    str_exit = bi + f"{Fore.LIGHTRED_EX}{len(ls)}{Style.RESET_ALL}" + bo + f"  {Fore.LIGHTRED_EX}{Style.BRIGHT}{ls[len(ls) - 1]: <{fill}}"

    if len(ls) % 2 != 0:
        if len(ls) < 10:
            print("\n  " + str_back0, end = "")
            print(str_exit0)
        else:
            print("\n  " + str_back, end = "")
            print(str_exit)
    else:
        if len(ls) < 10:
            print("  " + str_back0, end = "")
            print(str_exit0)
        elif len(ls) == 10:
            print("  " + str_back0, end = "")
            print(str_exit)
        else:
            print("  " + str_back, end = "")
            print(str_exit)

    while True:
        input_ls = [i.lower() for i in ls]

        s = input("\n" + bi + "?" + bo + "  Enter: ").strip()
        try:
            if s.lower() in input_ls:
                return input_ls.index(s) + 1
            elif int(s) in range(1, len(ls) + 1):
                return int(s)
            else:
                print(
                    Fore.LIGHTRED_EX + "Invalid input:" + Style.RESET_ALL + " Input must be a valid integer or valid name of option!")
        except:
            print(
                Fore.LIGHTRED_EX + "Invalid input:" + Style.RESET_ALL + " Input must be a valid integer or valid name of option!")


def input_func(print_str: str = "Enter: ", digit: bool = True):
    cl1 = Fore.LIGHTRED_EX + Style.BRIGHT

    bi = f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}[{Style.RESET_ALL}"
    bo = f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}]{Style.RESET_ALL}"

    if digit:
        while True:
            i = input(bi + "?" + bo + "  " + print_str)
            try:
                return float(i)
            except:
                print(cl1 + "Wrong Input: " + Style.RESET_ALL + "Input type must be a integer or a float.")
    else:
        return input(bi + "?" + bo + "  " + print_str).strip()


def converter_func(dict_: dict, name: str, more: bool = False, more_dict: dict | None = None, fill: int = 20,
                   back_func=exit):
    # cl1 = Fore.LIGHTRED_EX + Style.BRIGHT
    # cl2 = Fore.LIGHTGREEN_EX + Style.BRIGHT

    keys = list(dict_.keys())
    cap_keys = []
    for i in range(len(keys)):
        _ = keys[i].lower().capitalize()
        cap_keys.append(_)

    new_dict = {cap_keys[i]: dict_[keys[i]] for i in range(len(keys))}

    if more:
        cap_keys.append("More...")

    cap_keys.append("Back")
    cap_keys.append("Exit Program")

    great = f" Wellcome To {name} Converter "
    print(f"\n{great:-^50}")

    print("\nWhat to convert:- ")
    s1 = opt_iterator(cap_keys, fill)

    if s1 == len(cap_keys):
        exit()
    elif s1 == len(cap_keys) - 1:
        back_func()
    elif more and s1 == len(cap_keys) - 2:
        converter_func(dict_ = more_dict, name = name, fill = fill, back_func = back_func)
        converter_func(dict_ = dict_, name = name, more = more, more_dict = more_dict, fill = fill,
                       back_func = back_func)

    input_value = input_func("Enter Value: ")

    print("\nConvert in:- ")
    s2 = opt_iterator(cap_keys, fill)

    if s2 == len(cap_keys):
        exit()
    elif s1 == len(cap_keys) - 1:
        back_func()
    elif more and s1 == len(cap_keys) - 2:
        converter_func(dict_ = more_dict, name = name, fill = fill, back_func = back_func)
        converter_func(dict_ = dict_, name = name, more = more, more_dict = more_dict, fill = fill,
                       back_func = back_func)

    s1_value = float(new_dict.get(cap_keys[s1 - 1]))
    s2_value = float(new_dict.get(cap_keys[s2 - 1]))

    ans = input_value * (s1_value / s2_value)
    finale_text = f"[bold red]{input_value}[/bold red] {cap_keys[s1 - 1]} = [bold red]{ans}[/bold red] {cap_keys[s2 - 1]}"

    panel = Panel(finale_text, expand = False, title = "Answer", padding = (0, 1))
    rprint(panel)

    # print(f"{cl1}>>>{Style.RESET_ALL}",
    #       f"{cl2}{input_value}{Style.RESET_ALL} {cap_keys[s1 - 1]} = {cl2}{ans}{Style.RESET_ALL} {cap_keys[s2 - 1]}")


def angle_con():
    converter_func(dictionary['angle'], name = "Angle", back_func = converter)


def area_con():
    print("coming soon...")


def energy_con():
    converter_func(dictionary['energy_common'], name = "Energy", more = True, more_dict = dictionary["energy_all"],
                   fill = 25, back_func = converter)


def length_con():
    converter_func(dictionary['length_common'], name = "Length", more = True, more_dict = dictionary["length_all"],
                   back_func = converter)


def speed_con():
    converter_func(dictionary['speed_common'], name = "Speed", more = True, more_dict = dictionary["speed_all"],
                   fill = 25, back_func = converter)


def storage_con():
    converter_func(dictionary["storage_common"], name = "Storage", more = True, more_dict = dictionary["storage_all"],
                   back_func = converter)


def temp_con():
    cl1 = Fore.LIGHTRED_EX + Style.BRIGHT
    cl2 = Fore.LIGHTCYAN_EX + Style.BRIGHT

    ls = ["Celsius", "Kelvin", "Fahrenheit", "Back", 'Exit Program']

    great = " Wellcome To Temperature Converter "
    print(f"\n{great:-^50}")
    print("What to convert:- ")

    s1 = opt_iterator(ls)
    if int(s1) == len(ls):
        exit()
    elif int(s1) == len(ls) - 1:
        converter()

    temp = input_func("Enter Temperature: ", True)

    print("\nConvert in :-")
    s2 = opt_iterator(ls)
    if int(s2) == len(ls):
        exit()
    elif int(s1) == len(ls) - 1:
        converter()

    key = f"{s1}{s2}"

    temp_dict = {
        "11": f"{temp}°C = {temp}°C",
        "12": f"{temp}°C = {temp + 273.15}K",
        "13": f"{temp}°C = {(temp * 9 / 5) + 32}°F",

        "21": f"{temp}°K = {temp - 273.15}°C",
        "22": f"{temp}°K = {temp}K",
        "23": f"{temp}°K = {round((temp - 273.15) * 9 / 5 + 32, 2)}°F",

        "31": f"{temp}°F = {round((temp - 32) * 5 / 9, 2)}°C",
        "32": f"{temp}°F = {round((temp - 32) * 5 / 9 + 273.15, 2)}K",
        "33": f"{temp}°F = {temp}°F",
    }

    x = (temp_dict.get(key))
    panel = Panel(x, title = "Answer", expand = False, padding = (0, 1), highlight = True)
    rprint(panel)


def time_con():
    converter_func(dictionary["time_common"], name = "Time", more = True, more_dict = dictionary["time_all"],
                   back_func = converter)


def volume_con():
    print("coming soon...")


def weight_con():
    print("coming soon...")


def converter():
    ls = list(dictionary["converter"])
    ls.sort()
    ls.append("Back")
    ls.append("Exit Program")

    opt_ls = [
        angle_con,
        area_con,
        energy_con,
        length_con,
        speed_con,
        storage_con,
        temp_con,
        time_con,
        volume_con,
        weight_con,
    ]

    while True:
        great = " Wellcome To Converter "
        print(f"\n{great:-^60}")
        s = opt_iterator(ls, 25)
        if int(s) == len(ls) or s == len(ls) - 1:
            exit()
        else:
            opt_ls[s - 1]()


if __name__ == "__main__":
    converter()
