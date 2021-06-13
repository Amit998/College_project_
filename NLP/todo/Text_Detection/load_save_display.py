import cv2
import random, string


# img=cv2.imread('test1.jpg')
vid=cv2.VideoCapture(0)

def get_random_name():
    x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
    return x

count=0

file_name=''
while(count !=60): 
      
    ret, frame = vid.read() 
  
   
    cv2.imshow('frame', frame) 
    
    if (count==59):
        random_name=get_random_name()
        file_name=f'img/test_{}.jpg'.format(random_name)
        cv2.imwrite(file_name,frame)
        break
    print(count)
    
    count+=1
  
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  

vid.release() 

cv2.destroyAllWindows() 
print(file_name,'here')

# cv2.imwrite('img/test1.jpg',img)


