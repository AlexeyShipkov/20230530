import view
import model
import text

def start():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_pb()
                view.print_message(text.load_successful)
            case 2:
                model.print_pb()
            case 3:
                view.print_message(text.quit_user)
                break