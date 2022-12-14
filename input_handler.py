import pygame

class Command:
    def execute(self, entity):
        raise NotImplemented

class Up(Command):
    def execute(self, entity):
        entity.up()

class Down(Command):
    def execute(self, entity):
        entity.down()

class Left(Command):
    def execute(self, entity):
        entity.left()

class Right(Command):
    def execute(self, entity):
        entity.right()

class InputHandler:
    def __init__(self):
        self.command = {
            'up': Up(),
            'down': Down(),
            'left': Left(),
            'right': Right()
        }
    
    def handle_input(self, key):
        return self.command[key]
