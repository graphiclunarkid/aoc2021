use std::fs::File;
use std::io::prelude::*;
use std::path::Path;
use counter::Counter;

fn increment_day(s: counter::Counter<&str>) -> counter::Counter<&str> {
    // We'll implement the logic here
    s
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
