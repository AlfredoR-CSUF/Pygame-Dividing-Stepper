import pygame
import math
import time
import array 
pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (77,77,255)

screen = pygame.display.set_mode((700,700))
pygame.display.set_caption('Division Stepper')
font = pygame.font.SysFont("Arial", 30)

askstring =  font.render("Please enter your 2 numbers into console...", 1, white)
askstring_rect = askstring.get_rect()
askstring_rect.center = ((350,350))
screen.blit(askstring, askstring_rect)
pygame.display.update()

num1 = input()
num2 = input()
rem_counter = 0
rem_array = array.array('d', [1,2,3,4])
num_flag = True

#################################
if(math.fmod(int(num1), int(num2)) > int(num2)):
    rem_array[0] = math.fmod(int(num1), int(num2))
    rem_counter+=1
    if(math.fmod(rem_array[0], int(num2)) > int(num2)):
        rem_array[1] = math.fmod(rem_array[0], int(num2))
        rem_counter+=1
        if(math.fmod(rem_array[1], int(num2)) > int(num2)):
            rem_array[2] = math.fmod(rem_array[1], int(num2))
            rem_counter+=1
#print(remainder)
#################################
print(rem_counter)
#################################
def printdiv(num_of_rems):
    print('test')
    y = 100;
    question = str(num1) + " / " + str(num2)
    screen.blit(font.render(question,1,blue), (300,50))
    pygame.display.update()
    if(num_of_rems):
        for i in range(int(num_of_rems)):
            y = y + 100
            #print(y)
            #print(rem_array[i])
            print('test2')
            test = "Step " + str(i+1) + ": " + str(rem_array[i]) + " / " + str(num2) + " = " + str(rem_array[i])
            screen.blit(font.render(test, 1, white), (0,y) )
            pygame.display.update()
    else:
        test = "Step: " + str(num1) + " / " + str(num2) + " = " + str(int(num1)/int(num2))
        screen.blit(font.render(test,1, white), (200,350))
        pygame.display.update()
        
    

while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()
    if(num_flag):
        if(num1.isnumeric() and num2.isnumeric()):        
            screen.blit(font.render("Numbers were received!", 1, white), (0,0))
            pygame.display.update()
            time.sleep(4)
            num_flag = False
        else:
            screen.blit(font.render("Invalid input please try again.", 1, white), (0,0))
            pygame.display.update()
            quit()
    
    printdiv(rem_counter)
    time.sleep(10)




    
        
