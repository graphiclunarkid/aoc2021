use std::fs::File;
use std::io::prelude::*;
use std::path::Path;
use counter::Counter;

fn increment_day(s: counter::Counter<&str>) -> counter::Counter<&str> {

    let mut new_school = s.clone();

    new_school[&"7"] = s[&"8"];
    new_school[&"6"] = s[&"7"];
    new_school[&"5"] = s[&"6"];
    new_school[&"4"] = s[&"5"];
    new_school[&"3"] = s[&"4"];
    new_school[&"2"] = s[&"3"];
    new_school[&"1"] = s[&"2"];
    new_school[&"0"] = s[&"1"];
    new_school[&"6"] += s[&"0"];    // Fish on timer 0 reset to timer 6
    new_school[&"8"] += s[&"0"];    // Fish on timer 0 also produce new fish on timer 8

    new_school
}

fn main() {

    // Open puzzle input file
    let path = Path::new("data/day6-input");
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
    let school: Counter<&str> = input.trim().split(',').collect();

    println!("   Today's school: {:?}", school);

    let new_school = increment_day(school);

    println!("Tomorrow's school: {:?}", new_school);
}
