import random
import tkinter
from tkinter import ttk, messagebox
import time

def roleWindows():
    global roles2

    roleWindow = tkinter.Tk()
    roleWindow.geometry("200x200+505+530")
    roleWindow.resizable(height = False, width = False)
    roleWindow.configure(bg = "yellow")

    rolesLabel = tkinter.Label(roleWindow, text = "Roles:")
    rolesLabel.grid(row = 0, column = 0)
    rolesLabel.configure(bg = "yellow")

    x = 1

    for role in roles2:
        roleLabel = tkinter.Label(roleWindow, text = role)
        roleLabel.grid(row = x, column = 0)
        if role == "Jailor" or role == "Doc" or role == "Cop" or role == "Heir" or role == "Retributionist":
            roleLabel.configure(bg = "#39ff14")
        if role == "Mafia":
            roleLabel.configure(bg = "red")
        if role == "Jester":
            roleLabel.configure(bg = "pink")
        if role == "Plaguebearer":
            roleLabel.configure(bg = "#96aa00")
        if role == "Guardian":
            roleLabel.configure(bg = "#ffffff")

        x += 1
            
        

def gPro(save):
    global gHeal, didgHeal, gHeals

    if gHeals < 4:


        if didgHeal == False:
            messagebox.showinfo("Protecting!", "You are protecting " + save + ": your target.")
            didgHeal = True
            gHeal = save
        else:
            messagebox.showinfo("Nevermind.", "You have changed your mind.")
            didgHeal = False
            gHeal = ""
    else:
        messagebox.showinfo("Out!", "You are out of saves!")

    

def windowForAlives():
    global Alive, dayNumber, windowForAlive

    wAR = 1
    
    windowForAlive = tkinter.Tk()
    windowForAlive.title("Alive")
    windowForAlive.geometry("200x200+105+530")
    windowForAlive.configure(bg = "#39ff14")

    aliveLabel = tkinter.Label(windowForAlive, text = "Alive:")
    aliveLabel.configure(bg = "#39ff14")
    aliveLabel.grid(row = 0, column = 0)

    for players in Alive:
        alabel = tkinter.Label(windowForAlive, text = str(wAR) + "  " + players)
        alabel.grid(row = wAR, column = 0)
        alabel.configure(bg = "#39ff14")
        wAR += 1

def windowForDeads():
    global Alive, dayNumber, windowForDead, playersAndTheirRoles
    wDR = 1

    windowForDead = tkinter.Tk()
    windowForDead.title("Dead")
    windowForDead.geometry("200x200+305+530")
    windowForDead.configure(bg = "red")

    deadLabel = tkinter.Label(windowForDead, text = "Dead:")
    deadLabel.configure(bg = "red")
    deadLabel.grid(row = 0, column = 0)

    for players in playersAndTheirRoles:
        if players not in Alive:
            dlabel = tkinter.Label(windowForDead, text = players)
            dlabel.configure(bg = "red")
            dlabel.grid(row = wDR, column = 0)

            dRole = tkinter.Label(windowForDead, text = "       " + playersAndTheirRoles[players])
            dRole.configure(bg = "red")
            dRole.grid(row = wDR, column = 1)

            wDR += 1


def jestKill(person):
    global jestHaunt, didJestHaunt, One, Two, Three, Four, Five, Six, Seven, RealName, playersAndTheirRoles
    jestHaunt = person
    jestHauntRole = playersAndTheirRoles[person]
    didJestHaunt = True
    messagebox.showinfo("Haunt", "You have chosen to Haunt " + person)

def pestKill(person):
    global pestKilled, pestKilledRole, One, Two, Three, Four, Five, Six, Seven, RealName, playersAndTheirRoles, didPestKill
    pestKilled = person
    pestKilledRole = playersAndTheirRoles[person]
    didPestKill = True
    messagebox.showinfo("Destroying", "You have chosen to destroy " + person)


def infect1():
    global infect, One
    infect = One
    messagebox.showinfo("Infecting!", "You are infecting " + One)

def infect2():
    global infect, Two
    infect = Two
    messagebox.showinfo("Infecting!", "You are infecting " + Two)

def infect3():
    global infect, Three
    infect = Three
    messagebox.showinfo("Infecting!", "You are infecting " + Three)

def infect4():
    global infect, Four
    infect = Four
    messagebox.showinfo("Infecting!", "You are infecting " + Four)

def infect5():
    global infect, Five
    infect = Five
    messagebox.showinfo("Infecting!", "You are infecting " + Five)

def infect6():
    global infect, Six
    infect = Six
    messagebox.showinfo("Infecting!", "You are infecting " + Six)

def infect7():
    global infect, Seven
    infect = Seven
    messagebox.showinfo("Infecting!", "You are infecting " + Seven)

def rev1():
    global toBeRevived, One, reviving, hasRevived
    if hasRevived == False:
        toBeRevived = One
        reviving = True
        messagebox.showinfo("Reviving!", "You are reviving " + One)
    else:
        messagebox.showinfo("Revived already!", "You already revived!")

def rev2():
    global toBeRevived, Two, reviving, hasRevived
    if hasRevived == False:
        toBeRevived = Two
        reviving = True
        messagebox.showinfo("Reviving!", "You are reviving " + Two)
    else:
        messagebox.showinfo("Revived already!", "You already revived!")

def rev3():
    global toBeRevived, Three, reviving, hasRevived
    if hasRevived == False:
        toBeRevived = Three
        reviving = True
        messagebox.showinfo("Reviving!", "You are reviving " + Three)
    else:
        messagebox.showinfo("Revived already!", "You already revived!")

def rev4():
    global toBeRevived, Four, reviving, hasRevived
    if hasRevived == False:
        toBeRevived = Four
        reviving = True
        messagebox.showinfo("Reviving!", "You are reviving " + Four)
    else:
        messagebox.showinfo("Revived already!", "You already revived!")

def rev5():
    global toBeRevived, Five, reviving, hasRevived
    if hasRevived == False:
        toBeRevived = One
        reviving = True
        messagebox.showinfo("Reviving!", "You are reviving " + Five)
    else:
        messagebox.showinfo("Revived already!", "You already revived!")

def rev6():
    global toBeRevived, Six, reviving, hasRevived
    if hasRevived == False:
        toBeRevived = Six
        reviving = True
        messagebox.showinfo("Reviving!", "You are reviving " + Six)
    else:
        messagebox.showinfo("Revived already!", "You already revived!")

def rev7():
    global toBeRevived, Seven, reviving, hasRevived
    if hasRevived == False:
        toBeRevived = Seven
        reviving = True
        messagebox.showinfo("Reviving!", "You are reviving " + Seven)
    else:
        messagebox.showinfo("Revived already!", "You already revived!")


def dayHeir():
    global mafKilled, mafKilledRole, playerHeirTo, PlayerRole, townRoles, Heirs, RealName
    global OneHeirTo, TwoHeirTo, ThreeHeirTo, FourHeirTo, FiveHeirTo, SixHeirTo, SevenHeirTo
    global bot1Role, bot2Role, bot3Role, bot4Role, bot5Role, bot6Role, bot7Role

    if playerHeirTo == mafKilled:
        townRoles.remove(PlayerRole)
        PlayerRole = mafKilledRole
        townRoles.append(PlayerRole)

        if mafKilledRole != "Heir":
            Heirs.remove(RealName)



    if One in Heirs and One in Alive and OneHeirTo == mafKilled:
        townRoles.remove(bot1Role)
        bot1Role = mafKilledRole
        townRoles.append(bot1Role)

        if mafKilledRole != "Heir":
            Heirs.remove(One)



    if Two in Heirs and Two in Alive and TwoHeirTo == mafKilled:
        townRoles.remove(bot2Role)
        bot2Role = mafKilledRole
        townRoles.append(bot2Role)

        if mafKilledRole != "Heir":
            Heirs.remove(Two)



    if Three in Heirs and Three in Alive and ThreeHeirTo == mafKilled:
        townRoles.remove(bot3Role)
        bot3Role = mafKilledRole
        townRoles.append(bot3Role)

        if mafKilledRole != "Heir":
            Heirs.remove(Three)



    if Four in Heirs and Four in Alive and FourHeirTo == mafKilled:
        townRoles.remove(bot4Role)
        bot4Role = mafKilledRole
        townRoles.append(bot4Role)

        if mafKilledRole != "Heir":
            Heirs.remove(Four)



    if Five in Heirs and Five in Alive and FiveHeirTo == mafKilled:
        townRoles.remove(bot5Role)
        bot5Role = mafKilledRole
        townRoles.append(bot5Role)

        if mafKilledRole != "Heir":
            Heirs.remove(Five)



    if Six in Heirs and Six in Alive and SixHeirTo == mafKilled:
        townRoles.remove(bot6Role)
        bot6Role = mafKilledRole
        townRoles.append(bot6Role)

        if mafKilledRole != "Heir":
            Heirs.remove(Six)


    if Seven in Heirs and Seven in Alive and SevenHeirTo == mafKilled:
        townRoles.remove(bot7Role)
        bot7Role = mafKilledRole
        townRoles.append(bot7Role)

        if mafKilledRole != "Heir":
            Heirs.remove(Seven)




def botsHeirTo():
    global One, Two, Three, Four, Five, Six, Seven, RealName, Heirs, Alive, jailed
    global OneHeirTo, TwoHeirTo, ThreeHeirTo, FourHeirTo, FiveHeirTo, SixHeirTo, SevenHeirTo
    
    if One in Heirs and One in Alive and jailed != One:
        OneHeirTo = random.choice(Alive)

    if Two in Heirs and Two in Alive and jailed != Two:
        TwoHeirTo = random.choice(Alive)

    if Three in Heirs and Three in Alive and jailed != Three:
        ThreeHeirTo = random.choice(Alive)

    if Four in Heirs and Four in Alive and jailed != Four:
        FourHeirTo = random.choice(Alive)

    if Five in Heirs and Five in Alive and jailed != Five:
        FiveHeirTo = random.choice(Alive)

    if Six in Heirs and Six in Alive and jailed != Six:
        SixHeirTo = random.choice(Alive)

    if Seven in Heirs and Seven in Alive and jailed != Seven:
        SevenHeirTo = random.choice(Alive)

def buyHeir():
    global Heir, money, starting, coins, rolesUnlocked

    if money >= Heir:
        messagebox.showinfo("Bought!", "You bought the Heir!")
        rolesUnlocked = open("rolesUnlocked.txt", "a+")
        rolesUnlocked.write("Heir\n")

        rolesUnlocked = open("rolesUnlocked.txt", "r")
        money = money - 20
        coins.configure(text = "Coins: " + str(money))
        rolesUnlocked = open("rolesUnlocked.txt", "w")
        rolesUnlocked.write("Heir\n")
        rolesUnlocked = open("rolesUnlocked.txt", "r")
        
    else:
        messagebox.showinfo("More needed!", "You need more money")
        

def store():
    global money, Heir, buyHeir

    store = tkinter.Tk()
    store.geometry("500x200+1001+530")
    store.title("Store")
    store.resizable(width = False, height = False)
    store.configure(bg = "#5cff5c")

    rolesUnlockedWrite = open("rolesUnlocked.txt", "a+")

    rolesUnlockedRead = open("rolesUnlocked.txt", "r")

    rolesUnlocked = rolesUnlockedRead.read()

    if "Jailor" not in rolesUnlocked:
        rolesUnlockedWrite.write("Jailor\nCop\nDoc\nMafia\nJester\nPlaguebearer\nGuardian\n")


    Heir = 20

    if "Heir" not in rolesUnlocked:
        buyHeir = tkinter.Button(store, text = "Buy the new Heir role! (20 coins)", command = buyHeir)
        buyHeir.place(x = 175, y = 100)
        buyHeir.configure(width = 25, bg = "blue")

    rolesUnlockedWrite = open("rolesUnlocked.txt", "r")
    store.mainloop()

def customizing():
    global heirs, rolesUnlocked, howManyHeirs, roles, townRoles, howManyJailors, jailors, howManyCops, cops, howManyDocs, docs, howManyMafia, mafia, howManyJesters, jesters, credit, customGame, townRoles
    global customWindow, howManyRetri, retris, howManyPb, plaguebearers, howManyGa, guardianangels, target, roles2
        
    canGameStart = True
    roles = []
    townRoles = []


    jailors = howManyJailors.get()
    cops = howManyCops.get()
    docs = howManyDocs.get()
    mafias = howManyMafia.get()
    jesters = howManyJesters.get()
    retris = howManyRetri.get()


    if "Heir" in rolesUnlocked:
        heirs = howManyHeirs.get()


    plaguebearers = howManyPb.get()
    if plaguebearers != "":
        plaguebearers = int(plaguebearers)
    else:
        plaguebearers = 0

    guardianangels = howManyGa.get()
    if guardianangels != "":
        guardianangels = int(guardianangels)
    else:
        guardianangels = 0

    

    if jailors != "":
        jailors = int(jailors)
    else:
        jailors = 0


    if cops != "":
        cops = int(cops)
    else:
        cops = 0


    if docs != "":
        docs = int(docs)
    else:
        docs = 0



    if mafias != "":
        mafias = int(mafias)
    else:
        mafias = 0


    if jesters != "":
        jesters = int(jesters)
    else:
        jesters = 0

    if retris != "":
        retris = int(retris)
    else:
        retris = 0

    if "Heir" in rolesUnlocked:
        if heirs != "":
            heirs = int(heirs)
        else:
            heirs = 0
    else:
        heirs = 0



    if jailors > 1:
        messagebox.showinfo("Too many!", "You can only have 1 Jailor")
        canGameStart = False

    if (mafias + plaguebearers) > (jailors + cops + docs + heirs + retris + jesters) and (jailors + cops + docs + heirs + retris) > 0:
        messagebox.showinfo("Too many!", "There are too many evil roles!")
        canGameStart = False

    if mafias < 2 and plaguebearers == 0 and jesters != 8:
        messagebox.showinfo("Not enought!", "There needs to be more mafia!")
        canGameStart = False

    if jesters > 2 and (jailors + cops + docs) != 0:
        messagebox.showinfo("Too many!", "There are too many jesters!")
        canGameStart = False

    if (jailors + cops + docs + mafias + jesters + heirs + retris + plaguebearers + guardianangels) != 8:
        messagebox.showinfo("Wrong amount!", "There needs to be 8 players!")
        canGameStart = False

    if jailors == 1 and heirs > 1:
        messagebox.showinfo("Wrong amount!", "There can not be more than one Heir if there is a Jailor!")
        canGameStart = False

    if retris > 1:
        messagebox.showinfo("Wrong amount!", "There can not be more than one Retributionist.")
        canGameStart = False

    if plaguebearers > 1:
        messagebox.showinfo("Wrong amount!", "There can not be more than one Plaguebearer.")
        canGameStart = False

    if mafias > 4:
        messagebox.showinfo("Wrong amount!", "Mafia cannot have majority")
        canGameStart = False

    if guardianangels > 1:
        messagebox.showinfo("Wrong amount!", "There can not be more than one Guardian!")
        canGameStart = False
    if canGameStart == True:
        i = 0

        while i < jailors:
            roles.append("Jailor")
            townRoles.append("Jailor")
            i += 1

        i = 0

        while i < cops:
            roles.append("Cop")
            townRoles.append("Cop")
            i += 1

        i = 0

        while i < docs:
            roles.append("Doc")
            townRoles.append("Doc")
            i += 1

        i = 0

        while i < mafias:
            roles.append("Mafia")
            i += 1

        i = 0

        while i < jesters:
            roles.append("Jester")
            townRoles.append("Jester")
            i += 1


        i = 0

        while i < retris:
            roles.append("Retri")
            townRoles.append("Retri")
            i += 1

        i = 0
        
        if "Heir" in rolesUnlocked:
            while i < heirs:
                roles.append("Heir")
                townRoles.append("Heir")
                i += 1

        i = 0

        while i < plaguebearers:
            roles.append("Plaguebearer")
            i += 1

        i = 0

        while i < guardianangels:
            roles.append("Guardian")
            i += 1
        roles2 = []
        for role in roles:
            roles2.append(role)
            


        if canGameStart == True:
 
            customGame = True
            credit()

    
        


