import pygame
import text
class ScoreBoard:

    def __init__(self, x, y, width, height):
        self.mX = x
        self.mY = y
        self.mWidth = width
        self.mHeight = height
        self.mLeftScore = 0
        self.mRightScore = 0
        self.mServeStatus = 1
        return

    def getX(self):
        return self.mX

    def getY(self):
        return self.mY

    def getWidth(self):
        return self.mWidth

    def getHeight(self):
        return self.mHeight

    def getLeftScore(self):
        return self.mLeftScore

    def getRightScore(self):
        return self.mRightScore

    def getServeStatus(self):
        return self.mServeStatus

    def isGameOver(self):
        if self.mServeStatus == 3 or self.mServeStatus == 4:
            return True
        else:
            return False

    def scoreLeft(self):
        if self.isGameOver() == True:
            return
        else:
            self.mLeftScore += 1
            if self.mLeftScore == 9:
                self.mServeStatus = 3
                return

    def scoreRight(self):
        if self.isGameOver() == True:
            return
        else:
            self.mRightScore += 1
            if self.mRightScore == 9:
                self.mServeStatus = 4
                return

    def swapServe(self):
        if self.isGameOver() is False:
            if self.mServeStatus == 1:
                self.mServeStatus = 2
                return
            if self.mServeStatus == 2:
                self.mServeStatus = 1
                return
        else:
            return

    def draw(self, surface):
        score1 = text.Text(str(self.mLeftScore), (self.mX + self.mWidth/4), (self.mY + self.mHeight/2))
        score2 = text.Text(str(self.mRightScore), (self.mX + 3*self.mWidth/4), (self.mY + self.mHeight/2))
        score1.setColor((255, 255, 255))
        score2.setColor((255, 255, 255))
        score1.draw(surface)
        score2.draw(surface)
        #rect = pygame.Rect(self.mX, self.mY, self.mWidth, self.mHeight)
        #pygame.draw.rect(surface, (255, 255, 255), rect, 0)
        return