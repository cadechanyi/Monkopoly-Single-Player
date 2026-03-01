from Labels import *
import time
import random
import sys

class game:
    def __init__(self, endgame, turn, playernumber, cycletrue, dice1list, dice2list, doubles, tradeto, openwindows):
        self.endgame = endgame
        self.turn = turn
        self.playernumber = playernumber
        self.cycletrue = cycletrue
        self.dice1list = dice1list
        self.dice2list = dice2list
        self.doubles = doubles
        self.tradeto = tradeto
        self.openwindows = openwindows

    def gui_diceroll(self, roll1, roll2):
        for dice in dice1lblist:
            dice.place_forget()
        for dice in dice2lblist:
            dice.place_forget()
        dice3lb.place(x=340, y=560)
        dice1lb2.place(x=380, y=560)
        gui.update()
        time.sleep(0.1)
        dice3lb.place_forget()
        dice1lb2.place_forget()
        dice6lb.place(x=340, y=560)
        dice2lb2.place(x=380, y=560)
        gui.update()
        time.sleep(0.1)
        dice6lb.place_forget()
        dice2lb2.place_forget()
        dice2lb.place(x=340, y=560)
        dice5lb2.place(x=380, y=560)
        gui.update()
        time.sleep(0.1)
        dice2lb.place_forget()
        dice5lb2.place_forget()

        dice1lb.place(x=340, y=560)
        dice6lb2.place(x=380, y=560)
        gui.update()
        time.sleep(0.1)
        dice1lb.place_forget()
        dice6lb2.place_forget()
        dice3lb.place(x=340, y=560)
        dice4lb2.place(x=380, y=560)
        gui.update()
        time.sleep(0.1)
        dice3lb.place_forget()
        dice4lb2.place_forget()
        dice5lb.place(x=340, y=560)
        dice6lb2.place(x=380, y=560)
        gui.update()
        time.sleep(0.1)
        dice5lb.place_forget()
        dice6lb2.place_forget()
        dice2lb.place(x=340, y=560)
        dice1lb2.place(x=380, y=560)
        gui.update()
        time.sleep(0.2)
        dice2lb.place_forget()
        dice1lb2.place_forget()
        dice1lb.place(x=340, y=560)
        dice3lb2.place(x=380, y=560)
        gui.update()
        time.sleep(0.2)
        dice1lb.place_forget()
        dice3lb2.place_forget()
        dice5lb.place(x=340, y=560)
        dice4lb2.place(x=380, y=560)
        gui.update()
        time.sleep(0.3)
        dice5lb.place_forget()
        dice4lb2.place_forget()
        dice2lb.place(x=340, y=560)
        dice6lb2.place(x=380, y=560)
        gui.update()
        time.sleep(0.3)
        dice2lb.place_forget()
        dice6lb2.place_forget()
        dice6lb.place(x=340, y=560)
        dice1lb2.place(x=380, y=560)
        gui.update()
        time.sleep(0.4)
        dice6lb.place_forget()
        dice1lb2.place_forget()
        try:
            dice1lblist[roll1-1].place(x=340, y=560)
            dice2lblist[roll2-1].place(x=380, y=560)
            gui.update()
            time.sleep(1.4)
        except:
            time.sleep(1.4)

    def colorset_check(self):
        if boardplaceslist[1].owner == boardplaceslist[3].owner and boardplaceslist[1].owner !='no':
            boardplaceslist[1].completeset = True
            boardplaceslist[3].completeset = True
        if boardplaceslist[6].owner == boardplaceslist[8].owner == boardplaceslist[9].owner and boardplaceslist[6].owner != 'no':
            boardplaceslist[6].completeset = True
            boardplaceslist[8].completeset = True
            boardplaceslist[9].completeset = True
        if boardplaceslist[11].owner == boardplaceslist[13].owner == boardplaceslist[14].owner and boardplaceslist[11].owner != 'no':
            boardplaceslist[11].completeset = True
            boardplaceslist[13].completeset = True
            boardplaceslist[14].completeset = True
        if boardplaceslist[16].owner == boardplaceslist[18].owner == boardplaceslist[19].owner and boardplaceslist[16].owner != 'no':
            boardplaceslist[16].completeset = True
            boardplaceslist[18].completeset = True
            boardplaceslist[19].completeset = True
        if boardplaceslist[21].owner == boardplaceslist[23].owner == boardplaceslist[24].owner and boardplaceslist[21].owner != 'no':
            boardplaceslist[21].completeset = True
            boardplaceslist[23].completeset = True
            boardplaceslist[24].completeset = True
        if boardplaceslist[26].owner == boardplaceslist[27].owner == boardplaceslist[29].owner and boardplaceslist[26].owner != 'no':
            boardplaceslist[26].completeset = True
            boardplaceslist[27].completeset = True
            boardplaceslist[29].completeset = True
        if boardplaceslist[31].owner == boardplaceslist[32].owner == boardplaceslist[34].owner and boardplaceslist[31].owner != 'no':
            boardplaceslist[31].completeset = True
            boardplaceslist[32].completeset = True
            boardplaceslist[34].completeset = True
        if boardplaceslist[37].owner == boardplaceslist[39].owner and boardplaceslist[37].owner != 'no':
            boardplaceslist[37].completeset = True
            boardplaceslist[39].completeset = True

    def line_check(self):
        for boardplace in boardplaceslist:
            if boardplace.owner != 'no':
                if boardplace.number < 10:
                    line_dictionary[boardplace.number].place(x=boardplace.cordx-12, y=boardplace.cordy-106)
                    line_dictionary[boardplace.number].config(bg=playerlist[boardplace.owner].color)
                    if boardplace.mortgaged == True:
                        mortgaged_line_dictionary[boardplace.number].place(x=boardplace.cordx-14, y=boardplace.cordy-35)
                    else:
                        mortgaged_line_dictionary[boardplace.number].place_forget()
                if 10 < boardplace.number < 20:
                    line_dictionary[boardplace.number].place(x=boardplace.cordx+110, y=boardplace.cordy-16)
                    line_dictionary[boardplace.number].config(bg=playerlist[boardplace.owner].color)
                    if boardplace.mortgaged == True:
                        mortgaged_line_dictionary[boardplace.number].place(x=boardplace.cordx, y=boardplace.cordy)
                    else:
                        mortgaged_line_dictionary[boardplace.number].place_forget()
                if 20 < boardplace.number < 30:
                    line_dictionary[boardplace.number].place(x=boardplace.cordx-19, y=boardplace.cordy+106)
                    line_dictionary[boardplace.number].config(bg=playerlist[boardplace.owner].color)
                    if boardplace.mortgaged == True:
                        mortgaged_line_dictionary[boardplace.number].place(x=boardplace.cordx-21, y=boardplace.cordy+40)
                    else:
                        mortgaged_line_dictionary[boardplace.number].place_forget()
                if boardplace.number > 30:
                    line_dictionary[boardplace.number].place(x=boardplace.cordx-94, y=boardplace.cordy-19)
                    line_dictionary[boardplace.number].config(bg=playerlist[boardplace.owner].color)
                    if boardplace.mortgaged == True:
                        mortgaged_line_dictionary[boardplace.number].place(x=boardplace.cordx-94, y=boardplace.cordy-59)
                    else:
                        mortgaged_line_dictionary[boardplace.number].place_forget()

    def pieceshift(self, piecenumber):
        counter = -1
        for player in playerlist:
            counter += 1
            if player.board_number == playerlist[piecenumber].old_board_number and player.number != piecenumber: ##OR it equals current board_nuber
                #print(playerlist[piecenumber].place_x, playerlist[piecenumber].place_y, playerlist[piecenumber].number)
                if playerlist[piecenumber].old_board_number <= 10:
                    playerlist[piecenumber].place_y = player.place_y - 30
                if 20 >= playerlist[piecenumber].old_board_number > 10:
                    playerlist[piecenumber].place_x = player.place_x + 30
                if 30 >= playerlist[piecenumber].old_board_number > 20:
                    playerlist[piecenumber].place_y = player.place_y + 30
                if playerlist[piecenumber].old_board_number > 30:
                    playerlist[piecenumber].place_x = player.place_x - 30
                #print(playerlist[piecenumber].place_x, playerlist[piecenumber].place_y, 'change', playerlist[piecenumber].number)
                playerlist[piecenumber].label.place(x=playerlist[piecenumber].place_x, y=playerlist[piecenumber].place_y)
                gui.update()



    def ai_cycle(self):
        rollbut['state'] = DISABLED
        managepropbutton['state'] = DISABLED
        tradebutton['state'] = DISABLED
        endturnbutton['state'] = DISABLED
        endgamebutton['state'] = DISABLED
        close_manage_window()
        playerlist[self.turn].rollfunc()

    def next_turn_check(self):
        #print(self.turn, 'turn')
        if self.turn != 0 and self.turn != 1 or self.turn == 1 and gameboard.doubles == True:
            self.ai_cycle()
        elif self.turn == 0:
            rollbut['state'] = NORMAL
            managepropbutton['state'] = NORMAL
            tradebutton['state'] = NORMAL
            endgamebutton['state'] = NORMAL
        elif self.turn == 1 and gameboard.doubles == False:
            managepropbutton['state'] = NORMAL
            tradebutton['state'] = NORMAL
            endturnbutton['state'] = NORMAL
            endgamebutton['state'] = NORMAL




