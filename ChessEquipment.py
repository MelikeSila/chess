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
        Colour = (100,120,10)
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)

        # Setup a board_length x board_length pixel display with caption
        ChessBoard = pygame.display.set_mode((board_length,board_length))
        ChessBoard.fill(WHITE)
        pygame.display.set_caption("CHESS")


        # create board squares
        exact_board_length = board_length
        board_length = exact_board_length - (exact_board_length/ (8 + 1))
        square_length = board_length/ (8 + 1)
        square_position1 = square_length
        square_position2 = square_length
        count = 0
        position_names = ["a","b","c","d","e","f","g","h"]
        
        ####################
        # draw the frame of the board
        pygame.draw.rect(ChessBoard, BLACK, 
                                 [square_length, square_length, 
                                  board_length - square_length, board_length - square_length], width = 4, 
                                 border_radius=2,border_top_left_radius=-1, border_top_right_radius=-1,
                                 border_bottom_left_radius=-1, border_bottom_right_radius=-1)
        
        ########################################
        #draw the position name and the squares of the chessboard
        while square_position1 < (board_length):
            from pygame import font
            square_position2 = square_length
            if count%2 == 0:
                square_position2 = square_length*2
            count = count + 1
            
            ####################
            ### draw the position name
            font = pygame.font.SysFont("comicsansms", int(square_length/4))
            text1 = font.render(str(count), True, BLACK)
            text2 = font.render(position_names[count-1], True, BLACK)
            ChessBoard.blit(text1,(0 + square_length/4 , square_position1  + square_length/4))
            pygame.display.flip()
            ChessBoard.blit(text2,(square_position1 + square_length/4 , 0  + square_length/4))
            
            ####################
            ### draw the squares of the chessboard
            while square_position2 < (board_length):
                pygame.draw.rect(ChessBoard, BLACK, 
                                 [square_position1, square_position2, square_length, square_length], 
                                 border_radius=2,border_top_left_radius=-1, border_top_right_radius=-1,
                                 border_bottom_left_radius=-1, border_bottom_right_radius=-1)
                square_position2 = square_position2 + square_length*2
            ####################
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