// kt includes
#include "auton.hpp"
#include "config.hpp"
#include "kt/devices/motor/motor.hpp"
#include "kt/util.hpp"
#include "pros/motors.h"

// ==================== add your auto functions here ==================== //
/*
this is were you can write your auto functions.
just make sure to add them to the autons class when your done.
*/

// Do intake and wing stuff
void near() {
    std::cout<<"Near"<<std::endl;
    chassis.drive_pid_constants(.5, .0003, .00005, 5);
    chassis.move(5, 0, 0);
    chassis.turn_pid_constants(.000000005, .0000007, 1, 20);
    chassis.move(0, 35, 1);
    //chassis.drive_pid_constants(.5, .0003, .00005, 50);
    //chassis.move(-20, 0, 0);

    //intake1.brake(); //Suposedly undeclared //and do intake2
}
void far() {
    //why did turn pid's have an extra value of 100000
    std::cout<<"Far"<<std::endl;
    //intake2.move(-150);
    pros::delay(300);
    chassis.drive_pid_constants(.18, .0003, .00005, 50);
    chassis.move(1, 0, 0);
    chassis.turn_pid_constants(2.5, .007, .002, 5);
    chassis.move(0, 35, 1);
    pros::delay(500);

    //intake2.move(80);
    pros::delay(500);
    chassis.turn_pid_constants(1.5, .007, .0002, 6);
    chassis.move(0, -98, 1);
    pros::delay(500);
    //intake2.move(-150);
    chassis.drive_pid_constants(.18, .0003, .00005, 50);
    chassis.move(16, 0, 0);
    pros::delay(700);
    chassis.turn_pid_constants(1.5, .007, .0002, 6);
    chassis.move(0, 65, 1);
    chassis.drive_pid_constants(.18, .0003, .00005, 50);
    chassis.move(14, 0, 0);
    chassis.turn_pid_constants(1.5, .007, .0002, 6);
    chassis.move(0, 85, 1);
    //wings.set_value(true);
    pros::delay(500);
    //intake2.move(150);
    //Becuase the pid constants dont change can we do it once for several?
    chassis.drive_pid_constants(.18, .0003, .00005, 5);
    chassis.move(25, 0, 0);
    chassis.drive_pid_constants(.18, .0003, .00005, 50);
    chassis.move(-11, 0, 0);
    chassis.drive_pid_constants(.18, .0003, .00005, 50);
    chassis.move(12, 0, 0);
    chassis.drive_pid_constants(.18, .0003, .00005, 50);
    chassis.move(-10, 0, 0);
    //intake2.brake();
}
void backUp() {
    std::cout<<"BackUp"<<std::endl;
    chassis.set_brake_modes(pros::E_MOTOR_BRAKE_BRAKE);
    chassis.drive_pid_constants(.25, .0003, 2, 35);
    chassis.move(-7, 0, 0);
    chassis.drive_pid_constants(.25, .0003, 2, 5);
    chassis.move(7, 0, 0);
    chassis.set_brake_modes(pros::E_MOTOR_BRAKE_COAST);
}

// ==================== save your auto functions here ==================== //
/*
function called in initialize to set up the autons. 
add your auton by typing autons.add_auton("your autons name", "your autons description", your_autons_function);
doing so will add your auton to the auton class which handles the auto select and running the auton function for you.
*/
void initialize_auton() {// autons can be accessed in all 3 files
    autons.add_auton("Near", "Near (left) side auto, disrution auto.", near); // for function dont do "()"
    autons.add_auton("Far", "Auto for far (right) side", far);
    autons.add_auton("BackUp", "Backs into goal", backUp);
}

// ==================== auton select function ==================== //
/*
this is a task function used to check inputs for the auton select function. 
DO NOT CHANGE ANYTHING IN THIS FUNCTION UNLESS YOU KNOW WHAT YOU ARE DOING.
*/
void auton_select_task() {
    while (true) {
        autons.auton_select_task();
        pros::delay(kt::util::DELAY_TIME); //DELAY_TIME is 20
    }
}