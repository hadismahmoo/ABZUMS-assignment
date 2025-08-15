import pandas as pd
import os
from datetime import datetime



class Dataframe:
    def __init__(self,event_ID,user_ID,timestamp,platform,event_type,video_ID=None,watch_time_sec=None,video_duration_sec=None):
        self.event_ID=event_ID
        self.user_ID=user_ID
        self.timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        self.platform=platform
        self.event_type=event_type
        self.video_ID=video_ID
        self.watch_time_sec=watch_time_sec
        self.video_duration_sec=video_duration_sec
        self.event_ID_type={
            1001:"login",
            1002:"logout",
            1003:"comment",
            1004:"like",
            1005:"play_video"
        }
        self.Dataframe={
            "event_ID":self.event_ID,
            "user_ID":self.user_ID,
            "timestamp":self.timestamp,
            "platform":self.platform,
            "event_type":self.event_type,
            "video_ID":self.video_ID,
            "watch_time_sec":self.watch_time_sec,
            "video_duration_sec":self.video_duration_sec
        }

    def make_data(self):
        
        while True:
            if self.event_ID not in self.event_ID_type.keys():
                print("this ID does not exist")
                self.event_ID=int(input("enter another ID: "))
                continue

            if self.event_type.lower() !=self.event_ID_type[self.event_ID]:
                print("this type and ID does not match ")
                self.event_type=input("enter your type correctly: ")
                continue

            

            if self.watch_time_sec is not None and self.video_duration_sec is not None and self.watch_time_sec>self.video_duration_sec:
                print("this data is invalid try again: ")
                self.watch_time_sec=int(input("enter another valid time: "))
                continue

            break 

    def save_to_csv(self,filename="events.csv"):
        df_new_events=pd.DataFrame([self.Dataframe])
        if os.path.exists(filename):
            df_existing_events=pd.read_csv(filename)
            df_combined=pd.concat([df_new_events,df_existing_events],ignore_index=False)
        else:
            df_combined=df_new_events
        df_combined.to_csv(filename,index=False)

        

        
    def __str__(self):
        return str(self.Dataframe)
    



event_ID=int(input("enter the event_ID: "))
user_ID=input("enter your ID: ")
timestamp=input("enter the date and time for this event: ")
platform=input("enter the platform you used for this event (android,ios,web): ")
event_type=input("enter the type of event you did : ")
video_ID=input("enter the video ID if you have watched a video : ")
watch_time_sec=input("How long did you watched the video ? ")
watch_time_sec=int(watch_time_sec) if watch_time_sec else None
video_duration_sec=input("How long is the video? ")
video_duration_sec=int(video_duration_sec) if video_duration_sec else None

user=Dataframe(event_ID,user_ID,timestamp,platform,event_type,video_ID,watch_time_sec,video_duration_sec)
user.make_data()
user.save_to_csv()
print(user)



            

            











