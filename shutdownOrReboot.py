import os

acceptedValues = [
    "shutdown",
    "shutdownnow",
    "reboot",
    "rebootnow",
    "cancel"
]

def shutdown(time):
    #os.system('shutdown -s -t %a' %(time))
    print('shutdown -s -t %a' %(time))

def reboot(time):
    #os.system('shutdown -t %a  -r -f' %(time))
    print('shutdown -t %a -r -f' %(time))

def cancelAction():
    #os.system('shutdown -a')
    print('os.system(shutdown -a)')

def actionNotAccepted():
    newAction = input('This isn\'t a valid option, try again.\n')
    checkIfValid(newAction)

def setTimeForLater(action):
    try:
        minutesToAction = int(input('Please, write in how many minutes do you wish to execute this action. \n'))
    except:
        print('Number invalid.')
        setTimeForLater(action)
    
    secondsToAction = minutesToAction * 60

    actionLater(action, secondsToAction)


def actionLater(actionToDo, secondsToAction):
    return globals()[actionToDo](secondsToAction)

def actionNow(actionToDo):
    actionToDoWithNoNow = actionToDo.replace("now", "")
    return globals()[actionToDoWithNoNow](0)

#region oldCode 
# def rebootLater():
#     try:
#         minutesToReboot = int(input('Please, write in how many minutes do you wish to restart the computers. \n'))
#     except:
#         print('Please, write a valid number.')
#         rebootLater()
#     minutesToReboot = minutesToReboot * 60
#     reboot(minutesToReboot)

# def turnOffLater():
#     try:
#         minutesToTurnOff = int(input('Please, write in how many minutes do you wish to restart the computers. \n'))
#     except:
#         print('Please, write a valid number.')
#         rebootLater()
#     minutesToTurnOff = minutesToTurnOff * 60
#     reboot(minutesToTurnOff)


# def rebootOptions():
#     rebootNowOrLater = input('Do you wish to restart now? Y/N \n').strip()
#     match rebootNowOrLater.lower():
#         case 'y':
#             return reboot(0)
#         case 'n':
#             return rebootLater()
#         case _:
#             print('Select a valid option.')
#             rebootOptions()

# def turnOffOptions():
#     turnOffNowOrLater = input('Do you wish to turn off now? Y/N \n').strip()
#     match turnOffNowOrLater.lower():
#         case 'y':
#             return turnOff(0)
#         case 'n':
#             return turnOffLater()
#         case _:
#             print('Select a valid option.')
#             turnOffOptions()
#endregion

def checkIfValid(optionSelected):
    if optionSelected not in acceptedValues:
        return actionNotAccepted()
    else:
        return checkIfCancel(optionSelected)

def checkIfCancel(action):
    if action == 'cancel':
        return cancelAction()
    else:
        return checkIfNowOrLater(action)

def checkIfNowOrLater(action):
    if 'now' not in action:
        setTimeForLater(action)
    else:
        actionNow(action)

#region OldCode
    # match action:      
        # case 'reboot':
        #     return rebootOptions()
        # case 'reboot now':
        #     return(reboot(0))
        # case 'turn off':
        #     return turnOffOptions()
        # case 'turn off now':
        #     return (turnOff(0))
        # case 'cancel':
        #     exit()
        # case _:
        #     action = input('This option is not supported. Try again: \n').strip()
        #     return actionToDo(action.lower())
#endregion

def start():
    optionSelector = input('Please, write your desired outcome. The options are \n-Reboot \n-Reboot Now \n-Shut down \n-Shut down now \n-Cancel \n').replace(" ", "")
    checkIfValid(optionSelector)
    
    #actionToDo(optionSelector.lower())

start()