from datetime import time, datetime, timedelta
from pydantic import BaseModel, Field
from typing import Annotated
from abc import ABC, abstractmethod

min_time = 3
Rt_bike_capacity = 4
vehicle_no = {'Bikes': [], 'Cars':[], 'Suv\'s':[]}

#per hour cost for each vehicle  depending on the track
bike_cost = 60
car_cost = 120
vip_car_cost = 250
suv_cost = 200
vip_suv_cost = 300

class Revenue():
    def __init__(self, bike_count, car_count, suv_count, vip_car_count, vip_suv_count):
        self.bike_count = bike_count
        self.car_count = car_count
        self.suv_count = suv_count
        self.vip_car_count = vip_car_count
        self.vip_suv_count = vip_suv_count 
        
    def Regular_track_profit():
        pass


class track_Management(ABC):
      @abstractmethod
      def __init__(self, V_Type, V_No, V_Time):
          self.V_Type = V_Type
          self.V_No = V_No
          self.V_Time = V_Time
       
      def regular_bike_time(self):
          entry_time = datetime.strptime(str(self.V_Time), '%H:%M:%S')
          update_time = entry_time + timedelta(hours = 3) 
          exit_time = update_time.time()
          
          bike_count = len(vehicle_no['Bikes'])
          if bike_count == Rt_bike_capacity :
             for bike in vehicle_no['Bikes'][:]:
                 if bike['exit_time'] < self.V_Time:
                    vehicle_no['Bikes'].remove(bike)
             bike_count = len(vehicle_no['Bikes'])

          if bike_count  ==  Rt_bike_capacity: 
               print("RACE TRACK FULL")
               return(bike_count)
          if any(bike['bike_no'] == self.V_No for bike in vehicle_no['Bikes']):
                 print('This bike number is already registered')
          else:
              vehicle_no['Bikes'].append({'bike_no':self.V_No, 'entry_time':entry_time, 'exit_time':exit_time})
              print("SUCCESS")
          bike_count = len(vehicle_no['Bikes'])
          return bike_count
             
             
                   
                    
      def regular_car_time(self):
          pass
      def regular_suv_time(self):
          pass 
      def vip_car_time(self):
          pass
      def vip_suv_time(self):
          pass   
      @abstractmethod
      def tracks(self):
          pass     
       


class Regular_track(track_Management):
      bike_count = 0
      car_count = 0 
      suv_count = 0 
      def __init__(self, v_type, v_no, v_time):
          super().__init__(v_type, v_no, v_time)
          
      def tracks(self):
          if self.V_Type.lower() == 'bike':
             count  = self.regular_bike_time()
             Regular_track.bike_count = count 
             Revenue(Regular_track.bike_count)
          
    

   
class VIP_track(track_Management):
      def tracks():
          pass 
      
class Book(BaseModel):
      V_Type:str
      V_No:str
      Etr_T:Annotated[time, Field(ge = '13:00:00', le ='17:00:00')]
      def book(self):
          x = Regular_track(self.V_Type, self.V_No, self.Etr_T)
          return x.tracks()


class Additional(BaseModel):
      V_No: str
      Ex_T:Annotated[time, Field(ge = '13:00:00' , le = '20:00:00')]      
      
      
vehicle1 = Book(V_Type='bike', V_No='23', Etr_T='13:00:00') 
vehicle2 = Book(V_Type='bike', V_No='223', Etr_T='17:00:00') 
vehicle3 = Book(V_Type='bike', V_No='231', Etr_T='13:00:00') 
vehicle4 = Book(V_Type='bike', V_No='2234', Etr_T='13:00:00') 
vehicle5 = Book(V_Type='bike', V_No='2312', Etr_T='17:00:00') 

vehicle1.book()
vehicle2.book()
vehicle3.book()
vehicle4.book()
vehicle5.book()
     

print(vehicle_no['Bikes'])