gameboard = game(False, 0, 4, False, dice1lblist, dice2lblist, False, 0, 2)

class boardplaces:
    def __init__(self, number, cordx, cordy, propertyname, propertytype, subpropertytype, label, tradelb, cost, owner, rent0, rent1, rent2, rent3, rent4, rent5, housecost, housenumber, colorset, completeset, smallerlabel, mortgaged):
        self.number = number
        self.cordx = cordx
        self.cordy = cordy
        self.propertyname = propertyname
        self.propertytype = propertytype
        self.subpropertytype = subpropertytype
        self.label = label
        self.tradelb = tradelb
        self.cost = cost
        self.owner = owner
        self.rent0 = rent0
        self.rent1 = rent1
        self.rent2 = rent2
        self.rent3 = rent3
        self.rent4 = rent4
        self.rent5 = rent5
        self.housecost = housecost
        self.housenumber = housenumber
        self.colorset = colorset
        self.completeset = completeset
        self.smallerlabel = smallerlabel
        self.mortgaged = mortgaged

    def mortgage_property(self):
        if self.mortgaged == False:
            self.mortgaged = True
            playerlist[self.owner].money += int(self.cost / 2)
            playerlist[self.owner].money_label.config(text=playerlist[self.owner].money)

        elif self.mortgaged == True:
            self.mortgaged = False
            playerlist[self.owner].money -= int(self.cost / 2 * 1.1)
            playerlist[self.owner].money_label.config(text=playerlist[self.owner].money)
        gameboard.line_check()
        gui.update()


#class of board places which number two coordinates, property name, type, and the label image that pops up

