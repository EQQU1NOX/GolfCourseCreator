#######################
## Golf Course Creator 
## Jace D. Butcher
#######################

import math;

from math import pi;

class GolfCreator:

    #Implementation of calculate_sq_yrds_smooth_sod() method

    def calculate_sq_yrds_smooth_sod(self,courseWidth):

     

       #Calculate greenAreaRadius

       self.greenAreaRadius = courseWidth/4;

     

       #Calculate total_Smooth_Sod by multiply the values of

       #2 * pi * self.greenAreaRadius * self.greenAreaRadius

       self.total_Smooth_Sod = 2 * pi * self.greenAreaRadius * self.greenAreaRadius;

     

       #Return total_Smooth_Sod

       return self.total_Smooth_Sod;

    #Implementation of calculatesand_trap_area() method

    def calculatesand_trap_area(self,courseWidth):

     

       #Calculate sand_Trap_Radius

       self.sand_Trap_Radius = courseWidth/6;

     

       #Calculate sand_Trap_Radius

       self.sand_trap_area = round(pi * self.sand_Trap_Radius * self.sand_Trap_Radius);

     

       #Return sand_trap_area

       return self.sand_trap_area;

     

    #Implementation of calculate_sq_yrds_rough_sod() method

    def calculate_sq_yrds_rough_sod(self,courseLength, courseWidth, total_Smooth_Sod, sand_trap_area):

     

       #Calculate total_area by multiply the values of courseLength and courseWidth

       self.total_area = courseLength * courseWidth;

     

       #Calculate total_Rough_Sod

       self.total_Rough_Sod = self.total_area - total_Smooth_Sod - sand_trap_area;

     

       #Return total_Rough_Sod

       return self.total_Rough_Sod;

    #Implementation of calculateBricks() method

    def calculateBricks(self,courseWidth):

     

       #Calculate lengthof_brickwall

       self.lengthof_brickwall = pi * (courseWidth * 3/6);

     

       #Calculate number_of_bricks by multiply the value of lengthof_brickwall with 3

       self.number_of_bricks =    self.lengthof_brickwall * 3;

     

       #Return number_of_bricks

       return self.number_of_bricks;

    #Implementation of calculateSand() method

    def calculateSand(self,courseWidth):

     

       #Calculate width_in_feets by multiply the value of courseWidth with 3

       self.width_in_feets = courseWidth * 3;

     

       #Calculate sand_Trap_Radius

       self.sand_Trap_Radius = self.width_in_feets/6;

     

       #Calculate sand_trap_area

       self.sand_trap_area = pi * self.sand_Trap_Radius * self.sand_Trap_Radius;

     

       #Calculate total_tonsof_sand

       self.total_tonsof_sand = (self.sand_trap_area * 100)/2000;

     

       #Return total_tonsof_sand

       return self.total_tonsof_sand;

    #Implementation of calculateBushes() method

    def calculateBushes(self,courseLength, courseWidth):

     

       #Calculate perimeter

       self.perimeter = 2 * (courseLength + courseWidth);

     

       #Calculate total_Bushes

       self.total_Bushes = self.perimeter - 2;

     

       #Return total_Bushes

       return self.total_Bushes;

    #Implementation of calculatetotal_time() method

    def calculatetotal_time(self,total_Rough_Sod, total_Smooth_Sod):

     

       #Calculate total_time

       self.total_time = (total_Rough_Sod * 0.5) + (total_Smooth_Sod * 1);

     

       #Return total_time

       return self.total_time;

    #Implementation of display() method

    def display(self,total_Rough_Sod, total_Smooth_Sod, total_tonsof_sand, number_of_bricks, total_Bushes, total_time):

     

       #Display statement of total_Rough_Sod

       print('Total square yards of rough sod: ', round(total_Rough_Sod));

     

     #Display statement of total_Smooth_Sod

       print('Total square yards of smooth sod: ', math.ceil(total_Smooth_Sod));

     

       #Display statement of total_tonsof_sand

       print('Tons of sand: ', round(total_tonsof_sand));

     

       #Display statement of number_of_bricks

       print('Number of retaining wall bricks: ', math.ceil(number_of_bricks));

     

       #Display statement of total_Bushes

       print('Number of bushes: ', round(total_Bushes));

   

       #calculate mowing_mins     

       mowing_mins = round(total_time/60)

       #Display statement of total mowing time

       print('Total Mowing Time (mins): ', mowing_mins);

#create an object of GeneGolfCenter class

object1 = GolfCreator()

  

#Get the course length from user

courseLength = float(input('Enter Course Length: '));

#Get the course width from user

courseWidth = float(input('Enter Course Width: '));

#Implementation of calculate_sq_yrds_smooth_sod() method

total_Smooth_Sod = object1.calculate_sq_yrds_smooth_sod(courseWidth);

#Implementation of calculatesand_trap_area() method

sand_trap_area = object1.calculatesand_trap_area(courseWidth);

#Implementation of calculate_sq_yrds_rough_sod() method

total_Rough_Sod = object1.calculate_sq_yrds_rough_sod(courseLength,courseWidth, total_Smooth_Sod, sand_trap_area);

#Implementation of calculateBricks() method

number_of_bricks = object1.calculateBricks(courseWidth);

#Implementation of calculateSand() method

total_tonsof_sand = object1.calculateSand(courseWidth);

#Implementation of calculateBushes() method

total_Bushes = object1.calculateBushes(courseLength, courseWidth);

#Implementation of calculatetotal_time() method

total_time = object1.calculatetotal_time(total_Rough_Sod, total_Smooth_Sod);

#Implementation of display() method

object1.display(total_Rough_Sod, total_Smooth_Sod, total_tonsof_sand, number_of_bricks, total_Bushes, total_time);






