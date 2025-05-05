import pygame

class Paddle:

    def __init__(self, x, y, width, height, speed, min_y, max_y):
        self.mX = x
        self.mY = y
        self.mWidth = width
        self.mHeight = height
        self.mSpeed = speed
        self.mMinY = min_y
        self.mMaxY = max_y
        return

    def getX(self):
        return self.mX

    def getY(self):
        return self.mY

    def getWidth(self):
        return self.mWidth

    def getHeight(self):
        return self.mHeight

    def getSpeed(self):
        return self.mSpeed

    def getRightX(self):
        return self.mX + self.mWidth

    def getBottomY(self):
        return self.mY + self.mHeight

    def getMinY(self):
        return self.mMinY

    def getMaxY(self):
        return self.mMaxY

    def setPosition(self, y):
        if y >= self.mMinY and y + self.mHeight <=  self.mMaxY:
            self.mY = y
            return
        else:
            return

    def moveUp(self, dt):
        y = self.mY - (dt * self.mSpeed)
        if y >= self.mMinY:
            self.mY = y
            return
        else:
            self.mY = self.mMinY
            return

    def moveDown(self, dt):
        y = self.mY + (dt * self.mSpeed)
        if y + self.mHeight <= self.mMaxY:
            self.mY = y
            return
        else:
            self.mY = self.mMaxY - self.mHeight
            return

    def draw(self, surface):
        rect = pygame.Rect(self.mX, self.mY, self.mWidth, self.mHeight)
        pygame.draw.rect(surface, (255, 255, 255), rect, 0)
        return