boardplaceslist = [boardplaces(0, 640, 715, 'GO', 'go', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 0, 'no', False, 'no', False),
                   boardplaces(1, 588, 715, 'Caledon', 'property', 'property', caledonimg, caledontradelb, 60, 'no', 2, 10, 30, 90, 160, 250, 50, 0, 1, False, caledonsmalllb, False),
                   boardplaces(2, 528, 715, 'Baboon Bin', 'chest', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 0, 'no', False, 'no', False),
                   boardplaces(3, 474, 715, 'Milton','property', 'property', miltonimg, miltontradelb, 60, 'no', 4, 20, 60, 180, 320, 450, 50, 0, 1, False, miltonsmalllb, False),
                   boardplaces(4, 416, 715, 'Mentor School Fees 200', 'tax', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 0, 'no', False, 'no', False),
                   boardplaces(5, 358, 715, 'Wayne Bus', 'property', 'bus', waynebusimg, waynebustradelb, 200, 'no', 25, 50, 100, 200, 'no', 'no', 'no', 0, 10, False, waynebussmalllb, False),
                   boardplaces(6, 301, 715, 'Angola', 'property', 'property', angolaimg, angolatradelb, 100, 'no', 6, 30, 90, 270, 400, 550, 50, 0, 2, False, angolasmalllb, False),
                   boardplaces(7, 248, 715, 'Healthcare Hazard', 'chest', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 0, 'no', False, 'no', False),
                   boardplaces(8, 186, 715, 'Somalia', 'property', 'property', somaliaimg, somaliatradelb, 100, 'no', 6, 30, 90, 270, 400, 550, 50, 0, 2, False, somaliasmalllb, False), #to demonstrate the new debt function changed base rent to 1600
                   boardplaces(9, 129, 715, 'Chad', 'property', 'property', chadimg, chadtradelb, 120, 'no', 8, 40, 100, 300, 450, 600, 50, 0, 2, False, chadsmalllb, False),
                   boardplaces(10, 5, 715, 'Jail', 'jail', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 0, 'no', False, 'no', False),
                   boardplaces(11, 5, 590, 'Scarborough', 'property', 'property', scarboroughimg, scarboroughtradelb, 140, 'no', 10, 50, 150, 450, 625, 750, 100, 0, 3, False, scarboroughsmalllb, False),
                   boardplaces(12, 5, 532, 'Pepsi Company', 'property', 'company', pepsicompanyimg, pepsicompanytradelb, 150, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 0, 9, False, pepsicompanysmalllb, False),
                   boardplaces(13, 5, 475, 'Markham', 'property', 'property', markhamimg, markhamtradelb, 140, 'no', 10, 50, 150, 450, 625, 750, 100, 0, 3, False, markhamsmalllb, False),
                   boardplaces(14, 5, 417, 'Primary Campus', 'property', 'property', primarycampusimg, primarycampustradelb, 160, 'no', 12, 60, 180, 500, 700, 900, 100, 0, 3, False, primarycampussmalllb, False),
                   boardplaces(15, 5, 359, 'Jeff Bus', 'property', 'bus', jeffbusimg, jeffbustradelb, 200, 'no', 25, 50, 100, 200, 'no', 'no', 'no', 0, 10, False, jeffbussmalllb, False),
                   boardplaces(16, 5, 302, 'GCP', 'property', 'property', gcpimg, gcptradelb, 180, 'no', 14, 70, 200, 550, 750, 950, 100, 0, 4, False, gcpsmalllb, False),
                   boardplaces(17, 5, 246, 'Baboon Bin', 'chest', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 0, 'no', False, 'no', False),
                   boardplaces(18, 5, 186, 'Mentor Lobby', 'property', 'property', mentorlobbyimg, mentorlobbytradelb, 180, 'no', 14, 70, 200, 550, 750, 950, 100, 0, 4, False, mentorlobbysmalllb, False),
                   boardplaces(19, 5, 129, 'Bhav Barn', 'property', 'property', bhavbarnimg, bhavbarntradelb, 200, 'no', 16, 80, 220, 600, 800, 1000, 100, 0, 4, False, bhavbarnsmalllb, False),
                   boardplaces(20, 5, 5, 'Lunch Break', 'lunch', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 0, 'no', False, 'no', False),
                   boardplaces(21, 136, 5, 'Mentor Gym', 'property', 'property', mentorgymimg, mentorgymtradelb, 220, 'no', 18, 90, 250, 700, 875, 1050, 150, 0, 5, False, mentorgymsmalllb, False),
                   boardplaces(22, 192, 5, 'Healthcare hazard', 'chest', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 0, 'no', False, 'no', False),
                   boardplaces(23, 250, 5, 'North Korea', 'property', 'property', northkoreaimg, northkoreatradelb, 220, 'no', 18, 90, 250, 700, 875, 1050, 150, 0, 5, False, northkoreasmalllb, False),
                   boardplaces(24, 308, 5 ,'mentor office', 'property', 'property', mentorofficeimg, mentorofficetradelb, 240, 'no', 20, 100, 300, 750, 925, 1100, 150, 0, 5, False, mentorofficesmalllb, False),
                   boardplaces(25, 365, 5, 'Smith Bus', 'property', 'bus', smithbusimg, smithbustradelb, 200, 'no', 25, 50, 100, 200, 'no', 'no', 'no', 0, 10, False, smithbussmalllb, False),
                   boardplaces(26, 423, 5, 'Yehia Pyramid', 'property', 'property', yehiapyramidimg, yehiapyramidtradelb, 260, 'no', 22, 110, 330, 800, 975, 1150, 150, 0, 6, False, yehiapyramidsmalllb, False),
                   boardplaces(27, 481, 5, 'Egypt', 'property', 'property', egyptimg, egypttradelb, 260, 'no', 22, 110, 330, 800, 975, 1150, 150, 0, 6, False, egyptsmalllb, False),
                   boardplaces(28, 538, 5, 'Coca Cola Company', 'property', 'company', cokecompanyimg, cokecompanytradelb, 150, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 0, 9, False, cokecompanysmalllb, False),
                   boardplaces(29, 595, 5, 'Land Down Under', 'property', 'property', landdownunderimg, landdownundertradelb, 280, 'no', 24, 120, 360, 850, 1025, 1200, 150, 0, 6, False, landdownundersmalllb, False),
                   boardplaces(30, 710, 5, 'Go To Brampton', 'gotojail', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 0, 'no', False, 'no', False),
                   boardplaces(31, 710, 132, 'Evan Camp', 'property', 'property', evancampimg, evancamptradelb, 300, 'no', 26, 130, 390, 900, 1100, 1275, 200, 0, 7, False, evancampsmalllb, False),
                   boardplaces(32, 710, 189, 'Greenland Park', 'property', 'property', greenwoodimg, greenwoodtradelb, 300, 'no', 26, 130, 390, 900, 1100, 1275, 200, 0, 7, False, greenwoodsmalllb, False),
                   boardplaces(33, 710, 246, 'Baboon Bin', 'chest', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 0, 'no', False, 'no', False),
                   boardplaces(34, 710, 304, 'Oakville', 'property', 'property', oakvilleimg, oakvilletradelb, 320, 'no', 28, 150, 450, 1000, 1200, 1400, 200, 0, 7, False, oakvillesmalllb, False),
                   boardplaces(35, 710, 362, 'Dan Bus', 'property', 'bus', danbusimg, danbustradelb, 200, 'no', 25, 50, 100, 200, 'no', 'no', 'no', 0, 10, False, danbussmalllb, False),
                   boardplaces(36, 710, 422, 'Healthcare hazard', 'chest', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 0, 'no', False, 'no', False),
                   boardplaces(37, 710, 478, 'Crystal Cove', 'property', 'property', crystalcoveimg, crystalcovetradelb, 350, 'no', 35, 175, 500, 1100, 1300, 1500, 200, 0, 8, False, crystalcovesmalllb, False),
                   boardplaces(38, 710, 534, 'field trip 100', 'tax', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 0, 'no', False, 'no', False),
                   boardplaces(39, 710, 593, 'jungle of the monkeys', 'property', 'property', jungleofmonkeysimg, jungleofmonkeystradelb, 400, 'no', 50, 200, 600, 1400, 1700, 2000, 200, 0, 8, False, jungleofmonkeyssmalllb, False)]
#list of all boardplaces with there numbers coordinates, name, etc.
class chest:
    def __init__(self, lbtext, movecom, moneycom):
        self.lbtext = lbtext
        self.movecom = movecom
        self.moneycom = moneycom

    def chest_command(self, piecenumber):
        playerlist[piecenumber].money += self.moneycom
        playerlist[piecenumber].money_label.config(text=playerlist[piecenumber].money)
        gui.update()
        if self.movecom is not False:
            if self.movecom < playerlist[piecenumber].board_number and self.movecom != 30:
                playerlist[piecenumber].money += 200
                playerlist[piecenumber].money_label.config(text=playerlist[piecenumber].money)
            playerlist[piecenumber].board_number = self.movecom
            playerlist[piecenumber].old_board_number = self.movecom ##NOTE may change with some cards or affects other aspects
            playerlist[piecenumber].place_x = boardplaceslist[self.movecom].cordx
            playerlist[piecenumber].place_y = boardplaceslist[self.movecom].cordy
            playerlist[piecenumber].label.place(x=playerlist[piecenumber].place_x, y=playerlist[piecenumber].place_y)
            gameboard.pieceshift(piecenumber)
            gui.update()
            #playerlist[gameboard.turn].rollfunc()
            playerlist[piecenumber].identify_property()
        else:
            gameboard.next_turn_check()


#class chest has values for all chest cards

chestlist = [chest('You were late coming in from lunch\n go to the office', 24, -0),
             chest('You went to Brampton and were shot\n and mugged a $100. You were then taken\n to a hospital and were charged $200\n for treatment, then sent back to Brampton', 30, -300),
             chest('Advance to Smith class to get double the normal cokes', 0, -0),
             chest('Monkey fees, lose 50 cokes', False, -50),
             chest('Brayden needs your muck\n lose 25 cokes', False, -25),
             chest('You hate yourself\n go to Scarborough', 11, -0),
             chest('You decided you were tired of cokes\n go to the Pepsi company', 12, -0),
             chest('You completed an assignment on time\n receive 50 cokes', False, +50),
             chest('Bhavjeet wants you to be his Hartag\n he gave you 200 cokes for it', False, +200),
             chest('Smith deemed you king of the monkeys\n Receive 100 cokes', False, +100),
             chest('Take a trip on Bus Wayne', 5, -0),
             chest('You a ugly ah monkey and won\n second last in a beauty contest\n collect 10 cokes', False, +10),
             chest('Some monkey robbed a class\n and dropped the cokes\n collect 150 cokes', False, +150),
             chest('You brought your coke into class\n and Mcrae took it\n lose 100 cokes', False, -100)]

