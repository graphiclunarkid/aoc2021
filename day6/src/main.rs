use std::fs::File;
use std::io::prelude::*;
use std::path::Path;
use counter::Counter;

fn increment_day<'a>(school: &Counter<&str>) -> Counter<&'a str> {

    let mut new_school = Counter::new();

    new_school[&"7"] = school[&"8"];    // Each number > 0 decreases by 1 if it was
    new_school[&"6"] = school[&"7"];    // present at the start of the day
    new_school[&"5"] = school[&"6"];
    new_school[&"4"] = school[&"5"];
    new_school[&"3"] = school[&"4"];
    new_school[&"2"] = school[&"3"];
    new_school[&"1"] = school[&"2"];
    new_school[&"0"] = school[&"1"];
    new_school[&"6"] += school[&"0"];    // Each day, each 0 becomes a 6
    new_school[&"8"] += school[&"0"];    // and adds a new 8 to the school

    new_school

}

fn simulate_lanternfish(days: u32, school: &Counter<&str>) {

    println!("");
    println!("Initial state: {:?}", school);

    // Initialise our internal tracking Counter
    // and perform the first iteration
    let mut new_school: Counter<&str> = increment_day(school);

    // Start looping from day 2 since day 1 was done above
    for _ in 2..days+1 {

        new_school = increment_day(&new_school);

    }

    let count: usize = new_school.values().sum();

    println!("State after {} days: {:?}", days, new_school);
    println!("Total number of lanternfish after {} days: {:?}", days, count);
    
}

fn get_school(filename: &str) -> Counter<&str> {

    // Open puzzle input file
    let path = Path::new(&filename);
    let display = path.display();
    let mut file = match File::open(&path) {
        Err(why) => panic!("Couldn't open {}: {}", display, why),
        Ok(file) => file,
    };

    // Read puzzle input from file
    let mut input = String::new();
    match file.read_to_string(&mut input) {
        Err(why) => panic!("Couldn't read {}: {}", display, why),
        Ok(input) => input,
    };

    // Convert puzzle input into a Counter object (https://docs.rs/counter/latest/counter/)
    input.trim().split(',').collect::<Counter<_>>()

}

fn main() {

    let test_school = get_school("data/test-input");
    simulate_lanternfish(80, &test_school);
   
    let school = get_school("data/day6-input");
    simulate_lanternfish(80, &school);
    simulate_lanternfish(256, &school);

}
