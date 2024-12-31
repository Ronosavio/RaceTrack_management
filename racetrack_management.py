from datetime import time, datetime, timedelta
from pydantic import BaseModel, Field, ValidationError
from typing import Annotated
from abc import ABC, abstractmethod

mini_book_time = 3 #minimum booking time is three hours 

Rt_bike_capacity = 4
vehicle_no = {'Bikes': [], 'Cars':[], 'Suv\'s':[]}

#per hour cost for each vehicle  depending on the track
bike_cost = 60
car_cost = 120
vip_car_cost = 250
suv_cost = 200
vip_suv_cost = 300

class Revenue():
    Regular_revenue  = 0 
    def __init__(self, bike_count = 0, car_count = 0, suv_count = 0, vip_car_count = 0, vip_suv_count = 0):
        self.bike_count = bike_count
        self.car_count = car_count
        self.suv_count = suv_count
        self.vip_car_count = vip_car_count
        self.vip_suv_count = vip_suv_count
        
    def Regular_track_profit(self):
        profit_bike = self.bike_count * (mini_book_time *bike_cost)  
        profit_car = self.car_count * (mini_book_time * car_cost)
        profit_suv = self.suv_count * (mini_book_time * suv_cost)
        Revenue.Regular_revenue = profit_bike + profit_car + profit_suv
        return Revenue.Regular_revenue
        
    
    def Vip_track_profit():
        pass


class track_Management(ABC):
      @abstractmethod
      def __init__(self, V_Type, V_No, V_Time):
          self.V_Type = V_Type
          self.V_No = V_No
          self.V_Time = V_Time
       
      def regular_bike_time(self):
          entry_time = datetime.strptime(str(self.V_Time), '%H:%M:%S')
          update_time = entry_time + timedelta(hours = mini_book_time) 
          exit_time = update_time.time()
          
          bike_count = len(vehicle_no['Bikes'])
          if bike_count == Rt_bike_capacity:
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
             prf = Revenue(Regular_track.bike_count).Regular_track_profit()
             print(prf)
          
    

   
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
          
      
book = [['bike', 'M20' , '17:00:00'], ['bike', 'M201' , '17:00:00'], ['bike', 'M203' , '18:00:00'], ['bike', 'M204' , '14:00:00'], ]

for vehicle in book:
    try:      
        v_type, v_no, entr_t = vehicle
        Book(V_Type  = v_type, V_No= v_no, Etr_T= entr_t).book()
    except ValidationError as e:
            print(f"\n\nError for vehicle ( {v_type}) No: {v_no}: {e}\n\n")



print(vehicle_no['Bikes'])  # Outputs the final state of the bike records