def customGame():
    global roles, custom, howManyJailors, howManyCops, howManyDocs, howManyMafia, howManyJesters, howManyHeirs, customizing, rolesUnlocked, customWindow, howManyRetri, howManyPb, howManyGa

    customWindow = tkinter.Tk()
    customWindow.title("Custom game!")
    customWindow.geometry("600x300+401+200")
    customWindow.resizable(width = False, height = False)

    customLabel = tkinter.Label(customWindow, text = "Make a custom game!").place(x = 280, y = 0)
    leaveBlank = tkinter.Label(customWindow, text = "Leave blank if you don't want any. \nThey have to add up to eight!").place(x = 400, y = 15)

    howManyJailorsLabel = tkinter.Label(customWindow, text = "How many jailors?").place(x = 15, y = 40)
    howManyJailors = tkinter.Entry(customWindow)
    howManyJailors.place(x = 120, y = 40)

    howManyCopsLabel = tkinter.Label(customWindow, text = "How many cops?").place(x = 15, y = 80)
    howManyCops = tkinter.Entry(customWindow)
    howManyCops.place(x = 120, y = 80)

    howManyDocsLabel = tkinter.Label(customWindow, text = "How many docs?").place(x = 15, y = 120)
    howManyDocs = tkinter.Entry(customWindow)
    howManyDocs.place(x = 120, y = 120)

    howManyMafiaLabel = tkinter.Label(customWindow, text = "How many Mafia?").place(x = 15, y = 160)
    howManyMafia = tkinter.Entry(customWindow)
    howManyMafia.place(x = 120, y = 160)

    howManyJestersLabel = tkinter.Label(customWindow, text = "How many jesters?").place(x = 15, y = 200)
    howManyJesters = tkinter.Entry(customWindow)
    howManyJesters.place(x = 120, y = 200)

    howManyRetriLabel = tkinter.Label(customWindow, text = "How many Retributionists?").place(x = 250, y = 80)
    howManyRetri = tkinter.Entry(customWindow)
    howManyRetri.place(x = 410, y = 80)

    howManyPbLabel = tkinter.Label(customWindow, text = "How many Plaguebearers?").place(x = 250, y = 120)
    howManyPb = tkinter.Entry(customWindow)
    howManyPb.place(x = 410, y = 120)

    howManyGaLabel = tkinter.Label(customWindow, text = "How many Guardians?").place(x = 250, y = 160)
    howManyGa = tkinter.Entry(customWindow)
    howManyGa.place(x = 410, y = 160)

    if "Heir" in rolesUnlocked:
        howManyHeirsLabel = tkinter.Label(customWindow, text = "How many heirs?").place(x = 15, y = 240)
        howManyHeirs = tkinter.Entry(customWindow)
        howManyHeirs.place(x = 120, y = 240) 

    submitCustom = tkinter.Button(customWindow, text = "Start a custom game!", command = customizing).place(x = 280, y = 280)

    customWindow.mainloop()
    


    



def finished():
    global root, nightNumber, dayNumber, coins, winners, wins, winLabel, file, money, game1, target, playersAndTheirRoles, deadWindow, One, Two, Three, Four, Five, Six, Seven, RealName, PlayerRole, bot1Role, bot2Role, bot3Role, bot4Role, bot5Role, bot6Role, bot7Role, night, Day, deadWindow, jestersLynched
    totalWinners = "Winners: \n"


    if target in Alive:
        for player in playersAndTheirRoles:
            if playersAndTheirRoles[player] == "Guardian":
                if player not in winners:
                    winners.append(player)
    else:
        for player in playersAndTheirRoles:
            if playersAndTheirRoles[player] == "Guardian":
                if player in winners:
                    winners.remove(player)

                    
    for players in playersAndTheirRoles:
        if playersAndTheirRoles[players] == "Jester" and players not in jestersLynched and players in winners:
            winners.remove(players)

    if len(winners) == 0:
        totalWinners = totalWinners + "Nobody won!"
    
    else:
        for player in playersAndTheirRoles:
            if player in winners:
                totalWinners = totalWinners + player + "\n"
    messagebox.showinfo("Winners!", totalWinners)
    messagebox.showinfo("Roles", One + ": " + bot1Role + "\n" + Two + ": " + bot2Role + "\n" + Three + ": " + bot3Role + "\n" + Four + ": " + bot4Role + "\n" + Five + ": " + bot5Role + "\n" + Six + ": " + bot6Role + "\n" + Seven + ": " + bot7Role + "\n" + RealName + ": " + PlayerRole)

    if RealName in winners:
        file.close()
        money += 2
        wins += 1
        coins.configure(text = "Coins: " + str(money))
        file = open("tosCoins.txt", "w")
        file.write(str(money) + "\n \nTrue")

        readWinFile = open("tosCoins.txt", "w")
        readWinFile.write(str(wins) + "\n \nTrue")
        winLabel.configure(text = "Wins: " + str(wins))
        game1 = False

        readWinFile = open("tosWins.txt", "r")
        file = open("tosCoins.txt", "r")

def died2():
    if mafKilled == RealName or jailorKilled == RealName or pestKilled == RealName or jestHaunt == RealName:
        Day.configure(bg = "cyan")
    else:
        night.configure(bg = "#A9A9A9")

def died():
    global night, Day, mafKilled, lynched, RealName, jailorKilled, pestKilled, jestHaunt

    if mafKilled == RealName or jailorKilled == RealName or pestKilled == RealName or jestHaunt == RealName:
        Day.configure(bg = "red")
        Day.after(100, died2)
    else:
        night.configure(bg = "red")
        night.after(100, died2)


def roleInfo():
    global PlayerRole, target, playersAndTheirRoles

    info = tkinter.Tk()
    info.configure(bg = "orange")
    info.geometry("+505+530")
    info.title("Role Info")
    

    if PlayerRole == "Mafia":
        mafRoleInfo = tkinter.Label(info, text = "Attributes: \nYou kill a person at night. \n \n Win Conditions: \nWins if outnumbers the Town.")
        mafRoleInfo.configure(bg = "blue")
        mafRoleInfo.grid(row = 0, column = 0)
        

    elif PlayerRole == "Doc":
        docRoleInfo = tkinter.Label(info, text = "Attributes: \nYou can choose to heal a person at night. \n You can only heal yourself once. \n\n Win Conditions: \nWins if all mafia are dead.")
        docRoleInfo.configure(bg = "blue")
        docRoleInfo.grid(row = 0, column = 0)

    elif PlayerRole == "Cop":
        copRoleInfo = tkinter.Label(info, text = "Attributes: \nYou can investigate one person a night. \nYou will see their role. \n\n Win Conditions: \nWins if all the mafia are dead.")
        copRoleInfo.configure(bg = "blue")
        copRoleInfo.grid(row = 0, column = 0)
        
    elif PlayerRole == "Jailor":
        jailorRoleInfo = tkinter.Label(info, text = "Attributes: \nYou can choose to jail a person during the day. \nAt night, you will see that person's role \nand can choose to execute them. \n\n Win Conditions: \nWins if all the mafia are dead.")
        jailorRoleInfo.configure(bg = "blue")
        jailorRoleInfo.grid(row = 0, column = 0)

    elif PlayerRole == "Jester":
        jesterRoleInfo = tkinter.Label(info, text = "Attributes: \n You are a crazed lunatic whos life \n goal is to be publicly executed. \n\nWin Conditions: \nWins if executed during the day.")
        jesterRoleInfo.configure(bg = "blue")
        jesterRoleInfo.grid(row = 0, column = 0)

    elif PlayerRole == "Heir":
        heirRoleInfo = tkinter.Label(info, text = "Attributes: \nYou can be an heir to someone at night. If that person dies that night,\nyou will become their role. \n\nWin Conditions: \nWins if all the mafia are dead.")
        heirRoleInfo.configure(bg = "blue")
        heirRoleInfo.grid(row = 0, column = 0)

    elif PlayerRole == "Retri":
        retriRoleInfo = tkinter.Label(info, text = "Attributes: \nYou can revive one dead person a game. \nYou cannot revive a Mafia.\n\nWin Conditions: \nWins if all the mafia are dead.")
        retriRoleInfo.configure(bg = "blue")
        retriRoleInfo.grid(row = 0, column = 0)

    elif PlayerRole == "Plaguebearer":
        pbRoleInfo = tkinter.Label(info, text = "Attributes: \nYou infect one person a night. When everyone is infected you become Pestilence.\n\nWin Conditions: \nWins if last one alive.")
        pbRoleInfo.configure(bg = "blue")
        pbRoleInfo.grid(row = 0, column = 0)

    elif PlayerRole == "Pestilence":
        pestRoleInfo = tkinter.Label(info, text = "Attributes: \nYou can destroy one person a night. \n\nWin Conditions: \nWins if last one alive.")
        pestRoleInfo.configure(bg = "blue")
        pestRoleInfo.grid(row = 0, column = 0)

    elif PlayerRole == "Guardian":
        gaRoleInfo = tkinter.Label(info, text = "Attributes: \nTarget: " + target + "\nHis role is " + playersAndTheirRoles[target] + "\nYou can protect your target 3 times a game,\n even if you are dead. \n\nWin Conditions: \nWins if target survives the game.")
        gaRoleInfo.configure(bg = "blue")
        gaRoleInfo.grid(row = 0, column = 0)

    info.resizable(width = False, height = False)

    info.mainloop()


def vote1():
    global lynched, lynchedTrue, One, votes, canvas, yCoor, votedBefore, myVote, myVoteText, running, previous
    myVote = One

    running[One] += 1
    lynchedTrue = True


    if votedBefore == True:
        canvas.delete(myVoteText)
        yCoor = yCoor + 20

        running[previous] -= 1

    previous = One

    myVoteText = canvas.create_text(100, yCoor, text = One + " was voted!")
    votedBefore = True
    yCoor = yCoor - 20
    messagebox.showinfo("Lynching", "You are lynching " + One)
def vote2():
    global lynched, lynchedTrue, Two, votes, canvas, yCoor, votedBefore, myVote, myVoteText, running, previous
    myVote = Two

    running[Two] += 1

    lynchedTrue = True

    if votedBefore == True:
        canvas.delete(myVoteText)
        yCoor = yCoor + 20

        running[previous] -= 1

    previous = Two

    myVoteText = canvas.create_text(100, yCoor, text = Two + " was voted!")
    votedBefore = True
    yCoor = yCoor - 20
    messagebox.showinfo("Lynching", "You are lynching " + Two)
def vote3():
    global lynched, lynchedTrue, Three, votes, canvas, yCoor, votedBefore, myVote, myVoteText, running, previous
    myVote = Three


    running[Three] += 1
    lynchedTrue = True

    if votedBefore == True:
        canvas.delete(myVoteText)
        yCoor = yCoor + 20

        running[previous] -= 1

    previous = Three

    myVoteText = canvas.create_text(100, yCoor, text = Three + " was voted!")
    votedBefore = True
    yCoor = yCoor - 20
    messagebox.showinfo("Lynching", "You are lynching " + Three)
def vote4():
    global lynched, lynchedTrue, Four, votes, yCoor, votedBefore, myVote, myVoteText, running, previous
    myVote = Four
    running[Four] += 1


    lynchedTrue = True

    if votedBefore == True:
        canvas.delete(myVoteText)
        yCoor = yCoor + 20

        running[previous] -= 1

    previous = Four
    
    myVoteText = canvas.create_text(100, yCoor, text = Four + " was voted!")
    votedBefore = True
    yCoor = yCoor - 20
    messagebox.showinfo("Lynching", "You are lynching " + Four)
    
def vote5():
    global lynched, lynchedTrue, Five, votes, yCoor, votedBefore, myVote, myVoteText, running, previous
    myVote = Five
    

    running[Five] += 1
    lynchedTrue = True

    if votedBefore == True:
        canvas.delete(myVoteText)
        yCoor = yCoor + 20

        running[previous] -= 1

    previous = Five
    
    myVoteText = canvas.create_text(100, yCoor, text = Five + " was voted!")
    votedBefore = True
    yCoor = yCoor - 20
    messagebox.showinfo("Lynching", "You are lynching " + Five)




def vote6():
    global lynched, lynchedTrue, Six, votes, yCoor, votedBefore, myVote, myVoteText, running, previous
    myVote = Six
    

    running[Six] += 1
    lynchedTrue = True

    if votedBefore == True:
        canvas.delete(myVoteText)
        yCoor = yCoor + 20

        running[previous] -= 1

    previous = Six
    
    myVoteText = canvas.create_text(100, yCoor, text = Six + " was voted!")
    votedBefore = True
    yCoor = yCoor - 20
    messagebox.showinfo("Lynching", "You are lynching " + Six)

def vote7():
    global lynched, lynchedTrue, Seven, votes, yCoor, votedBefore, myVote, myVoteText, running, previous
    myVote = Seven
    

    running[Seven] += 1
    lynchedTrue = True

    if votedBefore == True:
        canvas.delete(myVoteText)
        yCoor = yCoor + 20

        running[previous] -= 1

    previous = Seven
    
    myVoteText = canvas.create_text(100, yCoor, text = Seven + " was voted!")
    votedBefore = True
    yCoor = yCoor - 20
    messagebox.showinfo("Lynching", "You are lynching " + Seven)
    

#LYNCH LYNCH LYNCH LYNCH LYNCH LYNCH LYNCH LYNCH

