import pygame
import random

class Ball:
    
    def __init__(self, size, min_x, max_x, min_y, max_y, left_paddle_x, right_paddle_x):
        self.mX = min_x
        self.mY = min_y
        self.mSize = size
        self.mDX = 0
        self.mDY = 0
        self.mMinX = min_x
        self.mMaxX = max_x
        self.mMinY = min_y
        self.mMaxY = max_y
        self.mLeftPaddleX = left_paddle_x
        self.mLeftPaddleMinY = min_y
        self.mLeftPaddleMaxY = max_y
        self.mRightPaddleX = right_paddle_x
        self.mRightPaddleMinY = min_y
        self.mRightPaddleMaxY = max_y
        return
        
    def getX(self):
        return self.mX
    
    def getY(self):
        return self.mY
    
    def getSize(self):
        return self.mSize
    
    def getDX(self):
        return self.mDX
    
    def getDY(self):
        return self.mDY
    
    def getMinX(self):
        return self.mMinX
    
    def getMaxX(self):
        return self.mMaxX
    
    def getMinY(self):
        return self.mMinY
    
    def getMaxY(self):
        return self.mMaxY
    
    def getLeftPaddleX(self):
        return self.mLeftPaddleX
    
    def getLeftPaddleMinY(self):
        return self.mLeftPaddleMinY
    
    def getLeftPaddleMaxY(self):
        return self.mLeftPaddleMaxY
    
    def getRightPaddleX(self):
        return self.mRightPaddleX
    
    def getRightPaddleMinY(self):
        return self.mRightPaddleMinY
    
    def getRightPaddleMaxY(self):
        return self.mRightPaddleMaxY
    
    def setPosition(self, x, y):
        if (x >= self.mMinX and x <= (self.mMaxX - self.mSize)) and (y >= self.mMinY and y <= (self.mMaxY - self.mSize)):
            self.mX = x
            self.mY = y
            return
        else:
            return
        
    def setSpeed(self, dx, dy):
        self.mDX = dx
        self.mDY = dy
        return
    
    def setLeftPaddleY(self, paddle_min_y, paddle_max_y):
        if (paddle_min_y < paddle_max_y):
            if (paddle_min_y >= self.mMinY and paddle_min_y <= self.mMaxY) and (paddle_max_y >= self.mMinY and paddle_max_y <= self.mMaxY):
                self.mLeftPaddleMinY = paddle_min_y
                self.mLeftPaddleMaxY = paddle_max_y
                return
    
    def setRightPaddleY(self, paddle_min_y, paddle_max_y):
        if (paddle_min_y < paddle_max_y):
            if (paddle_min_y >= self.mMinY and paddle_min_y <= self.mMaxY) and (paddle_max_y >= self.mMinY and paddle_max_y <= self.mMaxY):
                self.mRightPaddleMinY = paddle_min_y
                self.mRightPaddleMaxY = paddle_max_y
                return

    def checkTop(self, new_y):
        if new_y > self.mMinY:
            return new_y
        else:
            self.mDY = -(self.mDY)
            d = self.mMinY - new_y
            new_y = self.mMinY + d
            return new_y

    def checkBottom(self, new_y):
        if new_y + self.mSize < self.mMaxY:
            return new_y
        else:
            self.mDY = -(self.mDY)
            d = self.mMaxY - new_y - self.mSize
            new_y = self.mMaxY + d - self.mSize
            return new_y

    def checkLeft(self, new_x):
        if new_x > self.mMinX:
            return new_x
        else:
            self.mDX = 0
            self.mDY = 0
            new_x = self.mMinX
            return new_x

    def checkRight(self, new_x):
        if new_x + self.mSize < self.mMaxX:
            return new_x
        else:
            self.mDX = 0
            self.mDY = 0
            new_x = self.mMaxX - self.mSize
            return new_x

    def checkLeftPaddle(self, new_x, new_y):
        mid_y = (new_y + self.mY) / 2
        if mid_y >= self.mLeftPaddleMinY and mid_y <= self.mLeftPaddleMaxY and new_x <= self.mLeftPaddleX and self.mX >= self.mLeftPaddleX:
            self.mDX = -(self.mDX)
            d = self.mLeftPaddleX - new_x
            new_x = self.mLeftPaddleX + d
            return new_x
        else:
            return new_x

    def checkRightPaddle(self, new_x, new_y):
        mid_y = (new_y + self.mY) / 2
        if (mid_y >= self.mRightPaddleMinY) and (mid_y <= self.mRightPaddleMaxY) and (new_x + self.mSize >= self.mRightPaddleX) and (self.mX + self.mSize <= self.mRightPaddleX):
            self.mDX = -(self.mDX)
            d = self.mRightPaddleX - new_x - self.mSize
            new_x = self.mRightPaddleX + d - self.mSize
            return new_x
        else:
            return new_x

    def move(self, dt):
        new_x = (dt * self.mDX) + self.mX
        new_y = (dt * self.mDY) + self.mY
        new_y = self.checkTop(new_y)
        new_y = self.checkBottom(new_y)
        new_x = self.checkLeft(new_x)
        new_x = self.checkRight(new_x)
        new_x = self.checkLeftPaddle(new_x, new_y)
        new_x = self.checkRightPaddle(new_x, new_y)
        self.setPosition(new_x, new_y)
        return

    def serveLeft(self, x, min_y, max_y, min_dx, max_dx, min_dy, max_dy):
        self.setPosition(x, random.uniform(min_y, max_y))
        self.mDX = random.uniform(min_dx, max_dx)
        self.mDY = random.uniform(min_dy, max_dy)
        return

    def serveRight(self, x, min_y, max_y, min_dx, max_dx, min_dy, max_dy):
        self.setPosition(x, random.uniform(min_y, max_y))
        self.mDX = random.uniform(-min_dx, -max_dx)
        self.mDY = random.uniform(min_dy, max_dy)
        return

    def draw(self, surface):
        rect = pygame.Rect(self.mX, self.mY, self.mSize, self.mSize)
        pygame.draw.rect(surface, (255, 255, 255), rect, 0)
        return