class player:
    def __init__(self, playable, number, color, color2, color3, label, money, money_label, board_number, old_board_number, place_x, place_y, previous_roll, company_number, bus_number, trade_property_counter, worth_dict):
        self.playable = playable
        self.number = number
        self.color = color
        self.color2 = color2
        self.color3 = color3
        self.label = label
        self.money = money
        self.money_label = money_label
        self.board_number = board_number
        self.old_board_number = old_board_number
        self.place_x = place_x
        self.place_y = place_y
        self.previous_roll = previous_roll
        self.company_number = company_number
        self.bus_number = bus_number
        self.trade_property_counter = trade_property_counter
        self.worth_dict = worth_dict

    def set_property_worth(self):
        for item in self.worth_dict:
            owned_in_set = 0
            for property in boardplaceslist:
                if property.colorset == boardplaceslist[item].colorset:
                    if property.owner == self.number and property.owner != 'no':
                        owned_in_set += 1
                        if property.number in [1, 3, 37, 39]:
                            owned_in_set *= 2
            if item not in [5, 15, 25, 35]:
                self.worth_dict[item] = ((boardplaceslist[item].cost/10)*((2**owned_in_set)**owned_in_set))
            else:
                self.worth_dict[item] = ((boardplaceslist[item].cost/10)*(2**owned_in_set))
        #print(self.worth_dict, self.number)

    def ai_property_buy_check(self, property_number):
        buy_value = self.worth_dict[property_number] * (self.money - boardplaceslist[property_number].cost)
        #print(self.worth_dict[property_number])
        if buy_value >= 2200:
            return True
        else:
            return False

    def ai_trade_check(self, tradelist, trade_to, trade_from):
        trade_from_list = []
        trade_to_list = []
        worth_from = 0
        worth_to = 0
        for item in tradelist:
            if type(item) == str:
                if item[0] == str(trade_from):
                    money_item = int(item[1:5])
                    money_item = money_item * 5 // ((max(playerlist[trade_to].money, 100)**0.5)**0.5)
                    worth_from += money_item
                elif item[0] == str(trade_to):
                    money_item = int(item[1:5])
                    money_item = money_item * 5 // ((min(playerlist[trade_to].money, 100)**0.5)**0.5)
                    worth_to += money_item
            else:
                if item.owner == trade_from:
                    trade_from_list.append(item)
                elif item.owner == trade_to:
                    trade_to_list.append(item)

        for trade_from_property in trade_from_list:
            owned_in_set = 0
            worth_from += (trade_from_property.cost / 2)
            for property in boardplaceslist:
                if property.colorset == trade_from_property.colorset:
                    if property.owner == trade_to and property.number != trade_from_property.number:
                        owned_in_set += 1
                        if property.number in [1, 3, 37, 39]:
                            owned_in_set *= 2
            for second_property in trade_from_list:
                if second_property.colorset == trade_from_property.colorset and second_property.number != trade_from_property.number:
                    owned_in_set += 1
                    if second_property.number in [1, 3, 37, 39]:
                        owned_in_set *= 2

            if trade_from_property.owner not in [5, 15, 25, 35]:
                worth_from += 1 * ((trade_from_property.cost/10)*((2**owned_in_set)**owned_in_set))
            else:
                worth_from += 1 * ((trade_from_property.cost/10)*(2**owned_in_set))

        for trade_to_property in trade_to_list:
            owned_in_set = 0
            worth_to += (trade_to_property.cost / 2)
            for property in boardplaceslist:
                if property.colorset == trade_to_property.colorset:
                    if property.owner == trade_from and property.number != trade_to_property.number:
                        owned_in_set += 1
                        if property.number in [1, 3, 37, 39]:
                            owned_in_set *= 2

            for second_property in trade_to_list:
                if second_property.colorset == trade_to_property.colorset and second_property.number != trade_to_property.number:
                    owned_in_set += 1
                    if second_property.number in [1, 3, 37, 39]:
                        owned_in_set *= 2

            if trade_to_property.owner not in [5, 15, 25, 35]:
                worth_to += 1 * ((trade_to_property.cost/10)*((2**owned_in_set)**owned_in_set))
            else:
                worth_to += 1 * ((trade_to_property.cost/10)*(2**owned_in_set))

        #print(worth_from, 'worthfrom')
        #print(worth_to, 'worthto')
        if worth_from >= worth_to:
            return True
        else:
            return False

    def ai_internal_trade(self):
        complete_owned_sets = []
        for set in range(1, 9):
            complete_sets = []
            owner_list = []
            counter = 0
            ai_included = False
            for boardplace in boardplaceslist:
                if boardplace.colorset == set and boardplace.owner != 'no':
                    counter += 1
                    if boardplace.owner == self.number:
                        ai_included = True
                    else:
                        if boardplace.owner not in owner_list:
                            owner_list.append(boardplace.owner)
            if set == 1 or set == 8:
                if counter == 2 and ai_included == True:
                    complete_owned_sets.append(set)
            else:
                if counter == 3 and ai_included == True and len(owner_list) == 1:
                    complete_owned_sets.append(set)
        ##Note add for after trade with player
        for player in playerlist:
            sets_to_switch = [
                boardplace.colorset for boardplace in boardplaceslist if boardplace.colorset in complete_owned_sets and boardplace.owner == player.number and boardplace.owner != self.number and boardplace.owner != 0
            ]
            if len(sets_to_switch) >= 2:
                #sets_to_switch = list(islice(sets_to_switch, 2))
                self_set_1_value = 0
                opponent_set_1_value = 0
                for boardplace in boardplaceslist:
                    if boardplace.colorset == sets_to_switch[0]:
                        if boardplace.owner == self:
                            self_set_1_value += boardplace.cost
                        elif boardplace.owner == player:
                            opponent_set_1_value += boardplace.cost
                if self_set_1_value >= opponent_set_1_value:
                    pass





    def identify_property(self):
        if self.board_number == 0:
            self.money += 200
            self.money_label.config(text=self.money)
            cashlb.config(text='+$400', fg='green') #when landing directly will result in 400, but chance will be 200
            gui.update()
            time.sleep(1)
            gameboard.next_turn_check()

        elif self.board_number == 4:
            self.money -= 200
            self.money_label.config(text=self.money)
            cashlb.config(text='-$200', fg='red')
            gui.update()
            time.sleep(1)
            gameboard.next_turn_check()

        elif self.board_number == 38:
            self.money -= 100
            self.money_label.config(text=self.money)
            cashlb.config(text='-$100', fg='red')
            gui.update()
            time.sleep(1)
            gameboard.next_turn_check()

        elif self.board_number == 30:
            time.sleep(0.2)
            self.board_number = 10
            self.place_x = 48
            self.place_y = 668 #NOTE second player in brampton will be moved outside ##Also player don't stay in Brampton they can leave thankfully
            self.label.place(x=self.place_x, y=self.place_y)
            doubleslb.config(text='GO TO BRAMPTON!', fg='red')
            gui.update()
            time.sleep(1)
            gameboard.next_turn_check()

        elif self.board_number == 2 or self.board_number == 17 or self.board_number == 33:
            chest_card_number = random.randint(0,12)
            piecenumber = self.number
            def chestbuttondestroy():
                chestbutton.destroy()
            chestbutton = Button(gui, bg = 'brown', highlightbackground='brown', text=chestlist[chest_card_number].lbtext, height=12, width=30, command=lambda piecenumber = piecenumber: [chestbuttondestroy(), chestlist[chest_card_number].chest_command(piecenumber=piecenumber)])##chestlist[chest_card_number].chest_command(chest_card_number))
            chestbutton.place(x=300, y=270)
        elif self.board_number == 7 or self.board_number == 22 or self.board_number == 36:
            chest_card_number = random.randint(0,12)
            #chest_card_number = 1
            piecenumber = self.number
            def chestbuttondestroy():
                chestbutton.destroy()
            chestbutton = Button(gui, bg = 'yellow', highlightbackground='yellow', text=chestlist[chest_card_number].lbtext, height=12, width=30, command=lambda piecenumber = piecenumber: [chestbuttondestroy(), chestlist[chest_card_number].chest_command(piecenumber=piecenumber)])##chestlist[chest_card_number].chest_command(chest_card_number))
            chestbutton.place(x=300, y=270)

        elif self.board_number == 1 or self.board_number == 3 or self.board_number == 5 or self.board_number == 6 or self.board_number == 8 or self.board_number == 9 or self.board_number == 11 or self.board_number == 12 or self.board_number == 13 or self.board_number == 14 or self.board_number == 15 or self.board_number == 16 or self.board_number == 18 or self.board_number == 19 or self.board_number == 21 or self.board_number == 23 or self.board_number == 24 or self.board_number == 25 or self.board_number == 26 or self.board_number == 27 or self.board_number == 28 or self.board_number == 29 or self.board_number == 31 or self.board_number == 32 or self.board_number == 34 or self.board_number == 35 or self.board_number == 37 or self.board_number == 39:
            if boardplaceslist[self.board_number].owner == 'no':
                if self.number == 0:
                    def buyfunc():
                        boardplaceslist[self.board_number].owner = self.number
                        self.money -= boardplaceslist[self.board_number].cost
                        self.money_label.config(text=self.money)
                        gui.update()

                        if self.board_number == 12 or self.board_number == 28:
                            self.company_number += 1
                        if self.board_number == 5 or self.board_number == 15 or self.board_number == 25 or self.board_number == 35:
                            self.bus_number += 1

                        gameboard.line_check()
                        gameboard.colorset_check()
                        buy_property_gui.destroy()
                        for player in playerlist:
                            player.set_property_worth()
                        gameboard.next_turn_check()

                    def passfunc():
                        buy_property_gui.destroy()
                        gameboard.next_turn_check()

                    buy_property_gui = tk.Toplevel()
                    buy_property_gui.geometry('820x608')
                    buy_property_gui.wm_protocol("WM_DELETE_WINDOW", noclose)
                    buy_property_gui.resizable(False, False)
                    costlb = Label(buy_property_gui, text='$'+str(boardplaceslist[self.board_number].cost), height =1, width=10, font=('Cooper Std Black', 48))
                    costlb.place(x=508, y =1)
                    propertylb = tk.Label(buy_property_gui, image=boardplaceslist[self.board_number].label)
                    propertylb.place(x=1, y=1)
                    buybutton = Button(buy_property_gui, text='buy', bg='green', highlightbackground='green',height=10, width=26, command=buyfunc)
                    buybutton.place(x=528, y=74)
                    passbutton = Button(buy_property_gui, text='pass', bg='red', highlightbackground='red',height=10, width=26, command=passfunc)
                    passbutton.place(x=528, y=304)
                else:
                    buy_decision = self.ai_property_buy_check(self.board_number)
                    if buy_decision == True:
                        boardplaceslist[self.board_number].owner = self.number
                        self.money -= boardplaceslist[self.board_number].cost
                        self.money_label.config(text=self.money)
                        gui.update()

                        if self.board_number == 12 or self.board_number == 28:
                            self.company_number += 1
                        if self.board_number == 5 or self.board_number == 15 or self.board_number == 25 or self.board_number == 35:
                            self.bus_number += 1

                        gameboard.line_check()
                        gameboard.colorset_check()
                        for player in playerlist:
                            player.set_property_worth()
                        self.ai_internal_trade()
                        gameboard.next_turn_check()
                    else:
                        gameboard.next_turn_check()

            else:
                if boardplaceslist[self.board_number].mortgaged == False and boardplaceslist[self.board_number].owner != self.number:
                    if self.board_number == 12 or self.board_number == 28:
                        if boardplaceslist[12].owner == boardplaceslist[28].owner:
                            company_rent = self.previous_roll * 10
                        else:
                            company_rent = self.previous_roll * 5
                        self.money -= company_rent
                        self.money_label.config(text=self.money)
                        playerlist[boardplaceslist[self.board_number].owner].money += company_rent
                        playerlist[boardplaceslist[self.board_number].owner].money_label.config(text=playerlist[boardplaceslist[self.board_number].owner].money)
                        gui.update()
                    elif self.board_number == 5 or self.board_number == 15 or self.board_number == 25 or self.board_number == 35:
                        bus_rent = 12.5
                        for boardplace in boardplaceslist:
                            if boardplace.subpropertytype == 'bus' and boardplace.owner == boardplaceslist[self.board_number].owner:
                                bus_rent *= 2
                        bus_rent = int(bus_rent)

                        self.money -= bus_rent
                        self.money_label.config(text=self.money)
                        playerlist[boardplaceslist[self.board_number].owner].money += bus_rent
                        playerlist[boardplaceslist[self.board_number].owner].money_label.config(text=playerlist[boardplaceslist[self.board_number].owner].money)
                        gui.update()
                    elif self.board_number in [1, 3, 6, 8, 9, 11, 13, 14, 16, 18, 19, 21, 23, 24, 26, 27, 29, 31, 32, 34, 37, 39]:
                        if boardplaceslist[self.board_number].housenumber == 0:
                            property_rent = boardplaceslist[self.board_number].rent0
                        elif boardplaceslist[self.board_number].housenumber == 1:
                            property_rent = boardplaceslist[self.board_number].rent1
                        elif boardplaceslist[self.board_number].housenumber == 2:
                            property_rent = boardplaceslist[self.board_number].rent2
                        elif boardplaceslist[self.board_number].housenumber == 3:
                            property_rent = boardplaceslist[self.board_number].rent3
                        elif boardplaceslist[self.board_number].housenumber == 4:
                            property_rent = boardplaceslist[self.board_number].rent4
                        elif boardplaceslist[self.board_number].housenumber == 5:
                            property_rent = boardplaceslist[self.board_number].rent5
                        else:
                            property_rent = 0
                        self.money -= property_rent
                        self.money_label.config(text=self.money)
                        playerlist[boardplaceslist[self.board_number].owner].money += property_rent
                        playerlist[boardplaceslist[self.board_number].owner].money_label.config(text=playerlist[boardplaceslist[self.board_number].owner].money)
                        gui.update()

                gameboard.next_turn_check()


        else:
            gameboard.next_turn_check()

        self.money_label.config(text=self.money) ##NOTE: check if still need at end
        self.label.place(x=self.place_x, y=self.place_y)
        gui.update()

    def manage_property(self):
        if gameboard.openwindows < 3:
            gameboard.openwindows = 3
            gameboard.colorset_check()
            managegui.deiconify()
            counter = 0

            def mortgage_button_text_change(button, theboardplace):
                if theboardplace.mortgaged == False:
                    button.config(text='Unmortgage')
                elif theboardplace.mortgaged == True:
                    button.config(text='Mortgage')

            def add_house(theboardplace, button):
                if theboardplace.housenumber < 5 and theboardplace.mortgaged == False and self.money >= theboardplace.housecost:
                    for boardplace in boardplaceslist:
                        if boardplace.colorset == theboardplace.colorset:
                            if theboardplace.housenumber == boardplace.housenumber + 1:
                                return False

                    if theboardplace.housenumber != 0:
                        houses_dictionary[theboardplace.number][theboardplace.housenumber-1].place_forget()

                    theboardplace.housenumber += 1
                    if theboardplace.number < 10:
                        houses_dictionary[theboardplace.number][theboardplace.housenumber-1].place(x=theboardplace.cordx + 92, y=theboardplace.cordy - 80)
                        playerlist[theboardplace.owner].money -= 50
                        playerlist[theboardplace.owner].money_label.config(text=playerlist[theboardplace.owner].money)
                    elif 10 < theboardplace.number < 20:
                        houses_dictionary[theboardplace.number][theboardplace.housenumber-1].place(x=theboardplace.cordx + 194, y=theboardplace.cordy - 12)
                        playerlist[theboardplace.owner].money -= 100
                        playerlist[theboardplace.owner].money_label.config(text=playerlist[theboardplace.owner].money)
                    elif 20 < theboardplace.number < 30:
                        houses_dictionary[theboardplace.number][theboardplace.housenumber-1].place(x=theboardplace.cordx + 85, y=theboardplace.cordy + 90)
                        playerlist[theboardplace.owner].money -= 150
                        playerlist[theboardplace.owner].money_label.config(text=playerlist[theboardplace.owner].money)
                    elif 30 < theboardplace.number < 40:
                        houses_dictionary[theboardplace.number][theboardplace.housenumber-1].place(x=theboardplace.cordx + 28, y=theboardplace.cordy - 15)
                        playerlist[theboardplace.owner].money -= 200
                        playerlist[theboardplace.owner].money_label.config(text=playerlist[theboardplace.owner].money)
                    button['state'] = DISABLED

            def minus_house(theboardplace, button):
                if theboardplace.housenumber > 0 and theboardplace.mortgaged == False:
                    for boardplace in boardplaceslist:
                        if boardplace.colorset == theboardplace.colorset:
                            if theboardplace.housenumber == boardplace.housenumber - 1:
                                return False

                    if theboardplace.housenumber != 0:
                        houses_dictionary[theboardplace.number][theboardplace.housenumber-1].place_forget()
                    playerlist[theboardplace.owner].money += int(theboardplace.housecost / 2)
                    playerlist[theboardplace.owner].money_label.config(text=playerlist[theboardplace.owner].money)

                    theboardplace.housenumber -= 1
                    if theboardplace.housenumber > 0:
                        if theboardplace.number < 10:
                            houses_dictionary[theboardplace.number][theboardplace.housenumber-1].place(x=theboardplace.cordx + 92, y=theboardplace.cordy - 80)
                        elif 10 < theboardplace.number < 20:
                            houses_dictionary[theboardplace.number][theboardplace.housenumber-1].place(x=theboardplace.cordx + 194, y=theboardplace.cordy - 12)
                        elif 20 < theboardplace.number < 30:
                            houses_dictionary[theboardplace.number][theboardplace.housenumber-1].place(x=theboardplace.cordx + 85, y=theboardplace.cordy + 90)
                        elif 30 < theboardplace.number < 40:
                            houses_dictionary[theboardplace.number][theboardplace.housenumber-1].place(x=theboardplace.cordx + 28, y=theboardplace.cordy - 15)
                if theboardplace.housenumber == 0:
                    button['state'] = NORMAL



            for boardplace in boardplaceslist:
                if boardplace.owner == self.number:
                    counter += 1
                    boardplace.smallerlabel.place(x=smalllbcord_dictionary[counter][0], y=smalllbcord_dictionary[counter][1])
                    mortgage_button = Button(managegui, height=1, width=7, text='Mortgage')
                    if boardplace.mortgaged == True:
                        mortgage_button.config(text='Unmortgage')
                    mortgage_button.config(command=lambda b=mortgage_button, place=boardplace: [mortgage_button_text_change(button=b, theboardplace=place), place.mortgage_property()])
                    mortgage_button.place(x=smalllbcord_dictionary[counter][2], y=smalllbcord_dictionary[counter][3])
                    if boardplace.subpropertytype == 'property':
                        minus_house_button = Button(managegui, height=1, width=3, text='-House')
                        minus_house_button.config(command=lambda b=mortgage_button, place=boardplace: minus_house(theboardplace=place, button=b))
                        minus_house_button.place(x=smalllbcord_dictionary[counter][4], y=smalllbcord_dictionary[counter][6])
                        plus_house_button = Button(managegui, height=1, width=3, text='+House')
                        plus_house_button.config(command=lambda b=mortgage_button, place=boardplace: add_house(theboardplace=place, button=b))
                        plus_house_button.place(x=smalllbcord_dictionary[counter][5], y=smalllbcord_dictionary[counter][6])
                        if boardplace.completeset == False:
                            minus_house_button['state'] = DISABLED
                            plus_house_button['state'] = DISABLED
                        if boardplace.housenumber != 0:
                            mortgage_button['state'] = DISABLED

    def trade(self): ##Add limit for properties traded
        if gameboard.openwindows < 3:
            gameboard.openwindows = 3
            trade_gui.deiconify()
            tradefromlb.place(x=540, y=171)
            tradetolb.place(x=542, y=208)
            explanation_label.place(x=0, y=440)
            explanation_label2.place(x=0, y=460)
            tradeline.place(x=0, y=191)

            def complete_trade(tradelist: list, trade_to: int):
                valid_trade = self.ai_trade_check(tradelist, trade_to, trade_from=0)
                if valid_trade == True:
                    for item in tradelist:
                        if type(item) == str:
                            if item[0] == '0':
                                try:
                                    playerlist[0].money -= int(item[1:5])
                                    playerlist[0].money_label.config(text=playerlist[0].money)
                                    playerlist[trade_to].money += int(item[1:5])
                                    playerlist[trade_to].money_label.config(text=playerlist[trade_to].money)
                                except:
                                    pass
                            else:
                                try:
                                    playerlist[0].money += int(item[1:5])
                                    playerlist[0].money_label.config(text=playerlist[0].money)
                                    playerlist[trade_to].money -= int(item[1:5])
                                    playerlist[trade_to].money_label.config(text=playerlist[trade_to].money)
                                except:
                                    pass
                        elif item.owner == 0:
                            item.owner = trade_to
                        else:
                            item.owner = 0
                    trade_accepted_label = Label(trade_gui, text='Trade Accepted', font=('Cooper Std Black', 100), fg='green')
                    trade_accepted_label.place(x='310', y='140')
                    trade_accepted_label.after(1500, lambda: (trade_accepted_label.destroy(), close_trade_window()))

                else:
                    trade_denied_label = Label(trade_gui, text='Trade Denied', font=('Cooper Std Black', 100), fg='red')
                    trade_denied_label.place(x='340', y='140')
                    trade_denied_label.after(1500, trade_denied_label.destroy)



            tradelist = []
            playerlist[0].trade_property_counter = 0
            playerlist[1].trade_property_counter = 8
            playerlist[2].trade_property_counter = 8
            playerlist[3].trade_property_counter = 8

            def add_trade_property(event, theboardplace):
                if line_dictionary[theboardplace.number].cget('bg') != playerlist[theboardplace.owner].color3:
                    if line_dictionary[theboardplace.number].cget('bg') == playerlist[theboardplace.owner].color:
                        line_dictionary[theboardplace.number].config(bg=playerlist[theboardplace.owner].color2)
                        playerlist[theboardplace.owner].trade_property_counter += 1
                        theboardplace.tradelb.place(x=smalllbcord_dictionary[playerlist[theboardplace.owner].trade_property_counter][0], y=smalllbcord_dictionary[playerlist[theboardplace.owner].trade_property_counter][1])

                        if theboardplace.owner != 0:
                            for boardplace in boardplaceslist:
                                if boardplace.owner != 'no' and boardplace.owner != theboardplace.owner and boardplace.owner != 0:
                                    line_dictionary[boardplace.number].config(bg=playerlist[boardplace.owner].color3)
                        tradelist.append(theboardplace)
                        if playerlist[0].trade_property_counter > 0 and (playerlist[1].trade_property_counter > 8 or playerlist[2].trade_property_counter > 8 or playerlist[3].trade_property_counter > 8):
                            propose_trade_button['state'] = NORMAL
                        if theboardplace.owner != 0:
                            gameboard.tradeto = theboardplace.owner

                    elif line_dictionary[theboardplace.number].cget('bg') == playerlist[theboardplace.owner].color2:
                        line_dictionary[theboardplace.number].config(bg=playerlist[theboardplace.owner].color)
                        tradelist.remove(theboardplace)
                        theboardplace.tradelb.place_forget()
                        playerlist[theboardplace.owner].trade_property_counter -= 1
                        if not any(getattr(place, 'owner', None) in {1, 2, 3} for place in tradelist):
                            for boardplace in boardplaceslist:
                                if boardplace.owner != 'no' and boardplace.owner != 0:
                                    line_dictionary[boardplace.number].config(bg=playerlist[boardplace.owner].color)
                        if playerlist[0].trade_property_counter == 0 or (playerlist[1].trade_property_counter == 8 and playerlist[2].trade_property_counter == 8 and playerlist[3].trade_property_counter == 8):
                            propose_trade_button['state'] = DISABLED

            for boardplace in boardplaceslist:
                if boardplace.owner != 'no':
                    line_dictionary[boardplace.number].bind("<Button-1>", lambda event, place=boardplace: add_trade_property(event, place))
                if boardplace.housenumber != 0:
                    line_dictionary[boardplace.number].config(bg=playerlist[boardplace.owner].color3)


            propose_trade_button = Button(trade_gui, height=3, width=8, text='Propose Trade', command=lambda: complete_trade(tradelist=tradelist, trade_to=gameboard.tradeto))
            propose_trade_button.place(x = '1130', y = '428')
            propose_trade_button['state'] = DISABLED

            def limit_text_length(event):
                gain_text = gain_money_text.get("1.0", tk.END)
                gain_text = gain_text.strip()
                lose_text = lose_money_text.get("1.0", tk.END)
                lose_text = lose_text.strip()
                if len(gain_text) > 4 or (gain_text and not gain_text.isdigit()):
                    gain_money_text.delete("1.0", tk.END)
                    new_gain_text = ''.join(filter(str.isdigit, gain_text))
                    gain_money_text.insert("1.0", new_gain_text[:4])
                if len(lose_text) > 4 or (lose_text and not lose_text.isdigit()):
                    lose_money_text.delete("1.0", tk.END)
                    new_lose_text = ''.join(filter(str.isdigit, lose_text))
                    lose_money_text.insert("1.0", new_lose_text[:4])

            def add_player_money(event):
                lose_money_value = lose_money_text.get("1.0", "end-1c").strip()
                if lose_money_value:
                    try:
                        int_lose_money = int(lose_money_value)
                    except ValueError:
                        lose_money_text.delete("1.0", tk.END)
                        return
                    if int_lose_money <= playerlist[0].money:
                        if int_lose_money != 0:
                            lose_money_lb.config(text='$'+str(int_lose_money))
                            lose_money = '0'+str(int_lose_money)
                            for item in tradelist:
                                if type(item) == str:
                                    if item[0] == '0':
                                        tradelist.remove(item)
                                        playerlist[0].trade_property_counter -= 1
                            tradelist.append(lose_money)
                            playerlist[0].trade_property_counter += 1
                            if playerlist[0].trade_property_counter > 0 and (playerlist[1].trade_property_counter > 8 or playerlist[2].trade_property_counter > 8 or playerlist[3].trade_property_counter > 8):
                                propose_trade_button['state'] = NORMAL

                        else:
                            lose_money_lb.config(text='')
                            for item in tradelist:
                                if type(item) == str:
                                    if item[0] == '0':
                                        tradelist.remove(item)
                            playerlist[0].trade_property_counter -= 1
                            if playerlist[0].trade_property_counter == 0:
                                propose_trade_button['state'] = DISABLED
                        #print(tradelist)

                lose_money_text.delete("1.0", tk.END)

            def add_opponent_money(event):
                for player in playerlist:
                    if player.trade_property_counter > 8:
                        gain_money_value = gain_money_text.get("1.0", "end-1c").strip()
                        if gain_money_value:
                            try:
                                int_gain_money = int(gain_money_value)
                            except ValueError:
                                lose_money_text.delete("1.0", tk.END)
                                return
                            if int_gain_money <= player.money:
                                if int_gain_money != 0:
                                    gain_money_lb.config(text='$'+str(int_gain_money))
                                    gain_money = str(player.number)+str(int_gain_money)
                                    for item in tradelist:
                                        if type(item) == str:
                                            if item[0] != '0':
                                                tradelist.remove(item)
                                                playerlist[player.number].trade_property_counter -= 1
                                    tradelist.append(gain_money)
                                    playerlist[player.number].trade_property_counter += 1
                                else:
                                    gain_money_lb.config(text='')
                                    for item in tradelist:
                                        if type(item) == str:
                                            if item[0] != '0':
                                                tradelist.remove(item)
                                    playerlist[player.number].trade_property_counter -= 1
                                #print(tradelist)

                gain_money_text.delete("1.0", tk.END)

            def disable_enter_and_tab(event):
                pass


            lose_money_text = Text(trade_gui, height=1, width=4, font=('Cooper Std Black', 30), fg='red')
            lose_money_text.place(x='834', y='440')
            lose_money_text.bind("<KeyRelease>", limit_text_length)
            lose_money_text.bind("<Tab>", disable_enter_and_tab)
            lose_money_text.bind("<Return>", add_player_money)
            add_your_lb = Label(trade_gui, text='Add your')
            add_your_lb.place(x='730', y='442')
            money_to_lb = Label(trade_gui, text='money to trade')
            money_to_lb.place(x='714', y='462')
            dollar_sign_lb1 = Label(trade_gui, text='$', font=('Cooper Std Black', 30), fg='red')
            dollar_sign_lb1.place(x='809', y='440')
            lose_money_lb = Label(trade_gui, text='', height=1, width=6, font=('Cooper Std Black', 30), fg='red')
            lose_money_lb.place(x=1120, y=72)

            gain_money_text = Text(trade_gui, height=1, width=4, font=('Cooper Std Black', 30), fg='green')
            gain_money_text.place(x='1042', y='440')
            gain_money_text.bind("<KeyRelease>", limit_text_length)
            gain_money_text.bind("<Tab>", disable_enter_and_tab)
            gain_money_text.bind("<Return>", add_opponent_money)
            add_opponent_lb = Label(trade_gui, text='Add opponent')
            add_opponent_lb.place(x='924', y='442')
            money_to_lb = Label(trade_gui, text='money to trade')
            money_to_lb.place(x='922', y='462')
            dollar_sign_lb1 = Label(trade_gui, text='$', font=('Cooper Std Black', 30), fg='green')
            dollar_sign_lb1.place(x='1017', y='440')
            gain_money_lb = Label(trade_gui, text='', height=1, width=6, font=('Cooper Std Black', 30), fg='green')
            gain_money_lb.place(x=1120, y=300)

    def gui_movefunc(self):
        #self.label.place(x= boardplaceslist[2].cordx, y=boardplaceslist[2].cordy)
        #for boardmove in range(self.old_board_number, self.board_number):
        if self.old_board_number != self.board_number:
            self.old_board_number += 1
            if self.old_board_number >= 40:
                self.old_board_number -= 40
                self.money += 200
                self.money_label.config(text=self.money)
                cashlb.config(text='+$200', fg='green')
            self.place_x = boardplaceslist[self.old_board_number].cordx
            self.place_y = boardplaceslist[self.old_board_number].cordy
            self.label.place(x=self.place_x, y=self.place_y)
            self.label.lift()
            gui.update()
            gameboard.pieceshift(self.number)
            time.sleep(0.6)
            self.gui_movefunc()

        else:
            self.identify_property()

    def rollfunc(self):
        rollbut['state'] = DISABLED ##TO DO make disable and enable methods of the gameboard object
        managepropbutton['state'] = DISABLED
        tradebutton['state'] = DISABLED
        endturnbutton['state'] = DISABLED
        endgamebutton['state'] = DISABLED
        close_manage_window()
        close_trade_window()
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        #roll1 = 4
        #roll2 = 5
        game.gui_diceroll(gameboard, roll1, roll2)
        if roll1 != roll2:
            gameboard.doubles = False
            doubleslb.config(text='')
            gameboard.turn += 1
            if gameboard.turn == 3:
                gameboard.cycletrue = True ##Not in use, get rid of later
            if gameboard.turn == gameboard.playernumber:
                gameboard.turn -= gameboard.playernumber
        else:
            doubleslb.config(text='DOUBLES!', fg='green')
            gameboard.doubles = True
        #time.sleep(0.1)
        sum = roll1 + roll2
        self.previous_roll = sum
        self.old_board_number = self.board_number
        self.board_number += sum
        if self.board_number>= 40:
            self.board_number -= 40
        cashlb.config(text='')
        self.gui_movefunc()