def Lynch():
    global lynch, lynched, lynchedTrue, lynchedRole
    global player1Vote, player2Vote, player3Vote, Alive, votes, vote, canvas, yCoor, votedBefore, myVote, runners, running
    global One, Two, Three, Four, Five, Six, Seven, RealName

    myVote = ""

    votedBefore = False

    Day.destroy()
    
    lynch = tkinter.Tk()
    lynch.configure(bg = "cyan")
    lynch.geometry("300x300+105+200")
    lynch.title("Vote to Lynch")

    votes = {One: 0, Two: 0, Three: 0, Four: 0, Five: 0, Six: 0, Seven: 0, RealName: 0}


    canvas = tkinter.Canvas(deadWindow, width = 200, height = 300)
    canvas.place(x = 400, y = 0)




    if RealName in Alive:
        if One in Alive:
            vote1Button = tkinter.Button(lynch, text = One, command = vote1)
            vote1Button.configure(bg = "red", width = 14)
            vote1Button.place(x = 0, y = 275)

        if Two in Alive:
            vote2Button = tkinter.Button(lynch, text = Two, command = vote2)
            vote2Button.configure(bg = "red", width = 14)
            vote2Button.place(x = 95, y = 275)

        if Three in Alive:
            vote3Button = tkinter.Button(lynch, text = Three, command = vote3)
            vote3Button.configure(bg = "red", width = 14)
            vote3Button.place(x = 190, y = 275)

        if Four in Alive:
            vote4Button = tkinter.Button(lynch, text = Four, command = vote4)
            vote4Button.configure(bg = "red", width = 14)
            vote4Button.place(x = 0, y = 250)

        if Five in Alive:
            vote5Button = tkinter.Button(lynch, text = Five, command = vote5)
            vote5Button.configure(bg = "red", width = 14)
            vote5Button.place(x = 95, y = 250)

        if Six in Alive:
            vote6Button = tkinter.Button(lynch, text = Six, command = vote6)
            vote6Button.configure(bg = "red", width = 14)
            vote6Button.place(x = 190, y = 250)

        if Seven in Alive:
            vote7Button = tkinter.Button(lynch, text = Seven, command = vote7)
            vote7Button.configure(bg = "red", width = 14)
            vote7Button.place(x = 95, y = 225)
            
    else:
        death = tkinter.Label(lynch, text = "You are dead, so you can't vote.")
        death.place(x = 130, y = 0)

    voters = 0
    yCoor = 100
    
    if RealName in Alive:

        

        running = {One: 0, Two: 0, Three: 0, Four: 0, Five: 0, Six: 0, Seven: 0, RealName: 0}


        while voters < len(Alive) - 1:
            voter = Alive[voters]
            vote = random.choice(Alive)

            if vote != voter:
                running[vote] += 1

            

                text = canvas.create_text(100, yCoor, text = vote + " was voted!")
                yCoor = yCoor + 20

            voters += 1


    else:
        
        running = {One: 0, Two: 0, Three: 0, Four: 0, Five: 0,Six: 0, Seven: 0, RealName: 0}


        for runner in Alive:
            vote = random.choice(Alive)
            running[vote] += 1



            text = canvas.create_text(100, yCoor, text = vote + " was voted!")
            yCoor = yCoor + 20



    lynch.after(20000, nights)
    

def docHeal1():
    global docHeal, One
    docHeal.append(One)
    messagebox.showinfo("Healing", "You chose to heal " + One)

def docHeal2():
    global docHeal, Two
    docHeal.append(Two)
    messagebox.showinfo("Healing", "You chose to heal " + Two)

def docHeal3():
    global docHeal, Three
    docHeal.append(Three)
    messagebox.showinfo("Healing", "You chose to heal " + Three)

def docHeal4():
    global docHeal, Four
    docHeal.append(Four)
    messagebox.showinfo("Healing", "You chose to heal " + Four)

def docHeal5():
    global docHeal, Five
    docHeal.append(Five)
    messagebox.showinfo("Healing", "You chose to heal " + Five)

def docHeal6():
    global docHeal, Six
    docHeal.append(Six)
    messagebox.showinfo("Healing", "You chose to heal " + Six)

def docHeal7():
    global docHeal, Seven
    docHeal.append(Seven)
    messagebox.showinfo("Healing", "You chose to heal " + Seven)



    
def docHealSelf():
    global docHeal, RealName, selfHealedYet
    if selfHealedYet < 1:
        docHeal.append(RealName)
        messagebox.showinfo("Healing", "You chose to heal yourself.")
        selfHealedYet = selfHealedYet + 1
    else:
        messagebox.showinfo("Selfish!", "You already healed yourself!")

def mafKill1():
    global mafKilled, mafKilledRole, One, bot1Role, didMafKill
    mafKilled = One
    mafKilledRole = bot1Role
    messagebox.showinfo("Killing", "You are killing " + mafKilled)
    didMafKill = True

def mafKill2():
    global mafKilled, mafKilledRole, Two, bot2Role, didMafKill
    mafKilled = Two
    mafKilledRole = bot2Role
    messagebox.showinfo("Killing", "You are killing " + mafKilled)
    didMafKill = True

def mafKill3():
    global mafKilled, mafKilledRole, Three, bot3Role, didMafKill
    mafKilled = Three
    mafKilledRole = bot3Role
    messagebox.showinfo("Killing", "You are killing " + mafKilled)
    didMafKill = True

def mafKill4():
    global mafKilled, mafKilledRole, Four, bot4Role, didMafKill
    mafKilled = Four
    mafKilledRole = bot4Role
    messagebox.showinfo("Killing", "You are killing " + mafKilled)
    didMafKill = True

def mafKill5():
    global mafKilled, mafKilledRole, Five, bot5Role, didMafKill
    mafKilled = Five
    mafKilledRole = bot5Role
    messagebox.showinfo("Killing", "You are killing " + mafKilled)
    didMafKill = True

def mafKill6():
    global mafKilled, mafKilledRole, Six, bot6Role, didMafKill
    mafKilled = Six
    mafKilledRole = bot6Role
    messagebox.showinfo("Killing", "You are killing " + mafKilled)
    didMafKill = True

def mafKill7():
    global mafKilled, mafKilledRole, Seven, bot7Role, didMafKill
    mafKilled = Seven
    mafKilledRole = bot7Role
    messagebox.showinfo("Killing", "You are killing " + mafKilled)
    didMafKill = True

def invest1():
    global bot1Role, One
    global didInvest
    if didInvest < 1:
        messagebox.showinfo("Investigated!", One + "'s role is " + bot1Role)
        didInvest += 1

def invest2():
    global bot2Role, Two
    global didInvest
    if didInvest < 1:
        messagebox.showinfo("Investigated!", Two + "'s role is " + bot2Role)
        didInvest += 1

def invest3():
    global bot3Role, Three
    global didInvest
    if didInvest < 1:
        messagebox.showinfo("Investigated!", Three + "'s role is " + bot3Role)
        didInvest = 1

def invest4():
    global bot4Role, Four
    global didInvest
    if didInvest < 1:
        messagebox.showinfo("Investigated!", Four + "'s role is " + bot4Role)
        didInvest = 1

def invest5():
    global bot5Role, Five
    global didInvest
    if didInvest < 1:
        messagebox.showinfo("Investigated!", Five + "'s role is " + bot5Role)
        didInvest = 1

def invest6():
    global bot6Role, Six
    global didInvest
    if didInvest < 1:
        messagebox.showinfo("Investigated!", Six + "'s role is " + bot6Role)
        didInvest = 1

def invest7():
    global bot7Role, Seven
    global didInvest
    if didInvest < 1:
        messagebox.showinfo("Investigated!", Seven + "'s role is " + bot7Role)
        didInvest = 1



def heir1():
    global One, playerHeirTo
    playerHeirTo = One
    messagebox.showinfo("Heir!", "You chose to be an heir to " + One)
def heir2():
    global Two, playerHeirTo
    playerHeirTo = Two
    messagebox.showinfo("Heir!", "You chose to be an heir to " + Two)
def heir3():
    global Three, playerHeirTo
    playerHeirTo = Three
    messagebox.showinfo("Heir!", "You chose to be an heir to " + Three)    
def heir4():
    global Four, playerHeirTo
    playerHeirTo = Four
    messagebox.showinfo("Heir!", "You chose to be an heir to " + Four)
def heir5():
    global Five, playerHeirTo
    playerHeirTo = Five
    messagebox.showinfo("Heir!", "You chose to be an heir to " + Five)
def heir6():
    global Six, playerHeirTo
    playerHeirTo = Six
    messagebox.showinfo("Heir!", "You chose to be an heir to " + Six)
def heir7():
    global Seven, playerHeirTo
    playerHeirTo = Seven
    messagebox.showinfo("Heir!", "You chose to be an heir to " + Seven)


def jailorKill():
    global jailed
    global jailorKilled, didJailorKill, docHeal
    global Alive, AliveTown, AliveMaf, townRoles
    global One, Two, Three, Four, Five, PlayerRole, RealName
    global jailorKilledRole

    if PlayerRole == "Jailor":
        messagebox.showinfo("Executing", "You have decided to execute " + jailed)
    if jailed == One:
        if One in Alive:
            Alive.remove(One)
        jailorKilled = One
        jailorKilledRole = bot1Role
        didJailorKill = True

    elif jailed == Two:
        if Two in Alive:
            Alive.remove(Two)
        jailorKilled = One
        jailorKilledRole = bot2Role
        didJailorKill = True

    elif jailed == Three:
        if Three in Alive:
            Alive.remove(Three)
        jailorKilled = Three
        jailorKilledRole = bot3Role
        didJailorKill = True

    elif jailed == Four:
        if Four in Alive:
            Alive.remove(Four)
        jailorKilled = Four
        jailorKilledRole = bot4Role
        didJailorKill = True

    elif jailed == Five:
        if Five in Alive:
            Alive.remove(Five)
        jailorKilled = Five
        jailorKilledRole = bot5Role
        didJailorKill = True

    elif jailed == Six:
        if Six in Alive:
            Alive.remove(Six)
        jailorKilled = Six
        jailorKilledRole = bot6Role
        didJailorKill = True

    elif jailed == Seven:
        if Seven in Alive:
            Alive.remove(Seven)
        jailorKilled = Seven
        jailorKilledRole = bot7Role
        didJailorKill = True
        
    elif jailed == RealName:
        if RealName in Alive:
            Alive.remove(RealName)
        jailorKilled = RealName
        jailorKilledRole = PlayerRole
        didJailorKill = True
                





