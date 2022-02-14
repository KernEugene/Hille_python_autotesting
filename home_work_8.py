def run_logger(func):
    def wrapper(*args, **kwargs):
        print("Title\n"
              "CEO Red Bull Inc.\n"
              "Mr.John Bigbull")

        return func(*args, **kwargs)

    return wrapper


@run_logger
def vacation(firstname,surname,date_from,date_to):
    print("Hi John\n"
          f"I need the paid vacations from {date_from} to {date_to}\n"
          f"{firstname} {surname}")
    print("")


@run_logger
def sick_leave(firstname,surname,date_from,date_to):
    print("Hi John\n"
          f"I need the paid sick leave from {date_from} to {date_to}\n"
          f"{firstname} {surname}")
    print("")


@run_logger
def day_off(firstname,surname,date_from,date_to):
    print("Hi John\n"
          f"I need the paid day off from {date_from} to {date_to}\n"
          f"{firstname} {surname}")
    print("")


if __name__ == "__main__":
    vacation('Yevhenii',"Kern",'11/06/2022','15/06/2022')
    sick_leave('Yevhenii',"Kern",'11/06/2022','15/06/2022')
    day_off('Yevhenii',"Kern",'11/06/2022','15/06/2022')

