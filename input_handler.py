import pygame

class Command:
    def execute(self, entity):
        raise NotImplemented

class Up(Command):
    def execute(self, entity):
        entity.up()

class Left(Command):
    def execute(self, entity):
        entity.left()

class Right(Command):
    def execute(self, entity):
        entity.right()

class InputHandler:
    def __init__(self):
        self.command = {
            'w': Up(),
            'a': Left(),
            'd': Right(),
            'up': Up(),
            'left': Left(),
            'right': Right()
        }
    
    def handle_input(self, key):
        return self.command[key]
