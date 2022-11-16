from userInterface.mainWindow import MainWindow
from businessLogic.controller import Controller

def main():
    
    controller = Controller()
    window = MainWindow(controller)


if __name__ == "__main__":
    main()