def Days():
    global role, game
    global dayNumber, nightNumber
    dayNumber = dayNumber + 1
    global RealName
    global Alive, AliveMaf, townRoles
    global Day
    global night
    global jailed, jailorKilled, jailorKilledRole, didJailorKill, mafKilled, mafKilledRole, didMafKill, docHeal
    global lynched, lynchedRole, lynchedTrue
    global RealName, deadWindow, r, c, runners
    global One, Two, Three, Four, Five, Six, Seven, RealName, root
    global Maf, Town, winners, playersAndTheirRoles, jester, heirs, Heirs
    global toBeRevived, reviving, hasRevived, infected, infect, pest
    global plaguebearer, text2
    global bot1Role, bot2Role, bot3Role, bot4Role, bot5Role, bot6Role, bot7Role, PlayerRole, copsCheck
    global iMafia, iDocs, iCops, Jailor
    global didPestKill, pestKilled, pestKilledRole, AliveRoles
    global jestHaunt, didJestHaunt, canHaunt, jestersLynched, windowForAlive, windowForDead
    global gHeal, didgHeal, gHeals



    if dayNumber == 1:
        gHeals = 0
        didgHeal = False
        gHeal = ""
        winners = []
        roleWindows()

    if didgHeal == True:
        gHeals += 1
    else:
        gHeal = ""



    playersAndTheirRoles = {One: bot1Role, Two: bot2Role, Three: bot3Role, Four: bot4Role, Five: bot5Role, Six: bot6Role, Seven: bot7Role, RealName: PlayerRole}
    

    lynchedTrue = False
    lynched = ""
    lynchedRole = ""

    if nightNumber > 0:
        night.destroy()
         
    Day = tkinter.Tk()
    Day.configure(background = "cyan")
    Day.title("ToS")
    Day.geometry("295x300+105+200")
    Day.resizable(height = False, width = False)

    if "Plaguebearer" not in AliveRoles:
        plaguebearer = []



    text1 = tkinter.Label(Day, text = "Day " + str(dayNumber))
    text1.place(x = 0, y = 0)
    text1.configure(background = "cyan")

    text2 = tkinter.Label(Day, text = "Role: " + str(PlayerRole))
    text2.place(x = 230 - (len(PlayerRole) * 4), y = 0)
    text2.configure(background = "cyan")

    text3 = tkinter.Label(Day, text = "Name: " + RealName)
    text3.place(x = 75, y = 0)
    text3.configure(background = "cyan")

    roleInfoButton = tkinter.Button(Day, text = "Role Info", command = roleInfo)
    roleInfoButton.place(x = 230, y = 20)

    


    if (dayNumber > 1 and len(AliveMaf) > 1) or (len(AliveMaf) == 1 and jailed != AliveMaf[0]):
        if RealName not in AliveMaf and len(AliveTown) > 0:
            mafKilled = random.choice(AliveTown)
            didMafKill = True

        elif RealName in AliveMaf:
            mafKilled = mafKilled

        elif RealName not in AliveMaf:
            if len(AliveTown) > 0:
                mafKilled = random.choice(AliveTown)
            else:
                mafKilled = ""
                didMafKill = False

    else:
        mafKilled = ""
        didMafKill = False




    if dayNumber > 1 and didMafKill == True and game == True:

        if (mafKilled == One and One in docHeal) or (mafKilled == One and jailed == One) or (mafKilled == One and gHeal == One):
            saved = tkinter.Label(deadWindow, text = "Night: " + str(nightNumber) + "  " + mafKilled + " was almost killed by the mafia, but was saved!")
            saved.grid(row = r, column = c)
            r = r + 2
            messagebox.showinfo("Saved!", mafKilled + " was almost killed by the mafia, but was saved!")
            mafKilled = ""

        elif (mafKilled == Two and Two in docHeal) or (mafKilled == Two and jailed == Two) or (mafKilled == Two and gHeal == Two):
            saved = tkinter.Label(deadWindow, text = "Night: " + str(nightNumber) + "  " + mafKilled + " was almost killed by the mafia, but was saved!")
            saved.grid(row = r, column = c)
            r = r + 2
            messagebox.showinfo("Saved!", mafKilled + " was almost killed by the mafia, but was saved!")
            mafKilled = ""

        elif (mafKilled == Three and Three in docHeal) or (mafKilled == Three and jailed == Three) or (mafKilled == Three and gHeal == Three):
            saved = tkinter.Label(deadWindow, text = "Night: " + str(nightNumber) + "  " + mafKilled + " was almost killed by the mafia, but was saved!")
            saved.grid(row = r, column = c)
            r = r + 2
            messagebox.showinfo("Saved!", mafKilled + " was almost killed by the mafia, but was saved!")
            mafKilled = ""

        elif (mafKilled == Four and Four in docHeal) or (mafKilled == Four and jailed == Four) or (mafKilled == Four and gHeal == Four):
            messagebox.showinfo("Saved!", mafKilled + " was almost killed by the mafia, but was saved!")
            saved = tkinter.Label(deadWindow, text = "Night: " + str(nightNumber) + "  " + mafKilled + " was almost killed by the mafia, but was saved!")
            saved.grid(row = r, column = c)
            r = r + 2
            mafKilled = ""
        elif (mafKilled == Five and docHeal == Five) or (mafKilled == Five and jailed == Five) or (mafKilled == Five and gHeal == Five):
            saved = tkinter.Label(deadWindow, text = "Night: " + str(nightNumber) + "  " + mafKilled + " was almost killed by the mafia, but was saved!")
            saved.grid(row = r, column = c)
            r = r + 2
            messagebox.showinfo("Saved!", mafKilled + " was almost killed by the mafia, but was saved!")
            mafKilled = ""

        elif (mafKilled == Six and Six in docHeal) or (mafKilled == Six and jailed == Six) or (mafKilled == Six and gHeal == Six):
            saved = tkinter.Label(deadWindow, text = "Night: " + str(nightNumber) + "  " + mafKilled + " was almost killed by the mafia, but was saved!")
            saved.grid(row = r, column = c)
            r = r + 2
            messagebox.showinfo("Saved!", mafKilled + " was almost killed by the mafia, but was saved!")
            mafKilled = ""

        elif (mafKilled == Seven and Seven in docHeal) or (mafKilled == Seven and jailed == Seven) or (mafKilled == Seven and gHeal == Seven):
            saved = tkinter.Label(deadWindow, text = "Night: " + str(nightNumber) + "  " + mafKilled + " was almost killed by the mafia, but was saved!")
            saved.grid(row = r, column = c)
            r = r + 2
            messagebox.showinfo("Saved!", mafKilled + " was almost killed by the mafia, but was saved!")
            mafKilled = "";

        elif (mafKilled == RealName and RealName in docHeal) or (mafKilled == RealName and jailed == RealName) or (mafKilled == RealName and gHeal == RealName):
            saved = tkinter.Label(deadWindow, text = "Night: " + str(nightNumber) + "  " + mafKilled + " was almost killed by the mafia, but was saved!")
            saved.grid(row = r, column = c)
            r = r + 2
            messagebox.showinfo("Saved!", mafKilled + " was almost killed by the mafia, but was saved!")
            mafKilled = ""

        elif mafKilled == One and One not in docHeal:
            if One in Alive:
                Alive.remove(One)
            if One in AliveTown:
                AliveTown.remove(One)
            if One in runners:
                runners.remove(One)
            mafKilledRole = bot1Role
            if mafKilledRole in townRoles:
                townRoles.remove(bot1Role)
            didMafKill = True

        elif mafKilled == Two and Two not in docHeal:
            if One in Alive:
                Alive.remove(Two)
            if Two in AliveTown:
                AliveTown.remove(Two)
            if Two in runners:
                runners.remove(Two)
            mafKilledRole = bot2Role
            if mafKilledRole in townRoles:
                townRoles.remove(bot2Role)
            didMafKill = True

        elif mafKilled == Three and Three not in docHeal:
            if Three in Alive:
                Alive.remove(Three)
            if Three in AliveTown:
                AliveTown.remove(Three)
            if Three in runners:
                runners.remove(Three)
            mafKilledRole = bot3Role
            if mafKilledRole in townRoles:
                townRoles.remove(bot3Role)
            didMafKill = True

        elif mafKilled == Four and Four not in docHeal:
            if Four in Alive:
                Alive.remove(Four)
            if Four in AliveTown:
                AliveTown.remove(Four)
            if Four in runners:
                runners.remove(Four)
            mafKilledRole = bot4Role
            if mafKilledRole in townRoles:
                townRoles.remove(bot4Role)
            didMafKill = True

        elif mafKilled == Five and Five not in docHeal:
            if Five in Alive:
                Alive.remove(Five)
            if Five in AliveTown:
                AliveTown.remove(Five)
            if Five in runners:
                runners.remove(Five)
            mafKilledRole = bot5Role
            if mafKilledRole in townRoles:
                townRoles.remove(bot5Role)
            didMafKill = True

        elif mafKilled == Six and Six not in docHeal:
            if Six in Alive:
                Alive.remove(Six)
            if Six in AliveTown:
                AliveTown.remove(Six)
            if Six in runners:
                runners.remove(Six)
            mafKilledRole = bot6Role
            if mafKilledRole in townRoles:
                townRoles.remove(bot6Role)
            didMafKill = True

        elif mafKilled == Seven and Seven not in docHeal:
            if Seven in Alive:
                Alive.remove(Seven)
            if Seven in AliveTown:
                AliveTown.remove(Seven)
            if Seven in runners:    
                runners.remove(Seven)
            mafKilledRole = bot7Role
            if mafKilledRole in townRoles:
                townRoles.remove(bot7Role)
            didMafKill = True
            
        elif mafKilled == RealName and RealName not in docHeal:
            mafKilledRole = PlayerRole

            if RealName in Alive:
                Alive.remove(RealName)

            if PlayerRole in AliveTown:
                AliveTown.remove(RealName)

            if RealName in runners:
                runners.remove(RealName)

            if mafKilledRole in townRoles:
                townRoles.remove(PlayerRole)
            didMafKill = True


    if didMafKill == True:
        if mafKilledRole in AliveRoles:
            AliveRoles.remove(mafKilledRole)

        

    elif dayNumber > 1 and didMafKill == False and game == True and mafKilled != "":
        messagebox.showinfo("Maf is Dumb!", "Maf didn't kill anyone last night!")


    if didJailorKill == True:
        if jailorKilled != RealName:
            jailDeadWindow = tkinter.Label(deadWindow, text = "Night: " + str(nightNumber) + "  " + jailorKilled + " was killed by the Jailor. His role was " + jailorKilledRole)
            jailDeadWindow.grid(row = r, column = c)
            r = r + 2
            messagebox.showinfo("Jailor Killed", jailorKilled + " was killed by the Jailor. \n His role was " + jailorKilledRole)
            if jailorKilledRole in AliveRoles:
                AliveRoles.remove(jailorKilledRole)

        if jailorKilled == One:
            if One in runners:
                runners.remove(One)
            if jailorKilled in Alive:
                Alive.remove(One)
            if jailorKilledRole == "Mafia" and One in AliveMaf:
                AliveMaf.remove(One)
            else:
                if jailorKilledRole in townRoles:
                    townRoles.remove(jailorKilledRole)
                if One in AliveTown:
                    AliveTown.remove(One)

        if jailorKilled == Two:
            if Two in runners:
                runners.remove(Two)
            if jailorKilled in Alive:
                Alive.remove(Two)
            if jailorKilledRole == "Mafia" and Two in AliveMaf:
                AliveMaf.remove(Two)
            else:
                if jailorKilledRole in townRoles:
                    townRoles.remove(jailorKilledRole)
                if Two in AliveTown:
                    AliveTown.remove(Two)

        if jailorKilled == Three:
            if Three in runners:
                runners.remove(Three)
            if jailorKilled in Alive:
                Alive.remove(jailorKilled)
            if jailorKilledRole == "Mafia" and Three in AliveMaf:
                AliveMaf.remove(Three)
            else:
                if jailorKiledRole in townRoles:
                    townRoles.remove(jailorKilledRole)
                if Three in AliveTown:
                    AliveTown.remove(Three)
                
        if jailorKilled == Four:
            if Four in runners:
                runners.remove(Four)
            if jailorKilled in Alive:
                Alive.remove(Four)
            if jailorKilledRole == "Mafia" and Four in AliveMaf:
                AliveMaf.remove(Four)
            else:
                if jailorKilledRole in townRoles:
                    townRoles.remove(jailorKilledRole)
                if Four in AliveTown:
                    AliveTown.remove(Four)

        if jailorKilled == Five:
            if Five in runners:
                runners.remove(Five)
            if jailorKilled in Alive:
                Alive.remove(Five)
            if jailorKilledRole == "Mafia" and Five in AliveMaf:
                AliveMaf.remove(Five)
            else:
                if jailorKilledRole in townRoles:
                    townRoles.remove(jailorKilledRole)
                if Five in AliveTown:
                    AliveTown.remove(Five)

        if jailorKilled == Six:
            if Six in runners:
                runners.remove(Six)
            if jailorKilled in Alive:
                Alive.remove(Six)
            if jailorKilledRole == "Mafia" and Six in AliveMaf:
                AliveMaf.remove(Six)
            else:
                if jailorKilledRole in townRoles:
                    townRoles.remove(jailorKilledRole)
                if Six in AliveTown:
                    AliveTown.remove(Six)

        if jailorKilled == Seven:
            if Seven in runners:
                runners.remove(Seven)
            if jailorKilled in Alive:
                Alive.remove(Seven)
            if jailorKilledRole == "Mafia" and Seven in AliveMaf:
                AliveMaf.remove(Seven)
            else:
                if jailorKilledRole in townRoles:
                    townRoles.remove(jailorKilledRole)
                if Seven in AliveTown:
                    AliveTown.remove(Seven)
            
                
        if jailorKilled == RealName:
            died()
            if RealName in runners:
                runners.remove(RealName)
            jailedAndKilled = tkinter.Label(deadWindow, text = "Night: " + str(nightNumber) + "  You were executed by the Jailor!")
            jailedAndKilled.grid(row = r, column = c)
            r = r + 2
            messagebox.showinfo("Died!", "You were executed by the Jailor!")

            if jailorKilled in Alive:
                Alive.remove(RealName)
            if jailorKilledRole == "Mafia" and RealName in AliveMaf:
                AliveMaf.remove(RealName)
            else:
                if jailorKilledRole in townRoles:
                    townRoles.remove(jailorKilledRole)
                if RealName in AliveTown:
                    AliveTown.remove(RealName)


    else:
        jailorKilled = ""
        jailed = ""

    if didMafKill == True and mafKilled != RealName and mafKilled != "":
        killed = tkinter.Label(deadWindow, text = "Night: " + str(nightNumber) + "  " + mafKilled + " was killed by the mafia. His role was " + mafKilledRole)
        killed.grid(row = r, column = c)
        r = r + 2
        messagebox.showinfo("Mafia Killed", mafKilled + " was killed by the mafia \n His role was " + mafKilledRole)
        dayHeir()

        if mafKilled in Alive:
            Alive.remove(mafKilled)
    elif didMafKill == True and mafKilled == RealName and mafKilled != "":
        died()
        youDied = tkinter.Label(deadWindow, text = "Night: " + str(nightNumber) + "  " + mafKilled + " was killed by the mafia")
        youDied.grid(row = r, column = c)
        r = r + 2
        messagebox.showinfo("You died!", "You were killed by the mafia!")
        if mafKilled in Alive:
            Alive.remove(mafKilled)


    if reviving == True:
        Alive.append(toBeRevived)
        AliveTown.append(toBeRevived)
        hasRevived = True
        revivedPerson = tkinter.Label(deadWindow, text = "Night: " + str(nightNumber) + "  " + toBeRevived + " was revived!")
        revivedRole = playersAndTheirRoles[revivedPerson]
        AliveRoles.append(revivedRole)
        r += 2
        
    if len(plaguebearer) > 0 and PlayerRole != "Plaguebearer" and PlayerRole != "Pestilence" and dayNumber > 1:
        infect = random.choice(Alive)
        if infect in infected:
            infect = random.choice(Alive)
        infected.append(infect)

    pestsChoice = Alive


    for player in playersAndTheirRoles:
        if player in Alive and PlayerRole != "Plaguebearer":
            if playersAndTheirRoles[player] == "Pestilence":
                pestsChoice.remove(player)
                pestKilled = random.choice(pestsChoice)
                if pestKilled in plaguebearer:
                    pestKilled = random.choice(Alive)
                pestKilledRole = playersAndTheirRoles[pestKilled]
                didPestKill = True

    if dayNumber > 1:
        if mafKilledRole == "Heir":
            Heirs.remove(mafKilled)
    infectedYet = False


    if dayNumber > 1:
        if didPestKill == True:
            if pestKilled in Alive:
                Alive.remove(pestKilled)
            if pestKilled in AliveTown:
                AliveTown.remove(pestKilled)
            if pestKilled in AliveMaf:
                AliveMaf.remove(pestKilled)
            if playersAndTheirRoles[pestKilled] in AliveRoles:
                AliveRoles.remove(playersAndTheirRoles[pestKilled])

            pestKilledLabel = tkinter.Label(deadWindow, text = "Night: " + str(nightNumber) + "  " + pestKilled + " was killed by Pestilence, Horseman of the Apocalypse.")
            if PlayerRole == "Pestilence":
                messagebox.showinfo("Role", pestKilled + "'s role is " + pestKilledRole)
            pestKilledLabel.grid(row = r, column = 0)
            pestKilledLabel.configure(bg = "#636261")
            if pestKilledRole in AliveRoles:
                AliveRoles.remove(pestKilledRole)
            r += 2

    if dayNumber == 1:
        didJestHaunt = False
    if dayNumber > 1 and didJestHaunt == True:
        if jestHaunt in Alive:
            Alive.remove(jestHaunt)
        if jestHaunt in AliveTown:
            AliveTown.remove(jestHaunt)
        if jestHaunt in AliveMaf:
            AliveMaf.remove(jestHaunt)
        if jestHaunt in plaguebearer:
            plaguebearer.remove(jestHaunt)

        jestHauntRole = playersAndTheirRoles[jestHaunt]

        if jestHauntRole in townRoles:
            townRoles.remove(jestHauntRole)
        if jestHauntRole in AliveRoles:
            AliveRoles.remove(jestHauntRole)

        if jestHaunt != RealName:
            jestHauntLabel = tkinter.Label(deadWindow, text = "Night: " + str(nightNumber) + "  " + jestHaunt + " was haunted by the Jester. His role was " + jestHauntRole)
            jestHauntLabel.grid(row = r, column = 0)
        else:
            jestHauntLabel = tkinter.Label(deadWindow, text = "Night: " + str(nightNumber) + "  You were Haunted by the Jester!")
            jestHauntLabel.grid(row = r, column = 0)
            died()
            if RealName in Alive:
                Alive.remove(RealName)
        r += 1
    
    for player in plaguebearer:
        if player not in Alive:
            plaguebearer.remove(player)

    docInfected = False
    copInfected = True

    
    if "Plaguebearer" in AliveRoles and dayNumber > 1:
        if jailed in infected:
            if Jailor not in infected:
                infected.append(Jailor)

        for healed in docHeal:
            if healed in infected and len(iDocs) > 0:
                doc = random.choice(iDocs)
                if doc not in infected:
                    infected.append(doc)
                    iDocs.remove(doc)
        if mafKilled in infected and len(iMafia) > 0:
            iMaf = random.choice(iMafia)
            if iMaf not in infected:
                infected.append(iMaf)
                iMafia.remove(iMaf)

        for checked in copsCheck:
            if checked in infected and len(iCops) > 0:
                cop = random.choice(iCops)
                if cop not in infected:
                    infected.append(cop)
                    iCops.remove(cop)


    
    for players in infected:
        if players not in Alive:
            infected.remove(players)
                
            
    if PlayerRole == "Plaguebearer" and dayNumber > 1 and RealName in Alive:
        if infect in Alive and infect not in infected:
            infected.append(infect)
        if mafKilled in infected:
            infected.remove(mafKilled)

        messagebox.showinfo("Infected", "These are the infected: \n" + str(infected))


    if "Plaguebearer" in AliveRoles and dayNumber > 1 and PlayerRole == "Plaguebearer":
        
        if infect not in infected:
            infected.append(infect)
        

        if jailorKilled in infected:
            infected.remove(jailorKilled)
        
    elif PlayerRole == "Plaguebearer" and RealName not in Alive:
        plaguebearer = []
        infected = []
    elif PlayerRole == "Pestilence":
        infected = []

    if len(infected) >= len(Alive) and pest == False and "Plaguebearer" in AliveRoles:
        PestNoti = tkinter.Label(deadWindow, text = "A plague has consumed the Town summoning Pestilence!")
        PestNoti.configure(bg = "red")
        PestNoti.grid(row = r, column = 0)
        r += 2
        pest = True

        if bot1Role == "Plaguebearer":
            bot1Role = "Pestilence"
        elif bot2Role == "Plaguebearer":
            bot2Role = "Pestilence"
        elif bot3Role == "Plaguebearer":
            bot3Role = "Pestilence"
        elif bot4Role == "Plaguebearer":
            bot4Role = "Pestilence"
        elif bot5Role == "Plaguebearer":
            bot5Role = "Pestilence"
        elif bot6Role == "Plaguebearer":
            bot6Role = "Pestilence"
        elif bot7Role == "Plaguebearer":
            bot7Role = "Pestilence"
        elif PlayerRole == "Plaguebearer":
            PlayerRole = "Pestilence"
            text2.configure(text = "Role: " + str(PlayerRole))



    if dayNumber == 1:
        lynchedRole = ""


    if len(AliveMaf) < 1 and "Plaguebearer" not in AliveRoles:
        game = False
        callWinner = "Town"

    if len(AliveTown) < len(AliveMaf) and "Plaguebearer" not in AliveRoles:
        game = False
        callWinner = "Mafia"

    if len(Alive) == 1 and "Plaguebearer" in AliveRoles:
        game = False
        callWinner = "Pestilence"

    if len(Alive) == 0:
        game = False
        callWinner = "Draw"

    if game == True:
        if dayNumber < 2:
            Day.after(10000, nights)
            player1Vote = 0
            player2Vote = 0
            Player3Vote = 0
        else:
            Day.after(10000, Lynch)
            
    elif game == False and callWinner == "Mafia":
        winner = tkinter.Label(deadWindow, text = "The Mafia have won the game!")
        winner.grid(row = r, column = c)
        messagebox.showinfo("Winner!", "The mafia have won the game!")
        winners = Maf

        Day.destroy()
        finished()
    elif game == False and callWinner == "Town":
        winner = tkinter.Label(deadWindow, text = "The Town has won the game!")
        winner.grid(row = r, column = c)
        r = r + 2
        messagebox.showinfo("Winner!", "The town has won the game!")
        winners = Town

        Day.destroy()
        finished()
    elif game == False and callWinner == "Pestilence":
        winner = tkinter.Label(deadWindow, text = "Pestilence has won the game!")
        winner.grid(row = r, column = c)
        r += 2
        messagebox.showinfo("Winner!", "Pestilence has won the game!")
        for player in playersAndTheirRoles:
            if playersAndTheirRoles[player] == "Pestilence":
                winners.append(player)
        finished()

    elif game == False and callWinner == "Draw":
        winner = tkinter.Label(deadWindow, text = "The game has ended in a draw!")
        winner.grid(row = r, column = c)
        r += 2

        finished()
        

    if dayNumber > 1:
        windowForAlive.destroy()

    windowForAlives()

    if dayNumber > 1:
        windowForDead.destroy()

    windowForDeads()



    mafKilled = ""
    

    if One in Alive:
        bot1Button = tkinter.Button(Day, text = One, command = dayAbilities1)
        bot1Button.configure(bg = "yellow", width = 14)
        bot1Button.place(x = 0, y = 275)

    if Two in Alive:
        bot2Button = tkinter.Button(Day, text = Two, command = dayAbilities2)
        bot2Button.configure(bg = "yellow", width = 14)
        bot2Button.place(x = 95, y = 275)

    if Three in Alive:
        bot3Button = tkinter.Button(Day, text = Three, command = dayAbilities3)
        bot3Button.configure(bg = "yellow", width = 14)
        bot3Button.place(x = 190, y = 275)

    if Four in Alive:
        bot4Button = tkinter.Button(Day, text = Four, command = dayAbilities4)
        bot4Button.configure(bg = "yellow", width = 14)
        bot4Button.place(x = 0, y = 250)

    if Five in Alive:
        bot5Button = tkinter.Button(Day, text = Five, command = dayAbilities5)
        bot5Button.configure(bg = "yellow", width = 14)
        bot5Button.place(x = 95, y = 250)

    if Six in Alive:
        bot6Button = tkinter.Button(Day, text = Six, command = dayAbilities6)
        bot6Button.configure(bg = "yellow", width = 14)
        bot6Button.place(x = 190, y = 250)

    if Seven in Alive:
        bot7Button = tkinter.Button(Day, text = Seven, command = dayAbilities7)
        bot7Button.configure(bg = "yellow", width = 14)
        bot7Button.place(x = 95, y = 225)
            





    if "Jailor" in townRoles and PlayerRole != "Jailor":
        jailed = random.choice(Alive)



    Day.mainloop()


