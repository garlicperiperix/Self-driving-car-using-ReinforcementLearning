import pygame

class Wall:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def draw(self, win):
        pygame.draw.line(win, (255,255,255), (self.x1, self.y1), (self.x2, self.y2), 5)

def getWalls():
    walls = []

    wall1 = Wall(12, 451, 15, 130)
    wall2 = Wall(15, 130, 61, 58)
    wall3 = Wall(61, 58, 149, 14)
    wall4 = Wall(149, 14, 382, 20)
    wall5 = Wall(382, 20, 549, 31)
    wall6 = Wall(549, 31, 636, 58)
    wall7 = Wall(636, 58, 796, 182)
    #wall8 = Wall(678, 102, 669, 167)

    #wall9 = Wall(669, 167, 600, 206)

    #wall10 = Wall(600, 206, 507, 214)
    #wall11 = Wall(507, 214, 422, 232)
    #wall12 = Wall(422, 232, 375, 263)
    #wall13 = Wall(375, 263, 379, 283)
    #wall14 = Wall(379, 283, 454, 299)
    #wall15 = Wall(454, 299, 613, 286)
    #wall16 = Wall(613, 286, 684, 238)
    #wall17 = Wall(684, 238, 752, 180)
    wall18 = Wall(796, 182, 862, 185)
    wall19 = Wall(862, 185, 958, 279)
    wall20 = Wall(958, 279, 953, 410)
    wall21 = Wall(953, 410, 925, 505)
    wall22 = Wall(925, 505, 804, 566)
    wall23 = Wall(804, 566, 150, 570)
    wall24 = Wall(150, 570, 46, 529)
    wall25 = Wall(46, 529, 12, 451)
    wall27 = Wall(104, 436, 96, 161)
    wall28 = Wall(96, 161, 122, 122)
    wall29 = Wall(122, 122, 199, 91)
    wall30 = Wall(199, 91, 376, 94)
    wall31 = Wall(376, 94, 469, 100)
    wall32 = Wall(469, 100, 539, 102)
    wall33 = Wall(585, 144, 675, 243)
    wall34 = Wall(675, 243, 727, 281)
    wall35 = Wall(727, 281, 829, 342)
    wall351 = Wall(829,342, 856, 372)
    wall36 = Wall(581, 137, 570, 111)
    wall37 = Wall(570, 111, 540, 100)

    wall45 = Wall(854, 369, 854, 429)
    wall46 = Wall(854, 429, 754, 483)
    wall47 = Wall(754, 483, 192, 489)
    wall48 = Wall(192, 489, 104, 436)

    #obstacles are defined here
    wall38 = Wall(108, 545, 108, 550)
    wall39 = Wall(112, 551, 112, 556)
    wall40 = Wall(119, 545, 119, 550)
    wall41 = Wall(124, 554, 124, 559)
    wall42 = Wall(405, 501, 405, 506)
    wall43 = Wall(413, 500, 413, 505)
    wall44 = Wall(414, 501, 414, 506)
    wall49 = Wall(732, 548, 732, 553)
    wall50 = Wall(723, 552, 723, 552)
    wall51 = Wall(722, 560, 722, 565)
    wall52 = Wall(734, 555, 734, 560)
    wall53 = Wall(846, 218, 846, 223)
    wall54 = Wall(82, 358, 82, 363)
    wall55 = Wall(91, 358, 91, 363)
    wall56 = Wall(96, 359, 96, 364)
    wall57 = Wall(90, 370, 90, 375)
    wall58 = Wall(405, 508, 405, 513)
    wall59 = Wall(105, 536, 105, 541)
    wall60 = Wall(725, 541, 725, 546)
    wall61 = Wall(941, 367, 941, 372)
    wall62 = Wall(630, 163, 630, 168)
    wall64 = Wall(467, 82, 467, 87)
    wall65 = Wall(110, 52, 110, 57)
    wall66 = Wall(574, 124, 600, 161)
    wall67 = Wall(743, 557, 743, 562)
    wall68 = Wall(741, 558, 741, 563)
    wall69 = Wall(948,370, 948, 375)
    wall70 = Wall(944, 357, 944, 362)
    wall71 = Wall(949,349, 949, 354)
    wall72 = Wall(849,208, 849, 213)
    wall73 = Wall(867, 211, 867, 216)
    wall74 = Wall(857, 202, 857, 207)
    wall75 = Wall(849, 194, 849, 199)
    wall76 = Wall(859, 217, 859, 222)
    wall77 =Wall(623,175, 623, 180)
    wall78 = Wall(634, 175, 634, 179)
    wall79 = Wall(630, 184, 630, 189)
    wall80 = Wall(620, 176, 620, 181)
    wall81 = Wall(615, 164, 615, 169)
    wall82 = Wall(476, 89, 476, 94)
    wall83 = Wall(465, 91, 465, 96)
    wall84 = Wall(454, 87, 454, 92)
    wall85 = Wall(119, 36, 119, 41)
    wall86 = Wall(119,47, 119, 52)
    wall87 = Wall(100, 48, 100, 53)





    walls.append(wall1)
    #walls.append(wall50)
    #walls.append(wall51)
    #walls.append(wall52)
    walls.append(wall53)
    walls.append(wall54)
    walls.append(wall55)
    walls.append(wall56)
    walls.append(wall57)
    walls.append(wall351)

    walls.append(wall2)
    walls.append(wall3)
    walls.append(wall4)
    walls.append(wall5)
    walls.append(wall6)
    walls.append(wall7)
    #walls.append(wall57)
    walls.append(wall58)
    walls.append(wall59)
    walls.append(wall60)
    walls.append(wall61)
    walls.append(wall62)
    #walls.append(wall63)
    walls.append(wall64)
    walls.append(wall65)
    walls.append(wall69)
    walls.append(wall70)
    walls.append(wall71)
    walls.append(wall67)
    walls.append(wall18)
    walls.append(wall19)
    walls.append(wall20)
    walls.append(wall21)
    walls.append(wall22)
    walls.append(wall23)
    walls.append(wall24)
    walls.append(wall25)

    walls.append(wall27)
    walls.append(wall28)
    walls.append(wall29)
    walls.append(wall30)
    walls.append(wall31)
    walls.append(wall32)
    walls.append(wall33)
    walls.append(wall34)
    walls.append(wall35)
    walls.append(wall36)
    walls.append(wall37)
    walls.append(wall38)
    walls.append(wall39)
    walls.append(wall40)
    walls.append(wall41)
    walls.append(wall42)
    walls.append(wall43)
    walls.append(wall44)
    walls.append(wall49)
    walls.append(wall50)
    walls.append(wall51)
    walls.append(wall52)
    walls.append(wall66)
    walls.append(wall68)
    walls.append(wall72)
    walls.append(wall73)
    walls.append(wall74)
    walls.append(wall75)
    walls.append(wall76)
    walls.append(wall77)
    walls.append(wall78)
    walls.append(wall79)
    walls.append(wall80)
    walls.append(wall81)
    walls.append(wall82)
    walls.append(wall83)
    walls.append(wall84)
    walls.append(wall85)
    walls.append(wall86)
    walls.append(wall87)
    walls.append(wall45)
    walls.append(wall46)
    walls.append(wall47)
    walls.append(wall48)
    #walls.append(wall49)

    return(walls)