def close_trade_window():
    for widget in trade_gui.winfo_children():
        if widget.widgetName == 'button':
            widget.destroy()
        else:
            widget.place_forget()
    trade_gui.withdraw()
    gameboard.openwindows = 2
    for line_number in line_dictionary:
        line_dictionary[line_number].unbind("<Button-1>")
        if boardplaceslist[line_number].owner != 'no':
            line_dictionary[line_number].config(bg=playerlist[boardplaceslist[line_number].owner].color)

def close_manage_window():
    for widget in managegui.winfo_children():
        if widget.widgetName == 'button':
            widget.destroy()
        else:
            widget.place_forget()
    managegui.withdraw()
    gameboard.openwindows = 2

def endgame():
    rollbut['state'] = DISABLED ##TO DO make disable and enable methods of the gameboard object
    managepropbutton['state'] = DISABLED
    tradebutton['state'] = DISABLED
    endturnbutton['state'] = DISABLED
    endgamebutton['state'] = DISABLED
    close_manage_window()
    close_trade_window()

    def yes_endgame():
        sys.exit()
    def no_endgame():
        end_game_gui.destroy()
        gameboard.next_turn_check()

    end_game_gui = tk.Toplevel()
    end_game_gui.geometry('350x200+300+300')
    end_game_gui.title('End Game')
    end_game_lb = Label(end_game_gui, text='Would you like to end the game?', font=('Cooper Std Black', 20))
    end_game_lb.place(x=30, y=20)
    yes_button = Button(end_game_gui, text='YES', height=5, width=5, command=yes_endgame)
    yes_button.place(x=40, y=60)
    no_button = Button(end_game_gui, text='NO', height=5, width=5, command=no_endgame)
    no_button.place(x=220, y=60)
    end_game_gui.wm_protocol("WM_DELETE_WINDOW", noclose)