def nights():
    global bot1Role, bot2Role, bot3Role, bot4Role, bot5Role, bot6Role, bot7Role, jailed, mafKilled, lynched, lynchedTrue, RealName, playersAndTheirRoles, root
    global deadWindow, r, c, lynchedRole, yCoor, PlayerRole, rolesUnlocked
    if dayNumber > 1:
        lynch.destroy()
    else:
        Day.destroy()
    global nightNumber
    global night, day, Alive, AliveMaf, AliveTown, townRoles, game, otherMafs
    global didJailorKill, jailorKilled, didMafKill, mafKilledRole, didInvest, jailed
    global Player1Vote, Player2Vote, Player3Vote, myVote, runners, running
    global One, Two, Three, Four, Five, Six, Seven
    global jester, Maf, Town, winners, root2, playerHeirTo, reviving, infected, plaguebearer, text2, infect
    global copsCheck, didPestKill, pestKilled, pestKilledRole, pestNoti, pest, didJestHaunt, canHaunt, jestHaunt, jestersLynched
    global windowForAlive, gHeals, didgHeal, gHeal, target


    y = [1, 2, 3]

    if "Guardian" not in roles:
        target = ""

    if target in Alive:
        x = random.choice(y)
        if x == 1:
            gHeal = target
            didgHeal = True
            gHeals += 1
        else:
            didgHeal = False
            gHeal = ""
    
    didPestKill = False
    copsCheck = []
    reviving = False

    playersAndTheirRoles = {One: bot1Role, Two: bot2Role, Three: bot3Role, Four: bot4Role, Five: bot5Role, Six: bot6Role, Seven: bot7Role, RealName: PlayerRole}

    playerHeirTo = ""

    for player in playersAndTheirRoles:
        if player in Alive:
            if playersAndTheirRoles[player] == "Cop":
                copsCheck.append(random.choice(Alive))

    didMafKill = False
    mafKilledRole = ""
    


    didInvest = 0

    didJailorKill = False

    nightNumber = nightNumber + 1

    docHeal = []

    night = tkinter.Tk()
    night.configure(background = "#A9A9A9")
    night.title("Night")
    night.geometry("295x300+105+200")
    text1 = tkinter.Label(night, text = "Night " + str(nightNumber))
    text1.place(x = 0, y = 0)
    text1.configure(background = "#A9A9A9")
    night.resizable(width = False, height = False)

    text2 = tkinter.Label(night, text = "Role: " + str(PlayerRole))
    text2.place(x = 230 - (len(RealName) * 4), y = 0)
    text2.configure(background = "#A9A9A9")

    text3 = tkinter.Label(night, text = "Name: " + str(RealName))
    text3.place(x = 75, y = 0)
    text3.configure(background = "#A9A9A9")


    roleInfoButton = tkinter.Button(night, text = "Role Info", command = roleInfo)
    roleInfoButton.place(x = 230, y = 20)
 

    if dayNumber > 1:


        max_votes = max(running.values())
        cans = [candidate for candidate, votes in running.items() if votes == max_votes]

        if len(cans) > 1:
            lynchedTrue = False
        else:
            lynched = random.choice(cans)
            lynchedTrue = True

        bot1Role = bot1Role
        bot2Role = bot2Role
        bot3Role = bot3Role
        bot4Role = bot4Role
        bot5Role = bot5Role
        bot6Role = bot6Role
        bot7Role = bot7Role

        if lynchedTrue == True:
            lynchedRole = playersAndTheirRoles[lynched]


        if lynchedRole == "Plaguebearer" or lynchedRole == "Pestilence" and lynched in plaguebearer:
            plaguebearer.remove(lynched)
            

        

    if lynchedRole == "" and lynchedTrue == True:
        lynchedRole = "PROBLEM"

    if lynchedRole == "Jester":
        messagebox.showinfo("Ackkk!", "The Jester will get his revenge from the grave!")




    if lynchedTrue == True:
        Alive.remove(lynched)
        if lynchedRole == "Mafia":
            if lynched in AliveMaf:
                AliveMaf.remove(lynched)
        elif lynchedRole in townRoles:
            AliveTown.remove(lynched)
            townRoles.remove(lynchedRole)
        elif lynchedRole == "Plaguebearer" or lynchedRole == "Pestilence":
            if lynched in plaguebearer:
                plaguebearer.remove(lynched)
        if lynchedRole in AliveRoles:
            AliveRoles.remove(lynchedRole)

            
        if lynchedTrue == True and lynched != RealName:

            lynchedInfo = tkinter.Label(deadWindow, text = "Day: " + str(dayNumber) + "  " + lynched + " was lynched. His role was " + lynchedRole)
            lynchedInfo.grid(row = r, column = c)
            r = r + 2
            messagebox.showinfo("Lynched!", lynched + " was lynched. His role was " + lynchedRole)

        elif lynchedTrue == True and lynched == RealName:
            died()
            lynchedInfo = tkinter.Label(deadWindow, text = "Day: " + str(dayNumber) + "  You were lynched!")
            lynchedInfo.grid(row = r, column = c)
            r = r + 2
            messagebox.showinfo("Lynched!", "You were lynched!")

        runners.remove(lynched)

    else:
        lynched = ""
        lynchedRole = ""

    if lynchedRole in AliveRoles:
        AliveRoles.remove(lynchedRole)

    didJestHaunt = False

    if lynchedRole == "Jester":
        jestersLynched.append(lynched)
        jestHaunt = random.choice(Alive)
        didJestHaunt = True
        jestHauntRole = playersAndTheirRoles[jestHaunt]
    else:
        jestHaunt = ""
        jestHauntRole = ""
        didJestHaunt = False


    if lynched == RealName and PlayerRole == "Jester":
        canHaunt = True
        didJestHaunt = True


        


        
    if len(AliveMaf) == 0 and "Plaguebearer" not in AliveRoles:
         game = False
         callWinner = "Town"

    elif len(AliveTown) < len(AliveMaf) and "Plaguebearer" not in AliveRoles:
        game = False
        callWinner = "Mafia"

    elif len(Alive) == 1 and "Plaguebearer" in AliveRoles:
        game = False
        callWinner = "Pestilence"

    elif len(Alive) == 0 and len(jestersLynched) > 0:
        game = False
        callWinner = "Jester"

    elif len(Alive) == 0:
        game = False
        callWinner = "Draw"

    else:
        game = True
        
        

    if game == False and callWinner == "Jester":
        winner = tkinter.Label(deadWindow, text = "Winner! The Jester has won the game!")
        messagebox.showinfo("Winner!", "The Jester has won the game!")

        winners = jestersLynched

        night.destroy()
        finished()

    elif game == False and callWinner == "Mafia":
        winner = tkinter.Label(deadWindow, text = "Winner! The Mafia have won the game!")
        winner.grid(row = r, column = c)
        r = r + 2
        messagebox.showinfo("Winner!", "The mafia have won the game!")
        winners = Maf
        if len(jestersLynched) > 0:
            for jesters in jestersLynched:
                winners.append(jesters)


        night.destroy()
        finished()

    elif game == False and callWinner == "Town":
        if len(plaguebearer) == 0:
            winner = tkinter.Label(deadWindow, text = "Winner! The Town has won the game!")
            winner.grid(row = r, column = c)
            r = r + 2
            messagebox.showinfo("Winner!", "The town has won the game!")
            winners = Town
            if len(jestersLynched) > 0:
                for jesters in jestersLynched:
                    winners.append(jesters)

            night.destroy()
            finished()

    elif game == False and callWinner == "Pestilence":
        winner = tkinter.Label(deadWindow, text = "Winner! Pestilence has won the game!")
        winner.grid(row = r, column = c)
        r = r + 2
        messagebox.showinfo("Winner!", "Pestilence has won the game!")
        winners = plaguebearer
        if len(jestersLynched) > 0:
            for jesters in jestersLynched:
                winners.append(jesters)

        night.destroy()
        finished()
    else:
        game = True

    
    if len(infected) >= len(Alive) and pest == False and "Plaguebearer" in AliveRoles:
        PestNoti = tkinter.Label(deadWindow, text = "A plague has consumed the Town summoning Pestilence!")
        PestNoti.configure(bg = "red")
        PestNoti.grid(row = r, column = 0)
        r += 2
        pest = True


        if bot1Role == "Plaguebearer":
            bot1Role = "Pestilence"
        elif bot2Role == "Plaguebearer":
            bot2Role = "Pestilence"
        elif bot3Role == "Plaguebearer":
            bot3Role = "Pestilence"
        elif bot4Role == "Plaguebearer":
            bot4Role = "Plaguebearer"
        elif bot5Role == "Plaguebearer":
            bot5Role = "Pestilence"
        elif bot6Role == "Plaguebearer":
            bot6Role = "Pestilence"
        elif bot7Role == "Plaguebearer":
            bot7Role = "Pestilence"
        elif PlayerRole == "Plaguebearer":
            PlayerRole = "Pestilence"
            text2.configure(text = "Role: " + str(PlayerRole))
        
    if "Jailor" not in townRoles or jailed not in Alive or game == False:
        jailed = ""

    windowForAlive.destroy()

    windowForAlives()


    windowForDead.destroy()

    windowForDeads()


    if RealName in Alive:
        if jailed != RealName:
            
            if PlayerRole == "Jailor":
        
                if jailed == One:
                    messagebox.showinfo("Jailor Info", One + "'s role is " + bot1Role)
                    executeButton = tkinter.Button(night, text = "Kill " + One, command = jailorKill)
                    executeButton.place(x = 100, y = 200)
                elif jailed == Two:
                    messagebox.showinfo("Jailor Info", Two + "'s role is " + bot2Role)
                    executeButton = tkinter.Button(night, text = "Kill " + Two, command = jailorKill)
                    executeButton.place(x = 100, y = 200)
                elif jailed == Three:
                    messagebox.showinfo("Jailor Info", Three + "'s role is " + bot3Role)
                    executeButton = tkinter.Button(night, text = "Kill " + Three, command = jailorKill)
                    executeButton.place(x = 100, y = 200)
                elif jailed == Four:
                    messagebox.showinfo("Jailor Info", Four + "'s role is " + bot4Role)
                    executeButton = tkinter.Button(night, text = "Kill " + Four, command = jailorKill)
                    executeButton.place(x = 100, y = 200)
                elif jailed == Five:
                    messagebox.showinfo("Jailor Info", Five + "'s role is " + bot5Role)
                    executeButton = tkinter.Button(night, text = "Kill " + Five, command = jailorKill)
                    executeButton.place(x = 100, y = 200)
                elif jailed == Six:
                    messagebox.showinfo("Jailor Info", Six + "'s role is " + bot6Role)
                    executeButton = tkinter.Button(night, text = "Kill " + Six, command = jailorKill)
                    executeButton.place(x = 100, y = 200)
                elif jailed == Seven:
                    messagebox.showinfo("Jailor Info", Seven + "'s role is " + bot7Role)
                    executeButton = tkinter.Button(night, text = "Kill " + Seven, command = jailorKill)
                    executeButton.place(x = 100, y = 200)
                    
                else:
                    messagebox.showinfo("Jailor Info", "You didn't jail anyone tonight!")
            elif PlayerRole == "Doc":
                if One in Alive:
                    bot1Button = tkinter.Button(night, text = One, command = docHeal1)
                    bot1Button.configure(bg = "#B49B10", width = 14)
                    bot1Button.place(x = 0, y = 275)
                if Two in Alive:
                    bot2Button = tkinter.Button(night, text = Two, command = docHeal2)
                    bot2Button.configure(bg = "#B49B10", width = 14)
                    bot2Button.place(x = 95, y = 275)
                if Three in Alive:
                    bot3Button = tkinter.Button(night, text = Three, command = docHeal3)
                    bot3Button.configure(bg = "#B49B10", width = 14)
                    bot3Button.place(x = 190, y = 275)
                if Four in Alive:
                    bot4Button = tkinter.Button(night, text = Four, command = docHeal4)
                    bot4Button.configure(bg = "#B49B10", width = 14)
                    bot4Button.place(x = 0, y = 250)
                if Five in Alive:
                    bot5Button = tkinter.Button(night, text = Five, command = docHeal5)
                    bot5Button.configure(bg = "#B49B10", width = 14)
                    bot5Button.place(x = 95, y = 250)
                if Six in Alive:
                    bot6Button = tkinter.Button(night, text = Six, command = docHeal6)
                    bot6Button.configure(bg = "#B49B10", width = 14)
                    bot6Button.place(x = 190, y = 250)
                if Seven in Alive:
                    bot7Button = tkinter.Button(night, text = Seven, command = docHeal7)
                    bot7Button.configure(bg = "#B49B10", width = 14)
                    bot7Button.place(x = 0, y = 225)

                yourself = tkinter.Button(night, text = RealName, command = docHealSelf)
                yourself.configure(bg = "#B49B10", width = 14)
                yourself.place(x = 95, y = 225)
            elif PlayerRole == "Cop":
                if One in Alive:
                    bot1Button = tkinter.Button(night, text = One, command = invest1)
                    bot1Button.configure(bg = "#B49B10", width = 14)
                    bot1Button.place(x = 0, y = 275)
                if Two in Alive:
                    bot2Button = tkinter.Button(night, text = Two, command = invest2)
                    bot2Button.configure(bg = "#B49B10", width = 14)
                    bot2Button.place(x = 95, y = 275)
                if Three in Alive:
                    bot3Button = tkinter.Button(night, text = Three, command = invest3)
                    bot3Button.configure(bg = "#B49B10", width = 14)
                    bot3Button.place(x = 190, y = 275)
                if Four in Alive:
                    bot4Button = tkinter.Button(night, text = Four, command = invest4)
                    bot4Button.configure(bg = "#B49B10", width = 14)
                    bot4Button.place(x = 0, y = 250)
                if Five in Alive:
                    bot5Button = tkinter.Button(night, text = Five, command = invest5)
                    bot5Button.configure(bg = "#B49B10", width = 14)
                    bot5Button.place(x = 95, y = 250)
                if Six in Alive:
                    bot6Button = tkinter.Button(night, text = Six, command = invest6)
                    bot6Button.configure(bg = "#B49B10", width = 14)
                    bot6Button.place(x = 190, y = 250)
                if Seven in Alive:
                    bot7Button = tkinter.Button(night, text = Seven, command = invest7)
                    bot7Button.configure(bg = "#B49B10", width = 14)
                    bot7Button.place(x = 95, y = 225)
            elif PlayerRole == "Heir":
                if One in Alive:
                    bot1Button = tkinter.Button(night, text = One, command = heir1)
                    bot1Button.configure(bg = "#B49B10", width = 14)
                    bot1Button.place(x = 0, y = 275)
                if Two in Alive:
                    bot2Button = tkinter.Button(night, text = Two, command = heir2)
                    bot2Button.configure(bg = "#B49B10", width = 14)
                    bot2Button.place(x = 95, y = 275)
                if Three in Alive:
                    bot3Button = tkinter.Button(night, text = Three, command = heir3)
                    bot3Button.configure(bg = "#B49B10", width = 14)
                    bot3Button.place(x = 190, y = 275)
                if Four in Alive:
                    bot4Button = tkinter.Button(night, text = Four, command = heir4)
                    bot4Button.configure(bg = "#B49B10", width = 14)
                    bot4Button.place(x = 0, y = 250)
                if Five in Alive:
                    bot5Button = tkinter.Button(night, text = Five, command = heir5)
                    bot5Button.configure(bg = "#B49B10", width = 14)
                    bot5Button.place(x = 95, y = 250)
                if Six in Alive:
                    bot6Button = tkinter.Button(night, text = Six, command = heir6)
                    bot6Button.configure(bg = "#B49B10", width = 14)
                    bot6Button.place(x = 190, y = 250)
                if Seven in Alive:
                    bot7Button = tkinter.Button(night, text = Seven, command = heir7)
                    bot7Button.configure(bg = "#B49B10", width = 14)
                    bot7Button.place(x = 95, y = 225)

