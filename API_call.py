import cv2, requests
import os
from datetime import datetime

def mkdir(path):    
    try:
        if(os.path.isdir(path)==False):
            os.mkdir(path)
        return True
    except:
        return False

def get_last_serial_no(server_url):
	response = requests.get(server_url)
	if len(response.json()) <= 0:
		print("No entries in database.")
		return 0
	else:
		print(response.json()[-1]['serial_no'])
		return response.json()[-1]['serial_no']

print("Line from API Call.")

cwd = os.getcwd()

mkdir(cwd+'/'+'temp')
mkdir(cwd+'/'+'Detected')



def upload_to_server(frame, output_img, serial_no, result, server_url,save_failed=True):
    """ Parameters:
        frame : OpenCV frame of the image to be uploaded
        output_img : OpenCV frame of the output image to be uploaded
        serial_no : serial number of the field, It must be unique.
                    If the serial_no already exist in the database, response give error 400 (Bad request)
        result    : String ("ok"/"not_ok")
        server_url   : URL of the server
        save_failed(True/False) : Save frame localy if uploading on server failed."""
    
    cv2.imwrite('temp/img.jpg',frame)
    cv2.imwrite('temp/output_img.jpg',output_img)
    file = {'image':open('temp/img.jpg','rb'), 'result_image':open('temp/output_img.jpg','rb')}
    x = datetime.now()
    date = x.strftime("%Y")+'-'+x.strftime("%m")+'-'+x.strftime("%d")+' '+x.strftime("%H")+':'+x.strftime("%M")+':'+x.strftime("%S")
    date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    data = {"serial_no": serial_no,
            "time": date, 
            "result": result
           }
    
    response = requests.post(server_url,files=file,data=data)
    if(response!=201) and save_failed:
        date_now = x.strftime("%d")+'_'+x.strftime("%m")+'_'+x.strftime("%Y")+'_'+x.strftime("%H")+'_'+x.strftime("%M")+'_'+x.strftime("%S")[:-1]
        cv2.imwrite(cwd+"/Detected/"+date_now+'.png',frame)
        cv2.imwrite(cwd+"/Detected/"+date_now+'.png',output_img)
    return response