playerlist = [player(True, 0, 'blue', 'midnightblue', 'lightsteelblue', monbluelabel, 1500, bmoneyvallb, 0, 0, 640, 715, 0, 0, 0, 0, {1:6, 3:6, 6:10, 8:10, 9:12, 11:14, 13:14, 14:16, 16:18, 18:18, 19:20, 21:22, 23:22, 24:24, 26:26, 27:26, 29:28, 31:30, 32:30, 34:32, 37:35, 39:40, 12:15, 28:15, 5:20, 15:20, 25:20, 35:20}),
              player(False, 1, 'lime', 'darkgreen', 'lightgreen', mongreenlabel, 1500, gmoneyvallb, 0, 0, 640, 690, 0, 0, 0, 8, {1:6, 3:6, 6:10, 8:10, 9:12, 11:14, 13:14, 14:16, 16:18, 18:18, 19:20, 21:22, 23:22, 24:24, 26:26, 27:26, 29:28, 31:30, 32:30, 34:32, 37:35, 39:40, 12:15, 28:15, 5:20, 15:20, 25:20, 35:20}),
              player(False, 2, 'red', 'darkred', 'lightcoral', monredlabel, 1500, rmoneyvallb, 0, 0, 640, 665, 0, 0, 0, 8, {1:6, 3:6, 6:10, 8:10, 9:12, 11:14, 13:14, 14:16, 16:18, 18:18, 19:20, 21:22, 23:22, 24:24, 26:26, 27:26, 29:28, 31:30, 32:30, 34:32, 37:35, 39:40, 12:15, 28:15, 5:20, 15:20, 25:20, 35:20}),
              player(False, 3, 'fuchsia', 'purple', 'plum', monpinklabel, 1500, pmoneyvallb, 0, 0, 640, 640, 0, 0, 0, 8, {1:6, 3:6, 6:10, 8:10, 9:12, 11:14, 13:14, 14:16, 16:18, 18:18, 19:20, 21:22, 23:22, 24:24, 26:26, 27:26, 29:28, 31:30, 32:30, 34:32, 37:35, 39:40, 12:15, 28:15, 5:20, 15:20, 25:20, 35:20})]