#RETRI

            elif PlayerRole == "Retri":
                if One not in Alive and One not in Maf:
                    bot1Button = tkinter.Button(night, text = One, command = rev1)
                    bot1Button.configure(bg = "#B49B10", width = 14)
                    bot1Button.place(x = 0, y = 275)
                if Two not in Alive and Two not in Maf:
                    bot2Button = tkinter.Button(night, text = Two, command = rev2)
                    bot2Button.configure(bg = "#B49B10", width = 14)
                    bot2Button.place(x = 95, y = 275)
                if Three not in Alive and Three not in Maf:
                    bot3Button = tkinter.Button(night, text = Three, command = rev3)
                    bot3Button.configure(bg = "#B49B10", width = 14)
                    bot3Button.place(x = 190, y = 275)
                if Four not in Alive and Four not in Maf:
                    bot4Button = tkinter.Button(night, text = Four, command = rev4)
                    bot4Button.configure(bg = "#B49B10", width = 14)
                    bot4Button.place(x = 0, y = 250)
                if Five not in Alive and Five not in Maf:
                    bot5Button = tkinter.Button(night, text = Five, command = rev5)
                    bot5Button.configure(bg = "#B49B10", width = 14)
                    bot5Button.place(x = 95, y = 250)
                if Six not in Alive and Six not in Maf:
                    bot6Button = tkinter.Button(night, text = Six, command = rev6)
                    bot6Button.configure(bg = "#B49B10", width = 14)
                    bot6Button.place(x = 190, y = 250)
                if Seven not in Alive and Seven not in Maf:
                    bot7Button = tkinter.Button(night, text = Seven, command = rev7)
                    bot7Button.configure(bg = "#B49B10", width = 14)
                    bot7Button.place(x = 95, y = 225)
                

            
            elif jailed != RealName and PlayerRole == "Mafia":


                    
                
                if One in Alive and One not in AliveMaf:
                    bot1Button = tkinter.Button(night, text = One, command = mafKill1)
                    bot1Button.configure(bg = "red", width = 14)
                    bot1Button.place(x = 0, y = 275)
                if Two in Alive and Two not in AliveMaf:
                    bot2Button = tkinter.Button(night, text = Two, command = mafKill2)
                    bot2Button.configure(bg = "red", width = 14)
                    bot2Button.place(x = 95, y = 275)
                if Three in Alive and Three not in AliveMaf:
                    bot3Button = tkinter.Button(night, text = Three, command = mafKill3)
                    bot3Button.configure(bg = "red", width = 14)
                    bot3Button.place(x = 190, y = 275)
                if Four in Alive and Four not in AliveMaf:
                    bot4Button = tkinter.Button(night, text = Four, command = mafKill4)
                    bot4Button.configure(bg = "red", width = 14)
                    bot4Button.place(x = 0, y = 250)
                if Five in Alive and Five not in AliveMaf:
                    bot5Button = tkinter.Button(night, text = Five, command = mafKill5)
                    bot5Button.configure(bg = "red", width = 14)
                    bot5Button.place(x = 95, y = 250)
                if Six in Alive and Six not in AliveMaf:
                    bot6Button = tkinter.Button(night, text = Six, command = mafKill6)
                    bot6Button.configure(bg = "red", width = 14)
                    bot6Button.place(x = 190, y = 250)
                if Seven in Alive and Seven not in AliveMaf:
                    bot7Button = tkinter.Button(night, text = Seven, command = mafKill7)
                    bot7Button.configure(bg = "red", width = 14)
                    bot7Button.place(x = 95, y = 225)

                if jailed in AliveMaf:
                    messagebox.showinfo("Uh-oh!", jailed + " was hauled to Jail!")


                
        
        else:
            messagebox.showinfo("Jailed!", "You were jailed by the Jailor!")




        if PlayerRole == "Plaguebearer":
            infect = ""
            if jailed == RealName:
                for player in playersAndTheirRoles:
                    if playersAndTheirRoles[player] == "Jailor":
                        infect = player
                        messagebox.showinfo("Infected!", "You infected the Jailor. \nHis name is " + player)
                        
            else:
                if One in Alive and One not in infected:
                    bot1Button = tkinter.Button(night, text = One, command = infect1)
                    bot1Button.configure(bg = "#B49B10", width = 14)
                    bot1Button.place(x = 0, y = 275)
                if Two in Alive and Two not in infected:
                    bot2Button = tkinter.Button(night, text = Two, command = infect2)
                    bot2Button.configure(bg = "#B49B10", width = 14)
                    bot2Button.place(x = 95, y = 275)
                if Three in Alive and Three not in infected:
                    bot3Button = tkinter.Button(night, text = Three, command = infect3)
                    bot3Button.configure(bg = "#B49B10", width = 14)
                    bot3Button.place(x = 190, y = 275)
                if Four in Alive and Four not in infected:
                    bot4Button = tkinter.Button(night, text = Four, command = infect4)
                    bot4Button.configure(bg = "#B49B10", width = 14)
                    bot4Button.place(x = 0, y = 250)
                if Five in Alive and Five not in infected:
                    bot5Button = tkinter.Button(night, text = Five, command = infect5)
                    bot5Button.configure(bg = "#B49B10", width = 14)
                    bot5Button.place(x = 95, y = 250)
                if Six in Alive and Six not in infected:
                    bot6Button = tkinter.Button(night, text = Six, command = infect6)
                    bot6Button.configure(bg = "#B49B10", width = 14)
                    bot6Button.place(x = 190, y = 250)
                if Seven in Alive and Seven not in infected:
                    bot7Button = tkinter.Button(night, text = Seven, command = infect7)
                    bot7Button.configure(bg = "#B49B10", width = 14)
                    bot7Button.place(x = 0, y = 225)

        if PlayerRole == "Pestilence":
            if jailed == RealName:
                messagebox.showinfo("Jailed!", "The jailor has jailed you, but no chains can trap a Pestilence.\nYou killed the Jailor!")
                for player in playersAndTheirRoles:
                    if playersAndTheirRoles[player] == "Jailor":
                        pestKilled = player
                        pestKilledRole = "Jailor"
                        didPestKill = True
            else:

                if One in Alive:

                    bot1Button = tkinter.Button(night, text = One, command = lambda: pestKill(One))
                    bot1Button.configure(bg = "red", width = 14)
                    bot1Button.place(x = 0, y = 275)
                if Two in Alive:

                    bot2Button = tkinter.Button(night, text = Two, command = lambda: pestKill(Two))
                    bot2Button.configure(bg = "red", width = 14)
                    bot2Button.place(x = 95, y = 275)
                if Three in Alive:

                    bot3Button = tkinter.Button(night, text = Three, command = lambda: pestKill(Three))
                    bot3Button.configure(bg = "red", width = 14)
                    bot3Button.place(x = 190, y = 275)
                if Four in Alive:

                    bot4Button = tkinter.Button(night, text = Four, command = lambda: pestKill(Four))
                    bot4Button.configure(bg = "red", width = 14)
                    bot4Button.place(x = 0, y = 250)
                if Five in Alive:

                    bot5Button = tkinter.Button(night, text = Five, command = lambda: pestKill(Five))
                    bot5Button.configure(bg = "red", width = 14)
                    bot5Button.place(x = 95, y = 250)
                if Six in Alive:

                    bot6Button = tkinter.Button(night, text = Six, command = lambda: pestKill(Six))
                    bot6Button.configure(bg = "red", width = 14)
                    bot6Button.place(x = 190, y = 250)
                if Seven in Alive:

                    bot7Button = tkinter.Button(night, text = Seven, command = lambda: pestKill(Seven))
                    bot7Button.configure(bg = "red", width = 14)
                    bot7Button.place(x = 95, y = 225)


    if PlayerRole == "Jester" and lynched == RealName and RealName not in Alive:
        if One in Alive:
                
            bot1Button = tkinter.Button(night, text = One, command = lambda: jestKill(One))
            bot1Button.configure(bg = "red", width = 14)
            bot1Button.place(x = 0, y = 275)
        if Two in Alive:
            
            bot2Button = tkinter.Button(night, text = Two, command = lambda: jestKill(Two))
            bot2Button.configure(bg = "red", width = 14)
            bot2Button.place(x = 95, y = 275)
        if Three in Alive:
            
            bot3Button = tkinter.Button(night, text = Three, command = lambda: jestKill(Three))
            bot3Button.configure(bg = "red", width = 14)
            bot3Button.place(x = 190, y = 275)
        if Four in Alive:
            
            bot4Button = tkinter.Button(night, text = Four, command = lambda: jestKill(Four))
            bot4Button.configure(bg = "red", width = 14)
            bot4Button.place(x = 0, y = 250)
        if Five in Alive:
            
            bot5Button = tkinter.Button(night, text = Five, command = lambda: jestKill(Five))
            bot5Button.configure(bg = "red", width = 14)
            bot5Button.place(x = 95, y = 250)
        if Six in Alive:
            
            bot6Button = tkinter.Button(night, text = Six, command = lambda: jestKill(Six))
            bot6Button.configure(bg = "red", width = 14)
            bot6Button.place(x = 190, y = 250)
        if Seven in Alive:
            
            bot7Button = tkinter.Button(night, text = Seven, command = lambda: jestKill(Seven))
            bot7Button.configure(bg = "red", width = 14)
            bot7Button.place(x = 95, y = 225)

    if PlayerRole == "Guardian":
        if One == target:
                
            bot1Button = tkinter.Button(night, text = One, command = lambda: gPro(One))
            bot1Button.configure(bg = "red", width = 14)
            bot1Button.place(x = 0, y = 275)
        if Two == target:
            
            bot2Button = tkinter.Button(night, text = Two, command = lambda: gPro(Two))
            bot2Button.configure(bg = "red", width = 14)
            bot2Button.place(x = 95, y = 275)
        if Three == target:
            
            bot3Button = tkinter.Button(night, text = Three, command = lambda: gPro(Three))
            bot3Button.configure(bg = "red", width = 14)
            bot3Button.place(x = 190, y = 275)
        if Four == target:
            
            bot4Button = tkinter.Button(night, text = Four, command = lambda: gPro(Four))
            bot4Button.configure(bg = "red", width = 14)
            bot4Button.place(x = 0, y = 250)
        if Five == target:
            
            bot5Button = tkinter.Button(night, text = Five, command = lambda: gPro(Five))
            bot5Button.configure(bg = "red", width = 14)
            bot5Button.place(x = 95, y = 250)
        if Six == target:
            
            bot6Button = tkinter.Button(night, text = Six, command = lambda: gPro(Six))
            bot6Button.configure(bg = "red", width = 14)
            bot6Button.place(x = 190, y = 250)
        if Seven == target:
            
            bot7Button = tkinter.Button(night, text = Seven, command = lambda: gPro(Seven))
            bot7Button.configure(bg = "red", width = 14)
            bot7Button.place(x = 95, y = 225)
                

                
                    

    AliveDocs = Alive.count("Doc")

    if "Heir" in rolesUnlocked:
        botsHeirTo()


        

    heals = 0

    if PlayerRole == "Doc":
        while heals < (AliveDocs - 1):
            docHeal.append(random.choice(Alive))

    shouldJailorKill = [1, 2, 3]
    shouldJailorKillMaf = [1, 2]
        
    if PlayerRole != "Jailor":
        if jailed == One and bot1Role != "Jailor":
            if bot1Role == "Mafia" and random.choice(shouldJailorKillMaf) == 2:
                jailorKill()
            elif random.choice(shouldJailorKill) == 3:
                jailorKill()
        elif jailed == Two and bot2Role != "Jailor":
            if bot2Role == "Mafia" and random.choice(shouldJailorKillMaf) == 2:
                jailorKill()
            elif random.choice(shouldJailorKill) == 3:
                jailorKill()
        elif jailed == Three and bot3Role != "Jailor":
            if bot3Role == "Mafia" and random.choice(shouldJailorKillMaf) == 2:
                jailorKill()
            elif random.choice(shouldJailorKill) == 3:
                jailorKill()
        elif jailed == Four and bot4Role != "Jailor":
            if bot4Role == "Mafia" and random.choice(shouldJailorKillMaf) == 2:
                jailorKill()
            elif random.choice(shouldJailorKill) == 3:
                jailorKill()
        elif jailed == Five and bot5Role != "Jailor":
            if bot5Role == "Mafia" and random.choice(shouldJailorKillMaf) == 2:
                jailorKill()
            elif random.choice(shouldJailorKill) == 3:
                jailorKill()
        elif jailed == RealName:
            if PlayerRole == "Plaguebearer" or PlayerRole == "Pestilence":
                pass
            elif PlayerRole == "Mafia" and random.choice(shouldJailorKillMaf) == 2:
                jailorKill()
                messagebox.showinfo("To be executed:", "The Jailor has decided to execute you.")
            elif PlayerRole != "Mafia" and random.choice(shouldJailorKill) == 3:
                jailorKill()
                messagebox.showinfo("To be executed:", "The Jailor has decided to execute you.")

    night.after(15000, Days)


