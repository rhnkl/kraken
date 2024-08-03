// kt includes
#include "config.hpp"
#include "kt/devices/motor/motor.hpp"
#include "kt/util.hpp"
#include "liblvgl/llemu.h"
#include "liblvgl/llemu.hpp"
#include "pros/colors.h"
#include "pros/colors.hpp"
#include "pros/misc.h"
#include "pros/screen.hpp"

// namespace
using namespace pros;
using namespace kt;
using namespace v5;

#define SCREEN_WIDTH 480
#define SCREEN_HEIGHT 240

// ==================== setup your devices functions here ==================== //
/*
this is were you can setup your robots devices. this function will be called during initialize() in main.cpp
and any changes to the kt device classes will be kept and can then be used in both main.cpp and auton.cpp.
the exception to this is the chassis which is defined in main.cpp.
*/
void initialize_devices() {
    // define your devices here using their subclasses for them to be brought to both auton and main files


    // initialize the brains lcd for the auton select
    // lcd::initialize();

    screen::erase();
    screen::set_pen(Color::dim_gray);
    screen::fill_circle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 80);
    screen::set_pen(Color::black);
    screen::fill_circle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 50);
    screen::set_pen(Color::dark_green);
    screen::print(text_format_e_t::E_TEXT_LARGE_CENTER, 10, "Sehome Kraken 2605");


    // an example of how to setup a motor
    //motor.new_motor("motor", 1, E_CONTROLLER_DIGITAL_B, ON_PRESS);
    
    // Intake
    motor.new_motor("intake",10,E_CONTROLLER_DIGITAL_R1, ON_PRESS,E_CONTROLLER_DIGITAL_R2, ON_PRESS);
    //motor.new_motor("intake",-10,E_CONTROLLER_DIGITAL_R1,ON_PRESS);

    AdiDigitalOut.new_adi("MOGO-clamp", 'h', E_CONTROLLER_DIGITAL_L1, ON_NEW_PRESS, IN_TOGGLE_MODE,false);
} // end of initialize_devices function

// ==================== setup your devices functions here ==================== //
/*
this function is used to print data to the brain. it will run after initialize when the robot is turned on.
writing to the brain is done with the pros::lcd object.

feel free to add or remove anything from this function but remember that the while loop is needed for it to update
and the pros::delay helps it run better.
*/
void print_to_lcd_task() {
    while (true) {
        // print branding
        lcd::set_text(0, "Kraken Template");
        // print the current auton name
        lcd::set_text(1, autons.current_name());
        // print the current auton description
        lcd::set_text(2, autons.current_desc());
        // print the current drive imu heading
        if (std::to_string(chassis.imu.get_heading()) == "inf") lcd::set_text(3, "IMU Not Connected");
        else lcd::set_text(3, std::to_string(chassis.imu.get_heading()));
        

        // you can always remove some of these or add more


        // make sure to have some delay
        pros::delay(kt::util::DELAY_TIME);
    } // end of main loop
} // end of print_to_lcd_task function