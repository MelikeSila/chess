##################################################
##################################################
# The class is for establishing a chess game
#
##################################################
##################################################
class Board:
    
    def __init__(self):
        self.board_length = 800
        self.pygame = None

    ##################################################
    # Method for draw the chess board
    ##################################################
    def DrawChessBoard(self, board_length = 800):
        
        import pygame

        pygame.init()

        # Setting up color objects
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)

        # Setup a board_length x board_length pixel display with caption
        ChessBoard = pygame.display.set_mode((board_length,board_length))
        ChessBoard.fill(WHITE)
        pygame.display.set_caption("CHESS")


        # create board squares
        square_length = board_length/ (8 + 1)
        square_position1 = square_length
        square_position2 = square_length
        count = 0
        ########################################
        ###TODO draw the square names such as b1 a2 etc
        while square_position1 < (board_length):
            square_position2 = square_length
            if count%2 == 0:
                square_position2 = square_length*2
            count = count + 1
            while square_position2 < (board_length):
                pygame.draw.rect(ChessBoard, BLACK, 
                                 [square_position1, square_position2, square_length, square_length], 
                                 border_radius=2,border_top_left_radius=-1, border_top_right_radius=-1,
                                 border_bottom_left_radius=-1, border_bottom_right_radius=-1)
                square_position2 = square_position2 + square_length*2
            square_position1 = square_position1 + square_length
        self.pygame = pygame
    
    ##################################################
    # Draw Chess Pieces
    ##################################################
    def DrawChessPieces(self ):
        pygame = self.pygame
        
        

    
    ##################################################
    # Method for run the established pygame
    ##################################################
    def RunGame(self):
        from pygame.locals import QUIT
        import sys
        
        pygame = self.pygame
         # Assign FPS a value
        fps = 30
        FramePerSec = pygame.time.Clock()
        
        # Beginning Game Loop
        while True:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            FramePerSec.tick(fps)