def dayAbilities1():
    global jailed
    global bot1jailed
    global bot2jailed
    global bot3jailed
    global role, One
    jailed = ""
    if PlayerRole == "Jailor":
        jailed = One
        messagebox.showinfo("Jailor Info", "You chose to jail " + jailed)
        bot1jailed = True
        bot2jailed = False
        bot3jailed = False

def dayAbilities2():
    global jailed
    global bot1jailed
    global bot2jailed
    global bot3jailed, bot4jailed, bot5jailed
    global role, Two
    jailed = ""
    if PlayerRole == "Jailor":
        jailed = Two
        messagebox.showinfo("Jailor Info", "You chose to jail " + jailed)
        bot1jailed = False
        bot2jailed = True
        bot3jailed = False
        bot4jailed = False
        bot5jailed = False

def dayAbilities3():
    global jailed
    global bot1jailed
    global bot2jailed
    global bot3jailed, bot4jailed, bot5jailed
    global role, Three
    jailed = ""
    if PlayerRole == "Jailor":
        jailed = Three
        messagebox.showinfo("Jailor Info", "You chose to jail " + jailed)
        bot1jailed = False
        bot2jailed = False
        bot3jailed = True
        bot4jailed = False
        bot5jailed = False
        bot6jailed = False
        bot7jailed = False


def dayAbilities4():
    global jailed
    global bot1jailed
    global bot2jailed
    global bot3jailed, bot4jailed, bot5jailed
    global role, Four
    jailed = ""
    if PlayerRole == "Jailor":
        jailed = Four
        messagebox.showinfo("Jailor Info", "You chose to jail " + jailed)
        bot1jailed = False
        bot2jailed = False
        bot3jailed = False
        bot4jailed = True
        bot5jailed = False
        bot6jailed = False
        bot7jailed = False


def dayAbilities5():
    global jailed
    global bot1jailed
    global bot2jailed
    global bot3jailed, bot4jailed, bot5jailed, bot6jailed, bot7jailed
    global role, Five
    jailed = ""
    if PlayerRole == "Jailor":
        jailed = Five
        messagebox.showinfo("Jailor Info", "You chose to jail " + jailed)
        bot1jailed = False
        bot2jailed = False
        bot3jailed = False
        bot4jailed = False
        bot5jailed = True
        bot6jailed = False
        bot7jailed = False

def dayAbilities6():
    global jailed
    global bot1jailed
    global bot2jailed
    global bot3jailed, bot4jailed, bot5jailed, bot6jailed, bot7jailed
    global role, Six
    jailed = ""
    if PlayerRole == "Jailor":
        jailed = Six
        messagebox.showinfo("Jailor Info", "You chose to jail " + jailed)
        bot1jailed = False
        bot2jailed = False
        bot3jailed = False
        bot4jailed = False
        bot5jailed = False
        bot6jailed = True
        bot7jailed = False

def dayAbilities7():
    global jailed
    global bot1jailed
    global bot2jailed
    global bot3jailed, bot4jailed, bot5jailed, bot6jailed, bot7jailed
    global role, Seven
    jailed = ""
    if PlayerRole == "Jailor":
        jailed = Seven
        messagebox.showinfo("Jailor Info", "You chose to jail " + jailed)
        bot1jailed = False
        bot2jailed = False
        bot3jailed = False
        bot4jailed = False
        bot5jailed = True
        bot6jailed = False
        bot7jailed = False
        

    

    


def enterName():
    global name, root2, game, dayNumber, nightNumber, root1, start, root, customGame, hasRevived, jestersLynched

    root2.destroy()
    root1 = tkinter.Tk()
    root1.configure(background = "cyan")
    root1.title("Enter Name")
    root1.geometry("250x25")
    root1.resizable(height = False, width = False)

    labelName = tkinter.Label(root1, text = "Enter your name:")
    labelName.grid(row = 0, column = 0)

    name = tkinter.Entry(root1)
    name.grid(row = 0, column = 1)

    if customGame == True:
        root.after(10000, customStart)
    else:

        root.after(10000, start)

    game = True
    dayNumber = 0
    nightNumber = 0
    hasRevived = False
    jestersLynched = []


    root1.mainloop()


def credit():
    global game, customWindow


    if game == True:
        messagebox.showinfo("Game in progress!", "There is already a game in progress!")
        return
    global root2
    root2 = tkinter.Tk()
    root2.configure(background = "orange")
    root2.title("Town Of Salem by SanguineL")
    root2.resizable(width = False, height = False)

    root2.geometry("500x500")

    SanguineLabel = tkinter.Label(root2, text = "Made By SanguineL")
    SanguineLabel.configure(bg = "orange")
    SanguineLabel.place(x = 180, y = 250)

    root2.after(5000, enterName)


    root2.mainloop()

def customStart():
    global RealName, PlayerRole, reviving
    global Alive, AliveMaf, AliveTown, didJailorKill, didMafKill, docHeal, selfHealedYet, deadWindow, OtherMaf, OtherMaf2, r, c, runners, running, roles, Heirs
    global One, Two, Three, Four, Five, Six, Seven, RealName, jester, Maf, Town, playersAndTheirRoles, townRoles, roles, customWindow
    global bot1Role, bot2Role, bot3Role, bot4Role, bot5Role, bot6Role, bot7Role, deadWindow, game1, custom, howManyJailors, howManyCops, howManyDocs, howManyMafia, howManyJesters, infected
    global plaguebearer, pest
    global iMafia, iCops, iDocs, Jailor, AliveRoles, target, isThereGa

    names = ["Jester", "Shut up exe", "Deathless", "TotesNotMaf", "CrAzY", "Hippo", "Greenland", "Chicago", "notSK", "AbraKadabra", "smoothie", "smitty", "LukesFather",
             "pits", "Chemistry", "Gamethrower", "plasma", "lucrative", "iLy", "TownOfSalem", "Kandango", "Matoska", "Mitt", "Winner", "strick", "apple", "Cola", "Nike", "Obama", "zomBie",
             "OneHundred", "I", "Emx", "Loas", "Polar", "Udemy", "Mafy", "Opalas", "Charmander", "Knew Yorkk", "Barred", "Conor", "5 player", "Oofala", "Queen", "xylo", "S T Y L E", "Tookie", "Bubhead",
             "John Jacob", "Czu", "TheLetterP", "Alexa", "Tissue", "Massage", "Cake", "Faceball", "XC", "Points", "Chilled", "Fantastic", "Santa", "Outlet", "Tape", "Socker", "Lotion", "Armpit",
             "Place", "Rubik", "Head", "Dice", "TikTok", "Jessie", "Muscles", "Cardistry", "Pedicure", "Phones", "CD", "PARTY", "Tipsy", "Pop", "Tonight", "Stop", "DJ", "Fight", "Woah", "Vey", "Beer", "Here",
             "Dudes", "Swagger", "Curb", "PoPo", "VirtNet", "Built", "GotMe", "Hands", "Julius", "bLoW", "DNCE", "Key", "VIP", "Laugh", "Lead", "Please", "Jane Doe", "Ian", "Allen", "Dell", "Ember", "RandomHouse",
             "Art", "Control", "Coconut", "Charge", "Dunk", "Fire", "Time", "Tightrope", "Surrounded", "IDBM", "Madness", "Anyway", "Frey", "Bryson", "Eyeball", "Core", "Donut", "Mc", "Chopsticks", "Challenge", "Stone", "Gumball",
             "Perfect", "Atlas", "Antler", "Uncle", "Blinds", "Trophy", "Tracker", "Necromancer", "Case", "Cruel", "WalkLikeMe", "Frankie", "Nutella", "GaMeR", "YouTuber", "MrsMedi", "ClaraBarton",
             "Ttk", "Options", "ImJester", "ScuzeMe", "Pineapple", "Captain", "Ginger", "Alex", "FiveTwenty", "ExplodingCats", "Minds", "Ham", "Camera", "Mayo", "Georgia", "1f2u3n4", "Binder", "Plunder"]

    if game1 == False:
        deadWindow.destroy()

    

    infected = []

    reviving = False

    One = random.choice(names)
    names.remove(One)

    Two = random.choice(names)
    names.remove(Two)

    Three = random.choice(names)
    names.remove(Three)

    Four = random.choice(names)
    names.remove(Four)

    Five = random.choice(names)
    names.remove(Five)

    Six = random.choice(names)
    names.remove(Six)

    Seven = random.choice(names)


    pest = False

    while "Mafia" in townRoles:
        townRoles.remove("Mafia")

    if "Guardian" in roles:
        isThereGa = True
    else:
        isTherGa = False
    
    
    PlayerRole = random.choice(roles)

    roles.remove(PlayerRole)


    bot1Role = random.choice(roles)

    roles.remove(bot1Role)


    bot2Role = random.choice(roles)

    roles.remove(bot2Role)


    bot3Role = random.choice(roles)


    roles.remove(bot3Role)


    bot4Role = random.choice(roles)

    roles.remove(bot4Role)


    bot5Role = random.choice(roles)


    roles.remove(bot5Role)


    bot6Role = random.choice(roles)

    roles.remove(bot6Role)


    bot7Role = random.choice(roles)



    

    didJailorKill = False
    docHeal = []
    didMafKill = False

    selfHealedYet = 0
    
    RealName = name.get()

    if RealName == '' or RealName == " " or len(RealName) > 14:
        RandomNames = ["Jonathin Corwin", "Cotton Mather", "Deodat Lawson", "Edward Bishop", "Ann Sears", "Sarah Wildes"]
        RealName = random.choice(RandomNames)


    playersAndTheirRoles = {One: bot1Role, Two: bot2Role, Three: bot3Role, Four: bot4Role, Five: bot5Role, Six: bot6Role, Seven: bot7Role, RealName: PlayerRole}
    AliveRoles = [bot1Role, bot2Role, bot3Role, bot4Role, bot5Role, bot6Role, bot7Role, PlayerRole]

    possibleTargets = []

    for player in playersAndTheirRoles:
            if playersAndTheirRoles[player] != "Guardian":
                    possibleTargets.append(player)

    if isThereGa == True:
        target = random.choice(possibleTargets)

    iDocs = []
    iCops = []
    iMafia = []

    for players in playersAndTheirRoles:
        if playersAndTheirRoles[players] == "Jailor":
            Jailor = players
        if playersAndTheirRoles[players] == "Doc":
            iDocs.append(players)
        if playersAndTheirRoles[players] == "Cop":
            iCops.append(players)
        if playersAndTheirRoles[players] == "Mafia":
            iMafia.append(players)


    running = {One: 0, Two: 0, Three: 0, Four: 0, Five: 0, Six: 0, Seven: 0, RealName: 0}
    runners = [One, Two, Three, Four, Five, Six, Seven, RealName]
    jester = []
    

    deadWindow = tkinter.Tk()
    deadWindow.title("Game Information")
    deadWindow.geometry("600x300+401+200")
    deadWindow.configure(background = "pink")

    mafOne = False

    for player in playersAndTheirRoles:
        if playersAndTheirRoles[player] == "Mafia" and mafOne == False:
            OtherMaf = player
            mafOne = True
        elif playersAndTheirRoles[player] == "Mafia" and mafOne == True:
            OtherMaf2 = player

        if playersAndTheirRoles[player] == "Jester":
            jester = [player]

        if playersAndTheirRoles[player] == "Plaguebearer":
            plaguebearer = [player]

    r = 0
    c = 0

    



    


    
    Alive = [RealName, One, Two, Three, Four, Five, Six, Seven]
    AliveTown = [One, Two, Three, Four, Five, Six, Seven, RealName]
    AliveMaf = []
    Maf = []
    otherMafs = []
    Town = [One, Two, Three, Four, Five, Six, Seven, RealName]



    if bot1Role == "Mafia":
        Maf.append(One)
        otherMafs.append(One)
        AliveMaf.append(One)
        AliveTown.remove(One)
        Town.remove(One)
    if bot2Role == "Mafia":
        Maf.append(Two)
        otherMafs.append(Two)
        AliveMaf.append(Two)
        AliveTown.remove(Two)
        Town.remove(Two)
    if bot3Role == "Mafia":
        Maf.append(Three)
        otherMafs.append(Three)
        AliveMaf.append(Three)
        AliveTown.remove(Three)
        Town.remove(Three)
    if bot4Role == "Mafia":
        Maf.append(Four)
        otherMafs.append(Four)
        AliveMaf.append(Four)
        AliveTown.remove(Four)
        Town.remove(Four)
    if bot5Role == 'Mafia':
        Maf.append(Five)
        otherMafs.append(Five)
        AliveMaf.append(Five)
        AliveTown.remove(Five)
        Town.remove(Five)
    if bot6Role == "Mafia":
        Maf.append(Six)
        otherMafs.append(Six)
        AliveMaf.append(Six)
        AliveTown.remove(Six)
        Town.remove(Six)
    if bot7Role == "Mafia":
        Maf.append(Seven)
        otherMafs.append(Seven)
        AliveMaf.append(Seven)
        AliveTown.remove(Seven)
        Town.remove(Seven)
    if PlayerRole == "Mafia":
        Maf.append(RealName)
        AliveMaf.append(RealName)
        AliveTown.remove(RealName)
        Town.remove(RealName)



    for player in playersAndTheirRoles:
        if playersAndTheirRoles[player] == "Plaguebearer":
            if player in AliveTown:
                AliveTown.remove(player)
            if player in Town:
                Town.remove(player)
            infected.append(player)
            plaguebearer = [player]


    



    Heirs = []

    if bot1Role == "Heir":
        Heirs.append(One)
    if bot2Role == "Heir":
        Heirs.append(Two)
    if bot3Role == "Heir":
        Heirs.append(Three)
    if bot4Role == "Heir":
        Heirs.append(Four)
    if bot5Role == "Heir":
        Heirs.append(Five)
    if bot6Role == "Heir":
        Heirs.append(Six)
    if bot7Role == "Heir":
        Heirs.append(Seven)
    if PlayerRole == "Heir":
        Heirs.append(RealName)


    
    if PlayerRole == "Mafia":
        otherMaf = tkinter.Label(deadWindow, text = str(otherMafs) + " are the other Mafias.")
        otherMaf.grid(row = r, column = c)
        r = r + 2

    root1.destroy()
    Days()