rollbut = Button(Controlgui, height=5, width=5, text='roll', command=playerlist[0].rollfunc)
rollbut.place(x = '1', y = '1')
managepropbutton = Button(Controlgui, height=5, width=5, text='manage', command=playerlist[0].manage_property)#, command=managefunc)
managepropbutton.place(x='100', y='1')
tradebutton = Button(Controlgui, height=5, width=5, text='trade', command=playerlist[0].trade)#, command=tradefunc)
tradebutton.place(x='200', y='1')
endturnbutton = Button(Controlgui, height=5, width=5, text='End Turn', command=gameboard.ai_cycle)#, command=tradefunc)
endturnbutton.place(x='1', y='100')
endturnbutton['state'] = DISABLED
endgamebutton = Button(Controlgui, height=5, width=5, text='End Game', command=endgame)#, command=tradefunc)
endgamebutton.place(x='200', y='100')

Controlgui.resizable(False, False)
Controlgui.wm_protocol("WM_DELETE_WINDOW", noclose)

trade_gui.wm_protocol("WM_DELETE_WINDOW", close_trade_window)
managegui.wm_protocol("WM_DELETE_WINDOW", close_manage_window)

gameboard.line_check()

for player in playerlist:
    player.set_property_worth()

a = playerlist[0].ai_property_buy_check(3)
b = playerlist[0].ai_property_buy_check(9)
#print(a, b)

print('----RULES----')
print('No more than 3 windows can be open at a time')
print('Trading must have at least 1 element from each side and an opponent property must be included')
print('Inputted money for a trade that exceeds the amount that player has will not be included')
print('To remove money from the trade input a 0')
print('A mortgaged property cannot have houses and a property with houses cannot be mortgaged')
print('properties with houses cannot be traded')
print('When an opponent lands on a chest property the player will click to acknowledge the card, but will not receive the card, the opponent will')