def start():
    global RealName, PlayerRole, Heirs
    global Alive, AliveMaf, AliveTown, didJailorKill, didMafKill, docHeal, selfHealedYet, deadWindow, OtherMaf, OtherMaf2, r, c, runners, running
    global One, Two, Three, Four, Five, Six, Seven, RealName, jester, Maf, Town, playersAndTheirRoles, townRoles, roles
    global bot1Role, bot2Role, bot3Role, bot4Role, bot5Role, bot6Role, bot7Role, deadWindow, game1, Heirs, reviving, plaguebearer, AliveRoles, infected, roles2


    names = ["Jester", "Shut up exe", "Deathless", "TotesNotMaf", "CrAzY", "Hippo", "Greenland", "Chicago", "notSK", "AbraKadabra", "smoothie", "smitty", "LukesFather",
             "pits", "Chemistry", "Gamethrower", "plasma", "lucrative", "iLy", "TownOfSalem", "Kandango", "Matoska", "Mitt", "Winner", "strick", "apple", "Cola", "Nike", "Obama", "zomBie",
             "OneHundred", "I", "Emx", "Loas", "Polar", "Udemy", "Mafy", "Opalas", "Charmander", "Knew Yorkk", "Barred", "Conor", "5 player", "Oofala", "Queen", "xylo", "S T Y L E", "Tookie", "Bubhead",
             "John Jacob", "Czu", "TheLetterP", "Alexa", "Tissue", "Massage", "Cake", "Faceball", "XC", "Points", "Chilled", "Fantastic", "Santa", "Outlet", "Tape", "Socker", "Lotion", "Armpit",
             "Place", "Rubik", "Head", "Dice", "TikTok", "Jessie", "Muscles", "Cardistry", "Pedicure", "Phones", "CD", "PARTY", "Tipsy", "Pop", "Tonight", "Stop", "DJ", "Fight", "Woah", "Vey", "Beer", "Here",
             "Dudes", "Swagger", "Curb", "PoPo", "VirtNet", "Built", "GotMe", "Hands", "Julius", "bLoW", "DNCE", "Key", "VIP", "Laugh", "Lead", "Please", "Jane Doe", "Ian", "Allen", "Dell", "Ember", "RandomHouse",
             "Art", "Control", "Coconut", "Charge", "Dunk", "Fire", "Time", "Tightrope", "Surrounded", "IDBM", "Madness", "Anyway", "Frey", "Bryson", "Eyeball", "Core", "Donut", "Mc", "Chopsticks", "Challenge", "Stone", "Gumball",
             "Perfect", "Atlas", "Antler", "Uncle", "Blinds", "Trophy", "Tracker", "Necromancer", "Case", "Cruel", "WalkLikeMe", "Frankie", "Nutella", "GaMeR", "YouTuber", "MrsMedi", "ClaraBarton",
             "Ttk", "Options", "ImJester", "ScuzeMe", "Pineapple", "Captain", "Ginger", "Alex", "FiveTwenty", "ExplodingCats", "Minds", "Ham", "Camera", "Mayo", "Georgia", "1f2u3n4", "Binder", "Plunder"]

    if game1 == False:
        deadWindow.destroy()

    Heirs = []
    infected = []

    reviving = False

    One = random.choice(names)
    names.remove(One)

    Two = random.choice(names)
    names.remove(Two)

    Three = random.choice(names)
    names.remove(Three)

    Four = random.choice(names)
    names.remove(Four)

    Five = random.choice(names)
    names.remove(Five)

    Six = random.choice(names)
    names.remove(Six)

    Seven = random.choice(names)



    roles = ['Jailor', "Cop", 'Jester', "Doc", "Doc", "Mafia", "Mafia", "Mafia"]
    townRoles = ['Jailor', "Cop", 'Jester', 'Doc', "Doc"]
    roles2 = []

    for role in roles:
        roles2.append(role)

    PlayerRole = random.choice(roles)

    roles.remove(PlayerRole)

    bot1Role = random.choice(roles)

    roles.remove(bot1Role)

    bot2Role = random.choice(roles)

    roles.remove(bot2Role)

    bot3Role = random.choice(roles)

    roles.remove(bot3Role)

    bot4Role = random.choice(roles)

    roles.remove(bot4Role)

    bot5Role = random.choice(roles)

    roles.remove(bot5Role)

    bot6Role = random.choice(roles)

    roles.remove(bot6Role)

    bot7Role = random.choice(roles)

    roles.remove(bot7Role)



    AliveRoles = [bot1Role, bot2Role, bot3Role, bot4Role, bot5Role, bot6Role, bot7Role, PlayerRole]


    didJailorKill = False
    docHeal = []
    didMafKill = False

    selfHealedYet = 0
    
    RealName = name.get()

    playersAndTheirRoles = {One: bot1Role, Two: bot2Role, Three: bot3Role, Four: bot4Role, Five: bot5Role, Six: bot6Role, Seven: bot7Role, RealName: PlayerRole}

    if RealName == '' or RealName == " " or len(RealName) > 14:
        RandomNames = ["Jonathin Corwin", "Cotton Mather", "Deodat Lawson", "Edward Bishop", "Ann Sears", "Sarah Wildes"]
        RealName = random.choice(RandomNames)


    running = {One: 0, Two: 0, Three: 0, Four: 0, Five: 0, Six: 0, Seven: 0, RealName: 0}
    runners = [One, Two, Three, Four, Five, Six, Seven, RealName]
    jester = []
    

    deadWindow = tkinter.Tk()
    deadWindow.title("Game Information")
    deadWindow.geometry("600x300+401+200")
    deadWindow.configure(background = "pink")

    mafOne = False

    for player in playersAndTheirRoles:
        if playersAndTheirRoles[player] == "Mafia" and mafOne == False:
            OtherMaf = player
            mafOne = True
        elif playersAndTheirRoles[player] == "Mafia" and mafOne == True:
            OtherMaf2 = player

        if playersAndTheirRoles[player] == "Jester":
            jester = [player]



    r = 0
    c = 0

    




    


    
    Alive = [RealName, One, Two, Three, Four, Five, Six, Seven]
    AliveTown = [One, Two, Three, Four, Five, Six, Seven, RealName]
    AliveMaf = []
    Maf = []
    Town = [One, Two, Three, Four, Five, Six, Seven, RealName]



    if bot1Role == "Mafia":
        Maf.append(One)
        AliveMaf.append(One)
        AliveTown.remove(One)
        Town.remove(One)
    if bot2Role == "Mafia":
        Maf.append(Two)
        AliveMaf.append(Two)
        AliveTown.remove(Two)
        Town.remove(Two)
    if bot3Role == "Mafia":
        Maf.append(Three)
        AliveMaf.append(Three)
        AliveTown.remove(Three)
        Town.remove(Three)
    if bot4Role == "Mafia":
        Maf.append(Four)
        AliveMaf.append(Four)
        AliveTown.remove(Four)
        Town.remove(Four)
    if bot5Role == 'Mafia':
        Maf.append(Five)
        AliveMaf.append(Five)
        AliveTown.remove(Five)
        Town.remove(Five)
    if bot6Role == "Mafia":
        Maf.append(Six)
        AliveMaf.append(Six)
        AliveTown.remove(Six)
        Town.remove(Six)
    if bot7Role == "Mafia":
        Maf.append(Seven)
        AliveMaf.append(Seven)
        AliveTown.remove(Seven)
        Town.remove(Seven)
    if PlayerRole == "Mafia":
        Maf.append(RealName)
        AliveMaf.append(RealName)
        AliveTown.remove(RealName)
        Town.remove(RealName)




    if PlayerRole == "Mafia":
        otherMafs = Maf
        otherMafia = ""
        for mafia in otherMafs:
            if mafia != RealName:
                otherMafia = otherMafia + mafia + ", "
                
        otherMafia = otherMafia + " are the other Mafias."
        otherMaf = tkinter.Label(deadWindow, text = otherMafia)
        otherMaf.grid(row = r, column = c)
        r = r + 2

    root1.destroy()
    Days()


root = tkinter.Tk()
root.configure(background = "cyan")
root.title("Town Of Salem")
root.resizable(width = False, height = False)
root.geometry("500x300+1001+200")


fileWins = open("tosWins.txt", "a+")


def readWins():
    global winContents, fileWins
    fileWins = open("tosWins.txt", "r")
    winContents = fileWins.read()

readWins()

if "True" not in winContents:
    fileWins = open("tosWins.txt", "w")
    fileWins.write("0")
    fileWins.write("\n \nTrue")

    fileWins = open("tosWins.txt", "r")
    winContents = fileWins.read()



wins = winContents.replace("\n \nTrue", "")
wins = int(wins)





fileWins.close()

file = open("tosCoins.txt", "a+")


def read():
    global contents, readFile
    readFile = open("tosCoins.txt", "r")
    contents = readFile.read()

read()

if "True" not in contents:
    readFile = open("tosCoins.txt", "w")
    readFile.write("0")
    readFile.write("\n \nTrue")

    readFile = open("tosCoins.txt", "r")
    contents = readFile.read()

contents = contents.replace("\n \nTrue", "")


money = int(contents)
coins = tkinter.Label(root, text = "Coins: " + str(money))
coins.place(x = 230, y = 0)

file.close()

winLabel = tkinter.Label(root, text = "Wins: " + str(wins))
winLabel.place(x = 230, y = 15)

description = tkinter.Label(root, text = "Town of Salem. The game of hidden identities and murder. \n\nEveryone gets a role.\n\nThe Mafia kills at night, the village decides the guilty the next day. \n\nMade by SanguineL. Based off of Town of Salem by BlankMediaGames.")
description.place(x = 15, y = 70)
description.configure(bg = "cyan", font = ("Helvetica", 11))

game1 = True
game = False

starting = tkinter.Button(root, text = "Start a game!", command = credit, width = 20)
starting.place(x = 180, y = 270)

customButton = tkinter.Button(root, text = "Make a custom game!", command = customGame, width = 20).place(x = 30, y = 270)

storeButton = tkinter.Button(root, text = "Store", command = store, width = 20).place(x = 310, y = 270)



rolesUnlockedWrite = open("rolesUnlocked.txt", "a+")

rolesUnlockedRead = open("rolesUnlocked.txt", "r")

rolesUnlocked = rolesUnlockedRead.read()



root.mainloop()



deadWindow.mainloop()










